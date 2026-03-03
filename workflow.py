"""
Workflow orchestrator - Orchestrates the full novel creation pipeline.
Flow: Planning → Worldbuilding + Style Guide (parallel) → Master Outline → Volume Outline → Chapter Writing
"""
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import config
import storage
from utils import multiline_input


# ==================== Language-aware word/character counting ====================
# CJK: count by characters (including spaces).
# Other languages: count by whitespace-delimited words.
# Note 1: CJK character counts include spaces, consistent with the
#          genkō yōshi (manuscript paper) counting convention.
# Note 2: Thai has no word-delimiting spaces, but its alphabetic characters
#          do not correspond 1:1 to "words"; accurate counting would require
#          a tokenizer. Character count is used as an approximation here,
#          only for progress display and does not affect generation logic.
_CHAR_BASED_LANGS = {"zh_cn", "zh_tw", "zh_cl", "ja", "ja_cl", "ko", "th"}


def count_words(text: str) -> int:
    """Choose character-based or word-based counting according to config.LANGUAGE."""
    if not text:
        return 0
    if config.LANGUAGE in _CHAR_BASED_LANGS:
        # Chinese / Japanese / Korean / Thai: count characters (including spaces)
        return len(text)
    else:
        # English / Vietnamese / Latin / Sanskrit, etc.: count whitespace-delimited words
        return len(text.split())
from locales import get_locale
from agents import (
    PlannerAgent, OutlineAgent, WorldbuildingAgent,
    StyleGuideAgent, WriterAgent, PostWriteAgent,
    QualityReviewerAgent, PolishAgent, FinalSummaryAgent,
)


class NovelWorkflow:
    """Novel creation workflow orchestrator."""

    def __init__(self):
        self.plan = None
        self.master_outline = None
        self.style_guide = None

    def _ui(self) -> dict:
        """Shortcut to get current locale UI strings."""
        return get_locale().UI

    # ==================== Phase 1: Planning ====================
    def phase_planning(self):
        """Planning phase - collect info through multi-turn dialogue."""
        ui = self._ui()
        print("\n" + "=" * 60)
        print(ui["phase_planning_title"])
        print("=" * 60)

        planner = PlannerAgent()

        # Show first question
        first_question = planner.start()
        print(f"{ui['planner_prefix']}{first_question}\n")

        rounds = 0
        while rounds < config.MAX_PLANNING_ROUNDS:
            user_input = multiline_input(ui["user_prefix"])
            if not user_input:
                print(ui["input_empty_hint"])
                continue

            if user_input.lower() in ["quit", "exit", "退出"]:
                print(ui["quit_planning"])
                return False

            if user_input.lower() in ["done", "完成", "够了", "可以了"]:
                print(ui["force_done"])
                break

            is_enough, response = planner.process_user_input(user_input)
            print(f"{ui['planner_prefix']}{response}\n")

            if is_enough:
                break
            rounds += 1

        # Generate plan
        print(ui["generating_plan"])
        self.plan = planner.generate_plan()

        # Display plan for user confirmation
        self._display_plan()

        while True:
            confirm = multiline_input(ui["confirm_plan"])
            if confirm.lower() in ["y", "yes", "好", "可以", "满意", "確認"]:
                break
            elif confirm.lower() in ["quit", "exit", "退出"]:
                return False
            else:
                p = get_locale().PROMPTS
                revision_msg = p["plan_revision_request"].format(feedback=confirm)
                # Ensure strict user/assistant alternation: if the last message
                # is already a user message, merge instead of appending.
                if (planner.conversation_history
                        and planner.conversation_history[-1]["role"] == "user"):
                    planner.conversation_history[-1]["content"] += "\n\n" + revision_msg
                else:
                    planner.conversation_history.append(
                        {"role": "user", "content": revision_msg}
                    )
                print(ui["adjusting_plan"])
                self.plan = planner.generate_plan()
                self._display_plan()

        # Save plan
        self._save_plan()
        print(ui["plan_confirmed"])

        # Offer to rename project directory to the novel title
        self._offer_rename_project_dir()

        return True

    def _display_plan(self):
        """Display the plan to the user."""
        if not self.plan:
            return
        ui = self._ui()
        print("\n" + "-" * 40)
        print(ui["plan_display_title"])
        print("-" * 40)
        display_items = [
            (ui["plan_label_title"], "title"),
            (ui["plan_label_genre"], "genre"),
            (ui["plan_label_theme"], "theme"),
            (ui["plan_label_target_words"], "target_words"),
            (ui["plan_label_total_chapters"], "total_chapters"),
            (ui["plan_label_volumes"], "volumes"),
            (ui["plan_label_pov"], "pov"),
            (ui["plan_label_tags"], "tags"),
            (ui["plan_label_one_line"], "one_line_summary"),
        ]
        for label, key in display_items:
            if key in self.plan:
                print(f"  {label}: {self.plan[key]}")

        three_act = self.plan.get("three_act_summary", {})
        if three_act:
            print(f"\n  {ui['plan_label_beginning']}: {three_act.get('beginning', '')}")
            print(f"  {ui['plan_label_middle']}: {three_act.get('middle', '')}")
            print(f"  {ui['plan_label_end']}: {three_act.get('end', '')}")

        if self.plan.get("main_characters"):
            print(f"\n  {ui['plan_label_characters']}:")
            for char in self.plan["main_characters"]:
                print(f"    - {char.get('name', '?')} ({char.get('role', '?')}): "
                      f"{char.get('personality', '')[:50]}...")
        print("-" * 40)

    def _save_plan(self):
        """Save the plan to files."""
        # Save raw JSON
        storage.write_file("plan.json", json.dumps(self.plan, ensure_ascii=False, indent=2))

        # Initialize directory structure and base files
        storage.init_readme(self.plan)
        storage.init_progress(self.plan)
        storage.init_hooks_tracker()
        storage.init_chapter_briefs()

        # Save synopsis
        tpl = get_locale().TEMPLATES
        synopsis = self.plan.get("synopsis", self.plan.get("one_line_summary", ""))
        if synopsis:
            storage.write_file(
                f"{config.DIR_META}/synopsis.md",
                tpl["synopsis_title"] + synopsis + "\n"
            )

    def _offer_rename_project_dir(self):
        """Ask the user whether to rename the project directory to the novel title."""
        title = self.plan.get("title", "")
        if not title:
            return

        current_dir_name = os.path.basename(config.PROJECT_ROOT)
        # Skip if the directory already matches the title
        if current_dir_name == title:
            return

        ui = self._ui()
        print(ui.get("rename_dir_prompt",
                      "\n📁 Novel title is \"{title}\", but the project directory is \"{dir}\".")
              .format(title=title, dir=current_dir_name))
        answer = input(ui.get("rename_dir_confirm",
                               "   Rename project directory to \"{title}\"? (y/n): ")
                       .format(title=title)).strip().lower()
        if answer in ("y", "yes", "好", "是", "确认", "確認", "はい", "ええ"):
            config.rename_project_dir(title)

    # ==================== Writing Parameters Confirmation ====================
    def _ask_writing_params(self):
        """Ask the user to confirm/adjust key writing parameters before starting."""
        ui = self._ui()
        print(ui.get("writing_params_title", "\n⚙️ Writing Parameters"))

        # --- CHAPTER_MIN_WORDS ---
        current_min = config.CHAPTER_MIN_WORDS
        val = input(ui.get("ask_chapter_min_words",
                           "   Min words per chapter (current: {current}, Enter to keep): ")
                    .format(current=current_min)).strip()
        if val.isdigit() and int(val) > 0:
            config.CHAPTER_MIN_WORDS = int(val)

        # --- CHAPTER_MAX_WORDS ---
        current_max = config.CHAPTER_MAX_WORDS
        val = input(ui.get("ask_chapter_max_words",
                           "   Max words per chapter (current: {current}, Enter to keep): ")
                    .format(current=current_max)).strip()
        if val.isdigit() and int(val) > 0:
            config.CHAPTER_MAX_WORDS = int(val)

        # Sanity: ensure min <= max
        if config.CHAPTER_MIN_WORDS > config.CHAPTER_MAX_WORDS:
            config.CHAPTER_MIN_WORDS, config.CHAPTER_MAX_WORDS = (
                config.CHAPTER_MAX_WORDS, config.CHAPTER_MIN_WORDS
            )
            print(ui.get("writing_params_swapped",
                         "   ⚠️ Min > Max detected, values swapped."))

        # --- CHAPTER_WORD_COUNT_CHECK ---
        current_check = config.CHAPTER_WORD_COUNT_CHECK
        check_label = "ON" if current_check else "OFF"
        val = input(ui.get("ask_word_count_check",
                           "   Enable word count check? (current: {status}, y/n, Enter to keep): ")
                    .format(status=check_label)).strip().lower()
        if val in ("y", "yes"):
            config.CHAPTER_WORD_COUNT_CHECK = True
        elif val in ("n", "no"):
            config.CHAPTER_WORD_COUNT_CHECK = False

        # --- LAZY_MODE ---
        current_lazy = config.LAZY_MODE
        lazy_label = "ON" if current_lazy else "OFF"
        val = input(ui.get("ask_lazy_mode",
                           "   Enable lazy mode (auto-confirm everything)? (current: {status}, y/n, Enter to keep): ")
                    .format(status=lazy_label)).strip().lower()
        if val in ("y", "yes"):
            config.LAZY_MODE = True
        elif val in ("n", "no"):
            config.LAZY_MODE = False

        # --- Summary ---
        print(ui.get("writing_params_summary",
                     "   ✅ Writing params: {min}-{max} words/chapter, "
                     "word count check: {check}, lazy mode: {lazy}")
              .format(
                  min=config.CHAPTER_MIN_WORDS,
                  max=config.CHAPTER_MAX_WORDS,
                  check="ON" if config.CHAPTER_WORD_COUNT_CHECK else "OFF",
                  lazy="ON" if config.LAZY_MODE else "OFF",
              ))

        # Persist changes to novel_config.json
        self._save_writing_params_to_novel_config()

    def _save_writing_params_to_novel_config(self):
        """Persist the confirmed writing parameters back to novel_config.json."""
        novel_config_path = os.path.join(config.PROJECT_ROOT, config.NOVEL_CONFIG_FILE)
        if not os.path.exists(novel_config_path):
            return
        try:
            with open(novel_config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            data["CHAPTER_MIN_WORDS"] = config.CHAPTER_MIN_WORDS
            data["CHAPTER_MAX_WORDS"] = config.CHAPTER_MAX_WORDS
            data["CHAPTER_WORD_COUNT_CHECK"] = config.CHAPTER_WORD_COUNT_CHECK
            data["LAZY_MODE"] = config.LAZY_MODE
            with open(novel_config_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception:
            pass  # Non-critical, silently ignore

    # ==================== Quote Style Selection ====================
    def _select_quote_style(self):
        """Let the user choose dialogue quote style and inner thought quote style."""
        ui = self._ui()

        # --- Step 1: Dialogue quote style ---
        if config.QUOTE_STYLE == "auto":
            lang = config.LANGUAGE
            if lang in ("zh_cn", "zh_tw", "zh_cl"):
                options = [
                    ("curly", ui["quote_style_option_curly"]),
                    ("corner", ui["quote_style_option_corner"]),
                ]
            elif lang in ("ja", "ja_cl"):
                options = [
                    ("corner", ui["quote_style_option_corner"]),
                    ("curly", ui["quote_style_option_curly"]),
                ]
            elif lang == "vi":
                options = [
                    ("dash", ui["quote_style_option_dash"]),
                    ("curly", ui["quote_style_option_curly"]),
                ]
            elif lang in ("fr",):
                options = [
                    ("guillemet", ui["quote_style_option_guillemet"]),
                    ("dash", ui["quote_style_option_dash"]),
                ]
            elif lang in ("la", "sa"):
                options = [
                    ("curly", ui["quote_style_option_curly"]),
                    ("guillemet", ui["quote_style_option_guillemet"]),
                    ("dash", ui["quote_style_option_dash"]),
                ]
            else:
                options = [
                    ("straight", ui["quote_style_option_straight"]),
                    ("curly", ui["quote_style_option_curly"]),
                ]

            print(ui["quote_style_title"])
            for i, (_, desc) in enumerate(options, 1):
                print(f"  {i}. {desc}")

            while True:
                choice = input(ui["quote_style_prompt"].format(max=len(options))).strip()
                if choice.isdigit() and 1 <= int(choice) <= len(options):
                    selected = options[int(choice) - 1]
                    config.QUOTE_STYLE = selected[0]
                    print(ui["quote_style_selected"].format(style=selected[1]))
                    break
                print(ui["quote_style_invalid"].format(max=len(options)))

        # --- Step 2: Inner thought / internal monologue quote style ---
        if config.INNER_QUOTE_STYLE == "auto":
            lang = config.LANGUAGE
            if lang in ("zh_cn", "zh_tw", "zh_cl"):
                inner_options = [
                    ("corner_double", ui["inner_quote_option_corner_double"]),
                    ("corner", ui["inner_quote_option_corner"]),
                    ("paren", ui["inner_quote_option_paren"]),
                    ("none", ui["inner_quote_option_none"]),
                ]
            elif lang in ("ja", "ja_cl"):
                inner_options = [
                    ("corner_double", ui["inner_quote_option_corner_double"]),
                    ("corner", ui["inner_quote_option_corner"]),
                    ("italic", ui["inner_quote_option_italic"]),
                ]
            elif lang in ("ko",):
                inner_options = [
                    ("curly_single", ui["inner_quote_option_curly_single"]),
                    ("italic", ui["inner_quote_option_italic"]),
                    ("none", ui["inner_quote_option_none"]),
                ]
            elif lang in ("vi",):
                inner_options = [
                    ("italic", ui["inner_quote_option_italic"]),
                    ("curly_single", ui["inner_quote_option_curly_single"]),
                    ("none", ui["inner_quote_option_none"]),
                ]
            else:
                # English, Latin, Sanskrit, Thai, etc.
                inner_options = [
                    ("italic", ui["inner_quote_option_italic"]),
                    ("curly_single", ui["inner_quote_option_curly_single"]),
                    ("same", ui["inner_quote_option_same"]),
                    ("none", ui["inner_quote_option_none"]),
                ]

            print(ui["inner_quote_title"])
            for i, (_, desc) in enumerate(inner_options, 1):
                print(f"  {i}. {desc}")

            while True:
                choice = input(ui["inner_quote_prompt"].format(max=len(inner_options))).strip()
                if choice.isdigit() and 1 <= int(choice) <= len(inner_options):
                    selected = inner_options[int(choice) - 1]
                    config.INNER_QUOTE_STYLE = selected[0]
                    print(ui["inner_quote_selected"].format(style=selected[1]))
                    break
                print(ui["inner_quote_invalid"].format(max=len(inner_options)))

    # ==================== Phase 2: Worldbuilding + Style Guide (parallel) ====================
    def phase_worldbuilding(self):
        """Worldbuilding phase - generate world settings and style guide in parallel."""
        ui = self._ui()
        print("\n" + "=" * 60)
        print(ui["phase_world_title"])
        print("=" * 60)

        if not self.plan:
            self.plan = self._load_plan()

        worldbuilding_agent = WorldbuildingAgent()
        style_agent = StyleGuideAgent()

        # Parallel execution: worldbuilding + style guide
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_world = executor.submit(worldbuilding_agent.generate_all, self.plan)
            future_style = executor.submit(style_agent.generate, self.plan)

            try:
                world_results = future_world.result()
                for filename, content in world_results.items():
                    storage.write_file(f"{config.DIR_WORLDBUILDING}/{filename}", content)
                print(ui["world_done"].format(count=len(world_results)))
            except Exception as e:
                print(ui["world_failed"].format(error=e))

            try:
                self.style_guide = future_style.result()
                # Inject quote style rule into style guide if set
                import prompts as _prompts_mod
                quote_rule = _prompts_mod.get_quote_style_instruction()
                if quote_rule:
                    heading = _prompts_mod.get_quote_rules_heading()
                    self.style_guide += f"\n\n## {heading}\n{quote_rule}\n"
                storage.write_file(f"{config.DIR_META}/style_guide.md", self.style_guide)
                print(ui["style_done"])
            except Exception as e:
                print(ui["style_failed"].format(error=e))

    # ==================== Phase 3: Master Outline (Feature #1: Multi-Draft) ====================
    def phase_master_outline(self):
        """Generate the master outline. Uses multi-draft comparison if enabled."""
        ui = self._ui()
        print("\n" + "=" * 60)

        if not self.plan:
            self.plan = self._load_plan()

        outline_agent = OutlineAgent()

        if config.OUTLINE_DRAFT_COUNT > 1:
            # Feature #1: Multi-draft comparison mode
            print(ui["outline_multi_draft_title"])
            print("=" * 60)

            drafts = outline_agent.generate_master_outline_multi(self.plan)

            if not drafts:
                raise RuntimeError("All outline drafts failed to generate")

            if len(drafts) == 1:
                # Only one draft succeeded, use it directly
                self.master_outline = drafts[0]["content"]
            elif config.LAZY_MODE:
                # Lazy mode: auto-merge all drafts
                print(ui["lazy_auto_merge"])
                print(ui["draft_merging"])
                self.master_outline = outline_agent.merge_outlines(self.plan, drafts)
                print(ui["draft_merged"])
            else:
                # Display drafts for comparison
                print(ui["draft_comparison_title"])
                for d in drafts:
                    separator = '\u2500' * 40
                    print(f"\n{separator}")
                    print(f"\U0001f4c4 Draft {d['index']} \u2014 Style: {d['style']}")
                    print(f"{separator}")
                    # Show first 500 chars as preview
                    preview = d["content"][:500]
                    if len(d["content"]) > 500:
                        preview += "\n... (truncated for display)"
                    print(preview)

                # Let user choose
                while True:
                    choice = input(ui["draft_select_prompt"].format(max=len(drafts))).strip().lower()
                    if choice == 'm':
                        print(ui["draft_merging"])
                        self.master_outline = outline_agent.merge_outlines(self.plan, drafts)
                        print(ui["draft_merged"])
                        break
                    elif choice.isdigit() and 1 <= int(choice) <= len(drafts):
                        idx = int(choice)
                        self.master_outline = drafts[idx - 1]["content"]
                        print(ui["draft_selected"].format(num=idx))
                        break
                    else:
                        print(ui["draft_invalid"].format(max=len(drafts)))
        else:
            # Single draft mode (original behavior)
            print(ui["phase_outline_title"])
            print("=" * 60)
            print(ui["generating_outline"])
            self.master_outline = outline_agent.generate_master_outline(self.plan)

        storage.write_file(f"{config.DIR_PLOT}/master_outline.md", self.master_outline)
        print(ui["outline_done"])

        print(ui["outline_review"])
        if config.LAZY_MODE:
            print(ui["lazy_auto_continue"])
        else:
            input(ui["press_enter_continue"])

    # ==================== Phase 4: Volume Outline ====================
    def phase_volume_outline(self, volume_num: int = 1):
        """Generate a detailed outline for the specified volume."""
        ui = self._ui()
        print(ui["generating_volume"].format(num=volume_num))

        if not self.plan:
            self.plan = self._load_plan()
        if not self.master_outline:
            self.master_outline = storage.read_file(f"{config.DIR_PLOT}/master_outline.md")

        outline_agent = OutlineAgent()
        volume_info = self._extract_volume_info(volume_num)

        volume_outline = outline_agent.generate_volume_outline(
            self.plan, self.master_outline, volume_num, volume_info
        )
        storage.write_file(f"{config.DIR_PLOT}/volume_{volume_num:02d}.md", volume_outline)
        print(ui["volume_done"].format(num=volume_num))

        return volume_outline

    # ==================== Phase 5: Chapter Writing ====================
    def phase_writing(self, start_chapter: int = 1, end_chapter: int = None):
        """Chapter-by-chapter writing phase with polish loop, parallel review, and volume checkpoints."""
        ui = self._ui()
        print("\n" + "=" * 60)
        print(ui["phase_writing_title"])
        print("=" * 60)

        if not self.plan:
            self.plan = self._load_plan()
        if not self.style_guide:
            self.style_guide = storage.read_file(f"{config.DIR_META}/style_guide.md") or ""

        writer = WriterAgent()
        post_writer = PostWriteAgent()
        # Feature #2: Parallel quality reviewer
        reviewer = QualityReviewerAgent() if config.ENABLE_PARALLEL_REVIEW else None
        # Feature #3: Polish agent
        polisher = PolishAgent() if config.ENABLE_POLISH_LOOP else None

        # Determine writing range
        if end_chapter is None:
            total = self.plan.get("total_chapters", "30")
            try:
                end_chapter = int(re.search(r'\d+', str(total)).group())
            except (AttributeError, ValueError):
                end_chapter = 30

        # Checkpoint resume: skip completed chapters
        completed = storage.get_completed_chapter_count()
        if completed >= start_chapter:
            print(ui["checkpoint_resume"].format(count=completed, next=completed + 1))
            start_chapter = completed + 1

        # Load current volume outline
        current_volume = 1
        volume_outline = storage.read_file(f"{config.DIR_PLOT}/volume_{current_volume:02d}.md")
        if not volume_outline:
            print(ui["volume_not_found"].format(num=current_volume))
            volume_outline = self.phase_volume_outline(current_volume)

        for chapter_num in range(start_chapter, end_chapter + 1):
            print(f"\n{'\u2500' * 40}")
            print(ui["writing_chapter"].format(num=chapter_num))
            print(f"{'\u2500' * 40}")

            # Check if we need to switch to a new volume
            new_volume = self._get_volume_for_chapter(chapter_num)
            if new_volume != current_volume:
                current_volume = new_volume

                # Feature #4: Mid-volume checkpoint
                if config.ENABLE_VOLUME_CHECKPOINT:
                    checkpoint_result = self._volume_checkpoint(current_volume, chapter_num)
                    if checkpoint_result == "stop":
                        break

                volume_outline = storage.read_file(
                    f"{config.DIR_PLOT}/volume_{current_volume:02d}.md"
                )
                if not volume_outline:
                    print(ui["generating_volume_outline"].format(num=current_volume))
                    volume_outline = self.phase_volume_outline(current_volume)

            # Extract chapter outline from volume outline
            chapter_outline = self._extract_chapter_outline(volume_outline, chapter_num)

            # Get recent chapter summaries
            recent_briefs = self._get_recent_briefs(chapter_num)

            # Get current character status
            character_status = self._get_character_status()

            # Get foreshadowing info
            hooks_info = self._get_hooks_info()

            # Get authoritative character profiles and world settings
            character_profiles = self._get_character_profiles()
            world_setting = self._get_world_setting()

            # Write
            try:
                review_attempt = 0
                review_feedback = ""
                while True:
                    chapter_text = writer.write_chapter(
                        chapter_num=chapter_num,
                        chapter_outline=chapter_outline,
                        style_guide=self.style_guide,
                        recent_briefs=recent_briefs,
                        character_status=character_status,
                        hooks_info=hooks_info,
                        character_profiles=character_profiles,
                        world_setting=world_setting,
                        review_feedback=review_feedback,
                    )

                    # Feature #3: Polish loop
                    if polisher:
                        chapter_text, polish_score = polisher.polish_loop(
                            chapter_text, chapter_outline, self.style_guide
                        )

                    # Word count validation
                    if config.CHAPTER_WORD_COUNT_CHECK:
                        chapter_text, extra_chapter = self._validate_word_count(
                            writer, chapter_text, chapter_outline, chapter_num, end_chapter
                        )
                        # If split occurred, save both chapters and adjust numbering
                        if extra_chapter is not None:
                            extra_num, extra_text = extra_chapter
                            # Save current chapter (first half)
                            storage.write_file(
                                f"{config.DIR_CHAPTERS}/chapter_{chapter_num:03d}.txt",
                                chapter_text
                            )
                            wc_a = count_words(chapter_text)
                            print(ui["chapter_done"].format(num=chapter_num, words=wc_a))
                            # Save extra chapter (second half)
                            storage.write_file(
                                f"{config.DIR_CHAPTERS}/chapter_{extra_num:03d}.txt",
                                extra_text
                            )
                            wc_b = count_words(extra_text)
                            print(ui["wordcount_split_done"].format(
                                num_a=chapter_num, words_a=wc_a,
                                num_b=extra_num, words_b=wc_b
                            ))
                            # Adjust end_chapter: one extra chapter was inserted
                            end_chapter += 1
                            print(ui["wordcount_split_renumber"])

                            # Post-processing for both chapters
                            print(ui["post_processing"])
                            for ch_num, ch_text in [(chapter_num, chapter_text), (extra_num, extra_text)]:
                                analysis = post_writer.analyze_chapter(ch_num, ch_text, chapter_outline)
                                if analysis:
                                    post_writer.update_files(ch_num, analysis)
                                else:
                                    print(ui["post_failed"].format(num=ch_num))

                            # Skip the normal save/review/post-process flow below
                            break

                    word_count = count_words(chapter_text)
                    print(ui["chapter_done"].format(num=chapter_num, words=word_count))

                    # Feature #2: Parallel quality review
                    should_retry = False
                    if reviewer:
                        # Load character profiles for name cross-checking
                        character_profiles = storage.read_file(
                            f"{config.DIR_WORLDBUILDING}/characters.md"
                        ) or ""

                        issues = reviewer.review_chapter(
                            chapter_text=chapter_text,
                            chapter_outline=chapter_outline,
                            style_guide=self.style_guide,
                            recent_briefs=recent_briefs,
                            hooks_info=hooks_info,
                            character_profiles=character_profiles,
                        )
                        if issues:
                            # Display issues
                            print(ui["review_issues_found"].format(count=len(issues)))
                            has_critical = False
                            feedback_parts = []
                            for issue in issues:
                                severity = issue.get("severity", "info").upper()
                                print(ui["review_issue_item"].format(
                                    severity=severity,
                                    reviewer=issue.get("reviewer", "?"),
                                    confidence=issue.get("confidence", "?"),
                                    description=issue.get("description", ""),
                                ))
                                if issue.get("severity") == "critical":
                                    has_critical = True
                                # Collect CRITICAL and MAJOR issues as feedback for rewrite
                                if issue.get("severity") in ("critical", "major"):
                                    feedback_parts.append(
                                        f"[{severity}] {issue.get('description', '')}"
                                    )

                            # If critical issues, offer retry
                            if has_critical and review_attempt < config.MAX_REVIEW_RETRIES:
                                review_attempt += 1
                                # Build feedback string for the rewriter
                                review_feedback = ui["review_retry_feedback"].format(
                                    attempt=review_attempt,
                                    max_attempts=config.MAX_REVIEW_RETRIES,
                                    issues="\n".join(feedback_parts),
                                )
                                if config.LAZY_MODE:
                                    print(ui["lazy_auto_retry"])
                                    should_retry = True
                                else:
                                    retry_choice = input(ui["review_critical_prompt"]).strip().lower()
                                    if retry_choice == "y":
                                        should_retry = True

                            # Max retries exhausted for critical issues
                            if has_critical and review_attempt >= config.MAX_REVIEW_RETRIES and not should_retry:
                                print(ui["review_max_retries_reached"].format(
                                    max=config.MAX_REVIEW_RETRIES, num=chapter_num
                                ))
                        else:
                            print(ui["review_no_issues"])

                    if should_retry:
                        continue  # Re-run the while loop for the same chapter

                    # Review passed (or no critical issues) — save the chapter
                    storage.write_file(
                        f"{config.DIR_CHAPTERS}/chapter_{chapter_num:03d}.txt",
                        chapter_text
                    )

                    # Post-processing: generate summary and update metadata
                    print(ui["post_processing"])
                    analysis = post_writer.analyze_chapter(chapter_num, chapter_text, chapter_outline)
                    if analysis:
                        post_writer.update_files(chapter_num, analysis)
                    else:
                        print(ui["post_failed"].format(num=chapter_num))

                    break  # Done with this chapter, exit the while loop

            except Exception as e:
                print(ui["chapter_error"].format(num=chapter_num, error=e))
                if config.LAZY_MODE:
                    print(ui["lazy_auto_retry"])
                    continue
                retry = input(ui["retry_prompt"]).strip().lower()
                if retry == "y":
                    continue
                else:
                    print(ui["skip_chapter"].format(num=chapter_num))
                    continue

            # Every 5 chapters, offer the user a chance to pause
            if chapter_num % 5 == 0 and chapter_num < end_chapter:
                if not config.LAZY_MODE:
                    print(ui["pause_prompt"].format(num=chapter_num))
                    cmd = input(ui["pause_input"]).strip().lower()
                    if cmd == "stop":
                        print(ui["paused"].format(next=chapter_num + 1))
                        break

        print("\n" + "=" * 60)
        print(ui["writing_complete"])
        print("=" * 60)

        # Feature #6: Final summary (if all chapters are done)
        if config.ENABLE_FINAL_SUMMARY:
            completed_now = storage.get_completed_chapter_count()
            try:
                expected_total = int(re.search(r'\d+', str(self.plan.get("total_chapters", "30"))).group())
            except (AttributeError, ValueError):
                expected_total = 30
            if completed_now >= expected_total:
                self._generate_final_summary()

    # ==================== Helper Methods ====================

    def _validate_word_count(self, writer, chapter_text: str, chapter_outline: str,
                             chapter_num: int, end_chapter: int) -> tuple[str, tuple | None]:
        """Validate chapter word count and expand/compress/split as needed.

        Returns:
            (final_text, None) if no split occurred.
            (first_half_text, (extra_chapter_num, second_half_text)) if split occurred.
        """
        ui = self._ui()
        min_words = config.CHAPTER_MIN_WORDS
        max_words = config.CHAPTER_MAX_WORDS
        split_threshold = config.CHAPTER_SPLIT_THRESHOLD
        max_retries = config.MAX_WORD_COUNT_RETRIES

        word_count = count_words(chapter_text)
        print(ui["wordcount_check_start"].format(words=word_count, min=min_words, max=max_words))

        # Check if word count is within range
        if min_words <= word_count <= max_words:
            print(ui["wordcount_ok"].format(words=word_count))
            return chapter_text, None

        # Check if split is needed (far too long)
        if word_count >= max_words * split_threshold:
            print(ui["wordcount_split_needed"].format(
                words=word_count, threshold=int(split_threshold * 100)
            ))
            try:
                extra_num = chapter_num + 1
                part_a, part_b = writer.split_chapter(
                    chapter_text=chapter_text,
                    chapter_outline=chapter_outline,
                    style_guide=self.style_guide,
                    current_words=word_count,
                    chapter_num_a=chapter_num,
                    chapter_num_b=extra_num,
                )
                return part_a, (extra_num, part_b)
            except Exception as e:
                print(ui["chapter_error"].format(num=chapter_num, error=f"Split failed: {e}"))
                # Fall through to compress instead
                print(ui["wordcount_too_long"].format(words=word_count, max=max_words))

        # Expand or compress loop
        for attempt in range(1, max_retries + 1):
            word_count = count_words(chapter_text)

            if min_words <= word_count <= max_words:
                print(ui["wordcount_ok"].format(words=word_count))
                return chapter_text, None

            if word_count < min_words:
                # Too short: expand
                print(ui["wordcount_too_short"].format(words=word_count, min=min_words))
                if attempt > 1:
                    print(ui["wordcount_retry"].format(attempt=attempt, max_attempts=max_retries))
                target = (min_words + max_words) // 2
                try:
                    chapter_text = writer.expand_chapter(
                        chapter_text=chapter_text,
                        chapter_outline=chapter_outline,
                        style_guide=self.style_guide,
                        current_words=word_count,
                        target_words=target,
                    )
                    new_count = count_words(chapter_text)
                    print(ui["wordcount_expand_done"].format(words=new_count))
                except Exception as e:
                    print(ui["chapter_error"].format(num=chapter_num, error=f"Expand failed: {e}"))
                    break

            elif word_count > max_words:
                # Too long: compress
                print(ui["wordcount_too_long"].format(words=word_count, max=max_words))
                if attempt > 1:
                    print(ui["wordcount_retry"].format(attempt=attempt, max_attempts=max_retries))
                target = (min_words + max_words) // 2
                try:
                    chapter_text = writer.compress_chapter(
                        chapter_text=chapter_text,
                        chapter_outline=chapter_outline,
                        style_guide=self.style_guide,
                        current_words=word_count,
                        target_words=target,
                    )
                    new_count = count_words(chapter_text)
                    print(ui["wordcount_compress_done"].format(words=new_count))
                except Exception as e:
                    print(ui["chapter_error"].format(num=chapter_num, error=f"Compress failed: {e}"))
                    break

        # Final check
        final_count = count_words(chapter_text)
        if min_words <= final_count <= max_words:
            print(ui["wordcount_ok"].format(words=final_count))
        else:
            print(ui["wordcount_give_up"].format(max_attempts=max_retries, words=final_count))

        return chapter_text, None

    def _load_plan(self) -> dict:
        """Load the plan from file."""
        ui = self._ui()
        content = storage.read_file("plan.json")
        if content:
            return json.loads(content)
        raise RuntimeError(ui["plan_not_found_error"])

    def _extract_volume_info(self, volume_num: int) -> str:
        """Extract info for the specified volume from the master outline."""
        if not self.master_outline:
            return f"Volume {volume_num}"

        patterns = [
            rf'(###?\s*第{volume_num}卷.*?)(?=###?\s*第\d+卷|$)',
            rf'(第{volume_num}卷.*?)(?=第\d+卷|$)',
            rf'(###?\s*Volume\s*{volume_num}.*?)(?=###?\s*Volume\s*\d+|$)',
            rf'(Volume\s*{volume_num}.*?)(?=Volume\s*\d+|$)',
        ]
        for pattern in patterns:
            match = re.search(pattern, self.master_outline, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return f"Volume {volume_num} (no detailed info found in master outline)"

    def _extract_chapter_outline(self, volume_outline: str, chapter_num: int) -> str:
        """Extract the outline for a specific chapter from the volume outline."""
        if not volume_outline:
            return f"Chapter {chapter_num} (no outline info)"

        patterns = [
            rf'(###?\s*第{chapter_num}章.*?)(?=###?\s*第\d+章|$)',
            rf'(第{chapter_num}章.*?)(?=第\d+章|$)',
            rf'(###?\s*Chapter\s*{chapter_num}.*?)(?=###?\s*Chapter\s*\d+|$)',
            rf'(Chapter\s*{chapter_num}.*?)(?=Chapter\s*\d+|$)',
        ]
        for pattern in patterns:
            match = re.search(pattern, volume_outline, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return f"Chapter {chapter_num} (no outline found, improvise based on master outline)"

    def _get_recent_briefs(self, current_chapter: int) -> str:
        """Get the most recent N chapter summaries."""
        briefs = storage.read_file(f"{config.DIR_PLOT}/chapter_briefs.md")
        if not briefs:
            return ""

        sections = re.split(r'(?=### (?:第\d+章|Chapter \d+))', briefs)
        recent = sections[-config.RECENT_CHAPTERS_FOR_CONTEXT:]
        return "\n".join(recent) if recent else ""

    def _get_character_status(self) -> str:
        """Get the current character status."""
        progress = storage.read_file(f"{config.DIR_META}/progress.md")
        if progress:
            match = re.search(r'(## (?:当前角色状态速查|Current Character Status).*?)(?=##|\Z)',
                              progress, re.DOTALL)
            if match:
                return match.group(1).strip()

        characters = storage.read_file(f"{config.DIR_WORLDBUILDING}/characters.md")
        if characters:
            return characters[:3000] + "\n(...see full character profiles)"
        return ""

    def _get_hooks_info(self) -> str:
        """Get the foreshadowing/hooks information."""
        hooks = storage.read_file(f"{config.DIR_META}/hooks_tracker.md")
        if hooks:
            return hooks[:2000]
        return ""

    def _get_character_profiles(self) -> str:
        """Get authoritative character profiles for the writer prompt."""
        characters = storage.read_file(f"{config.DIR_WORLDBUILDING}/characters.md")
        if characters:
            return characters[:4000]
        return ""

    def _get_world_setting(self) -> str:
        """Get authoritative world setting and location names for the writer prompt."""
        parts = []
        world = storage.read_file(f"{config.DIR_WORLDBUILDING}/world_setting.md")
        if world:
            parts.append(world[:2000])
        locations = storage.read_file(f"{config.DIR_WORLDBUILDING}/locations.md")
        if locations:
            parts.append(locations[:2000])
        return "\n\n".join(parts) if parts else ""

    def _get_volume_for_chapter(self, chapter_num: int) -> int:
        """Determine which volume a chapter belongs to."""
        if self.plan:
            volumes_str = str(self.plan.get("volumes", ""))
            total_chapters_str = str(self.plan.get("total_chapters", "30"))

            try:
                total_chapters = int(re.search(r'\d+', total_chapters_str).group())
            except (AttributeError, ValueError):
                total_chapters = 30

            volumes_match = re.search(r'(\d+)', volumes_str)
            if volumes_match:
                num_volumes = int(volumes_match.group(1))
                chapters_per_volume = total_chapters // num_volumes
                return min((chapter_num - 1) // chapters_per_volume + 1, num_volumes)

        # Default: 30 chapters per volume
        return (chapter_num - 1) // 30 + 1

    # ==================== Feature #4: Volume Checkpoint ====================
    def _volume_checkpoint(self, volume_num: int, next_chapter: int) -> str:
        """
        Mid-volume checkpoint - lets the user review progress and adjust before continuing.
        Returns 'continue', 'adjust', or 'stop'.
        """
        ui = self._ui()
        print(ui["volume_checkpoint_title"].format(num=volume_num))

        completed = storage.get_completed_chapter_count()
        # Estimate total words from completed chapters
        total_words = 0
        for ch_file in storage.list_chapter_files():
            content = storage.read_file(f"{config.DIR_CHAPTERS}/{ch_file}")
            if content:
                total_words += count_words(content)

        print(ui["volume_checkpoint_summary"].format(
            completed=completed, words=total_words
        ))

        # Lazy mode: auto-continue without user input
        if config.LAZY_MODE:
            print(ui["lazy_auto_volume_continue"].format(num=volume_num))
            return "continue"

        while True:
            choice = input(ui["volume_checkpoint_prompt"].format(num=volume_num)).strip().lower()
            if choice in ["y", "yes", ""]:
                return "continue"
            elif choice in ["stop", "quit", "exit"]:
                print(ui["volume_checkpoint_stopped"].format(
                    num=volume_num, next=next_chapter
                ))
                return "stop"
            elif choice in ["adjust", "a"]:
                feedback = multiline_input(ui["volume_checkpoint_adjust"])
                if feedback:
                    print(ui["volume_checkpoint_adjusting"])
                    # Re-generate volume outline with feedback
                    outline_agent = OutlineAgent()
                    volume_outline = storage.read_file(
                        f"{config.DIR_PLOT}/volume_{volume_num:02d}.md"
                    ) or ""

                    import prompts as prompts_mod
                    adjust_prompt = prompts_mod.volume_adjust_prompt(
                        volume_num=volume_num,
                        feedback=feedback,
                        volume_outline=volume_outline,
                    )
                    from llm_client import get_client
                    client = get_client()
                    revised = client.chat(
                        prompts_mod.volume_outline_system(),
                        [{"role": "user", "content": adjust_prompt}]
                    )
                    if revised:
                        storage.write_file(
                            f"{config.DIR_PLOT}/volume_{volume_num:02d}.md", revised
                        )
                        print(ui["volume_done"].format(num=volume_num))
                return "continue"
            else:
                print(ui["volume_checkpoint_prompt"].format(num=volume_num))

    # ==================== Feature #6: Final Summary ====================
    def _generate_final_summary(self):
        """Generate a comprehensive final summary report."""
        ui = self._ui()
        print(ui["final_summary_title"])

        try:
            if not self.plan:
                self.plan = self._load_plan()

            # Gather all data
            all_briefs = storage.read_file(f"{config.DIR_PLOT}/chapter_briefs.md") or ""
            characters = storage.read_file(f"{config.DIR_WORLDBUILDING}/characters.md") or ""
            hooks_info = storage.read_file(f"{config.DIR_META}/hooks_tracker.md") or ""

            total_chapters = storage.get_completed_chapter_count()
            total_words = 0
            for ch_file in storage.list_chapter_files():
                content = storage.read_file(f"{config.DIR_CHAPTERS}/{ch_file}")
                if content:
                    total_words += count_words(content)

            agent = FinalSummaryAgent()
            summary = agent.generate(
                plan=self.plan,
                all_briefs=all_briefs,
                characters=characters,
                hooks_info=hooks_info,
                total_chapters=total_chapters,
                total_words=total_words,
            )

            tpl = get_locale().TEMPLATES
            filename = tpl.get("final_summary_filename", "meta/final_summary.md")
            storage.write_file(filename, summary)
            print(ui["final_summary_done"])

        except Exception as e:
            print(ui["final_summary_failed"].format(error=e))

    # ==================== Full Workflow ====================
    def run_full(self):
        """Execute the complete creation pipeline."""
        ui = self._ui()

        if not self.phase_planning():
            print(ui["planning_incomplete"])
            return

        # Ask user to confirm/adjust writing parameters
        self._ask_writing_params()

        # Ask user for dialogue quote style preference
        self._select_quote_style()

        self.phase_worldbuilding()
        self.phase_master_outline()
        self.phase_volume_outline(1)
        self.phase_writing()

    def resume(self):
        """Resume writing from the last checkpoint."""
        ui = self._ui()
        print(ui["resume_checking"])

        if not storage.file_exists("plan.json"):
            print(ui["no_plan_found"])
            return self.run_full()

        self.plan = self._load_plan()
        self.style_guide = storage.read_file(f"{config.DIR_META}/style_guide.md")
        self.master_outline = storage.read_file(f"{config.DIR_PLOT}/master_outline.md")

        completed = storage.get_completed_chapter_count()
        print(ui["resume_completed"].format(count=completed))

        if not self.style_guide:
            print(ui["no_style_guide"])
            self.phase_worldbuilding()

        if not self.master_outline:
            print(ui["no_outline"])
            self.phase_master_outline()

        self.phase_writing(start_chapter=completed + 1)

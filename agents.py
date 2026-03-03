"""
Agent module - Implements all specialized agents.
Includes: PlannerAgent, OutlineAgent, WorldbuildingAgent, StyleGuideAgent,
          WriterAgent, PostWriteAgent, QualityReviewerAgent, PolishAgent,
          FinalSummaryAgent.
"""
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import config
import prompts
import storage
from llm_client import get_client
from exceptions import ContextLengthExceededError
from locales import get_locale


def _ui() -> dict:
    """Module-level shortcut for locale UI strings."""
    return get_locale().UI


def _extract_json(text: str) -> dict | None:
    """Extract JSON from LLM response text."""
    # Try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Try extracting from markdown code blocks
    patterns = [r'```json\s*(.*?)\s*```', r'```\s*(.*?)\s*```', r'\{.*\}']
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1) if '```' in pattern else match.group(0))
            except (json.JSONDecodeError, IndexError):
                continue
    return None


# ==================== Planner Agent ====================
class PlannerAgent:
    """Planner Agent - Collects info through multi-turn dialogue to determine novel settings."""

    def __init__(self):
        self.client = get_client()
        self.conversation_history = []
        self.collected_info = {
            "genre": False, "theme": False, "structure": False,
            "pov": False, "tags": False, "summary": False,
            "style": False, "characters": False, "world": False,
        }

    def start(self) -> str:
        """Start planning, return the first question."""
        return prompts.planner_first_question()

    def process_user_input(self, user_input: str) -> tuple[bool, str]:
        """
        Process user input. Returns (is_complete, agent_response).
        """
        ui = get_locale().UI
        self.conversation_history.append({"role": "user", "content": user_input})

        # Ask LLM to check if info is sufficient
        check_prompt = prompts.planner_check_enough(
            has_genre="✅" if self.collected_info["genre"] else "❌",
            has_theme="✅" if self.collected_info["theme"] else "❌",
            has_structure="✅" if self.collected_info["structure"] else "❌",
            has_pov="✅" if self.collected_info["pov"] else "❌",
            has_tags="✅" if self.collected_info["tags"] else "❌",
            has_summary="✅" if self.collected_info["summary"] else "❌",
            has_style="✅" if self.collected_info["style"] else "❌",
            has_characters="✅" if self.collected_info["characters"] else "❌",
            has_world="✅" if self.collected_info["world"] else "❌",
        )

        # Merge check_prompt into the last user message to ensure
        # strict user/assistant alternation in the message list.
        check_messages = list(self.conversation_history)
        if check_messages and check_messages[-1]["role"] == "user":
            check_messages[-1] = {
                "role": "user",
                "content": check_messages[-1]["content"] + "\n\n" + check_prompt,
            }
        else:
            check_messages.append({"role": "user", "content": check_prompt})

        check_response = self.client.chat(prompts.planner_system(), check_messages)
        if not check_response:
            return False, ui["llm_error_retry"]

        check_result = _extract_json(check_response)

        if check_result and check_result.get("is_enough", False):
            # Info is sufficient, proceed to summary stage.
            # Append assistant message to maintain strict user/assistant alternation,
            # so that subsequent workflow steps can safely append user messages.
            self.conversation_history.append({"role": "assistant", "content": ui["info_enough"]})
            return True, ui["info_enough"]
        else:
            # Not enough, continue asking questions
            if check_result and "next_questions" in check_result:
                response = check_result["next_questions"]
                # Update collected info status
                if check_result.get("missing_items"):
                    for item in list(self.collected_info.keys()):
                        if not any(item_name in str(check_result["missing_items"]).lower()
                                   for item_name in [item]):
                            self.collected_info[item] = True
            else:
                # JSON parse failed, fall back to direct conversation mode
                response = self.client.chat(
                    prompts.planner_system(),
                    self.conversation_history
                )
                if not response:
                    response = ui["continue_input"]

            self.conversation_history.append({"role": "assistant", "content": response})
            return False, response

    def generate_plan(self) -> dict:
        """Generate the final novel plan."""
        # Merge summarize prompt into the last user message if needed
        # to ensure strict user/assistant alternation.
        summary_messages = list(self.conversation_history)
        summarize_prompt = prompts.planner_summarize()
        if summary_messages and summary_messages[-1]["role"] == "user":
            summary_messages[-1] = {
                "role": "user",
                "content": summary_messages[-1]["content"] + "\n\n" + summarize_prompt,
            }
        else:
            summary_messages.append({"role": "user", "content": summarize_prompt})

        response = self.client.chat(prompts.planner_system(), summary_messages)
        if not response:
            raise RuntimeError("Plan generation failed")

        plan = _extract_json(response)
        if not plan:
            # Retry once
            response = self.client.chat(prompts.planner_system(), summary_messages)
            plan = _extract_json(response)
            if not plan:
                raise RuntimeError(f"Plan JSON parse failed, raw response:\n{response}")

        return plan


# ==================== Outline Agent ====================
class OutlineAgent:
    """Outline Agent - Generates master outline and volume-level outlines."""

    def __init__(self):
        self.client = get_client()

    def generate_master_outline(self, plan: dict) -> str:
        """Generate the master outline for the entire book (single draft mode)."""
        p = prompts.get_prompts()
        prompt = p["master_outline_prompt"].format(
            plan_json=json.dumps(plan, ensure_ascii=False, indent=2)
        )

        response = self.client.chat(
            prompts.outline_system(),
            [{"role": "user", "content": prompt}]
        )
        if not response:
            raise RuntimeError("Master outline generation failed")
        return response

    def generate_master_outline_multi(self, plan: dict) -> list[dict]:
        """
        Generate multiple outline drafts with different styles (feature #1).
        Returns a list of {"index": int, "style": str, "content": str}.
        """
        ui = _ui()
        p = prompts.get_prompts()
        plan_json = json.dumps(plan, ensure_ascii=False, indent=2)

        styles = [
            (ui["outline_style_dramatic"],
             "Focus on dramatic tension, high-stakes conflicts, shocking twists, and emotional peaks."),
            (ui["outline_style_literary"],
             "Focus on character depth, subtle themes, literary prose quality, and emotional nuance."),
            (ui["outline_style_commercial"],
             "Focus on fast pacing, page-turner hooks, clear plot momentum, and commercial appeal."),
        ]
        # Trim to configured draft count
        styles = styles[:config.OUTLINE_DRAFT_COUNT]

        drafts = []

        with ThreadPoolExecutor(max_workers=config.MAX_PARALLEL_WORKERS) as executor:
            future_to_style = {}
            for i, (style_name, style_instruction) in enumerate(styles, 1):
                print(ui["generating_draft"].format(num=i, total=len(styles), style=style_name))
                base_prompt = p["master_outline_prompt"].format(plan_json=plan_json)
                styled_prompt = f"{base_prompt}\n\n**Style Emphasis**: {style_instruction}"
                future = executor.submit(
                    self.client.chat,
                    prompts.outline_system(),
                    [{"role": "user", "content": styled_prompt}]
                )
                future_to_style[future] = (i, style_name)

            for future in as_completed(future_to_style):
                idx, style_name = future_to_style[future]
                try:
                    result = future.result()
                    if result:
                        drafts.append({"index": idx, "style": style_name, "content": result})
                        print(ui["draft_done"].format(num=idx))
                    else:
                        print(ui["draft_failed"].format(num=idx, error="empty response"))
                except Exception as e:
                    print(ui["draft_failed"].format(num=idx, error=e))

        # Sort by original index
        drafts.sort(key=lambda d: d["index"])
        return drafts

    @staticmethod
    def _estimate_tokens(text: str) -> int:
        """Rough token count estimation.
        CJK characters are counted at ~1.5 tokens/char,
        Latin characters at ~1 token / 4 chars.
        """
        cjk_count = 0
        latin_count = 0
        for ch in text:
            cp = ord(ch)
            # CJK Unified Ideographs + Hiragana + Katakana + Hangul + CJK extensions
            if (0x4E00 <= cp <= 0x9FFF or 0x3400 <= cp <= 0x4DBF
                    or 0x3040 <= cp <= 0x309F or 0x30A0 <= cp <= 0x30FF
                    or 0xAC00 <= cp <= 0xD7AF or 0x0E00 <= cp <= 0x0E7F):
                cjk_count += 1
            else:
                latin_count += 1
        return int(cjk_count * 1.5 + latin_count / 4) + 10  # +10 safety margin

    @staticmethod
    def _build_drafts_text(drafts: list[dict], truncate_ratio: float | None = None) -> str:
        """Concatenate draft texts. When truncate_ratio is None, no truncation is applied;
        otherwise each draft is truncated proportionally."""
        drafts_text = ""
        for d in drafts:
            header = f"\n\n{'=' * 40}\nDraft {d['index']} ({d['style']})\n{'=' * 40}\n"
            content = d["content"]
            if truncate_ratio is not None and 0 < truncate_ratio < 1.0:
                max_chars = int(len(content) * truncate_ratio)
                if max_chars < len(content):
                    content = content[:max_chars] + "\n\n... [truncated due to context window limit]"
            drafts_text += header + content
        return drafts_text

    def _calc_truncate_ratio(self, drafts: list[dict], system_prompt: str) -> float:
        """Calculate the truncation ratio (0~1) based on the token budget."""
        base_prompt = prompts.outline_merge_prompt(count=len(drafts), drafts_text="")
        base_tokens = self._estimate_tokens(system_prompt + base_prompt)
        header_tokens = self._estimate_tokens(
            f"\n\n{'=' * 40}\nDraft 1 (SomeStyle)\n{'=' * 40}\n"
        ) * len(drafts)

        available = config.MAX_INPUT_TOKENS - base_tokens - header_tokens - 500
        if available <= 0:
            available = 2000

        total_draft_tokens = sum(self._estimate_tokens(d["content"]) for d in drafts)
        if total_draft_tokens <= 0:
            return 1.0
        ratio = available / total_draft_tokens
        return min(ratio * 0.95, 1.0)  # leave 5% margin

    def merge_outlines(self, plan: dict, drafts: list[dict]) -> str:
        """Merge multiple outline drafts into one optimal outline.
        First attempts with full drafts; if a ContextLengthExceededError is raised,
        automatically truncates the drafts and retries once.
        """
        ui = _ui()
        system_prompt = prompts.outline_system()

        # ── First attempt: full drafts ──
        drafts_text = self._build_drafts_text(drafts)
        prompt = prompts.outline_merge_prompt(count=len(drafts), drafts_text=drafts_text)
        try:
            response = self.client.chat(system_prompt, [{"role": "user", "content": prompt}])
            if response:
                return response
        except ContextLengthExceededError as e:
            # ── Caught context-length-exceeded error → truncate and retry ──
            ratio = self._calc_truncate_ratio(drafts, system_prompt)
            if ratio < 1.0:
                total_est = sum(self._estimate_tokens(d["content"]) for d in drafts)
                budget_est = int(total_est * ratio)
                print(ui.get("outline_drafts_truncating",
                             "   ⚠️ Outline drafts too long ({total} est. tokens, budget {budget}), truncating each draft proportionally...")
                      .format(total=total_est, budget=budget_est))
                drafts_text = self._build_drafts_text(drafts, truncate_ratio=ratio)
                prompt = prompts.outline_merge_prompt(count=len(drafts), drafts_text=drafts_text)
                response = self.client.chat(system_prompt, [{"role": "user", "content": prompt}])
                if response:
                    return response
            # Still failed after truncation
            raise RuntimeError(f"Outline merge failed (context length exceeded: {e})") from e

        # ── First attempt failed for non-token-limit reasons ──
        raise RuntimeError("Outline merge failed")

    def generate_volume_outline(self, plan: dict, master_outline: str, volume_num: int,
                                volume_info: str) -> str:
        """Generate a detailed chapter-level outline for a single volume."""
        p = prompts.get_prompts()
        prompt = p["volume_outline_prompt"].format(
            volume_num=volume_num,
            title=plan.get("title", ""),
            genre=plan.get("genre", ""),
            chapter_words=plan.get("chapter_words", f"{config.CHAPTER_MIN_WORDS}-{config.CHAPTER_MAX_WORDS}"),
            volume_info=volume_info,
            master_outline=master_outline,
        )

        response = self.client.chat(
            prompts.volume_outline_system(),
            [{"role": "user", "content": prompt}]
        )
        if not response:
            raise RuntimeError(f"Volume {volume_num} outline generation failed")
        return response


# ==================== Worldbuilding Agent ====================
class WorldbuildingAgent:
    """Worldbuilding Agent - Generates world settings in parallel."""

    def __init__(self):
        self.client = get_client()

    def generate_all(self, plan: dict) -> dict[str, str]:
        """Generate all worldbuilding documents in parallel."""
        ui = get_locale().UI
        p = prompts.get_prompts()
        plan_text = json.dumps(plan, ensure_ascii=False, indent=2)

        tasks = {
            "world_setting.md": (
                prompts.worldbuilding_system(),
                p["task_world_setting"].format(plan_text=plan_text),
            ),
            "characters.md": (
                prompts.character_system(),
                p["task_characters"].format(plan_text=plan_text),
            ),
            "locations.md": (
                prompts.worldbuilding_system(),
                p["task_locations"].format(plan_text=plan_text),
            ),
            "timeline.md": (
                prompts.worldbuilding_system(),
                p["task_timeline"].format(plan_text=plan_text),
            ),
        }

        # Add special system settings based on genre
        genre = plan.get("genre", "").lower()
        world_setting = plan.get("world_setting", "").lower()
        combined = genre + world_setting
        fantasy_kw = p.get("genre_fantasy_keywords", [])
        scifi_kw = p.get("genre_scifi_keywords", [])

        if any(kw in combined for kw in fantasy_kw):
            tasks["power_system.md"] = (
                prompts.worldbuilding_system(),
                p["task_power_system"].format(plan_text=plan_text),
            )
        elif any(kw in combined for kw in scifi_kw):
            tasks["tech_system.md"] = (
                prompts.worldbuilding_system(),
                p["task_tech_system"].format(plan_text=plan_text),
            )

        results = {}
        print(ui["worldbuilding_start"].format(count=len(tasks)))

        with ThreadPoolExecutor(max_workers=config.MAX_PARALLEL_WORKERS) as executor:
            future_to_name = {}
            for filename, (sys_prompt, task_prompt) in tasks.items():
                future = executor.submit(
                    self.client.chat,
                    sys_prompt,
                    [{"role": "user", "content": task_prompt}]
                )
                future_to_name[future] = filename

            for future in as_completed(future_to_name):
                filename = future_to_name[future]
                try:
                    result = future.result()
                    if result:
                        results[filename] = result
                        print(ui["doc_done"].format(filename=filename))
                    else:
                        print(ui["doc_failed"].format(filename=filename))
                except Exception as e:
                    print(ui["doc_error"].format(filename=filename, error=e))

        return results


# ==================== Style Guide Agent ====================
class StyleGuideAgent:
    """Style Guide Agent - Generates writing style guidelines."""

    def __init__(self):
        self.client = get_client()

    def generate(self, plan: dict) -> str:
        """Generate the style guide document."""
        plan_text = json.dumps(plan, ensure_ascii=False, indent=2)
        p = prompts.get_prompts()
        prompt = p.get("task_style_guide",
                       f"Based on the following novel plan, generate a detailed writing style guide (Markdown).\n\nPlan:\n{plan_text}")

        response = self.client.chat(
            prompts.style_guide_system(),
            [{"role": "user", "content": prompt}]
        )
        if not response:
            raise RuntimeError("Style guide generation failed")
        return response


# ==================== Writer Agent ====================
class WriterAgent:
    """Writer Agent - Writes chapter text."""

    def __init__(self):
        self.client = get_client()

    def write_chapter(self, chapter_num: int, chapter_outline: str,
                      style_guide: str, recent_briefs: str,
                      character_status: str, hooks_info: str,
                      character_profiles: str = "",
                      world_setting: str = "",
                      review_feedback: str = "") -> str:
        """Write a single chapter. If review_feedback is provided, it is appended
        to the prompt so the writer can avoid previously identified issues."""
        # Inject quote style instruction into style guide
        quote_instruction = prompts.get_quote_style_instruction()
        effective_style_guide = style_guide
        if quote_instruction:
            heading = prompts.get_quote_rules_heading()
            effective_style_guide = style_guide + f"\n\n**{heading}**: {quote_instruction}"

        system = prompts.writer_system(
            style_guide=effective_style_guide,
            min_words=config.CHAPTER_MIN_WORDS,
            max_words=config.CHAPTER_MAX_WORDS,
        )

        # Build the "no previous" / "see profiles" fallback texts
        no_prev = "(First chapter, no previous text)"
        see_profiles = "(See character profiles)"
        no_hooks = "(No special foreshadowing requirements)"
        no_profiles = "(No character profiles available)"
        no_world = "(No world setting available)"

        user_prompt = prompts.writer_chapter_prompt(
            chapter_num=chapter_num,
            chapter_outline=chapter_outline,
            recent_briefs=recent_briefs or no_prev,
            character_status=character_status or see_profiles,
            hooks_info=hooks_info or no_hooks,
            character_profiles=character_profiles or no_profiles,
            world_setting=world_setting or no_world,
            min_words=config.CHAPTER_MIN_WORDS,
            max_words=config.CHAPTER_MAX_WORDS,
        )

        # Append review feedback from previous attempt so the writer avoids the same mistakes
        if review_feedback:
            user_prompt += "\n\n" + review_feedback

        response = self.client.chat(
            system,
            [{"role": "user", "content": user_prompt}],
            max_tokens=config.MAX_OUTPUT_TOKENS,
        )
        if not response:
            raise RuntimeError(f"Chapter {chapter_num} writing failed")
        return response

    def expand_chapter(self, chapter_text: str, chapter_outline: str,
                       style_guide: str, current_words: int, target_words: int) -> str:
        """Expand a chapter that is too short."""
        prompt = prompts.expand_chapter_prompt(
            current_words=current_words,
            target_words=target_words,
            style_guide=style_guide or "(no style guide)",
            chapter_outline=chapter_outline or "(no outline)",
            chapter_text=chapter_text,
        )
        response = self.client.chat(
            prompts.expand_chapter_system(),
            [{"role": "user", "content": prompt}],
            max_tokens=config.MAX_OUTPUT_TOKENS,
        )
        if not response:
            raise RuntimeError("Chapter expansion failed")
        return response

    def compress_chapter(self, chapter_text: str, chapter_outline: str,
                         style_guide: str, current_words: int, target_words: int) -> str:
        """Compress a chapter that is too long."""
        prompt = prompts.compress_chapter_prompt(
            current_words=current_words,
            target_words=target_words,
            style_guide=style_guide or "(no style guide)",
            chapter_outline=chapter_outline or "(no outline)",
            chapter_text=chapter_text,
        )
        response = self.client.chat(
            prompts.compress_chapter_system(),
            [{"role": "user", "content": prompt}],
            max_tokens=config.MAX_OUTPUT_TOKENS,
        )
        if not response:
            raise RuntimeError("Chapter compression failed")
        return response

    def split_chapter(self, chapter_text: str, chapter_outline: str,
                      style_guide: str, current_words: int,
                      chapter_num_a: int, chapter_num_b: int) -> tuple[str, str]:
        """Split a chapter that is far too long into two chapters.
        Returns (chapter_a_text, chapter_b_text).
        """
        target_words = (config.CHAPTER_MIN_WORDS + config.CHAPTER_MAX_WORDS) // 2
        prompt = prompts.split_chapter_prompt(
            current_words=current_words,
            min_words=config.CHAPTER_MIN_WORDS,
            max_words=config.CHAPTER_MAX_WORDS,
            target_words=target_words,
            style_guide=style_guide or "(no style guide)",
            chapter_outline=chapter_outline or "(no outline)",
            chapter_text=chapter_text,
            chapter_num_a=chapter_num_a,
            chapter_num_b=chapter_num_b,
        )
        response = self.client.chat(
            prompts.split_chapter_system(),
            [{"role": "user", "content": prompt}],
            max_tokens=config.MAX_OUTPUT_TOKENS,
        )
        if not response:
            raise RuntimeError("Chapter split failed")

        # Parse the split response
        separator = "===CHAPTER_SPLIT==="
        if separator in response:
            parts = response.split(separator, 1)
            return parts[0].strip(), parts[1].strip()
        else:
            # Fallback: try to split at roughly the midpoint by paragraphs
            paragraphs = response.split("\n\n")
            mid = len(paragraphs) // 2
            part_a = "\n\n".join(paragraphs[:mid])
            part_b = "\n\n".join(paragraphs[mid:])
            return part_a.strip(), part_b.strip()


# ==================== Post-Write Agent ====================
class PostWriteAgent:
    """Post-Write Agent - Generates chapter summaries and updates metadata after writing."""

    def __init__(self):
        self.client = get_client()

    def analyze_chapter(self, chapter_num: int, chapter_text: str,
                        chapter_outline: str) -> dict | None:
        """Analyze chapter content and generate summary + update data."""
        p = prompts.get_prompts()
        prompt = p["analyze_chapter_prompt"].format(
            chapter_outline=chapter_outline,
            chapter_text=chapter_text,
        )

        response = self.client.chat(
            prompts.post_write_system(),
            [{"role": "user", "content": prompt}]
        )
        if not response:
            return None

        return _extract_json(response)

    def update_files(self, chapter_num: int, analysis: dict):
        """Update metadata files based on chapter analysis."""
        ui = get_locale().UI
        tpl = get_locale().TEMPLATES
        brief = analysis.get("chapter_brief", {})
        progress = analysis.get("progress_update", {})

        # Update chapter briefs
        if brief:
            brief_text = tpl["chapter_brief_entry"].format(
                chapter_num=chapter_num,
                title=brief.get("title", ""),
                word_count=brief.get("word_count", "?"),
            )
            for event in brief.get("main_events", []):
                brief_text += f"- {event}\n"

            if brief.get("character_changes"):
                brief_text += tpl["character_changes_header"]
                for change in brief["character_changes"]:
                    brief_text += f"- {change}\n"

            if brief.get("hooks_planted"):
                brief_text += tpl["hooks_planted_header"]
                for hook in brief["hooks_planted"]:
                    brief_text += f"- {hook}\n"

            if brief.get("next_chapter_hook"):
                brief_text += tpl["next_hook_prefix"] + brief["next_chapter_hook"] + "\n"

            storage.append_file(f"{config.DIR_PLOT}/chapter_briefs.md", brief_text)

        # Update progress file
        if progress:
            update_text = tpl["progress_update_entry"].format(
                chapter_num=chapter_num,
                latest_chapter=progress.get("latest_chapter", f"Chapter {chapter_num}"),
                total_words=progress.get("total_words", "?"),
            )

            if progress.get("character_status"):
                update_text += tpl["character_status_header"]
                for name, status in progress["character_status"].items():
                    update_text += f"- **{name}**: {status}\n"

            storage.append_file(f"{config.DIR_META}/progress.md", update_text)

        print(ui["post_done"].format(num=chapter_num))


# ==================== Quality Reviewer Agent (Feature #2 + #5) ====================
class QualityReviewerAgent:
    """
    Quality Reviewer Agent - Runs parallel multi-perspective reviews on chapters.
    Uses confidence-based severity filtering (feature #5).
    """

    def __init__(self):
        self.client = get_client()

    def review_chapter(
        self,
        chapter_text: str,
        chapter_outline: str,
        style_guide: str,
        recent_briefs: str,
        hooks_info: str,
        character_profiles: str = "",
    ) -> list[dict]:
        """
        Run parallel reviews from 3 perspectives: consistency, style, foreshadowing.
        Returns aggregated list of issues above the confidence threshold.
        """
        ui = _ui()
        print(ui["parallel_review_title"])

        review_prompt_text = prompts.review_chapter_prompt(
            style_guide=style_guide or "(no style guide)",
            chapter_outline=chapter_outline or "(no outline)",
            recent_briefs=recent_briefs or "(no previous chapters)",
            hooks_info=hooks_info or "(no hooks)",
            chapter_text=chapter_text,
            character_profiles=character_profiles or "(no character profiles available)",
        )

        reviewers = [
            (ui["review_consistency"], prompts.consistency_reviewer_system()),
            (ui["review_style"], prompts.style_reviewer_system()),
            (ui["review_foreshadowing"], prompts.foreshadowing_reviewer_system()),
        ]

        all_issues = []
        threshold = config.REVIEW_CONFIDENCE_THRESHOLD

        with ThreadPoolExecutor(max_workers=3) as executor:
            future_to_reviewer = {}
            for reviewer_name, system_prompt in reviewers:
                future = executor.submit(
                    self.client.chat,
                    system_prompt,
                    [{"role": "user", "content": review_prompt_text}]
                )
                future_to_reviewer[future] = reviewer_name

            for future in as_completed(future_to_reviewer):
                reviewer_name = future_to_reviewer[future]
                try:
                    result = future.result()
                    if result:
                        parsed = _extract_json(result)
                        if parsed and "issues" in parsed:
                            # Filter by confidence threshold
                            filtered = [
                                issue for issue in parsed["issues"]
                                if issue.get("confidence", 0) >= threshold
                            ]
                            for issue in filtered:
                                issue["reviewer"] = reviewer_name
                            all_issues.extend(filtered)
                            print(ui["review_done"].format(
                                reviewer=reviewer_name,
                                count=len(filtered),
                                threshold=threshold,
                            ))
                        else:
                            print(ui["review_done"].format(
                                reviewer=reviewer_name, count=0, threshold=threshold,
                            ))
                    else:
                        print(ui["review_failed"].format(
                            reviewer=reviewer_name, error="empty response"
                        ))
                except Exception as e:
                    print(ui["review_failed"].format(reviewer=reviewer_name, error=e))

        # Sort by severity (critical > major > minor > info)
        severity_order = {"critical": 0, "major": 1, "minor": 2, "info": 3}
        all_issues.sort(key=lambda x: severity_order.get(x.get("severity", "info"), 4))

        return all_issues


# ==================== Polish Agent (Feature #3) ====================
class PolishAgent:
    """
    Polish Agent - Self-iterating chapter refinement loop.
    Evaluates quality -> applies improvements -> re-evaluates until threshold is met.
    """

    def __init__(self):
        self.client = get_client()

    def evaluate(self, chapter_text: str, chapter_outline: str,
                 style_guide: str) -> dict | None:
        """Evaluate chapter quality and return score + improvement suggestions."""
        prompt = prompts.polish_evaluate_prompt(
            style_guide=style_guide or "(no style guide)",
            chapter_outline=chapter_outline or "(no outline)",
            chapter_text=chapter_text,
        )
        response = self.client.chat(
            prompts.polish_evaluate_system(),
            [{"role": "user", "content": prompt}]
        )
        if not response:
            return None
        return _extract_json(response)

    def improve(self, chapter_text: str, evaluation: dict) -> str | None:
        """Rewrite the chapter based on evaluation feedback."""
        weaknesses = "\n".join(f"- {w}" for w in evaluation.get("weaknesses", []))
        improvements = ""
        for imp in evaluation.get("specific_improvements", []):
            improvements += (
                f"- [{imp.get('location', '?')}] "
                f"{imp.get('current', '')} -> {imp.get('suggested', '')}\n"
            )

        prompt = prompts.polish_improve_prompt(
            weaknesses=weaknesses or "(none specified)",
            improvements=improvements or "(no specific improvements)",
            chapter_text=chapter_text,
        )
        response = self.client.chat(
            prompts.polish_improve_system(),
            [{"role": "user", "content": prompt}],
            max_tokens=config.MAX_OUTPUT_TOKENS,
        )
        return response

    def polish_loop(self, chapter_text: str, chapter_outline: str,
                    style_guide: str) -> tuple[str, int]:
        """
        Run the polish loop: evaluate -> improve -> re-evaluate until quality threshold.
        Returns (final_text, final_score).
        """
        ui = _ui()
        max_iter = config.MAX_POLISH_ITERATIONS
        threshold = config.POLISH_QUALITY_THRESHOLD
        print(ui["polish_start"].format(max_iter=max_iter))

        best_text = chapter_text
        best_score = 0

        for iteration in range(1, max_iter + 1):
            print(ui["polish_iteration"].format(iter=iteration, max_iter=max_iter))

            evaluation = self.evaluate(best_text, chapter_outline, style_guide)
            if not evaluation:
                print(ui["polish_failed"])
                return best_text, best_score

            score = evaluation.get("score", 0)
            print(ui["polish_score"].format(score=score, threshold=threshold))

            if score >= threshold:
                print(ui["polish_passed"])
                return best_text, score

            if score > best_score:
                best_score = score

            # Apply improvements
            print(ui["polish_improving"])
            improved = self.improve(best_text, evaluation)
            if improved:
                best_text = improved
            else:
                print(ui["polish_failed"])
                return best_text, best_score

        # Final evaluation after last improvement
        final_eval = self.evaluate(best_text, chapter_outline, style_guide)
        if final_eval:
            best_score = final_eval.get("score", best_score)

        print(ui["polish_max_reached"].format(score=best_score))
        return best_text, best_score


# ==================== Final Summary Agent (Feature #6) ====================
class FinalSummaryAgent:
    """Final Summary Agent - Generates a comprehensive report after the novel is complete."""

    def __init__(self):
        self.client = get_client()

    def generate(self, plan: dict, all_briefs: str, characters: str,
                 hooks_info: str, total_chapters: int, total_words: int) -> str:
        """Generate the final novel summary report."""
        prompt = prompts.final_summary_prompt(
            plan_json=json.dumps(plan, ensure_ascii=False, indent=2),
            all_briefs=all_briefs or "(no chapter summaries available)",
            characters=characters or "(no character profiles available)",
            hooks_info=hooks_info or "(no hooks tracker available)",
            total_chapters=total_chapters,
            total_words=total_words,
        )
        response = self.client.chat(
            prompts.final_summary_system(),
            [{"role": "user", "content": prompt}],
        )
        if not response:
            raise RuntimeError("Final summary generation failed")
        return response

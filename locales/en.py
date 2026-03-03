"""
English locale - Base reference language file.
All other locale files should have the same structure.
"""

# ============================================================
# UI: All user-facing interface strings
# ============================================================
UI = {
    # -- main.py --
    "welcome_title": "📖 Novel Agent Workflow v1.0",
    "welcome_subtitle": "   AI-Powered Novel Writing System",
    "no_backend": "\n❌ No available LLM backend!",
    "no_backend_hint": "   Please ensure at least one of llm_openai.py or llm_local.py exists",
    "select_api_mode": "\n🔌 Select LLM API mode:",
    "api_openai_desc": "OpenAI Standard Format (requires API Key)",
    "api_local_desc": "Local stream-server API",
    "auto_selected": "\n  (Only detected {desc}, auto-selected)",
    "input_choice": "\n👤 Enter your choice (1-{max}): ",
    "invalid_choice": "Invalid choice, please enter 1-{max}",
    "input_openai_key": "Enter OpenAI API Key: ",
    "api_key_empty": "API Key cannot be empty!",
    "input_base_url": "API Base URL (press Enter for default: {default}): ",
    "input_model": "Model name (press Enter for default: {default}): ",
    "input_local_url": "Enter local API address: ",
    "api_url_empty": "API address cannot be empty!",
    "input_api_key": "Enter API Key (press Enter to skip): ",
    "input_wsid": "Enter WSID (press Enter to skip): ",
    "input_model_marker": "Enter model marker (press Enter to skip): ",
    "project_setup": "\n📁 Project Setup",
    "input_novel_name": "👤 Enter novel project name (used to create folder): ",
    "scan_projects_header": "\n📂 Existing projects found:",
    "no_existing_projects": "\n📂 No existing projects found.",
    "project_status_chapters": "{count} ch.",
    "project_status_plan": "plan",
    "project_status_meta": "meta",
    "project_status_plot": "outline",
    "or_input_manually": "Enter project name manually...",
    "select_project_prompt": "\n👤 Select a project (1-{max}): ",
    "select_operation": "\n🎯 Select operation:",
    "op_full": "  1. Start from scratch (full workflow)",
    "op_resume": "  2. Resume from checkpoint",
    "op_planning": "  3. Planning phase only",
    "op_worldbuilding": "  4. Generate worldbuilding & style guide only",
    "op_outline": "  5. Generate outline only",
    "op_writing": "  6. Writing only (requires existing outline)",
    "op_batch": "  7. Batch mode (generate multiple novels)",
    "input_op_choice": "\n👤 Enter your choice (1-7): ",
    "invalid_op": "Invalid choice, please enter 1-7",
    "input_volume_num": "Generate outline for which volume? (enter number, or press Enter to skip): ",
    "input_start_chapter": "Start from which chapter? (press Enter to start from chapter 1): ",
    "input_end_chapter": "Write until which chapter? (press Enter to write to the end): ",
    "interrupted": "\n\n⏸️ User interrupted. Progress saved. Choose 'Resume from checkpoint' next time.",
    "error_occurred": "\n❌ Error occurred: {error}",
    "goodbye": "\n👋 Goodbye!",

    # -- Batch mode --
    "batch_input_names": "\n📚 Enter novel names separated by commas (e.g. novel_A, novel_B, novel_C):",
    "batch_empty": "❌ No novel names provided, returning to main menu.",
    "batch_select_op": "\n🎯 Select operation for each novel:",
    "batch_start": "\n🚀 Batch mode: will generate {total} novel(s) in order: {names}",
    "batch_progress": "📖 [{current}/{total}] Starting novel: {name}",
    "batch_novel_done": "✅ Novel '{name}' completed!",
    "batch_interrupted": "\n⏸️ Interrupted while writing '{name}'. {remaining} novel(s) remaining.",
    "batch_continue_prompt": "Continue with remaining novels? (y/n): ",
    "batch_stopped": "🛑 Batch stopped by user.",
    "batch_novel_error": "\n❌ Error on novel '{name}': {error}",
    "batch_all_done": "\n🎉 Batch complete! All {total} novel(s) finished.",

    # -- Language selection --
    "select_language": "\n🌐 Select the language for your novel:",
    "lang_choice_prompt": "\n👤 Enter your choice (1-{max}): ",

    # -- workflow.py --
    "phase_planning_title": "\n📝 Phase 1: Novel Planning",
    "planner_prefix": "\n🤖 Planning Assistant:\n",
    "user_prefix": "👤 You: ",
    "input_empty_hint": "(Please enter your response)",
    "multiline_hint": "(Multi-line input supported; blank line to finish. Type /paste for paste mode)",
    "multiline_paste_hint": "(Paste mode: freely paste content with blank lines, type /end to finish)",
    "quit_planning": "Exited planning phase.",
    "force_done": "Alright, let me compile the plan...",
    "generating_plan": "\n⏳ Generating complete novel plan...",
    "plan_display_title": "\n📋 Novel Plan",
    "plan_label_title": "Title",
    "plan_label_genre": "Genre",
    "plan_label_theme": "Core Theme",
    "plan_label_target_words": "Target Word Count",
    "plan_label_total_chapters": "Estimated Chapters",
    "plan_label_volumes": "Volumes",
    "plan_label_pov": "POV",
    "plan_label_tags": "Tags",
    "plan_label_one_line": "One-line Summary",
    "plan_label_beginning": "Beginning",
    "plan_label_middle": "Middle",
    "plan_label_end": "End",
    "plan_label_characters": "Main Characters",
    "confirm_plan": "\n👤 Satisfied with this plan? (y/revision notes): ",
    "adjusting_plan": "\n⏳ Adjusting plan based on your feedback...",
    "plan_confirmed": "✅ Plan confirmed and saved!",
    "rename_dir_prompt": "\n📁 Novel title is \"{title}\", but the project directory is \"{dir}\".",
    "rename_dir_confirm": "   Rename project directory to \"{title}\"? (y/n): ",
    "rename_dir_done": "  ✅ Project directory renamed to: {path}",
    "rename_dir_exists": "  ⚠️ Directory already exists: {path}",
    "rename_dir_failed": "  ❌ Failed to rename directory: {error}",
    "phase_world_title": "\n🌍 Phase 2: Worldbuilding & Style Guide (generating in parallel...)",
    "world_done": "✅ Worldbuilding complete ({count} documents)",
    "world_failed": "❌ Worldbuilding failed: {error}",
    "style_done": "✅ Style guide generated",
    "style_failed": "❌ Style guide generation failed: {error}",
    "phase_outline_title": "\n📋 Phase 3: Master Outline Generation",
    "generating_outline": "⏳ Generating master outline...",
    "outline_done": "✅ Master outline generated",
    "outline_review": "\n📖 Master outline saved to plot/master_outline.md. Please review.",
    "press_enter_continue": "👤 Press Enter to continue generating Volume 1 outline...",
    "generating_volume": "📑 Generating Volume {num} outline...",
    "volume_done": "✅ Volume {num} outline generated",
    "phase_writing_title": "\n✍️ Phase 5: Writing",
    "checkpoint_resume": "[Checkpoint] Detected {count} completed chapters, resuming from chapter {next}",
    "volume_not_found": "⚠️ Volume {num} outline not found, generating...",
    "generating_volume_outline": "⏳ Generating Volume {num} outline...",
    "writing_chapter": "📖 Writing Chapter {num}...",
    "chapter_done": "  ✅ Chapter {num} complete (~{words} characters)",
    "post_processing": "  ⏳ Analyzing and updating metadata...",
    "post_done": "  ✅ Chapter {num} post-processing complete",
    "post_failed": "  ⚠️ Chapter {num} post-processing analysis failed, skipping update",
    "chapter_error": "  ❌ Error writing Chapter {num}: {error}",
    "retry_prompt": "  Retry? (y/n): ",
    "skip_chapter": "  Skipping Chapter {num}, continuing to next",
    "pause_prompt": "\n📊 Completed {num} chapters. Press Enter to continue, or type 'stop' to pause",
    "pause_input": "👤 ",
    "paused": "⏸️ Paused. Resume from chapter {next} next time",
    "writing_complete": "🎉 Writing phase complete!",
    "planning_incomplete": "Planning phase not completed, exiting.",
    "no_plan_found": "Plan not found, starting from scratch...",
    "resume_checking": "🔄 Checking project status...",
    "resume_completed": "Completed {count} chapters, continuing...",
    "no_style_guide": "Style guide not found, generating...",
    "no_outline": "Master outline not found, generating...",
    "plan_not_found_error": "Plan file plan.json not found. Please run the planning phase first.",

    # -- agents.py --
    "worldbuilding_start": "[Worldbuilding Agent] Generating {count} setting documents in parallel...",
    "doc_done": "  ✅ {filename} generated",
    "doc_failed": "  ❌ {filename} generation failed",
    "doc_error": "  ❌ {filename} error: {error}",
    "llm_error_retry": "Sorry, something went wrong. Please say that again~",
    "info_enough": "Great, I have enough information! Let me compile a complete novel plan... 🎯",
    "continue_input": "Please tell me more about the novel you want to create~",

    # -- config.py --
    "config_loaded": "[Config] Loaded settings from {file}: {keys}",
    "novel_config_loaded": "[Config] Loaded per-novel config from {file}: {keys}",
    "novel_config_skipped": "  ⚠️ Skipped API/path keys in {file} (use global config): {keys}",
    "novel_config_auto_created": "[Config] Auto-created {file} from template (edit to customize this novel's settings)",
"config_not_found": "[Config] {file} not found. Settings will use defaults; API keys must be entered at runtime.",
    "config_hint": "[Config] Refer to user_config.example.json to create {file}",
    "project_initialized": "[Project] Directory initialized: {path}",

    # -- llm backends --
    "openai_initialized": "[LLM-OpenAI] Initialized, model: {model}, Base URL: {url}",
    "openai_need_package": "OpenAI backend requires the openai package: pip install openai",
"openai_no_key": "OPENAI_API_KEY not configured. Please set it in user_config.json or enter at runtime.",
    "openai_attempt_failed": "[LLM-OpenAI] Attempt {n} failed: {error}",
    "openai_retry_wait": "[LLM-OpenAI] Retrying in {wait}s...",
    "openai_max_retries": "[LLM-OpenAI] Max retries ({max}) reached, giving up",
    "local_initialized": "[LLM-Local] Initialized, URL: {url}, model marker: {marker}",
    "local_need_package": "Local backend requires the requests package: pip install requests",
"local_no_url": "LOCAL_API_URL not configured. Please set it in user_config.json.",
    "local_attempt_failed": "[LLM-Local] Attempt {n} failed: {error}",
    "local_retry_wait": "[LLM-Local] Retrying in {wait}s...",
    "local_max_retries": "[LLM-Local] Max retries ({max}) reached, giving up",
    "cannot_load_openai": "Cannot load OpenAI backend: {error}\nPlease ensure llm_openai.py exists and openai is installed (pip install openai)",
    "cannot_load_local": "Cannot load local backend: {error}\nPlease ensure llm_local.py exists and requests is installed (pip install requests)",
    "unsupported_api_mode": "Unsupported API mode: {mode}. Available: 'openai', 'local'",

    # -- storage.py --
    "file_written": "[Storage] Written: {path}",

    # -- Feature #1: Multi-draft outline comparison --
    "outline_multi_draft_title": "\n📋 Phase 3: Master Outline Generation (Multi-Draft Comparison)",
    "generating_draft": "  ⏳ Generating outline draft {num}/{total} (style: {style})...",
    "draft_done": "  ✅ Draft {num} complete",
    "draft_failed": "  ❌ Draft {num} failed: {error}",
    "draft_comparison_title": "\n📊 Outline Draft Comparison",
    "draft_header": "\n{'─' * 40}\n📄 Draft {num} — Style: {style}\n{'─' * 40}",
    "draft_select_prompt": "\n👤 Select draft to use (1-{max}), or type 'm' to merge the best parts: ",
    "draft_merging": "⏳ Merging the best elements from all drafts...",
    "draft_selected": "✅ Draft {num} selected as master outline",
    "draft_merged": "✅ Merged outline generated",
    "outline_drafts_truncating": "   ⚠️ Outline drafts too long ({total} est. tokens, budget {budget}), truncating each draft proportionally...",
    "draft_invalid": "Invalid choice, please enter 1-{max} or 'm'",

    # -- Feature #2: Parallel quality review --
    "parallel_review_title": "  🔍 Running parallel quality review...",
    "review_consistency": "[Consistency Reviewer]",
    "review_style": "[Style Reviewer]",
    "review_foreshadowing": "[Foreshadowing Reviewer]",
    "review_done": "  ✅ {reviewer}: {count} issue(s) found (confidence ≥{threshold})",
    "review_failed": "  ⚠️ {reviewer} review failed: {error}",
    "review_no_issues": "  ✅ All reviewers passed — no significant issues!",
    "review_issues_found": "  ⚠️ {count} issue(s) found across all reviewers:",
    "review_issue_item": "    [{severity}] ({reviewer}, confidence: {confidence}) {description}",
    "review_critical_prompt": "  🚨 Critical issues found. Retry chapter? (y/n): ",

    # -- Feature #3: Polish loop --
    "polish_start": "  ✨ Starting polish loop (max {max_iter} iterations)...",
    "polish_iteration": "  ✨ Polish iteration {iter}/{max_iter}...",
    "polish_score": "  📊 Quality score: {score}/10 (threshold: {threshold})",
    "polish_passed": "  ✅ Quality threshold met! Exiting polish loop.",
    "polish_improving": "  ⏳ Score below threshold, applying improvements...",
    "polish_max_reached": "  ⚠️ Max polish iterations reached. Using best version (score: {score}/10).",
    "polish_failed": "  ⚠️ Polish evaluation failed, keeping current version.",

    # -- Feature #4: Mid-volume checkpoint --
    "volume_checkpoint_title": "\n📍 Volume {num} Checkpoint",
    "volume_checkpoint_summary": "  Summary so far: {completed} chapters completed, ~{words} words",
    "volume_checkpoint_prompt": "\n👤 About to begin Volume {num}. Continue? (y / adjust / stop): ",
    "volume_checkpoint_adjust": "👤 Enter your adjustment notes: ",
    "volume_checkpoint_adjusting": "⏳ Adjusting volume outline based on your feedback...",
    "volume_checkpoint_stopped": "⏸️ Stopped before Volume {num}. Resume from chapter {next} next time.",

    # -- Feature #5: Confidence-based severity --
    "severity_critical": "CRITICAL",
    "severity_major": "MAJOR",
    "severity_minor": "MINOR",
    "severity_info": "INFO",

    # -- Feature #6: Final summary --
    "final_summary_title": "\n📊 Generating Final Novel Summary...",
    "final_summary_done": "✅ Final summary generated and saved!",
    "final_summary_failed": "⚠️ Final summary generation failed: {error}",

    # -- Writing parameters confirmation --
    "writing_params_title": "\n⚙️ Writing Parameters Confirmation",
    "ask_chapter_min_words": "   Min words per chapter (current: {current}, Enter to keep): ",
    "ask_chapter_max_words": "   Max words per chapter (current: {current}, Enter to keep): ",
    "writing_params_swapped": "   ⚠️ Min > Max detected, values swapped.",
    "ask_word_count_check": "   Enable word count check? (current: {status}, y/n, Enter to keep): ",
    "ask_lazy_mode": "   Enable lazy mode (auto-confirm everything)? (current: {status}, y/n, Enter to keep): ",
    "writing_params_summary": "   ✅ Writing params: {min}-{max} words/chapter, word count check: {check}, lazy mode: {lazy}",

    # -- Quote style preference --
    "quote_style_title": "\n💬 Dialogue Quote Style Preference",
    "quote_style_prompt": "\n👤 Select dialogue quote style for your novel (1-{max}): ",
    "quote_style_invalid": "Invalid choice, please enter 1-{max}",
    "quote_style_selected": "✅ Dialogue quote style set to: {style}",
    "quote_style_option_curly": '\u201c\u201d double curly quotes (e.g. \u201cHello!\u201d)',
    "quote_style_option_corner": '\u300c\u300d corner brackets (e.g. \u300cHello!\u300d)',
    "quote_style_option_guillemet": '\u00ab\u00bb guillemets (e.g. \u00abHello!\u00bb)',
    "quote_style_option_dash": '\u2014 em-dash for dialogue (e.g. \u2014 Hello!)',
    "quote_style_option_straight": '"" straight double quotes (e.g. "Hello!")',

    # -- Inner thought quote style --
    "inner_quote_title": "\n💭 Inner Thought / Internal Monologue Quote Style",
    "inner_quote_prompt": "\n👤 Select the style for inner thoughts in your novel (1-{max}): ",
    "inner_quote_invalid": "Invalid choice, please enter 1-{max}",
    "inner_quote_selected": "✅ Inner thought style set to: {style}",
    "inner_quote_option_corner_double": '\u300e\u300f double corner brackets (e.g. \u300eI must be careful\u300f)',
    "inner_quote_option_corner": '\u300c\u300d corner brackets (e.g. \u300cI must be careful\u300d)',
    "inner_quote_option_curly_single": '\u2018\u2019 single curly quotes (e.g. \u2018I must be careful\u2019)',
    "inner_quote_option_italic": '*italic* for thoughts (e.g. *I must be careful*)',
    "inner_quote_option_dash": '\u2014\u2014 double em-dash (e.g. \u2014\u2014I must be careful\u2014\u2014)',
    "inner_quote_option_paren": '（）fullwidth parentheses (e.g. （I must be careful）)',
    "inner_quote_option_same": 'Same as dialogue quotes',
    "inner_quote_option_none": 'No special markers (describe thoughts narratively)',

    # -- Quote style rules (injected into style guide / writer prompt) --
    "quote_rules_heading": "Quote Style Rules",
    "quote_rule_dialogue_curly": 'Use \u201c\u201d (curly double quotes) for all dialogue. Example: \u201cHello!\u201d',
    "quote_rule_dialogue_corner": 'Use \u300c\u300d (corner brackets) for all dialogue. Example: \u300cHello!\u300d',
    "quote_rule_dialogue_guillemet": 'Use \u00ab\u00bb (guillemets) for all dialogue. Example: \u00abHello!\u00bb',
    "quote_rule_dialogue_dash": 'Use \u2014 (em-dash) to introduce dialogue. Example: \u2014 Hello!',
    "quote_rule_dialogue_straight": 'Use "" (straight double quotes) for all dialogue. Example: "Hello!"',
    "quote_rule_inner_corner_double": 'Use \u300e\u300f (double corner brackets) for inner thoughts / internal monologue. Example: \u300eI must be careful\u300f',
    "quote_rule_inner_corner": 'Use \u300c\u300d (corner brackets) for inner thoughts / internal monologue. Example: \u300cI must be careful\u300d',
    "quote_rule_inner_curly_single": 'Use \u2018\u2019 (single curly quotes) for inner thoughts / internal monologue. Example: \u2018I must be careful\u2019',
    "quote_rule_inner_italic": 'Use *italic* markers for inner thoughts / internal monologue. Example: *I must be careful*',
    "quote_rule_inner_dash": 'Use \u2014\u2014 (double em-dash) for inner thoughts / internal monologue. Example: \u2014\u2014I must be careful\u2014\u2014',
    "quote_rule_inner_paren": 'Use （）(fullwidth parentheses) for inner thoughts / internal monologue. Example: （I must be careful）',
    "quote_rule_inner_none": 'Do NOT use any special quote marks for inner thoughts. Instead, describe thoughts narratively.',
    "quote_rule_inner_same": 'Use the same quote style as dialogue for inner thoughts / internal monologue.',

    # -- Lazy mode --
    "lazy_mode_enabled": "🛋️ Lazy mode ON — all interactions after outline will be automatic!",
    "lazy_auto_merge": "🛋️ [Lazy] Auto-merging all outline drafts...",
    "lazy_auto_select": "🛋️ [Lazy] Only one draft available, auto-selected.",
    "lazy_auto_continue": "🛋️ [Lazy] Auto-continuing...",
    "lazy_auto_retry": "🛋️ [Lazy] Auto-retrying...",
    "lazy_auto_skip": "🛋️ [Lazy] Auto-skipping...",
    "lazy_auto_volume_continue": "🛋️ [Lazy] Auto-continuing to Volume {num}...",

    # -- Review retry --
    "review_retry_feedback": """⚠️ IMPORTANT: This is rewrite attempt {attempt}/{max_attempts}. The previous version had the following critical/major issues that MUST be fixed:
{issues}

Please rewrite the ENTIRE chapter from scratch, ensuring ALL the above issues are corrected while maintaining the story, tone, and structure.""",
    "review_max_retries_reached": "  ⚠️ Max review retries ({max}) reached for chapter {num}. Saving current version and continuing.",

    # -- Word count validation --
    "wordcount_check_start": "  📏 Word count validation: {words} words (target: {min}-{max})",
    "wordcount_too_short": "  ⚠️ Chapter too short ({words} words, minimum {min}). Expanding...",
    "wordcount_too_long": "  ⚠️ Chapter too long ({words} words, maximum {max}). Compressing...",
    "wordcount_split_needed": "  📑 Chapter far too long ({words} words, ≥{threshold}% of max). Splitting into two chapters...",
    "wordcount_expand_done": "  ✅ Expansion complete: {words} words",
    "wordcount_compress_done": "  ✅ Compression complete: {words} words",
    "wordcount_split_done": "  ✅ Split complete: Chapter {num_a} ({words_a} words) + Chapter {num_b} ({words_b} words)",
    "wordcount_retry": "  🔄 Word count retry {attempt}/{max_attempts}...",
    "wordcount_give_up": "  ⚠️ Word count still out of range after {max_attempts} retries. Using current version ({words} words).",
    "wordcount_ok": "  ✅ Word count OK: {words} words",
    "wordcount_split_renumber": "  📝 Note: Chapters after split will be renumbered automatically.",

    # -- Feature #1: Multi-draft outline styles --
    "outline_style_dramatic": "Dramatic & High-Tension",
    "outline_style_literary": "Literary & Character-Driven",
    "outline_style_commercial": "Commercial & Fast-Paced",
}

# ============================================================
# PROMPTS: All LLM prompt templates
# ============================================================
PROMPTS = {
    # -- Planner Agent --
    "planner_system": """You are a senior novel planning editor, skilled at conceiving a novel from scratch.
Your task is to collect enough information through conversation with the user to determine the following core elements:

1. **Genre/Type**: Fantasy, Urban, Mystery, Romance, Sci-Fi, etc.
2. **Core Theme**: What the novel aims to express
3. **Target Word Count & Structure**: Total words, words per chapter, estimated chapters, volumes
4. **Narrative POV**: First person / Third person
5. **Core Tags**: 3-5 key tags
6. **One-line Summary**: A single sentence that encapsulates the entire book
7. **Three-act Summary**: Beginning, middle, and end overview
8. **Writing Style**: Style, tone, reference works
9. **Taboos**: Content that must not appear
10. **Main Characters**: At least basic settings for protagonist(s)
11. **World Framework**: The world/setting where the story takes place

You need to proactively ask the user for this information. For parts the user doesn't want to decide themselves, fill in creatively.
When you believe you have enough information, output the final novel plan.

Notes:
- Ask only 2-3 related questions at a time, don't ask too many at once
- Flexibly adjust follow-up questions based on user responses
- For each element, explicitly ask if the user wants to specify it or leave it to you
- Maintain a friendly, professional conversational style""",

    "planner_first_question": """Hello! I'm your novel planning assistant~ 🎉

Before we start writing, I need to understand your ideas. Let's take it step by step:

**First, the most basic questions:**
1. What **genre/type** of novel do you want to write? (e.g., Fantasy, Urban, Mystery, Sci-Fi, Romance, Historical, etc.)
2. Do you have a rough **story direction** or **core idea** in mind? Even a vague notion is fine!
3. Would you like to specify these basic settings yourself, or would you prefer me to brainstorm for you?

Feel free to share your thoughts~""",

    "planner_check_enough": """Please analyze all the information collected so far and determine if it is sufficient to begin planning.

Core elements checklist:
1. Genre/Type - {has_genre}
2. Core Theme - {has_theme}
3. Target Word Count & Structure - {has_structure}
4. Narrative POV - {has_pov}
5. Core Tags - {has_tags}
6. One-line Summary - {has_summary}
7. Writing Style - {has_style}
8. Main Characters (at least protagonist concept) - {has_characters}
9. World Framework - {has_world}

Please reply in JSON format:
{{
    "is_enough": true/false,
    "missing_items": ["list of missing elements"],
    "next_questions": "If not enough info, your next questions for the user (2-3)"
}}

Return only JSON, nothing else.""",

    "planner_summarize": """Based on the information collected in the following conversation, generate a complete novel plan.
For parts not explicitly specified by the user, please creatively fill in to make the overall plan coherent and appealing.

Please output strictly in the following JSON format, no other content:
{{
    "title": "Book title",
    "genre": "Genre/Type",
    "theme": "Core theme (one paragraph)",
    "target_words": "Target total word count",
    "chapter_words": "Words per chapter range",
    "total_chapters": "Estimated total chapters",
    "volumes": "Number and division of volumes",
    "pov": "Narrative POV",
    "tags": "Core tags (comma-separated)",
    "one_line_summary": "One-line summary",
    "three_act_summary": {{
        "beginning": "Beginning (setup overview)",
        "middle": "Middle (development overview)",
        "end": "End (resolution overview)"
    }},
    "style_guide": "Writing style requirements and norms",
    "taboos": "Taboo items",
    "main_characters": [
        {{
            "name": "Name",
            "role": "Role (protagonist/antagonist/supporting etc.)",
            "age": "Age",
            "appearance": "Appearance description",
            "personality": "Personality description",
            "background": "Background story",
            "motivation": "Core motivation",
            "arc": "Character arc/growth trajectory"
        }}
    ],
    "world_setting": "World framework description",
    "synopsis": "Novel synopsis (for publishing)"
}}""",

    # -- Outline Agent --
    "outline_system": """You are an experienced novel outline planner. Based on the given novel plan, you will create a detailed plot outline.

You need to output:
1. Volume-level outline for the entire book (each volume's main plot, core conflict, key events, climax and cliffhanger)
2. Text description of character relationship map

Output in Markdown format. Ensure:
- Each volume outline contains clear main plot and key event lists
- Clear causal connections between volumes
- Character growth arcs run throughout
- Foreshadowing and suspense are reasonably designed
- Pacing alternates between tension and relaxation""",

    "volume_outline_system": """You are a novel outline specialist skilled at detailing plot.
Based on an overview of a volume from the master outline, you will create detailed chapter-level outlines.

Output in Markdown format. Each chapter needs:
- Chapter title
- Main events (3-5 key points)
- Appearing characters
- Emotional tone/atmosphere
- Foreshadowing (plant/resolve)
- Transition points""",

    # -- Worldbuilding Agent --
    "worldbuilding_system": """You are a professional worldbuilding specialist. Based on the given novel plan, you need to create detailed world setting documents.

Output in Markdown format, covering:
1. Overall world setting (era background, social structure, technology/magic level, etc.)
2. Geography/spatial settings (important locations and their features)
3. Special system settings (cultivation/magic/tech systems, depending on genre)
4. Timeline of major events (important historical events before the story begins)

Ensure settings are mutually consistent and non-contradictory.""",

    "character_system": """You are a character design specialist skilled at character creation. Based on the given novel plan and world settings, you need to create detailed character profiles.

Each character needs:
- Basic info (name, age, appearance, etc.)
- Personality description (multi-layered, including external behavior and inner personality)
- Background story
- Abilities/specialties
- Goals/motivations
- Speech patterns/verbal habits
- Character arc (growth trajectory)
- Character relationships

Output in Markdown format. Ensure characters have chemistry, with complementary or conflicting personalities.""",

    # -- Writer Agent --
    "writer_system": """You are a talented web novel writer.
You will write novel chapters based on provided settings, outlines, and context.

Writing requirements:
{style_guide}

Structure requirements:
- Each chapter {min_words}-{max_words} words
- Chapter needs a hook opening (connecting to previous chapter or creating new suspense)
- Core plot advancement (at least one key event)
- Ending hook (to attract readers to continue)

Strictly follow this format:
- Chapter title format: Chapter X Title
- Output chapter text directly, no meta-information or notes""",

    "writer_chapter_prompt": """Please write the full text of Chapter {chapter_num} based on the following information.

## Chapter Outline
{chapter_outline}

## Recent Chapter Summaries (for continuity)
{recent_briefs}

## Current Character Status
{character_status}

## Foreshadowing Notes
{hooks_info}

## Character Profiles (AUTHORITATIVE — names must match exactly)
{character_profiles}

## World Setting & Locations (AUTHORITATIVE — all place names, faction names, etc. must match exactly)
{world_setting}

⚠️ CRITICAL: All character names, place names, faction names, and terminology MUST exactly match the profiles and world setting above. Do NOT invent, alter, or substitute any names.

Please output the complete chapter text ({min_words}-{max_words} words), starting with "Chapter {chapter_num}".""",

    # -- Post-write Agent --
    "post_write_system": """You are a meticulous novel editor assistant. Your task is to analyze chapter content after each chapter is written and generate the following update information.

Please output in JSON format:
{{
    "chapter_brief": {{
        "chapter_num": chapter number,
        "title": "Chapter title",
        "word_count": approximate word count,
        "main_events": ["Main event 1", "Main event 2", ...],
        "character_changes": ["Character status change 1", ...],
        "hooks_planted": ["New foreshadowing 1", ...],
        "hooks_resolved": ["Resolved foreshadowing ID 1", ...],
        "next_chapter_hook": "Hook for the next chapter"
    }},
    "progress_update": {{
        "latest_chapter": "Chapter X · Title",
        "total_words": approximate cumulative word count,
        "character_status": {{
            "Character name": "Current status description"
        }}
    }}
}}

Return only JSON, nothing else.""",

    # -- Style Guide Agent --
    "style_guide_system": """You are a literary consultant specializing in writing style guidelines.
Based on the given novel plan, generate a detailed writing style guide document.

Output in Markdown format, including:
1. Narrative POV guidelines
2. Writing style requirements (overall tone, internal monologue style, external expression style, etc.)
3. Chapter structure guidelines
4. Dialogue guidelines (dialogue format, character speech styles)
5. Description guidelines (combat/emotional/environmental description requirements)
6. Pacing control suggestions
7. Core writing principles
8. Taboo items""",

    # -- Worldbuilding task prompts --
    "task_world_setting": """Based on the following novel plan, create an overall world setting document (Markdown format).
Include: era background, social structure, important factions/organizations, and other foundational worldbuilding.

Plan:
{plan_text}""",

    "task_characters": """Based on the following novel plan, create a detailed character profile document (Markdown format).
Reference format requirements: each character includes name, age, appearance, personality (multi-layered), background, abilities, motivations, verbal habits, character arc.
Append a character relationship map (text description) at the end.

Plan:
{plan_text}""",

    "task_locations": """Based on the following novel plan, create an important locations/settings document (Markdown format).
Include all important locations that will appear in the story and their characteristic descriptions.

Plan:
{plan_text}""",

    "task_timeline": """Based on the following novel plan, create a timeline of major events document (Markdown format).
Include important historical events before the story begins and timeline planning during the story.

Plan:
{plan_text}""",

    "task_power_system": """Based on the following novel plan, create a power/cultivation system setting document (Markdown format).
Include: level divisions, cultivation methods, special ability systems, and other detailed settings.

Plan:
{plan_text}""",

    "task_tech_system": """Based on the following novel plan, create a technology system setting document (Markdown format).
Include: technology level, key technologies, special devices, and other detailed settings.

Plan:
{plan_text}""",

    # -- Outline generation prompts --
    "master_outline_prompt": """Please create a master outline for the entire book based on the following novel plan.

## Novel Plan
{plan_json}

Please generate a master outline covering all volumes (Markdown format). Each volume needs:
- Main plot description
- Core conflict
- Key events (numbered list)
- Main character status
- Volume climax
- Volume cliffhanger
- Connection to next volume""",

    "volume_outline_prompt": """Please create a detailed chapter-level outline for Volume {volume_num} based on the following information.

## Novel Plan Summary
- Title: {title}
- Genre: {genre}
- Words per chapter: {chapter_words}

## This Volume's Description in Master Outline
{volume_info}

## Master Outline (complete, for global context)
{master_outline}

Please generate a detailed chapter-level outline for this volume, each chapter containing:
- Chapter number and title
- Main events (3-5)
- Appearing characters
- Emotional tone
- Foreshadowing (plant/resolve)
- Transition points""",

    # -- Post-write prompts --
    "analyze_chapter_prompt": """Please analyze the following novel chapter and generate summary and update information.

## Chapter Outline (reference)
{chapter_outline}

## Chapter Text
{chapter_text}

Please output strictly in the specified JSON format.""",

    # -- Plan revision --
    "plan_revision_request": "I have the following revision notes for the plan: {feedback}\nPlease adjust the plan accordingly.",

    # -- Genre detection keywords --
    "genre_fantasy_keywords": ["fantasy", "cultivation", "immortal", "magic", "wizard"],
    "genre_scifi_keywords": ["sci-fi", "future", "cyber", "space", "technology"],

    "outline_merge_prompt": """Below are {count} different master outlines for the same novel, each with a different style approach.

Please create a MERGED master outline that:
1. Takes the strongest structural elements from each draft
2. Combines the best plot ideas and character arcs
3. Maintains logical consistency throughout
4. Preserves the most compelling foreshadowing and climax designs

{drafts_text}

Output the merged outline in the same Markdown format.""",

    # -- Feature #2: Parallel reviewer system prompts --
    "consistency_reviewer_system": """You are a meticulous continuity editor for novels.
Your job is to review a chapter for consistency with previous chapters, the outline, AND the character profiles provided.

Check for:
1. **Character name accuracy**: Cross-reference EVERY character name in the chapter against the character profiles. Flag ANY name that does not exactly match the profiles (misspellings, wrong names, name swaps, inconsistent naming). This is the HIGHEST priority check.
2. **Character trait consistency**: Verify that each character's behavior, speech patterns, abilities, and personality match their profiles.
3. Timeline and chronological accuracy
4. Setting/location consistency
5. Plot continuity (events referenced must have actually happened)
6. Character knowledge consistency (characters shouldn't know things they haven't learned)

For each issue found, assign a confidence score (0-100):
- 0-25: Uncertain, might be intentional
- 26-50: Possible issue but could be subjective
- 51-75: Likely an error, needs verification
- 76-100: Definite error, verified against source material

Output JSON:
{{
    "issues": [
        {{
            "type": "consistency",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "Description of the issue",
            "location": "Approximate location in the chapter",
            "suggestion": "How to fix it"
        }}
    ],
    "overall_consistency_score": 1-10
}}

Return ONLY JSON.""",

    "style_reviewer_system": """You are an expert literary style reviewer.
Your job is to review a chapter for adherence to the writing style guide.

Check for:
1. POV consistency (no accidental POV shifts)
2. Tone and mood alignment with the style guide
3. Dialogue style consistency with character profiles
4. Pacing issues (too rushed or too slow)
5. Prose quality (awkward phrasing, repetitive words, etc.)

For each issue found, assign a confidence score (0-100).

Output JSON:
{{
    "issues": [
        {{
            "type": "style",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "Description of the issue",
            "location": "Approximate location in the chapter",
            "suggestion": "How to fix it"
        }}
    ],
    "overall_style_score": 1-10
}}

Return ONLY JSON.""",

    "foreshadowing_reviewer_system": """You are a foreshadowing and plot continuity specialist.
Your job is to review a chapter for proper handling of foreshadowing elements.

Check for:
1. Are planted foreshadowing elements properly subtle (not too obvious)?
2. Are previously planted hooks being progressed or resolved at appropriate times?
3. Are there missed opportunities for foreshadowing based on the outline?
4. Are resolved foreshadowing elements satisfying?
5. Does the chapter ending create adequate suspense for the next chapter?

For each issue found, assign a confidence score (0-100).

Output JSON:
{{
    "issues": [
        {{
            "type": "foreshadowing",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "Description of the issue",
            "location": "Approximate location in the chapter",
            "suggestion": "How to fix it"
        }}
    ],
    "overall_foreshadowing_score": 1-10
}}

Return ONLY JSON.""",

    "review_chapter_prompt": """Please review the following chapter.

## Character Profiles (AUTHORITATIVE reference for names and traits)
{character_profiles}

## Style Guide
{style_guide}

## Chapter Outline
{chapter_outline}

## Recent Chapter Summaries
{recent_briefs}

## Foreshadowing Tracker
{hooks_info}

## Chapter Text
{chapter_text}

IMPORTANT: Cross-check ALL character names in the chapter text against the Character Profiles above. Any name mismatch is a CRITICAL issue.

Please output your review in the specified JSON format.""",

    # -- Feature #3: Polish loop prompts --
    "polish_evaluate_system": """You are a senior novel editor. Evaluate the quality of the following chapter on a scale of 1-10.

Consider:
1. Prose quality and readability
2. Character voice consistency
3. Pacing and flow
4. Emotional impact
5. Hook strength (opening and ending)
6. Adherence to the outline

Output JSON:
{{
    "score": 1-10,
    "strengths": ["strength 1", "strength 2"],
    "weaknesses": ["weakness 1", "weakness 2"],
    "specific_improvements": [
        {{
            "location": "where in the text",
            "current": "current problematic text (brief)",
            "suggested": "how to improve it"
        }}
    ]
}}

Return ONLY JSON.""",

    "polish_evaluate_prompt": """Evaluate the quality of this chapter.

## Style Guide
{style_guide}

## Chapter Outline
{chapter_outline}

## Chapter Text
{chapter_text}

Please output your evaluation in JSON format.""",

    "polish_improve_system": """You are a talented novel writer performing a revision pass.
You will receive a chapter along with specific improvement suggestions from an editor.
Rewrite the COMPLETE chapter incorporating the improvements while preserving the overall story, tone, and structure.

Do NOT add any meta-commentary — output ONLY the revised chapter text.""",

    "polish_improve_prompt": """Please revise the following chapter based on the editor's feedback.

## Editor's Feedback
Weaknesses: {weaknesses}

Specific Improvements:
{improvements}

## Current Chapter Text
{chapter_text}

Output the complete revised chapter text.""",

    # -- Feature #4: Volume checkpoint adjustment --
    "volume_adjust_prompt": """The reader has provided the following feedback/adjustments for Volume {volume_num}.

Feedback: {feedback}

Current volume outline:
{volume_outline}

Please revise the volume outline to incorporate the reader's feedback while maintaining consistency with the master outline.

Output the revised volume outline in Markdown format.""",

    # -- Word count validation prompts --
    "expand_chapter_system": """You are a talented novel writer. You will receive a chapter that is too short and needs to be expanded.
Expand the chapter to meet the target word count while maintaining quality. Do NOT pad with filler content.

Expansion strategies:
- Add more detailed descriptions (environment, emotions, sensory details)
- Expand dialogue exchanges with natural back-and-forth
- Add character internal monologue and reactions
- Elaborate on action sequences with more vivid detail
- Add transitional scenes that build atmosphere

IMPORTANT: Output ONLY the complete expanded chapter text. No meta-commentary.""",

    "expand_chapter_prompt": """The following chapter is too short ({current_words} words). Please expand it to approximately {target_words} words.

## Style Guide
{style_guide}

## Chapter Outline
{chapter_outline}

## Current Chapter Text (too short)
{chapter_text}

Please output the complete expanded chapter text ({target_words}+ words).""",

    "compress_chapter_system": """You are a skilled novel editor. You will receive a chapter that is too long and needs to be compressed.
Compress the chapter to meet the target word count while preserving all key plot points and character moments.

Compression strategies:
- Tighten prose by removing redundant descriptions
- Consolidate repetitive dialogue
- Summarize less important transitional scenes
- Remove filler content that doesn't advance the plot
- Streamline action sequences

IMPORTANT: All key plot events, character developments, and foreshadowing MUST be preserved.
Output ONLY the complete compressed chapter text. No meta-commentary.""",

    "compress_chapter_prompt": """The following chapter is too long ({current_words} words). Please compress it to approximately {target_words} words.

## Style Guide
{style_guide}

## Chapter Outline (preserve all key events)
{chapter_outline}

## Current Chapter Text (too long)
{chapter_text}

Please output the complete compressed chapter text (~{target_words} words). Preserve ALL key plot points.""",

    "split_chapter_system": """You are a skilled novel editor. You will receive a chapter that is far too long and needs to be split into two chapters.
Find a natural narrative break point to split the chapter. Each resulting chapter should:
- Have its own dramatic arc (setup → development → hook ending)
- Be roughly equal in length
- End at a natural cliffhanger or transition point

Output format: Use the exact separator line "===CHAPTER_SPLIT===" between the two chapters.
Each chapter should start with its chapter title line.

IMPORTANT: Output ONLY the two chapter texts separated by ===CHAPTER_SPLIT===. No meta-commentary.""",

    "split_chapter_prompt": """The following chapter is far too long ({current_words} words, target per chapter: {min_words}-{max_words}). Please split it into two chapters.

## Style Guide
{style_guide}

## Original Chapter Outline
{chapter_outline}

## Current Chapter Text (to be split)
{chapter_text}

Split this into two well-structured chapters. Use "===CHAPTER_SPLIT===" as the separator between them.
Chapter {chapter_num_a} should be the first half, Chapter {chapter_num_b} should be the second half.
Each chapter should be approximately {target_words} words.""",

    # -- Feature #6: Final summary prompts --
    "final_summary_system": """You are a literary analyst. Generate a comprehensive summary report for a completed novel.

Output in Markdown format, including:
1. **Novel Overview** — Title, genre, final word count, chapter count
2. **Plot Summary** — Complete story synopsis (spoiler-full)
3. **Character Arc Analysis** — How each main character evolved
4. **Theme Analysis** — Core themes and how they were explored
5. **Statistical Overview** — Word counts per chapter, average words, longest/shortest chapters
6. **Foreshadowing Resolution Report** — Which hooks were planted and resolved
7. **Writing Quality Notes** — Overall prose quality, notable scenes
8. **Potential Sequel Hooks** — Open threads that could be continued""",

    "final_summary_prompt": """Generate a comprehensive final summary for this completed novel.

## Novel Plan
{plan_json}

## Chapter Summaries
{all_briefs}

## Character Profiles
{characters}

## Foreshadowing Tracker
{hooks_info}

## Statistics
- Total chapters: {total_chapters}
- Total words: ~{total_words}

Please generate the full summary report in Markdown format.""",
}

# ============================================================
# TEMPLATES: Markdown templates for generated files
# ============================================================
TEMPLATES = {
    "readme": """# 📖 Novel Writing Project

## Basic Information
- **Title**: "{title}"
- **Genre**: {genre}
- **Target Word Count**: {target_words}
- **Words per Chapter**: {min_words}-{max_words}
- **Estimated Chapters**: {total_chapters}
- **Volumes**: {volumes}
- **Narrative POV**: {pov}
- **Core Tags**: {tags}

## One-line Summary
{one_line_summary}

## 📁 Directory Structure

```
{title}/
├── README.md              # Project overview
├── meta/                  # Metadata management
│   ├── progress.md        # Writing progress tracker
│   ├── style_guide.md     # Writing style guide
│   └── hooks_tracker.md   # Foreshadowing tracker
├── worldbuilding/         # World settings
│   ├── characters.md      # Character profiles
│   ├── world_setting.md   # World settings overview
│   └── ...                # Other setting files
├── plot/                  # Plot management
│   ├── master_outline.md  # Master outline
│   ├── volume_XX.md       # Volume outlines
│   └── chapter_briefs.md  # Chapter summaries
└── chapters/              # Chapter outputs
    ├── chapter_001.txt    # Chapter 1
    └── ...
```

## 🔄 Writing Workflow
1. Read progress.md → Check current progress
2. Read chapter_briefs.md → Review recent chapters
3. Refer to current volume outline → Confirm chapter content
4. Check hooks_tracker.md → Review foreshadowing status
5. Consult characters.md → Confirm character status
6. Output chapter text to chapters/
7. Update progress.md, chapter_briefs.md, etc.
""",

    "progress": """# 📊 Writing Progress Tracker

## Current Status
- **Latest Completed Chapter**: Not started yet
- **Currently Writing**: TBD
- **Current Volume**: Volume 1
- **Total Word Count**: 0
- **Last Updated**: -

## Next Steps
> 1. ~~Determine novel genre/type~~ ✅
> 2. ~~Core settings and protagonist~~ ✅
> 3. ~~Master outline~~ ✅
> 4. **Complete Volume 1 outline** ← Current
> 5. Begin writing

## Completed Chapters Overview

| Chapter | Title | ~Words | Core Events |
|---------|-------|--------|-------------|

## Current Character Status Quick Reference
(To be updated)

## TODO
- [x] Determine novel genre
- [x] Complete worldbuilding
- [x] Complete character profiles
- [x] Complete master outline
- [ ] Complete Volume 1 outline
- [ ] Chapter 1 text
""",

    "hooks_tracker": """# 🎣 Foreshadowing/Hook Tracker

> Track all planted foreshadowing and suspense, monitor their status
> Status: 🔴 Planted | 🟡 Partially revealed | 🟢 Resolved | ⚪ Planned

---

## Long-term Foreshadowing (cross-volume)

| ID | Content | Planted In | Planned Resolution | Status | Notes |
|----|---------|-----------|-------------------|--------|-------|

## Short-term Foreshadowing (within current volume)

| ID | Content | Planted In | Planned Resolution | Status | Notes |
|----|---------|-----------|-------------------|--------|-------|

## Resolved Records

| ID | Content | Planted In | Resolved In | Notes |
|----|---------|-----------|------------|-------|
""",

    "chapter_briefs": """# 📝 Chapter Summary Records

> Record summaries after each chapter is written for quick plot review
> Format: Chapter | Title | Words | Main Events | Character Changes | Foreshadowing

---
""",

    "synopsis_title": "# Novel Synopsis\n\n",

    # -- Post-write update templates --
    "chapter_brief_entry": """
### Chapter {chapter_num} · {title} (~{word_count} words)
**Main Events**:
""",
    "character_changes_header": "\n**Character Status Changes**:\n",
    "hooks_planted_header": "\n**New Foreshadowing**:\n",
    "next_hook_prefix": "\n**Next Chapter Hook**: ",

    "progress_update_entry": """
---
### Chapter {chapter_num} Completion Update
- **Latest Completed**: {latest_chapter}
- **Cumulative Words**: ~{total_words}
""",
    "character_status_header": "\n**Character Status Quick Reference**:\n",

    # -- Feature #6: Final summary template --
    "final_summary_filename": "meta/final_summary.md",
}

"""
文言語言包 — 效法先秦兩漢，崇尚古雅
"""
from locales.en import UI as _BASE_UI, PROMPTS as _BASE_PROMPTS, TEMPLATES as _BASE_TEMPLATES

UI = dict(_BASE_UI)
UI.update({
    "welcome_title": "📖 綴文機樞 v1.0",
    "welcome_subtitle": "   藉器械之巧，以成綴文之功",
    "no_backend": "\n❌ 無可用之後臺！",
    "no_backend_hint": "   llm_openai.py 或 llm_local.py，須存其一",
    "select_api_mode": "\n🔌 擇通衢：",
    "api_openai_desc": "OpenAI 正途",
    "api_local_desc": "本府通途",
    "auto_selected": "\n  （唯得{desc}，遂用之）",
    "input_choice": "\n👤 擇之（1-{max}）：",
    "invalid_choice": "失宜。請入1-{max}",
    "input_openai_key": "請入符牒：",
    "api_key_empty": "符牒不可缺！",
    "input_base_url": "所在（Enter取常 {default}）：",
    "input_model": "機名（Enter取常 {default}）：",
    "input_local_url": "入本府所在：",
    "api_url_empty": "所在不可缺！",
    "input_api_key": "入符牒（Enter略）：",
    "input_wsid": "入WSID（Enter略）：",
    "input_model_marker": "入印記（Enter略）：",
    "project_setup": "\n📁 立卷",
    "input_novel_name": "👤 命書名（以充卷牘）：",
    "scan_projects_header": "\n📂 既有卷牘如左：",
    "no_existing_projects": "\n📂 未見既有卷牘。",
    "project_status_chapters": "{count}篇",
    "project_status_plan": "籌策",
    "project_status_meta": "志要",
    "project_status_plot": "綱目",
    "or_input_manually": "手書卷名...",
    "select_project_prompt": "\n👤 擇其一 (1-{max}): ",
    "select_operation": "\n🎯 何爲？",
    "op_full": "  1. 始末貫之",
    "op_resume": "  2. 踵續前功",
    "op_planning": "  3. 惟事籌謀",
    "op_worldbuilding": "  4. 惟營世界文風",
    "op_outline": "  5. 惟擬綱目",
    "op_writing": "  6. 惟事執筆（須先有綱目）",
    "op_batch": "  7. 連肆（續生數部書）",
    "input_op_choice": "\n👤 擇之（1-7）：",
    "invalid_op": "失宜。請入1-7",
    "input_volume_num": "擬何卷？（入數，Enter略）：",
    "input_start_chapter": "起何章？（Enter自首）：",
    "input_end_chapter": "止何章？（Enter至末）：",
    "interrupted": "\n\n⏸️ 暫歇。進度已錄，後可續之。",
    "error_occurred": "\n❌ 有故：{error}",
    "goodbye": "\n👋 告退。後會有期。",

    # -- 連肆 --
    "batch_input_names": "\n📚 列書名，以逗號隔之（如：甲書, 乙書, 丙書）：",
    "batch_empty": "❌ 未舉書名，還歸主肆。",
    "batch_select_op": "\n🎯 擇各書之事：",
    "batch_start": "\n🚀 連肆：將依次為 {total} 部書運筆：{names}",
    "batch_progress": "📖 [{current}/{total}] 始作：{name}",
    "batch_novel_done": "✅ 書《{name}》成矣！",
    "batch_interrupted": "\n⏸️ 書《{name}》中輟，尚餘 {remaining} 部未就。",
    "batch_continue_prompt": "續為餘書乎？(y/n)：",
    "batch_stopped": "🛑 連肆已止。",
    "batch_novel_error": "\n❌ 書《{name}》有故：{error}",
    "batch_all_done": "\n🎉 連肆畢！凡 {total} 部皆成。",

    "select_language": "\n🌐 擇書之語：",
    "lang_choice_prompt": "\n👤 擇之（1-{max}）：",
    "phase_planning_title": "\n📝 壹　籌謀",
    "planner_prefix": "\n🤖 謀者曰：\n",
    "user_prefix": "👤 君：",
    "input_empty_hint": "（請言）",
    "multiline_hint": "（容多行，空行以止；入 /paste 则入贴附之式）",
    "multiline_paste_hint": "（已入贴附之式，可任贴含空行之文，入 /end 以止）",
    "quit_planning": "止謀。",
    "force_done": "善。容理之。",
    "generating_plan": "\n⏳ 擬策中⋯⋯",
    "plan_display_title": "\n📋 著書策",
    "plan_label_title": "名",
    "plan_label_genre": "體",
    "plan_label_theme": "旨",
    "plan_label_target_words": "約字",
    "plan_label_total_chapters": "章數",
    "plan_label_volumes": "卷數",
    "plan_label_pov": "視角",
    "plan_label_tags": "標",
    "plan_label_one_line": "一言",
    "plan_label_beginning": "起",
    "plan_label_middle": "承",
    "plan_label_end": "合",
    "plan_label_characters": "人物",
    "confirm_plan": "\n👤 此策何如？（y／修之）：",
    "adjusting_plan": "\n⏳ 依言修之⋯⋯",
    "plan_confirmed": "✅ 策成。已錄。",
    "rename_dir_prompt": "\n📁 書名「{title}」，而案牘之匣名「{dir}」。",
    "rename_dir_confirm": "   欲易匣名為「{title}」乎？(y/n): ",
    "rename_dir_done": "  ✅ 匣已易名為: {path}",
    "rename_dir_exists": "  ⚠️ 匣已有之: {path}",
    "rename_dir_failed": "  ❌ 易名不成: {error}",
    "phase_world_title": "\n🌍 買　營世界、定文風（並行⋯⋯）",
    "world_done": "✅ 世界已成（{count}篇）",
    "world_failed": "❌ 世界未成：{error}",
    "style_done": "✅ 文風已定",
    "style_failed": "❌ 文風未定：{error}",
    "phase_outline_title": "\n📋 參　擬總綱",
    "generating_outline": "⏳ 擬綱中⋯⋯",
    "outline_done": "✅ 總綱成",
    "outline_review": "\n📖 綱存 plot/master_outline.md，請覽。",
    "press_enter_continue": "👤 按Enter續擬首卷⋯⋯",
    "generating_volume": "📑 擬第{num}卷⋯⋯",
    "volume_done": "✅ 第{num}卷成",
    "phase_writing_title": "\n✍️ 伍　執筆",
    "checkpoint_resume": "〔續〕已成{count}章，自第{next}章起",
    "volume_not_found": "⚠️ 未得第{num}卷綱。擬之⋯⋯",
    "generating_volume_outline": "⏳ 擬第{num}卷綱⋯⋯",
    "writing_chapter": "📖 撰第{num}章⋯⋯",
    "chapter_done": "  ✅ 第{num}章畢（約{words}字）",
    "post_processing": "  ⏳ 整理中⋯⋯",
    "post_done": "  ✅ 第{num}章後事竣",
    "post_failed": "  ⚠️ 第{num}章後事未竣，略之",
    "chapter_error": "  ❌ 第{num}章有故：{error}",
    "retry_prompt": "  再試否？（y/n）：",
    "skip_chapter": "  略第{num}章",
    "pause_prompt": "\n📊 已成{num}章。Enter續，'stop'歇",
    "pause_input": "👤 ",
    "paused": "⏸️ 歇。後可自第{next}章續",
    "writing_complete": "🎉 書成矣！",
    "planning_incomplete": "謀未竟，退。",
    "no_plan_found": "未見策。自始謀之。",
    "resume_checking": "🔄 檢視前功⋯⋯",
    "resume_completed": "已成{count}章，續行。",
    "no_style_guide": "文風未定。營之。",
    "no_outline": "未見總綱。擬之。",
    "plan_not_found_error": "未見plan.json。請先籌謀。",
    "worldbuilding_start": "〔世界〕並行營構{count}篇⋯⋯",
    "doc_done": "  ✅ {filename}成",
    "doc_failed": "  ❌ {filename}未成",
    "doc_error": "  ❌ {filename}有故：{error}",
    "llm_error_retry": "器械偶恙。請重言之。",
    "info_enough": "所得足矣！理之成策⋯⋯ 🎯",
    "continue_input": "請續道欲著何書。",
    "config_loaded": "〔設〕自{file}得配置：{keys}",
    "novel_config_loaded": "〔設〕自書之設{file}得：{keys}",
    "novel_config_skipped": "  ⚠️ 已略{file}中API/徑之設（請用通設）：{keys}",
    "novel_config_auto_created": "〔設〕已自範本造{file}（可修之以定此書之設）",
    "config_not_found": "〔設〕未見{file}，須手入符牒",
"config_hint": "〔設〕參user_config.example.json造{file}",
    "project_initialized": "〔卷〕已立：{path}",
    "openai_initialized": "〔機-OpenAI〕啟。機：{model}，在：{url}",
    "openai_need_package": "OpenAI後臺須openai包：pip install openai",
"openai_no_key": "OPENAI_API_KEY未設。填user_config.json或手入",
    "openai_attempt_failed": "〔機-OpenAI〕第{n}試敗：{error}",
    "openai_retry_wait": "〔機-OpenAI〕{wait}秒後再試",
    "openai_max_retries": "〔機-OpenAI〕試盡（{max}），罷",
    "local_initialized": "〔機-本府〕啟。在：{url}，記：{marker}",
    "local_need_package": "本府後臺須requests包：pip install requests",
"local_no_url": "LOCAL_API_URL未設。填user_config.json",
    "local_attempt_failed": "〔機-本府〕第{n}試敗：{error}",
    "local_retry_wait": "〔機-本府〕{wait}秒後再試",
    "local_max_retries": "〔機-本府〕試盡（{max}），罷",
    "cannot_load_openai": "不能載OpenAI後臺：{error}\n確llm_openai.py存且已安openai",
    "cannot_load_local": "不能載本府後臺：{error}\n確llm_local.py存且已安requests",
    "unsupported_api_mode": "不支此式：{mode}。可選：'openai'、'local'",
    "file_written": "〈錄〉書入：{path}",

    # -- Feature #1: 多方大綱 --
    "outline_multi_draft_title": "\n📋 參　擬總綱（多方並陳）",
    "generating_draft": "  ⏳ 擬綱第{num}/{total}方（風：{style}）……",
    "draft_done": "  ✅ 第{num}方成",
    "draft_failed": "  ❌ 第{num}方未成：{error}",
    "draft_comparison_title": "\n📊 各方比觀",
    "draft_header": "\n{'─' * 40}\n📄 第{num}方 — 風：{style}\n{'─' * 40}",
    "draft_select_prompt": "\n👤 擇何方（1-{max}），或入'm'合眾長：",
    "draft_merging": "⏳ 合眾方之長……",
    "draft_selected": "✅ 己擇第{num}方爲總綱",
    "draft_merged": "✅ 合綱己成",
    "outline_drafts_truncating": "   ⚠️ 綱稿過長（估 {total} tokens，限 {budget}），等分截之...",
    "draft_invalid": "失宜。請入1-{max}或'm'",
    "parallel_review_title": "  🔍 並行核查中……",
    "review_consistency": "〈前後一貫〉",
    "review_style": "〈文風審核〉",
    "review_foreshadowing": "〈伏筆審核〉",
    "review_done": "  ✅ {reviewer}: 得{count}事（信≥{threshold}）",
    "review_failed": "  ⚠️ {reviewer}未竟：{error}",
    "review_no_issues": "  ✅ 皆無礙——善哉！",
    "review_issues_found": "  ⚠️ 共得{count}事:",
    "review_issue_item": "    [{severity}] ({reviewer}, 信: {confidence}) {description}",
    "review_critical_prompt": "  🚨 有重礙。重撰此章否？(y/n)：",
    "polish_start": "  ✨ 始潤筆（至多{max_iter}遍）……",
    "polish_iteration": "  ✨ 潤筆第{iter}/{max_iter}遍……",
    "polish_score": "  📊 品等: {score}/10（閾: {threshold}）",
    "polish_passed": "  ✅ 己達閾。止潤筆。",
    "polish_improving": "  ⏳ 未達閾，改之……",
    "polish_max_reached": "  ⚠️ 潤筆己盡。用最優版（品: {score}/10）。",
    "polish_failed": "  ⚠️ 潤筆評未竟，保現版。",
    "volume_checkpoint_title": "\n📍 第{num}卷檢點",
    "volume_checkpoint_summary": "  己成{completed}章，約{words}字",
    "volume_checkpoint_prompt": "\n👤 即起第{num}卷。續否？(y / adjust / stop)：",
    "volume_checkpoint_adjust": "👤 入調整之語：",
    "volume_checkpoint_adjusting": "⏳ 依言調綱……",
    "volume_checkpoint_stopped": "⏸️ 止於第{num}卷前。後可自第{next}章續。",
    "severity_critical": "重",
    "severity_major": "次重",
    "severity_minor": "輕",
    "severity_info": "記",
    "final_summary_title": "\n📊 撬全書總結……",
    "final_summary_done": "✅ 總結己成，己錄！",
    "final_summary_failed": "⚠️ 總結未成：{error}",

    # -- 筆法之設 --
    "writing_params_title": "\n⚙️ 筆法之設",
    "ask_chapter_min_words": "   每章最少之字（今: {current}，徑按入則不改）: ",
    "ask_chapter_max_words": "   每章最多之字（今: {current}，徑按入則不改）: ",
    "writing_params_swapped": "   ⚠️ 下限逾上限，已互易之。",
    "ask_word_count_check": "   啟字數之校否？（今: {status}，y/n，徑按入則不改）: ",
    "ask_lazy_mode": "   啟閒逸之法否？（今: {status}，y/n，徑按入則不改）: ",
    "writing_params_summary": "   ✅ 筆法: {min}–{max} 字/章，字數校: {check}，閒逸法: {lazy}",

    # -- 對話引號 --
    "quote_style_title": "\n💬 對話引號之制",
    "quote_style_prompt": "\n👤 請擇對話引號之式 (1-{max}): ",
    "quote_style_invalid": "擇之不當，請入 1-{max}",
    "quote_style_selected": "✅ 對話引號定為: {style}",
    "quote_style_option_curly": '\u201c\u201d 彎引號（如：\u201c汝好！\u201d）',
    "quote_style_option_corner": '「」 直角引號（如：「汝好！」）',
    "quote_style_option_guillemet": '«» 書名號式（如：«汝好！»）',
    "quote_style_option_dash": '— 破折號式（如：——汝好！）',
    "quote_style_option_straight": '"" 直引號（如："汝好！"）',

    # -- 心思引號 --
    "inner_quote_title": "\n💭 心思內白引號之制",
    "inner_quote_prompt": "\n👤 請擇心思描寫之式 (1-{max}): ",
    "inner_quote_invalid": "擇之不當，請入 1-{max}",
    "inner_quote_selected": "✅ 心思引號定為: {style}",
    "inner_quote_option_corner_double": '『』 雙直角引號（如：『當慎之』）',
    "inner_quote_option_corner": '「」 直角引號（如：「當慎之」）',
    "inner_quote_option_curly_single": '\u2018\u2019 單彎引號（如：\u2018當慎之\u2019）',
    "inner_quote_option_italic": '*斜體* 示心思（如：*當慎之*）',
    "inner_quote_option_dash": '——雙破折號（如：——當慎之——）',
    "inner_quote_option_paren": '（）全形括號（如：（當慎之））',
    "inner_quote_option_same": '與對話引號同',
    "inner_quote_option_none": '不用記號（以敘述寫心思）',

    # -- 引號之法（注入風格指南中） --
    "quote_rules_heading": "引號之法",
    "quote_rule_dialogue_curly": '凡對話皆用\u201c\u201d（彎引號）。例：\u201c汝好！\u201d',
    "quote_rule_dialogue_corner": '凡對話皆用「」（直角引號）。例：「汝好！」',
    "quote_rule_dialogue_guillemet": '凡對話皆用«»（書名號式）。例：«汝好！»',
    "quote_rule_dialogue_dash": '對話以——（破折號）引之。例：——汝好！',
    "quote_rule_dialogue_straight": '凡對話皆用""（直引號）。例："汝好！"',
    "quote_rule_inner_corner_double": '心思以『』（雙直角引號）標之。例：『當慎之』',
    "quote_rule_inner_corner": '心思以「」（直角引號）標之。例：「當慎之」',
    "quote_rule_inner_curly_single": '心思以\u2018\u2019（單彎引號）標之。例：\u2018當慎之\u2019',
    "quote_rule_inner_italic": '心思以*斜體*標之。例：*當慎之*',
    "quote_rule_inner_dash": '心思以——（雙破折號）標之。例：——當慎之——',
    "quote_rule_inner_paren": '心思以（）（全形括號）標之。例：（當慎之）',
    "quote_rule_inner_none": '心思不用記號，以敘述寫之。',
    "quote_rule_inner_same": '心思與對話用同一引號。',

    # -- 閒逸之法 --
    "lazy_mode_enabled": "🛋️ 閒逸之法啟——綱既定後，一切自行運之！",
    "lazy_auto_merge": "🛋️ [閒逸] 諸綱自合……",
    "lazy_auto_select": "🛋️ [閒逸] 草稿唯一，自取之。",
    "lazy_auto_continue": "🛋️ [閒逸] 自續……",
    "lazy_auto_retry": "🛋️ [閒逸] 自再試……",
    "lazy_auto_skip": "🛋️ [閒逸] 自跳之……",
    "lazy_auto_volume_continue": "🛋️ [閒逸] 自續第{num}卷……",

    # -- 審校重試 --
    "review_retry_feedback": """⚠️ 切記：此乃第{attempt}/{max_attempts}次重撰。前稿有重礙如下，須悉正之：
{issues}

請重撰全章，務正上述諸病，而不失原文之旨、調、構。""",
    "review_max_retries_reached": "  ⚠️ 第{num}章審校重試已盡（{max}次），存此稿續行。",



    # -- 字數校驗 --
    "wordcount_check_start": "  📏 校字：{words}字（期：{min}至{max}）",
    "wordcount_too_short": "  ⚠️ 章短（{words}字，少於{min}）。擴之……",
    "wordcount_too_long": "  ⚠️ 章長（{words}字，逾{max}）。縮之……",
    "wordcount_split_needed": "  📑 章甚長（{words}字，≧{threshold}%上限）。裂爲兩章……",
    "wordcount_expand_done": "  ✅ 擴畢：{words}字",
    "wordcount_compress_done": "  ✅ 縮畢：{words}字",
    "wordcount_split_done": "  ✅ 裂畢：第{num_a}章（{words_a}字）＋第{num_b}章（{words_b}字）",
    "wordcount_retry": "  🔄 字校再試 {attempt}/{max_attempts}……",
    "wordcount_give_up": "  ⚠️ {max_attempts}試未達，用今版（{words}字）。",
    "wordcount_ok": "  ✅ 字數合：{words}字",
    "wordcount_split_renumber": "  📝 裂後續章自動重編。",

    # -- Feature #1: Multi-draft outline styles --
    "outline_style_dramatic": "戲劇張力",
    "outline_style_literary": "文學深蘊",
    "outline_style_commercial": "商業疾節",
})
PROMPTS = dict(_BASE_PROMPTS)
PROMPTS.update({
    "planner_system": """汝，善謀者也。能於虛無之中構思說部。
汝之任：與問者對語，盡蒐其意，以定下列諸要——

一、**體裁**：仙俠、世情、公案、志怪、傳奇等
二、**旨趣**：書之所言何事
三、**篇幅**：通計字數、章數、卷數
四、**敘法**：第一人稱抑第三人稱
五、**要詞**：三五關鍵之詞
六、**一言**：一語括全書
七、**起承合**：三段大略
八、**文風**：筆法、格調、所效何作
九、**所忌**：不可涉者
十、**要角**：至少主人公之設定
十一、**世界**：故事所在之天地

主動問之。問者不欲自決者，代爲創設。
訊足則出著書之策。

須知：
- 每問二三事，勿繁
- 依答靈活調問
- 各要素問其自定或委汝
- 辭氣從容""",

    "planner_first_question": """有禮。吾乃著書之謀者。🎉

未執筆，先問數事。

**先問其大者：**
一、欲著何**體裁**之書？（仙俠、世情、公案、志怪、傳奇、紀傳等）
二、心中可有大略之**故事走向**或**核心構想**？縱朦朧亦可
三、此等設定，欲親定之，抑委吾代謀？

隨意道來。""",

    "planner_check_enough": """請析目前所得之訊，判其足否以啟謀。

核心要素之表：
一、體裁 - {has_genre}
二、旨趣 - {has_theme}
三、篇幅結構 - {has_structure}
四、敘法 - {has_pov}
五、要詞 - {has_tags}
六、一言 - {has_summary}
七、文風 - {has_style}
八、要角（至少主人公之概） - {has_characters}
九、世界 - {has_world}

以JSON覆之：
{{
    "is_enough": true/false,
    "missing_items": ["所缺之要素"],
    "next_questions": "訊不足，則次當問何（二三問）"
}}

惟返JSON。""",

    "planner_summarize": """據所得之訊，成完策一份。
問者未明言者，以巧思補之，使策通貫而引人。

嚴依以下JSON式出，勿出他物：
{{
    "title": "書名",
    "genre": "體裁",
    "theme": "旨趣（一段）",
    "target_words": "約字數",
    "chapter_words": "每章字數",
    "total_chapters": "約章數",
    "volumes": "卷數及分",
    "pov": "敘法",
    "tags": "要詞（逗號隔）",
    "one_line_summary": "一言",
    "three_act_summary": {{
        "beginning": "起（始之大略）",
        "middle": "承（展之大略）",
        "end": "合（結之大略）"
    }},
    "style_guide": "文風及筆規",
    "taboos": "所忌",
    "main_characters": [
        {{
            "name": "名",
            "role": "位（主人公／對手／配角等）",
            "age": "齡",
            "appearance": "貌",
            "personality": "性",
            "background": "來歷",
            "motivation": "所求",
            "arc": "歷程"
        }}
    ],
    "world_setting": "天地之設",
    "synopsis": "書之概（可示人者）"
}}""",

    # -- 綱目 --
    "outline_system": """汝乃善擬綱目之人。據著書之策，成詳密之情節綱目。

須出：
一、全書卷級綱目（每卷之主線、要衝突、大事、卷末高潮與懸念）
二、人物關係之圖（以文述之）

以Markdown出之。須確：
- 每卷綱含明晰之主線與事列
- 卷間因果相銜
- 人物成長之弧貫全書
- 伏筆懸念佈局合宜
- 張弛有度""",

    "volume_outline_system": """汝善細化情節。據總綱中某卷之概，成該卷章級之詳綱。

以Markdown出之。每章須含：
- 章題
- 要事（三至五要點）
- 出場人物
- 情感基調
- 伏筆（埋／收）
- 承上啟下之接""",

    # -- 世界觀 --
    "worldbuilding_system": """汝乃世界營造之專才。據著書之策，成詳密之天地設定。

以Markdown出之，須涵：
一、天地總設（時代、社會、術法水準等）
二、地理空間（要地及其貌）
三、特殊體系（修煉／術法／機關體系，視體裁定）
四、大事年表（故事前之要史）

設定間須一貫，不可相悖。""",

    "character_system": """汝善塑人物。據著書之策及天地設定，成詳密之人物檔。

每人須含：
- 基本（名、齡、貌等）
- 性（多層，含外行內心）
- 來歷
- 能／長
- 所求所志
- 言談之風
- 歷程弧光
- 人物關係

以Markdown出之。人物間須有相激相生之趣，性或互補或相沖。""",

    # -- 著文 --
    "writer_system": """汝乃才具之著書人。
據所供之設定、綱目、前文，撰小說正文。

筆規：
{style_guide}

結構：
- 每章 {min_words}-{max_words} 字
- 章首須有鉤（承前章或造新懸）
- 要事推進（至少一要事）
- 章末留鉤（引人續讀）

嚴守此式：
- 章題式：第X章 題
- 直出正文，不出元訊或注""",

    "writer_chapter_prompt": """據以下訊撰第{chapter_num}章正文。

## 本章綱
{chapter_outline}

## 近章摘要（保連貫）
{recent_briefs}

## 當前人物態
{character_status}

## 須注之伏筆
{hooks_info}

## 角色檔案（權設——名必嚴合）
{character_profiles}

## 世界觀與地設（權設——凡地名、勢力名等必嚴合）
{world_setting}

⚠️ 切記：凡角色之名、地名、門派勢力名暨專名，必與上之角色檔案及世界觀設定一字不差。嚴禁自造、改易或替換任何名。

出完整章文（{min_words}-{max_words}字），以「第{chapter_num}章」起。""",

    # -- 後理 --
    "post_write_system": """汝乃細心之編助。每章畢，析章文，成更新訊。

以JSON出：
{{
    "chapter_brief": {{
        "chapter_num": 章號,
        "title": "章題",
        "word_count": 約字數,
        "main_events": ["要事一", "要事二", ...],
        "character_changes": ["人物變一", ...],
        "hooks_planted": ["新伏筆一", ...],
        "hooks_resolved": ["已收伏筆ID一", ...],
        "next_chapter_hook": "留與下章之鉤"
    }},
    "progress_update": {{
        "latest_chapter": "第X章·題",
        "total_words": 約累計字數,
        "character_status": {{
            "人物名": "當前態"
        }}
    }}
}}

惟返JSON。""",

    # -- 文風 --
    "style_guide_system": """汝乃文學顧問，專司文風規範。
據著書之策，成詳密文風指南。

以Markdown出，含：
一、敘法規範
二、文風（總調、內心獨白風、外在表現風等）
三、章節結構規範
四、對話規範（對話式、人物語風）
五、描摹規範（戰鬥／情感／山水等）
六、節奏之議
七、核心筆則
八、所忌""",

    # -- 世界觀任務 --
    "task_world_setting": """據以下著書策，成天地總設文（Markdown式）。
含：時代、社會、要勢力等基礎世界觀。

策：
{plan_text}""",

    "task_characters": """據以下著書策，成詳密人物檔文（Markdown式）。
格式：每人含名、齡、貌、性（多層）、來歷、能、志、言癖、弧光。
末附人物關係圖（以文述之）。

策：
{plan_text}""",

    "task_locations": """據以下著書策，成要地場景設文（Markdown式）。
含故事中將現之要地及其貌。

策：
{plan_text}""",

    "task_timeline": """據以下著書策，成大事年表文（Markdown式）。
含故事前之要史及故事中之時間規劃。

策：
{plan_text}""",

    "task_power_system": """據以下著書策，成力量修煉體系設文（Markdown式）。
含：等級、修煉法、特殊能力體系等。

策：
{plan_text}""",

    "task_tech_system": """據以下著書策，成機關技術體系設文（Markdown式）。
含：技術水準、核心技術、特殊器物等。

策：
{plan_text}""",

    # -- 綱目生成 --
    "master_outline_prompt": """據以下著書策，成全書總綱。

## 著書策
{plan_json}

成涵所有卷之總綱（Markdown式）。每卷須含：
- 主線述
- 核心衝突
- 要事（編號列）
- 要角態
- 卷末高潮
- 卷末懸念
- 與下卷之接""",

    "volume_outline_prompt": """據以下訊，成第{volume_num}卷之章級詳綱。

## 著書策摘
- 名：{title}
- 體：{genre}
- 每章字：{chapter_words}

## 此卷於總綱中之述
{volume_info}

## 總綱（全本，以觀全局）
{master_outline}

成此卷章級詳綱。每章含：
- 章號及題
- 要事（三至五）
- 出場人物
- 情感調
- 伏筆（埋／收）
- 銜接""",

    # -- 後理 --
    "analyze_chapter_prompt": """析以下小說章，成摘要及更新訊。

## 章綱（參）
{chapter_outline}

## 章文
{chapter_text}

嚴依指定JSON式出。""",

    "plan_revision_request": "吾有修策之議：{feedback}\n請據此調策。",

    "genre_fantasy_keywords": ["玄幻", "修仙", "仙俠", "法術", "奇幻"],
    "genre_scifi_keywords": ["志怪", "未來", "機關", "天外", "術數"],

    "outline_merge_prompt": """以下乃同一書之{count}種風之總綱。

請成**合一之總綱**，須：
一、取各方最強之構
二、融最佳之情節與人物弧
三、保通篇邏輯一貫
四、留最精之伏筆與高潮

{drafts_text}

以Markdown出合一之總綱。""",

    # -- 審查 --
    "consistency_reviewer_system": """汝乃精細之連貫性審者。
任：審章文與前文、綱以及所供人物檔之一致。

審：
一、**人名準確性**：將章中所現之每一人名與人物檔逐一比對。記任何與檔不合之名（誤字、名誤、名互換、稱呼不一）。此為最優先之審。
二、**人物特徵一致**：驗每人之行、語風、能、性合檔否。
三、時序之準
四、場景地點之一致
五、情節之連續（所引之事須確已發生）
六、人物認知之一致（人物不應知其未知之事）

每事予信度分（0-100）：
- 0-25: 未確，或有意爲之
- 26-50: 或有問，亦或主觀
- 51-75: 或誤，須驗
- 76-100: 確誤，已核

以JSON出：
{{
    "issues": [
        {{
            "type": "consistency",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "事述",
            "location": "章中約位",
            "suggestion": "修議"
        }}
    ],
    "overall_consistency_score": 1-10
}}

惟返JSON。""",

    "style_reviewer_system": """汝乃文風審查之專。
任：審章文合文風指南否。

審：
一、敘法一致（無意外之轉）
二、語氣氛圍合指南
三、對話風合人物檔
四、節奏（太急或太緩）
五、文筆（拙辭、重詞等）

每事予信度分（0-100）。

以JSON出：
{{
    "issues": [
        {{
            "type": "style",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "事述",
            "location": "章中約位",
            "suggestion": "修議"
        }}
    ],
    "overall_style_score": 1-10
}}

惟返JSON。""",

    "foreshadowing_reviewer_system": """汝乃伏筆情節連貫之專。
任：審章中伏筆之理。

審：
一、所埋伏筆夠隱否（不太露）？
二、前埋之鉤適時推進或收否？
三、據綱，有遺漏之伏筆機否？
四、已收之伏筆令人滿否？
五、章末爲下章造足懸否？

每事予信度分（0-100）。

以JSON出：
{{
    "issues": [
        {{
            "type": "foreshadowing",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "事述",
            "location": "章中約位",
            "suggestion": "修議"
        }}
    ],
    "overall_foreshadowing_score": 1-10
}}

惟返JSON。""",

    "review_chapter_prompt": """請審以下章。

## 人物檔（權威參照，用於核對姓名與特徵）
{character_profiles}

## 文風指南
{style_guide}

## 章綱
{chapter_outline}

## 近章摘
{recent_briefs}

## 伏筆追蹤
{hooks_info}

## 章文
{chapter_text}

重要：請將章文中所有人名與上方人物檔逐一比對。任何名不匹配皆為重障。

依指定JSON式出審果。""",
    # -- 潤色 --
    "polish_evaluate_system": """汝乃資深編者。以1-10分評章之品。

維度：
一、文筆品質及可讀性
二、人物聲音一致
三、節奏流暢
四、情感衝力
五、鉤之強度（首尾）
六、合綱之度

以JSON出：
{{
    "score": 1-10,
    "strengths": ["優一", "優二"],
    "weaknesses": ["不足一", "不足二"],
    "specific_improvements": [
        {{
            "location": "文中位",
            "current": "當前問文（簡）",
            "suggested": "改議"
        }}
    ]
}}

惟返JSON。""",

    "polish_evaluate_prompt": """評此章之品。

## 文風指南
{style_guide}

## 章綱
{chapter_outline}

## 章文
{chapter_text}

以JSON出評果。""",

    "polish_improve_system": """汝乃才具之著書人，正行修訂。
將得章文及編者之具體改議。
重撰**完整章文**，融改議而保故事、調性、結構。

勿加元評——惟出修訂後章文。""",

    "polish_improve_prompt": """據編者回饋修以下章。

## 編者回饋
不足：{weaknesses}

具體改議：
{improvements}

## 當前章文
{chapter_text}

出完整修訂後章文。""",

    # -- 卷間檢點 --
    "volume_adjust_prompt": """讀者對第{volume_num}卷有以下回饋。

回饋：{feedback}

當前卷綱：
{volume_outline}

修卷綱以融讀者之饋，保與總綱一致。

以Markdown出修後卷綱。""",

    # -- 字數校驗之令 --
    "expand_chapter_system": """汝乃才高之書者。字不足之章，需擴之。
保其品而擴之以達目標之數。勿以注水充之。

擴之術：
- 增細膩之描摹（景、情、五感）
- 展對話之往來，增自然之問答
- 添人物內心之獨白與反應
- 細寫動作之場，增生動之敘
- 添烘托氛圍之過渡

要：惟出擴後章之全文。勿出元資訊或注。""",

    "expand_chapter_prompt": """此章字數不足（{current_words}字）。請擴至約{target_words}字。

## 文風之引
{style_guide}

## 章之大綱
{chapter_outline}

## 今章正文（過短）
{chapter_text}

請出擴後章之全文（{target_words}字以上）。""",

    "compress_chapter_system": """汝乃老練之編者。字溢之章，需縮之。
保一切要緊之情節與人物之刻而縮之。

縮之術：
- 精煉文辭，去冗餘之描
- 合重複之對話
- 略不甚要之過渡
- 去不推情節之文
- 簡動作之場

要：一切要緊之事件、人物之長、伏筆須保。
惟出縮後章之全文。勿出元資訊或注。""",

    "compress_chapter_prompt": """此章字數過多（{current_words}字）。請縮至約{target_words}字。

## 文風之引
{style_guide}

## 章之大綱（保一切要事）
{chapter_outline}

## 今章正文（過長）
{chapter_text}

請出縮後章之全文（約{target_words}字）。保一切要緊之情節。""",

    "split_chapter_system": """汝乃老練之編者。甚長之章，需裂爲二。
尋自然之斷處以裂之。裂後各章須：
- 有己之戲劇弧（序 → 展 → 鉤結）
- 長短相若
- 終於自然之懸處或轉處

出之式：二章之間用 "===CHAPTER_SPLIT===" 爲界。
各章以章題行始。

要：惟出以 ===CHAPTER_SPLIT=== 爲界之二章正文。勿出餘注。""",

    "split_chapter_prompt": """此章甚長（{current_words}字，每章之標：{min_words}至{max_words}字）。請裂爲二章。

## 文風之引
{style_guide}

## 原章大綱
{chapter_outline}

## 今章正文（待裂）
{chapter_text}

裂爲結構完整之二章。以 "===CHAPTER_SPLIT===" 爲界。
第{chapter_num_a}章爲前半，第{chapter_num_b}章爲後半。
各章約{target_words}字。""",

    # -- 完結總結 --
    "final_summary_system": """汝乃文學分析者。爲已成之書成全面總結。

以Markdown出，含：
一、**書覽** — 名、體、終字數、章數
二、**情節綜述** — 全故事之梗概（含洩底）
三、**人物弧析** — 每要角之成長
四、**旨趣析** — 核心旨趣及展開
五、**數據統計** — 各章字數、均值、最長最短章
六、**伏筆收報** — 何伏筆已埋已收
七、**文品評注** — 整體文筆、亮點
八、**續書線索** — 可續之開放線""",

    "final_summary_prompt": """爲此已成之書成全面完結總結。

## 著書策
{plan_json}

## 章摘
{all_briefs}

## 人物檔
{characters}

## 伏筆追蹤
{hooks_info}

## 統計
- 總章：{total_chapters}
- 總字：約{total_words}

以Markdown出全結。""",

    # -- Language enforcement instruction --
    "language_instruction": (
        "**要旨——言語之則**："
        "凡所輸出，悉以{native_name}（{english_name}）爲之。"
        "一句一段，標題標簽，皆用{native_name}，不可雜以他語。"
        "惟引用專名術語，方可例外。"
    ),
})

# ============================================================
# TEMPLATES: Markdown模板（文言全譯）
# ============================================================
TEMPLATES = dict(_BASE_TEMPLATES)
TEMPLATES.update({
    "readme": """# 📖 著書之業

## 書之大要
- **書名**：《{title}》
- **體裁**：{genre}
- **約字**：{target_words}
- **每章字**：{min_words}-{max_words}
- **約章數**：{total_chapters}
- **卷分**：{volumes}
- **敘法**：{pov}
- **要詞**：{tags}

## 一言
{one_line_summary}

## 📁 卷牘之構

```
{title}/
├── README.md              # 總綱
├── meta/                  # 元訊
│   ├── progress.md        # 進度
│   ├── style_guide.md     # 文風
│   └── hooks_tracker.md   # 伏筆
├── worldbuilding/         # 天地設
│   ├── characters.md      # 人物檔
│   ├── world_setting.md   # 天地觀
│   └── ...                # 餘設
├── plot/                  # 情節
│   ├── master_outline.md  # 總綱目
│   ├── volume_XX.md       # 卷綱
│   └── chapter_briefs.md  # 章摘
└── chapters/              # 正文
    ├── chapter_001.txt    # 第一章
    └── ...
```

## 🔄 著文之序
一、閱progress.md → 知進度
二、閱chapter_briefs.md → 顧近章
三、參當前卷綱 → 定本章
四、查hooks_tracker.md → 觀伏筆
五、閱characters.md → 確人物態
六、出正文於chapters/
七、更progress.md、chapter_briefs.md等
""",

    "progress": """# 📊 進度

## 今態
- **最新成章**：未始
- **方撰**：待定
- **當前卷**：第一卷
- **總字**：0
- **末更**：-

## 後步
> 一、~~定體裁~~ ✅
> 二、~~核心設及主人公~~ ✅
> 三、~~總綱~~ ✅
> 四、**成首卷細綱** ← 今
> 五、始撰文

## 已成章

| 章 | 題 | 約字 | 要事 |
|----|---|------|------|

## 人物態速覽
（待更）

## 待爲
- [x] 定體裁
- [x] 成天地設
- [x] 成人物設
- [x] 成總綱
- [ ] 成首卷細綱
- [ ] 第一章文
""",

    "hooks_tracker": """# 🎣 伏筆追蹤

> 錄所埋伏筆懸念，追其態
> 態：🔴 已埋未收 | 🟡 部分揭 | 🟢 已收 | ⚪ 計中

---

## 長線伏筆（跨卷）

| ID | 內容 | 埋章 | 計收 | 態 | 注 |
|----|------|------|------|---|---|

## 短線伏筆（本卷內）

| ID | 內容 | 埋章 | 計收 | 態 | 注 |
|----|------|------|------|---|---|

## 已收記

| ID | 內容 | 埋章 | 收章 | 注 |
|----|------|------|------|---|
""",

    "chapter_briefs": """# 📝 章摘

> 每章畢錄摘，以速覽情節
> 式：章號 | 題 | 字 | 要事 | 人物變 | 伏筆

---
""",

    "synopsis_title": "# 書之概\n\n",

    "chapter_brief_entry": """
### 第{chapter_num}章 · {title}（約{word_count}字）
**要事**：
""",
    "character_changes_header": "\n**人物態變**：\n",
    "hooks_planted_header": "\n**新伏筆**：\n",
    "next_hook_prefix": "\n**下章鉤**：",

    "progress_update_entry": """
---
### 第{chapter_num}章畢更
- **最新成**：{latest_chapter}
- **累計字**：約{total_words}
""",
    "character_status_header": "\n**人物態速覽**：\n",

    "final_summary_filename": "meta/final_summary.md",
})

"""
古典日本語（文語体）ロケール — 源氏物語に倣ひ、平安朝の和文を旨とす
"""
from locales.en import PROMPTS as _BASE_PROMPTS, TEMPLATES as _BASE_TEMPLATES
from locales.ja import UI as _JA_UI

# Start from modern Japanese UI and override with classical bungo forms
UI = dict(_JA_UI)
UI.update({
    "welcome_title": "📖 物語綴りの工房 v1.0",
    "welcome_subtitle": "   からくりの智を以て物語を紡ぐ仕組みなり",
    "no_backend": "\n❌ 用ゐ得べきからくりの背後、一つも見えず！",
    "no_backend_hint": "   llm_openai.py もしくは llm_local.py、いづれか一つは在るべし",
    "select_api_mode": "\n🔌 からくりの道筋を選び給へ：",
    "auto_selected": "\n  （{desc}のみ見いだされたれば、おのづから定めつ）",
    "input_choice": "\n👤 選び給へ (1-{max}): ",
    "invalid_choice": "選び誤りなり。1-{max}を入れ給へ",
    "project_setup": "\n📁 著作の設ひ",
    "input_novel_name": "👤 物語の名を入れ給へ（文箱を造るに用ゐむ）: ",
    "scan_projects_header": "\n📂 既にある物語：",
    "no_existing_projects": "\n📂 既にある物語見えず。",
    "project_status_chapters": "{count}篇",
    "project_status_plan": "計",
    "project_status_meta": "志",
    "project_status_plot": "綱",
    "or_input_manually": "手づから名を書く...",
    "select_project_prompt": "\n👤 いづれか選び給へ (1-{max}): ",
    "select_operation": "\n🎯 いかにせむとするか選び給へ：",
    "op_full": "  1. はじめより通して営む",
    "op_resume": "  2. さきの続きより営む",
    "op_planning": "  3. はかりごとのみ",
    "op_worldbuilding": "  4. 世界の設ひと文の風のみ",
    "op_outline": "  5. 綱目のみ",
    "op_writing": "  6. 筆を執るのみ（綱目の備はりたるを要す）",
    "op_batch": "  7. 續けざまに數多の物語を營む",
    "goodbye": "\n👋 これにて御暇申す。いづれまた見え奉らむ。",

    # -- 續けざまの營み --
    "batch_input_names": "\n📚 物語の名を讀點にて分かちて入れ給へ（例：物語甲, 物語乙, 物語丙）：",
    "batch_empty": "❌ 物語の名なし。本肆に還る。",
    "batch_select_op": "\n🎯 各々の物語に何をなさむか選び給へ：",
    "batch_start": "\n🚀 續けざま：{total} 篇の物語を順に營まむ：{names}",
    "batch_progress": "📖 [{current}/{total}] 物語を始む：{name}",
    "batch_novel_done": "✅ 物語『{name}』成りにけり！",
    "batch_interrupted": "\n⏸️ 『{name}』を書きさしに中斷す。殘り {remaining} 篇いまだ成らず。",
    "batch_continue_prompt": "殘りの物語を續けて營まむか？(y/n)：",
    "batch_stopped": "🛑 續けざまの營みを止めにけり。",
    "batch_novel_error": "\n❌ 物語『{name}』に障りあり：{error}",
    "batch_all_done": "\n🎉 續けざま成就す！凡て {total} 篇みな成りにけり。",

    "select_language": "\n🌐 物語に用ゐる言の葉を選び給へ：",
    "phase_planning_title": "\n📝 其の一　はかりごと",
    "planner_prefix": "\n🤖 はかりびと申す：\n",
    "user_prefix": "👤 御方：",
    "input_empty_hint": "（御答へ給はらまほし）",
    "multiline_hint": "（数行の入力を許す、空行にて終了。/paste にて貼付の式に入る）",
    "multiline_paste_hint": "（貼付の式：空行を含む文を自在に貼り得。/end にて終了）",
    "quit_planning": "はかりごと、これにてやむ。",
    "force_done": "畏し。方略をまとめ申さむ……",
    "generating_plan": "\n⏳ 物語の方略を練りゐたり……",
    "plan_display_title": "\n📋 物語の方略",
    "plan_label_title": "書の名",
    "plan_label_genre": "体裁",
    "plan_label_theme": "旨趣",
    "plan_label_one_line": "一言にて",
    "plan_label_beginning": "起",
    "plan_label_middle": "承",
    "plan_label_end": "結",
    "plan_label_characters": "主なる人々",
    "confirm_plan": "\n👤 この方略にてよろしきや？(y／直すべき儀): ",
    "adjusting_plan": "\n⏳ 仰せに従ひて方略を改むる……",
    "plan_confirmed": "✅ 方略定まりぬ。記し置きつ！",
    "rename_dir_prompt": "\n📁 書の題は「{title}」なれど、匣の名は「{dir}」なり。",
    "rename_dir_confirm": "   匣の名を「{title}」に改めむや？ (y/n): ",
    "rename_dir_done": "  ✅ 匣の名を改めたり: {path}",
    "rename_dir_exists": "  ⚠️ 同じ名の匣あり: {path}",
    "rename_dir_failed": "  ❌ 名を改むること叶はず: {error}",
    "phase_world_title": "\n🌍 其の二　世界の営みと文の風（竝びて営む……）",
    "phase_outline_title": "\n📋 其の三　総綱目",
    "phase_writing_title": "\n✍️ 其の五　筆を執りて",
    "writing_complete": "🎉 書き了りぬ！",
    "planning_incomplete": "はかりごといまだ成らず、退く。",
    "llm_error_retry": "あな、からくりに障りありけり。今一度仰せ給へ。",
    "info_enough": "聞き及びたること十分なり。方略をまとめ申さむ…… 🎯",
    "continue_input": "御方の綴らむとする物語につきて、なほ語り給へ。",

    # -- Feature #1-#6: Classical overrides --
    "outline_multi_draft_title": "\n📋 其の三　総綱目（多き方を並べて比ぶ）",
    "generating_draft": "  ⏳ 綱の第{num}/{total}方を練りゐたり（風：{style}）……",
    "draft_done": "  ✅ 第{num}方成りぬ",
    "draft_failed": "  ❌ 第{num}方成らず：{error}",
    "draft_comparison_title": "\n📊 綱の各方を比べ観る",
    "draft_select_prompt": "\n👤 何れの方を用ゐ給ふ (1-{max})、または'm'にて諸方の精を合はす: ",
    "draft_merging": "⏳ 諸方の精を合はしゐたり……",
    "draft_selected": "✅ 第{num}方を総綱と定めつ",
    "draft_merged": "✅ 合はせたる綱成りぬ",
    "outline_drafts_truncating": "   ⚠️ 綱稿長きに過ぐ（推し量りて {total} tokens、限り {budget}）、等しく切り詰む...",
    "parallel_review_title": "  🔍 竟べて審かに核しゐたり……",
    "review_consistency": "〈前後の一貫〉",
    "review_style": "〈文の風〉",
    "review_foreshadowing": "〈伏線〉",
    "polish_start": "  ✨ 潤ひの繰り返しを始む（至りて{max_iter}遍）……",
    "polish_passed": "  ✅ 品の閾に達しぬ！潤ひを止む。",
    "volume_checkpoint_title": "\n📍 第{num}巻の檜をものするところ",
    "volume_checkpoint_prompt": "\n👤 第{num}巻を始めむとす。續くるや？(y / adjust / stop): ",
    "writing_complete": "🎉 書き了りぬ！",
    "final_summary_title": "\n📊 全書の総めを記しゐたり……",
    "final_summary_done": "✅ 総め成りて記し置きつ！",
    "final_summary_failed": "⚠️ 総め成らず：{error}",

    # -- 筆の設ひ --
    "writing_params_title": "\n⚙️ 筆の設ひ",
    "ask_chapter_min_words": "   章ごとの下限の文字（今: {current}、入を押さば変へず）: ",
    "ask_chapter_max_words": "   章ごとの上限の文字（今: {current}、入を押さば変へず）: ",
    "writing_params_swapped": "   ⚠️ 下限が上限を超えたれば、互ひに替へたり。",
    "ask_word_count_check": "   文字数の検めを行ふか？（今: {status}、y/n、入を押さば変へず）: ",
    "ask_lazy_mode": "   任せの法を用ゐるか？（今: {status}、y/n、入を押さば変へず）: ",
    "writing_params_summary": "   ✅ 筆の設ひ: {min}〜{max}字/章、文字数検め: {check}、任せの法: {lazy}",

    # -- 対話の引用符 --
    "quote_style_title": "\n💬 対話の符の設ひ",
    "quote_style_prompt": "\n👤 物語の対話に用ゐる符を選び給へ (1-{max}): ",
    "quote_style_invalid": "選び誤りなり。1-{max}を入れ給へ",
    "quote_style_selected": "✅ 対話の符を定めたり: {style}",
    "quote_style_option_curly": '\u201c\u201d 丸き二重の符（例：\u201cおはようございます\u201d）',
    "quote_style_option_corner": '「」 鉤の符（例：「おはようございます」）',
    "quote_style_option_guillemet": '«» 仏蘭西式の符（例：«おはようございます»）',
    "quote_style_option_dash": '— 棒引きの符（例：— おはようございます）',
    "quote_style_option_straight": '"" 直き符（例："おはようございます"）',

    # -- 心の内の符 --
    "inner_quote_title": "\n💭 心の内・独り言の符の設ひ",
    "inner_quote_prompt": "\n👤 心の裡の描写に用ゐる符を選び給へ (1-{max}): ",
    "inner_quote_invalid": "選び誤りなり。1-{max}を入れ給へ",
    "inner_quote_selected": "✅ 心の内の符を定めたり: {style}",
    "inner_quote_option_corner_double": '『』 二重鉤の符（例：『心せねばならぬ』）',
    "inner_quote_option_corner": '「」 鉤の符（例：「心せねばならぬ」）',
    "inner_quote_option_curly_single": '\u2018\u2019 丸き一重の符（例：\u2018心せねばならぬ\u2019）',
    "inner_quote_option_italic": '*傾き文字* にて心を示す（例：*心せねばならぬ*）',
    "inner_quote_option_dash": '——二重棒引き（例：——心せねばならぬ——）',
    "inner_quote_option_paren": '（）丸括弧（例：（心せねばならぬ））',
    "inner_quote_option_same": '対話と同じ符',
    "inner_quote_option_none": '符を用ゐず（地の文にて心を描く）',

    # -- 引用符の法（文體指南に注入さるる） --
    "quote_rules_heading": "引用符の法",
    "quote_rule_dialogue_curly": '對話には\u201c\u201d（丸き二重の符）を用ゐよ。例：\u201cおはようございます\u201d',
    "quote_rule_dialogue_corner": '對話には「」（鉤の符）を用ゐよ。例：「おはようございます」',
    "quote_rule_dialogue_guillemet": '對話には«»（仏蘭西式の符）を用ゐよ。例：«おはようございます»',
    "quote_rule_dialogue_dash": '對話には—（棒引き）を用ゐよ。例：— おはようございます',
    "quote_rule_dialogue_straight": '對話には""（直き符）を用ゐよ。例："おはようございます"',
    "quote_rule_inner_corner_double": '心の裡には『』（二重鉤の符）を用ゐよ。例：『心せねばならぬ』',
    "quote_rule_inner_corner": '心の裡には「」（鉤の符）を用ゐよ。例：「心せねばならぬ」',
    "quote_rule_inner_curly_single": '心の裡には\u2018\u2019（丸き一重の符）を用ゐよ。例：\u2018心せねばならぬ\u2019',
    "quote_rule_inner_italic": '心の裡には*傾き文字*を用ゐよ。例：*心せねばならぬ*',
    "quote_rule_inner_dash": '心の裡には——（二重棒引き）を用ゐよ。例：——心せねばならぬ——',
    "quote_rule_inner_paren": '心の裡には（）（丸括弧）を用ゐよ。例：（心せねばならぬ）',
    "quote_rule_inner_none": '心の裡に特別の符を用ゐず、地の文にて心を描くべし。',
    "quote_rule_inner_same": '心の裡にも對話と同じ符を用ゐよ。',

    # -- おまかせの法 --
    "lazy_mode_enabled": "🛋️ おまかせの法にて — 綱定まりし後は總て自ずと進む！",
    "lazy_auto_merge": "🛋️ [おまかせ] 總ての綱の草稿を自ずと統ぶ...",
    "lazy_auto_select": "🛋️ [おまかせ] 草稿唯一つ、自ずと選びたり。",
    "lazy_auto_continue": "🛋️ [おまかせ] 自ずと續く...",
    "lazy_auto_retry": "🛋️ [おまかせ] 自ずと再び試む...",
    "lazy_auto_skip": "🛋️ [おまかせ] 自ずと飛ばす...",
    "lazy_auto_volume_continue": "🛋️ [おまかせ] 第{num}巻へ自ずと續く...",

    # -- 審校の再試み --
    "review_retry_feedback": """⚠️ 肝要なり：此は{attempt}/{max_attempts}度目の書き直しなり。前の稿に下の重き障りありて、悉く正すべし：
{issues}

章の全體を初めより書き直し、上なる障り悉く正しつつ、物語の筋・調子・構へを損なふなかれ。""",
    "review_max_retries_reached": "  ⚠️ 第{num}章の審校再試み、上限（{max}度）に至りぬ。今の稿を存して續く。",

    # -- 以下、これまで現代語のままなりし条を文語に改む --

    # API 設ひ
    "api_openai_desc": "OpenAI標準の式（APIの鍵を要す）",
    "api_local_desc": "手許の stream-server API",
    "input_openai_key": "OpenAI APIの鍵を入れ給へ: ",
    "api_key_empty": "APIの鍵、空なるは叶はず！",
    "input_base_url": "API Base URL (そのままにてはEnter: {default}): ",
    "input_model": "からくりの名 (そのままにてはEnter: {default}): ",
    "input_local_url": "手許のAPIの在処を入れ給へ: ",
    "api_url_empty": "APIの在処、空なるは叶はず！",
    "input_api_key": "APIの鍵を入れ給へ (飛ばすはEnter): ",
    "input_wsid": "WSIDを入れ給へ (飛ばすはEnter): ",
    "input_model_marker": "からくりの印を入れ給へ (飛ばすはEnter): ",

    # 操作選択
    "input_op_choice": "\n👤 選び給へ (1-7): ",
    "invalid_op": "選び誤りなり。1-7を入れ給へ",

    # 巻・章の入力
    "input_volume_num": "いづれの巻の綱を成さむ？(番を入れ給へ、またはEnterにて飛ばす): ",
    "input_start_chapter": "何れの章より始めむ？(Enterにて第一章より): ",
    "input_end_chapter": "何れの章まで綴らむ？(Enterにて末まで): ",

    # 中断・過誤
    "interrupted": "\n\n⏸️ 御方の手により中断す。進みは記し置きつ。次の折に「さきの続きより」を選び給へ。",
    "error_occurred": "\n❌ 障りの起こりたり: {error}",

    # 言語選択
    "lang_choice_prompt": "\n👤 選び給へ (1-{max}): ",

    # 企画
    "plan_label_target_words": "目指す文字数",
    "plan_label_total_chapters": "見込みの章数",
    "plan_label_volumes": "巻数",
    "plan_label_pov": "語りの目",
    "plan_label_tags": "核なる標",

    # 世界観
    "world_done": "✅ 世界の設ひ成りぬ（{count}つの文）",
    "world_failed": "❌ 世界の設ひ成らず: {error}",
    "style_done": "✅ 文の風の指南成りぬ",
    "style_failed": "❌ 文の風の指南成らず: {error}",
    "worldbuilding_start": "〔世界の営み〕{count}つの設定を竝びて成す……",
    "doc_done": "  ✅ {filename} 成りぬ",
    "doc_failed": "  ❌ {filename} 成らず",
    "doc_error": "  ❌ {filename} に障りあり: {error}",

    # 綱目
    "generating_outline": "⏳ 総綱を練りゐたり……",
    "outline_done": "✅ 総綱成りぬ",
    "outline_review": "\n📖 総綱を plot/master_outline.md に記し置きたり。御覧じ給へ。",
    "press_enter_continue": "👤 Enterを押して第一巻の綱へ進み給へ……",
    "generating_volume": "📑 第{num}巻の綱を練りゐたり……",
    "volume_done": "✅ 第{num}巻の綱成りぬ",

    # 執筆
    "checkpoint_resume": "〔栞〕{count}章の成りたるを見出す。第{next}章より再び始む",
    "volume_not_found": "⚠️ 第{num}巻の綱見えず。今より成す……",
    "generating_volume_outline": "⏳ 第{num}巻の綱を練りゐたり……",
    "writing_chapter": "📖 第{num}章を綴りゐたり……",
    "chapter_done": "  ✅ 第{num}章綴り了りぬ（凡そ{words}文字）",
    "post_processing": "  ⏳ 元の情報を分析し改めゐたり……",
    "post_done": "  ✅ 第{num}章の後の処理了りぬ",
    "post_failed": "  ⚠️ 第{num}章の後の処理叶はず、飛ばす",
    "chapter_error": "  ❌ 第{num}章の綴りに障りあり: {error}",
    "retry_prompt": "  今一度試みむか？(y/n): ",
    "skip_chapter": "  第{num}章を飛ばし、次へ進む",
    "pause_prompt": "\n📊 {num}章成りぬ。Enterにて続く、'stop'にて暫し休む",
    "pause_input": "👤 ",
    "paused": "⏸️ 暫し休みぬ。次の折は第{next}章より再び始め得べし",

    # 企画書未了
    "no_plan_found": "方略見えず。はじめより始む……",
    "resume_checking": "🔄 著作の有様を確かめゐたり……",
    "resume_completed": "{count}章成りたり。綴りを続く……",
    "no_style_guide": "文の風の指南見えず。今より成す……",
    "no_outline": "総綱見えず。今より成す……",
    "plan_not_found_error": "方略の巻 plan.json 見えず。先にはかりごとを営み給へ",

    # 設定の読み込み
    "config_loaded": "〔設〕{file}より設ひを読みたり: {keys}",
    "novel_config_loaded": "〔設〕書の設{file}より読みたり: {keys}",
    "novel_config_skipped": "  ⚠️ {file}のAPI/経路の設ひを略しけり（通の設ひを用ゐ給へ）: {keys}",
    "novel_config_auto_created": "〔設〕範より{file}を自ら造りたり（此の書の設ひを調え給へ）",
    "config_not_found": "〔設〕{file}見えず。定めの儘を用ゐむ。APIの鍵は手にて入るべし",
    "config_hint": "〔設〕user_config.example.jsonを参じて{file}を造り給へ",
    "project_initialized": "〔著作〕文箱の整へ了りぬ: {path}",
    "file_written": "〔記〕書き了りぬ: {path}",

    # LLM OpenAI
    "openai_initialized": "〔LLM-OpenAI〕整へ了りぬ。からくり: {model}、在処: {url}",
    "openai_need_package": "OpenAIの背後にはopenaiの包みを要す: pip install openai",
    "openai_no_key": "OPENAI_API_KEY未だ設けず。user_config.jsonに記すか、走らする折に入れ給へ",
    "openai_attempt_failed": "〔LLM-OpenAI〕{n}度目の試み叶はず: {error}",
    "openai_retry_wait": "〔LLM-OpenAI〕{wait}秒待ちて再び試む……",
    "openai_max_retries": "〔LLM-OpenAI〕最多の試み({max}度)に至りぬ。止む",

    # LLM Local
    "local_initialized": "〔LLM-手許〕整へ了りぬ。在処: {url}、印: {marker}",
    "local_need_package": "手許の背後にはrequestsの包みを要す: pip install requests",
    "local_no_url": "LOCAL_API_URL未だ設けず。user_config.jsonに記し給へ",
    "local_attempt_failed": "〔LLM-手許〕{n}度目の試み叶はず: {error}",
    "local_retry_wait": "〔LLM-手許〕{wait}秒待ちて再び試む……",
    "local_max_retries": "〔LLM-手許〕最多の試み({max}度)に至りぬ。止む",

    # 読み込み不能
    "cannot_load_openai": "OpenAIの背後を読み込み得ず: {error}\nllm_openai.py在りてopenaiの入りたるを確かめ給へ",
    "cannot_load_local": "手許の背後を読み込み得ず: {error}\nllm_local.py在りてrequestsの入りたるを確かめ給へ",
    "unsupported_api_mode": "知らぬAPIの道: {mode}。選べるは 'openai' か 'local' なり",

    # ドラフト
    "draft_header": "\n{'─' * 40}\n📄 第{num}方 — 風：{style}\n{'─' * 40}",
    "draft_invalid": "選び誤りなり。1-{max}または'm'を入れ給へ",

    # 審査
    "review_done": "  ✅ {reviewer}：{count}つの事を見出す（信度≥{threshold}）",
    "review_failed": "  ⚠️ {reviewer} 審し叶はず: {error}",
    "review_no_issues": "  ✅ 審すもの皆通りぬ — 大事なし！",
    "review_issues_found": "  ⚠️ 審すもの合はせて{count}つの事を見出す:",
    "review_issue_item": "    [{severity}] ({reviewer}、信度: {confidence}) {description}",
    "review_critical_prompt": "  🚨 重き障り見つかりぬ。この章を書き直さむか？(y/n): ",
    "severity_critical": "甚大",
    "severity_major": "大",
    "severity_minor": "小",
    "severity_info": "報",

    # 潤ひ
    "polish_iteration": "  ✨ 潤ひ {iter}/{max_iter}度目……",
    "polish_score": "  📊 品の値: {score}/10（閾: {threshold}）",
    "polish_improving": "  ⏳ 値の閾に満たず、改めゐたり……",
    "polish_max_reached": "  ⚠️ 潤ひの最多に至りぬ。最も良き方を用ゐむ（値: {score}/10）。",
    "polish_failed": "  ⚠️ 潤ひの評し叶はず、今の儘を保つ。",

    # 巻間の檢め
    "volume_checkpoint_summary": "  今の進み: {completed}章成りぬ、凡そ{words}文字",
    "volume_checkpoint_adjust": "👤 直しの儀を入れ給へ: ",
    "volume_checkpoint_adjusting": "⏳ 仰せに従ひて巻の綱を改めゐたり……",
    "volume_checkpoint_stopped": "⏸️ 第{num}巻の手前にて止む。次は第{next}章より再び始め得べし。",

    # -- 多方の綱 --

    # -- 字数の校（文語） --
    "wordcount_check_start": "  📏 字数校：{words}字（目安：{min}〜{max}）",
    "wordcount_too_short": "  ⚠️ 章短し（{words}字、最少{min}字）。拡げゐたり……",
    "wordcount_too_long": "  ⚠️ 章長し（{words}字、最多{max}字）。縮めゐたり……",
    "wordcount_split_needed": "  📑 章甚だ長し（{words}字、≧{threshold}%上限）。二章に割らむ……",
    "wordcount_expand_done": "  ✅ 拡充了りぬ：{words}字",
    "wordcount_compress_done": "  ✅ 縮め了りぬ：{words}字",
    "wordcount_split_done": "  ✅ 割り了りぬ：第{num_a}章（{words_a}字）＋ 第{num_b}章（{words_b}字）",
    "wordcount_retry": "  🔄 字数校再試 {attempt}/{max_attempts}……",
    "wordcount_give_up": "  ⚠️ {max_attempts}度の試みも達せず。今の版を用ゐむ（{words}字）。",
    "wordcount_ok": "  ✅ 字数宜し：{words}字",
    "wordcount_split_renumber": "  📝 割りたる後、續く章の番を改む。",

    "outline_style_dramatic": "劇的にして張り詰めたる",
    "outline_style_literary": "文芸にして人物を重んずる",
    "outline_style_commercial": "世に売るべく疾き節の",
})

PROMPTS = dict(_BASE_PROMPTS)
PROMPTS.update({
    "planner_system": """汝は、物語を構ふることに習ひたるはかりびとなり。何もなき所より小説の根本を思ひ設くることをよくす。

使ひ手と語らひて、下に記す物語の核なる要を定むるに足る情報を集むるこそ汝の務めなれ。

一、**体裁**：幻想、世情、探偵、恋、天文など
二、**旨趣**：この物語にて何を語らむとするか
三、**文字数と構へ**：総じての文字数、一章ごとの文字数、章の数、巻の数
四、**語りの目**：われ（一人称）か、かれ（三人称）か
五、**核なる標**：三つより五つの肝要なる詞
六、**一言にて**：全書を括る一文
七、**三段の梗概**：起、承、結の大筋
八、**文の風の望み**：文体、調子、手本とすべき作
九、**忌むべきこと**：含むまじき内容
十、**主なる人々**：少なくとも主なる者の基き設定
十一、**世界の枠組み**：物語の開くる世の背景

みづから使ひ手に問ひかけてこれらの情報を集むべし。使ひ手の自ら決せざる所は、汝が創りて補ふべし。
情報十分なりと見做したるとき、最終の物語方略を出だすべし。

心すべきこと：
- 一度に問ふは二つ三つにとどむべし
- 答へに応じて後の問ひを柔らかに改むべし
- 各要素につき、使ひ手みづから定めむとするか、汝に委ねむとするかを確かむべし
- 親しみ深く、かつ事に通じたる語りの風を保つべし""",

    "planner_first_question": """御方に御挨拶申し上ぐ。物語のはかりびとなり。🎉

筆を執る前に、御方の思し召しを伺はまほし。一歩づつ参らむ。

**まづ、もつとも根本なる問ひにて：**
一、いかなる**体裁**の物語を綴らむと思し召すや？（たとへば、幻想、世情、探偵、天文、恋、歴史など）
二、おほよその**物語の行く末**、もしくは**核なる着想**はおはしますや？ほのかなる思ひにても構はず
三、かやうな基きの設定、御みづから定め給ふか、それともわれに委ね給ふか？

御心のままに語り給へ。""",

    "planner_check_enough": """目下集めたる情報を悉く分析し、方略を起こすに足るか判じ給へ。

核なる要素の一覧：
一、体裁 - {has_genre}
二、旨趣 - {has_theme}
三、文字数と構へ - {has_structure}
四、語りの目 - {has_pov}
五、核なる標 - {has_tags}
六、一言にて - {has_summary}
七、文の風の望み - {has_style}
八、主なる人々（少なくとも主人公の概） - {has_characters}
九、世界の枠組み - {has_world}

JSON形式にて答へ給へ：
{{
    "is_enough": true/false,
    "missing_items": ["足らざる要素の一覧"],
    "next_questions": "情報足らずんば、使ひ手に次に問ふべきこと（二つ三つ）"
}}

JSONのみ返し給へ。""",

    "planner_summarize": """以下の語らひにて集めたる情報に基づき、全き物語方略を成し給へ。
使ひ手の明示せざる所は、創りて補ひ、方略の全体をして一貫し、かつ人を惹くものとし給へ。

下の如きJSON形式にて厳に出だし給へ、他は何も出だすべからず：
{{
    "title": "書の名",
    "genre": "体裁",
    "theme": "旨趣（一段にて）",
    "target_words": "目指す総文字数",
    "chapter_words": "一章ごとの文字数の範囲",
    "total_chapters": "総章数の見込み",
    "volumes": "巻数と分け方",
    "pov": "語りの目",
    "tags": "核なる標（読点にて分かつ）",
    "one_line_summary": "一言の梗概",
    "three_act_summary": {{
        "beginning": "起（始まりの大要）",
        "middle": "承（展開の大要）",
        "end": "結（結末の大要）"
    }},
    "style_guide": "文の風の求めと筆の規",
    "taboos": "忌むべきこと",
    "main_characters": [
        {{
            "name": "名",
            "role": "立場（主人公／敵役／脇役など）",
            "age": "齢",
            "appearance": "姿形",
            "personality": "人となり",
            "background": "来歴",
            "motivation": "志",
            "arc": "人物の弧光"
        }}
    ],
    "world_setting": "世界の枠組みの描写",
    "synopsis": "物語の概（人に示すべきもの）"
}}""",

    # -- 綱目 --
    "outline_system": """汝は練達の物語綱目を立つる者なり。与へられたる物語方略に基づき、精しき情節の綱目を立て給へ。

出だすべきもの：
一、全書の巻ごとの綱目（各巻の主筋、核なる葛藤、要なる事、巻末の高潮と懸念）
二、人物の関はりの図（文にて述ぶ）

Markdown形式にて出だし給へ。心すべきこと：
- 各巻の綱目に明らかなる主筋と事の列を含むこと
- 巻と巻の間に因果の銜接あること
- 人物の成長の弧が全書を貫くこと
- 伏線と懸念の佈りが理に適ふこと
- 張りと弛みの具合よきこと""",

    "volume_outline_system": """汝は情節を細かに立つることに長けたる綱目の師なり。
総綱の中なるある巻の概に基づき、その巻の章ごとの精しき綱目を立て給へ。

Markdown形式にて出だし給へ。各章に要するもの：
- 章の題
- 要なる事（三つより五つ）
- 出づる人々
- 情の調べ
- 伏線（埋む／収む）
- 承前啓後の接ぎ""",

    # -- 世界の営み --
    "worldbuilding_system": """汝は世界を営み造ることの専門なり。与へられたる物語方略に基づき、精しき世界の設定を立て給へ。

Markdown形式にて、含むべきもの：
一、世界の総設定（時代、社会の仕組み、術法の水準など）
二、地理・空間（要なる地とその特色）
三、特別なる体系（修業／術法／機巧の体系、体裁に従ひて）
四、大事の年表（物語の始まる前の要なる史事）

設定の間に一貫あり、相矛盾せざるやう心し給へ。""",

    "character_system": """汝は人物を塑ることに秀でたる者なり。物語方略と世界の設定に基づき、精しき人物の檔を立て給へ。

各人に要するもの：
- 基きの事（名、齢、姿形など）
- 人となりの描写（幾重にも、外の振る舞ひと内の心を含む）
- 来歴
- 能／得手
- 志
- 言の葉の風・口癖
- 人物の弧光
- 人物の関はり

Markdown形式にて出だし給へ。人物の間に化合の趣あり、性の互ひに補ふか衝くものたるべし。""",

    # -- 筆を執りて --
    "writer_system": """汝は才ある物語の著し手なり。
与へられたる設定、綱目、前の文脈に基づき、小説の本文を綴り給へ。

筆の規：
{style_guide}

構への求め：
- 各章 {min_words}—{max_words} 文字
- 章の初めに鉤を要す（前の章を承くるか、新たなる懸念を造るか）
- 核なる情節を進ます（少なくとも一つの要事）
- 章の終はりに鉤を残す（読む人をして続きを求めしむ）

厳にこの形に従ひ給へ：
- 章題の式：第X章 題
- 本文をそのまま出だし、元の情報や注を出だすべからず""",

    "writer_chapter_prompt": """以下の情報に基づき、第{chapter_num}章の本文を綴り給へ。

## 本章の綱
{chapter_outline}

## 近き章の摘要（繋がりを保つため）
{recent_briefs}

## 当今の人物の有様
{character_status}

## 心すべき伏線
{hooks_info}

## 登場人物の檔案（正典——名は寸毫も違へるべからず）
{character_profiles}

## 世界の設と地名（正典——凡ての地名・勢力名等は寸毫も違へるべからず）
{world_setting}

⚠️ 肝要なる戒め：凡ての人物の名、地の名、門派・勢力の名、また固有の称は、上なる檔案と世界の設に一字一句違はず合はすべし。己が勝手に名を造り、改め、或いは替ふること堅く禁ず。

全き章の本文（{min_words}—{max_words}文字）を、「第{chapter_num}章」にて始め給へ。""",

    # -- 後の処理 --
    "post_write_system": """汝は細やかなる物語の編み手の助けなり。各章を綴り了へたるのち、章の内容を分析し、更新の情報を成し給へ。

JSON形式にて出だし給へ：
{{
    "chapter_brief": {{
        "chapter_num": 章の番,
        "title": "章の題",
        "word_count": おほよその文字数,
        "main_events": ["要事一", "要事二", ...],
        "character_changes": ["人物の変一", ...],
        "hooks_planted": ["新たなる伏線一", ...],
        "hooks_resolved": ["収めたる伏線のID一", ...],
        "next_chapter_hook": "次の章への鉤"
    }},
    "progress_update": {{
        "latest_chapter": "第X章·題",
        "total_words": おほよその累計文字数,
        "character_status": {{
            "人物の名": "当今の有様"
        }}
    }}
}}

JSONのみ返し給へ。""",

    # -- 文の風 --
    "style_guide_system": """汝は文の風の定めを専らにする文の顧問なり。
与へられたる物語方略に基づき、精しき文の風の指南を成し給へ。

Markdown形式にて、含むべきもの：
一、語りの目の規
二、文の風の求め（総じての調子、内なる独白の風、外なる表しの風など）
三、章の構への規
四、語らひの規（対話の式、人物の語り口）
五、描きの規（戦ひ／情／山水など）
六、緩急の議
七、核なる筆の則
八、忌むべきこと""",

    # -- 世界の営みの任 --
    "task_world_setting": """以下の物語方略に基づき、世界の総設定の文を成し給へ（Markdown形式）。
含むべきもの：時代、社会の仕組み、要なる勢力などの基き世界観。

方略：
{plan_text}""",

    "task_characters": """以下の物語方略に基づき、精しき人物の檔の文を成し給へ（Markdown形式）。
各人に名、齢、姿形、人となり（幾重にも）、来歴、能、志、口癖、弧光を含むこと。
末に人物の関はりの図を添へ給へ（文にて述ぶ）。

方略：
{plan_text}""",

    "task_locations": """以下の物語方略に基づき、要なる地と場面の設定の文を成し給へ（Markdown形式）。
物語に現はるる要なる地とその特色を含むこと。

方略：
{plan_text}""",

    "task_timeline": """以下の物語方略に基づき、大事の年表の文を成し給へ（Markdown形式）。
物語の始まる前の要なる史事と、物語の中の時の運びを含むこと。

方略：
{plan_text}""",

    "task_power_system": """以下の物語方略に基づき、力／修業の体系の設定の文を成し給へ（Markdown形式）。
含むべきもの：段の分け、修業の法、特別なる能の体系など。

方略：
{plan_text}""",

    "task_tech_system": """以下の物語方略に基づき、機巧の体系の設定の文を成し給へ（Markdown形式）。
含むべきもの：技の水準、核なる技、特別なる器物など。

方略：
{plan_text}""",

    # -- 綱目の生成 --
    "master_outline_prompt": """以下の物語方略に基づき、全書の総綱を成し給へ。

## 物語方略
{plan_json}

全ての巻を含む総綱（Markdown形式）を成し給へ。各巻に要するもの：
- 主筋の描写
- 核なる葛藤
- 要なる事（番号の列）
- 主なる人物の有様
- 巻末の高潮
- 巻末の懸念
- 次の巻との接ぎ""",

    "volume_outline_prompt": """以下の情報に基づき、第{volume_num}巻の章ごとの精しき綱目を成し給へ。

## 物語方略の摘
- 名：{title}
- 体裁：{genre}
- 一章の文字数：{chapter_words}

## この巻の総綱における描写
{volume_info}

## 総綱（全き本、全体を見渡すため）
{master_outline}

この巻の章ごとの精しき綱目を成し給へ。各章に含むべきもの：
- 章の番と題
- 要なる事（三つより五つ）
- 出づる人物
- 情の調べ
- 伏線（埋む／収む）
- 銜接""",

    # -- 後の処理 --
    "analyze_chapter_prompt": """以下の小説の章を分析し、摘要と更新の情報を成し給へ。

## 章の綱（参考）
{chapter_outline}

## 章の本文
{chapter_text}

指定のJSON形式にて厳に出だし給へ。""",

    "plan_revision_request": "方略につき修正の議あり：{feedback}\nこれに従ひて方略を改め給へ。",

    "genre_fantasy_keywords": ["幻想", "修行", "仙術", "魔法", "異世界"],
    "genre_scifi_keywords": ["天文", "未来", "機巧", "宇宙", "技術"],


    "outline_merge_prompt": """以下は同じ物語の{count}通りの風の総綱なり。

**合はせたる総綱**を成し給へ、求むるところ：
一、各方より最も強き構へを取ること
二、最も優れたる情節と人物の弧を融はすること
三、通篇の理の一貫を保つこと
四、最も精き伏線と高潮の設計を留むること

{drafts_text}

Markdown形式にて合はせたる総綱を出だし給へ。""",

    # -- 審査 --
    "consistency_reviewer_system": """汝は精しき連なりの審査人なり。
任：章の文が前の文、綱、および提げられたる人物の檔と一致するかを審し給へ。

審すべきもの：
一、**人の名の正確さ**：章中に出づるすべての人名を人物の檔と逐一照らし合はせ給へ。檔と完きに一致せざる名（誤り、名の違ひ、名の入れ替へ、称の不一致）を殉く記し給へ。これぞ最も優れる審の條なり。
二、**人物の特との一致**：每の人の行、語り口、能、性の檔と合ふかを驗し給へ。
三、時の順の正しさ
四、場・地の一致
五、情節の連なり（引かれたる事は真に起こりたるか）
六、人物の知の一致（人物は未だ知らぬことを知るべからず）

各事に信度の分（0-100）を附し給へ：- 0-25: 定かならず、意図的なるやも
- 26-50: 問あるやもしれぬが、主観的判断なるやも
- 51-75: 誤りの蓋然性高し、確むべし
- 76-100: 確かに誤り、原文と対照して確む

JSON形式にて出だし給へ：
{{
    "issues": [
        {{
            "type": "consistency",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "事の述べ",
            "location": "章中のおほよその位置",
            "suggestion": "直しの議"
        }}
    ],
    "overall_consistency_score": 1-10
}}

JSONのみ返し給へ。""",

    "style_reviewer_system": """汝は文の風の審査の専門なり。
任：章の文が文の風の指南に合ふかを審し給へ。

審すべきもの：
一、語りの目の一致（思はぬ転換なきこと）
二、調子と気の合ひ具合
三、語らひの風の人物との一致
四、緩急の具合（太急か太緩か）
五、文の質（拙き辞、重なる詞など）

各事に信度の分（0-100）を附し給へ。

JSON形式にて出だし給へ：
{{
    "issues": [
        {{
            "type": "style",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "事の述べ",
            "location": "章中のおほよその位置",
            "suggestion": "直しの議"
        }}
    ],
    "overall_style_score": 1-10
}}

JSONのみ返し給へ。""",

    "foreshadowing_reviewer_system": """汝は伏線と情節の連なりの専門なり。
任：章中の伏線の取り扱ひを審し給へ。

審すべきもの：
一、埋めたる伏線は十分に密やかなるか（露骨に過ぎざるか）？
二、先に埋めたる鉤は適時に進み、あるいは収められたるか？
三、綱に照らし、見落としたる伏線の機はなきか？
四、収めたる伏線は満足ゆくものなるか？
五、章の終はりは次の章のために十分なる懸念を造りたるか？

各事に信度の分（0-100）を附し給へ。

JSON形式にて出だし給へ：
{{
    "issues": [
        {{
            "type": "foreshadowing",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "事の述べ",
            "location": "章中のおほよその位置",
            "suggestion": "直しの議"
        }}
    ],
    "overall_foreshadowing_score": 1-10
}}

JSONのみ返し給へ。""",

    "review_chapter_prompt": """以下の章を審し給へ。

## 人物の檔（権威の參照、名と特を核すに用ゐる）
{character_profiles}

## 文の風の指南
{style_guide}

## 章の綱
{chapter_outline}

## 近き章の摘要
{recent_briefs}

## 伏線の追跡
{hooks_info}

## 章の文
{chapter_text}

要：章の文のすべての人名を上の人物の檔と逐一照らし合はせ給へ。名の不一致は重き障りなり。

指定のJSON形にて審査の結果を出だし給へ。""",
    # -- 潤ひ --
    "polish_evaluate_system": """汝は年経たる編み手なり。章の品を1-10にて評し給へ。

維：
一、文の品と読み易さ
二、人物の声の一致
三、緩急と流れ
四、情の衝きの力
五、鉤の強さ（首と尾）
六、綱との合ひ

JSON形式にて出だし給へ：
{{
    "score": 1-10,
    "strengths": ["優れたる所一", "優れたる所二"],
    "weaknesses": ["足らざる所一", "足らざる所二"],
    "specific_improvements": [
        {{
            "location": "文中の位置",
            "current": "当今の問ある文（簡に）",
            "suggested": "改めの議"
        }}
    ]
}}

JSONのみ返し給へ。""",

    "polish_evaluate_prompt": """この章の品を評し給へ。

## 文の風の指南
{style_guide}

## 章の綱
{chapter_outline}

## 章の本文
{chapter_text}

JSON形式にて評の結果を出だし給へ。""",

    "polish_improve_system": """汝は才ある著し手にして、今修訂を行ひゐたり。
章の文と編み手よりの改めの議を受けむ。
**全き章の文を**書き直し、改めの議を織り込みつつ、物語と調子と構へを保ち給へ。

いかなる元の評も添ふべからず——修訂したる章の文のみを出だし給へ。""",

    "polish_improve_prompt": """編み手の饋りに従ひ、以下の章を改め給へ。

## 編み手の饋り
足らざる所：{weaknesses}

具体なる改めの議：
{improvements}

## 当今の章の文
{chapter_text}

全き修訂したる章の文を出だし給へ。""",

    # -- 巻間の檢め --
    "volume_adjust_prompt": """読む人が第{volume_num}巻につき、以下の饋りを寄せたり。

饋り：{feedback}

当今の巻の綱：
{volume_outline}

巻の綱を改め、読む人の饋りを容れつつ、総綱との一致を保ち給へ。

Markdown形式にて改めたる巻の綱を出だし給へ。""",

    # -- 字数の校の令 --
    "expand_chapter_system": """汝は才溢るる物語の書き手なり。字数足らざる章を受け、之を拡げ給ふべし。
品を保ちつつ、目あての字数に至らしめ給へ。水増しの文は入れ給ふ勿れ。

拡ぐる術：
- 更なる細やかなる描写を加ふ（景、情、五感）
- 語らひを広げ、自然なる問答を増す
- 人物の胸の内の独白と反応を添ふ
- 立ち廻りの場を細やかに、生き生きと描く
- 雰囲気を醸す場の移り変はりを加ふ

肝要：成りたる拡げし章の本文のみを出だし給へ。余の情報や注は出だし給ふ勿れ。""",

    "expand_chapter_prompt": """此の章は字数足らず（{current_words}字）。約{target_words}字に拡げ給へ。

## 文体の手引
{style_guide}

## 章の綱
{chapter_outline}

## 今の章の本文（短し）
{chapter_text}

成りたる拡げし章の本文（{target_words}字以上）を出だし給へ。""",

    "compress_chapter_system": """汝は老練なる物語の編む者なり。字数溢るる章を受け、之を縮め給ふべし。
全ての要なる筋と人物の刻を保ちつつ章を縮め給へ。

縮むる術：
- 文を練り、冗なる描写を除く
- 重なる語らひを統ぶ
- 要ならざる場の移りを略す
- 筋を進めざる文を除く
- 立ち廻りの場を簡にす

肝要：全ての要なる筋の出来事、人物の成長、伏せたる線は必ず保ち給へ。
成りたる縮めし章の本文のみを出だし給へ。余の情報や注は出だし給ふ勿れ。""",

    "compress_chapter_prompt": """此の章は字数溢る（{current_words}字）。約{target_words}字に縮め給へ。

## 文体の手引
{style_guide}

## 章の綱（全ての要なる出来事を保つ）
{chapter_outline}

## 今の章の本文（長し）
{chapter_text}

成りたる縮めし章の本文（約{target_words}字）を出だし給へ。全ての要なる筋を保ち給へ。""",

    "split_chapter_system": """汝は老練なる物語の編む者なり。甚だ長き章を受け、二つの章に割り給ふべし。
自然なる物語の断ちどころを見出だし章を割り給へ。割りたる各章は：
- 己が劇の弧を持つ（序 → 展 → 鉤の結び）
- 大方同じ長さなるべし
- 自然なる懸かりどころ又は転じどころにて終はるべし

出だしの形：二つの章の間に精確に "===CHAPTER_SPLIT===" の仕切りを用ゐ給へ。
各章は章の題の行にて始め給へ。

肝要：===CHAPTER_SPLIT=== にて仕切りたる二つの章の本文のみを出だし給へ。余の注は要らず。""",

    "split_chapter_prompt": """此の章は甚だ長し（{current_words}字、章毎の目あて：{min_words}〜{max_words}字）。二つの章に割り給へ。

## 文体の手引
{style_guide}

## 元の章の綱
{chapter_outline}

## 今の章の本文（割るべし）
{chapter_text}

構へ全き二つの章に割り給へ。"===CHAPTER_SPLIT===" を仕切りとして用ゐ給へ。
第{chapter_num_a}章が前の半、第{chapter_num_b}章が後の半なり。
各章約{target_words}字。""",

    # -- 終はりの総め --
    "final_summary_system": """汝は文の分析者なり。成りたる物語の全き総めの報を成し給へ。

Markdown形式にて出だし、含むべきもの：
一、**書の覧** — 名、体裁、終の文字数、章の数
二、**情節の綜述** — 全き物語の梗概（種明かし含む）
三、**人物の弧の析** — 各主なる人物の成長
四、**旨趣の析** — 核なる旨趣とその展開
五、**数の統計** — 各章の文字数、平均、最長最短の章
六、**伏線の収めの報** — いかなる伏線を埋め、収めたるか
七、**文の品の評注** — 総じての文の品、光る場面
八、**続きの線** — 続け得る開かれたる筋""",

    "final_summary_prompt": """この成りたる物語の全き終はりの総めを成し給へ。

## 物語方略
{plan_json}

## 章の摘要
{all_briefs}

## 人物の檔
{characters}

## 伏線の追跡
{hooks_info}

## 数の統計
- 総章数：{total_chapters}
- 総文字数：凡そ{total_words}

Markdown形式にて全き総めの報を成し給へ。""",
})

# ============================================================
# TEMPLATES: Markdown雛形（古典日本語にて）
# ============================================================
TEMPLATES = dict(_BASE_TEMPLATES)
TEMPLATES.update({
    "readme": """# 📖 物語綴りの業

## 書の大要
- **書名**：『{title}』
- **体裁**：{genre}
- **目指す文字数**：{target_words}
- **一章ごとの文字数**：{min_words}—{max_words}
- **見込みの章数**：{total_chapters}
- **巻分け**：{volumes}
- **語りの目**：{pov}
- **核なる標**：{tags}

## 一言にて
{one_line_summary}

## 📁 文箱の構へ

```
{title}/
├── README.md              # 総綱
├── meta/                  # 元の情報
│   ├── progress.md        # 進みの跡
│   ├── style_guide.md     # 文の風
│   └── hooks_tracker.md   # 伏線の跡
├── worldbuilding/         # 世界の設ひ
│   ├── characters.md      # 人物の檔
│   ├── world_setting.md   # 世界の観
│   └── ...                # その他の設ひ
├── plot/                  # 情節
│   ├── master_outline.md  # 総綱目
│   ├── volume_XX.md       # 巻の綱
│   └── chapter_briefs.md  # 章の摘要
└── chapters/              # 本文
    ├── chapter_001.txt    # 第一章
    └── ...
```

## 🔄 綴りの順
一、progress.md を閲む → 進みを知る
二、chapter_briefs.md を閲む → 近き章を顧みる
三、当今の巻の綱を参ず → 本章を定む
四、hooks_tracker.md を確かむ → 伏線の有様を見る
五、characters.md を閲む → 人物の有様を確かむ
六、本文を chapters/ に出だす
七、progress.md、chapter_briefs.md 等を改む
""",

    "progress": """# 📊 進みの跡

## 当今の有様
- **最も新しき成りたる章**：未だ始まらず
- **今綴りゐるもの**：定まらず
- **当今の巻**：第一巻
- **総文字数**：0
- **最後の改め**：-

## 後の歩み
> 一、~~体裁を定む~~ ✅
> 二、~~核なる設定と主人公~~ ✅
> 三、~~総綱~~ ✅
> 四、**第一巻の細綱を成す** ← 今
> 五、本文の綴りを始む

## 成りたる章の一覧

| 章 | 題 | 凡その文字数 | 要なる事 |
|----|---|------------|---------|

## 当今の人物の有様
（改めを待つ）

## 爲すべきこと
- [x] 体裁を定む
- [x] 世界の設ひを成す
- [x] 人物の設定を成す
- [x] 総綱を成す
- [ ] 第一巻の細綱を成す
- [ ] 第一章の本文
""",

    "hooks_tracker": """# 🎣 伏線の追跡

> 埋めたる伏線と懸念を悉く記し、その有様を追ふ
> 有様：🔴 埋めたり未だ収めず | 🟡 一部明かす | 🟢 収めたり | ⚪ 企てゐる

---

## 長き伏線（巻を跨ぐ）

| ID | 内容 | 埋めたる章 | 収むる見込み | 有様 | 注 |
|----|------|----------|------------|-----|---|

## 短き伏線（この巻の内）

| ID | 内容 | 埋めたる章 | 収むる見込み | 有様 | 注 |
|----|------|----------|------------|-----|---|

## 収めたる記録

| ID | 内容 | 埋めたる章 | 収めたる章 | 注 |
|----|------|----------|----------|---|
""",

    "chapter_briefs": """# 📝 章の摘要の記

> 各章を綴り了へたるのち摘要を記す、情節を速やかに顧みるため
> 式：章の番 | 題 | 文字数 | 要なる事 | 人物の変 | 伏線

---
""",

    "synopsis_title": "# 物語の概\n\n",

    "chapter_brief_entry": """
### 第{chapter_num}章 · {title}（凡そ{word_count}文字）
**要なる事**：
""",
    "character_changes_header": "\n**人物の有様の変**：\n",
    "hooks_planted_header": "\n**新たなる伏線**：\n",
    "next_hook_prefix": "\n**次の章への鉤**：",

    "progress_update_entry": """
---
### 第{chapter_num}章了りたる改め
- **最も新しき成りたるもの**：{latest_chapter}
- **累計文字数**：凡そ{total_words}
""",
    "character_status_header": "\n**人物の有様速覧**：\n",

    "final_summary_filename": "meta/final_summary.md",
})

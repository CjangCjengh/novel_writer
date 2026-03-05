"""
繁體中文語言包
"""
from locales.en import UI as _BASE_UI

# ============================================================
# UI: 使用者介面文字（繼承英語基礎 + 繁中覆寫）
# ============================================================
UI = dict(_BASE_UI)
UI.update({
    "welcome_title": "📖 小說Agent工作流 v1.0",
    "welcome_subtitle": "   AI驅動的自動小說創作系統",
    "no_backend": "\n❌ 沒有可用的LLM後端！",
    "no_backend_hint": "   請確保 llm_openai.py 或 llm_local.py 至少有一個存在",
    "select_api_mode": "\n🔌 請選擇LLM API模式：",
    "api_openai_desc": "OpenAI 標準格式（需要配置API Key）",
    "api_local_desc": "本地 stream-server API",
    "auto_selected": "\n  （僅檢測到 {desc}，已自動選擇）",
    "input_choice": "\n👤 請輸入選擇 (1-{max}): ",
    "invalid_choice": "無效選擇，請輸入 1-{max}",
    "input_openai_key": "請輸入 OpenAI API Key: ",
    "api_key_empty": "API Key 不能為空！",
    "input_base_url": "API Base URL (按Enter使用預設: {default}): ",
    "input_model": "模型名稱 (按Enter使用預設: {default}): ",
    "input_local_url": "請輸入本地API地址: ",
    "api_url_empty": "API 地址不能為空！",
    "input_api_key": "請輸入 API Key (按Enter跳過): ",
    "input_wsid": "請輸入 WSID (按Enter跳過): ",
    "input_model_marker": "請輸入模型標記 (按Enter跳過): ",
    "project_setup": "\n📁 專案設置",
    "input_novel_name": "👤 請輸入小說專案名（用於建立資料夾）: ",
    "scan_projects_header": "\n📂 偵測到以下已有專案：",
    "no_existing_projects": "\n📂 未偵測到已有專案。",
    "project_status_chapters": "{count}章",
    "project_status_plan": "計畫",
    "project_status_meta": "元資料",
    "project_status_plot": "大綱",
    "or_input_manually": "手動輸入專案名...",
    "select_project_prompt": "\n👤 請選擇專案 (1-{max}): ",
    "select_operation": "\n🎯 請選擇操作：",
    "op_full": "  1. 從頭開始創作（完整流程）",
    "op_resume": "  2. 從斷點繼續寫作",
    "op_planning": "  3. 僅執行策劃階段",
    "op_worldbuilding": "  4. 僅生成世界觀和風格指南",
    "op_outline": "  5. 僅生成大綱",
    "op_writing": "  6. 僅執行寫作（需要已有大綱）",
    "op_batch": "  7. 批次模式（連續生成多部小說）",
    "input_op_choice": "\n👤 請輸入選擇 (1-7): ",
    "invalid_op": "無效選擇，請輸入 1-7",
    "input_volume_num": "要生成哪一卷的細綱？(輸入卷號，或按Enter跳過): ",
    "input_start_chapter": "從第幾章開始？(按Enter從第1章開始): ",
    "input_end_chapter": "寫到第幾章？(按Enter寫到末尾): ",
    "interrupted": "\n\n⏸️ 使用者中斷，已儲存當前進度。下次可以選擇'從斷點繼續'來恢復。",
    "error_occurred": "\n❌ 發生錯誤: {error}",
    "goodbye": "\n👋 再見！",

    # -- 批次模式 --
    "batch_input_names": "\n📚 請輸入多個小說名稱，用英文逗號分隔（如：小說A, 小說B, 小說C）：",
    "batch_empty": "❌ 未提供小說名稱，返回主選單。",
    "batch_select_op": "\n🎯 選擇每部小說要執行的操作：",
    "batch_start": "\n🚀 批次模式：將按順序生成 {total} 部小說：{names}",
    "batch_progress": "📖 [{current}/{total}] 開始生成小說：{name}",
    "batch_novel_done": "✅ 小說「{name}」已完成！",
    "batch_interrupted": "\n⏸️ 在寫作「{name}」時被中斷，還剩 {remaining} 部小說未完成。",
    "batch_continue_prompt": "是否繼續生成剩餘小說？(y/n): ",
    "batch_stopped": "🛑 批次生成已停止。",
    "batch_novel_error": "\n❌ 生成小說「{name}」時出錯：{error}",
    "batch_all_done": "\n🎉 批次完成！共 {total} 部小說全部生成完畢。",

    "select_language": "\n🌐 請選擇小說使用的語言：",
    "lang_choice_prompt": "\n👤 請輸入選擇 (1-{max}): ",
    # -- Continue from existing chapters (integrated in option 1) --
    "ask_existing_chapters": "\n\U0001f4dd Do you have any chapters already written? (y/n, Enter for no): ",
    "ask_chapter_count": "📚 您寫了幾章？請輸入數字: ",
    "ask_chapter_count_invalid": "❌ 請輸入一個有效的正整數。",
    "created_empty_chapters": "\n\U0001f4c2 Created {count} empty chapter file(s) in:\n   {path}\n",
    "created_empty_chapter_item": "   📄 {filename}",
    "checking_filled_chapters": """
🔍 正在檢查已填入的章節檔案...""",
    "filled_chapter_ok": "   ✅ 第{num}章：{words} 字",
    "filled_chapter_empty": "   ⚠️ 第{num}章：空白（將被跳過）",
    "all_chapters_empty": "❌ 所有章節檔案皆為空白。將以全新模式開始。",
    "skipping_chapter_writing": """
⏩ 第{num}章：已撰寫，跳過創作...""",
    "running_post_process_existing": "   🔄 Running post-processing (hook tracking, brief update) for chapter {num}...",
    "existing_chapters_processed": """
✅ 已處理全部 {count} 個已有章節。AI 將從第 {next} 章開始創作。""",
    "wait_fill_chapters": "\n✍️ Please fill in the chapter files with your written content.\n   When you are done, press Enter to continue...",

    "phase_planning_title": "\n📝 階段一：小說策劃",
    "planner_prefix": "\n🤖 策劃助手：\n",
    "user_prefix": "👤 你：",
    "input_empty_hint": "（請輸入你的回答）",
    "multiline_hint": "（支持多行輸入，輸入空行結束；輸入 /paste 進入貼上模式）",
    "multiline_paste_hint": "（已進入貼上模式，可自由貼上含空行的內容，輸入 /end 結束）",
    "quit_planning": "已退出策劃階段。",
    "force_done": "好的，讓我來整理策劃方案...",
    "generating_plan": "\n⏳ 正在生成完整的小說策劃方案...",
    "plan_display_title": "\n📋 小說策劃方案",
    "plan_label_title": "書名",
    "plan_label_genre": "類型",
    "plan_label_theme": "核心主題",
    "plan_label_target_words": "目標字數",
    "plan_label_total_chapters": "預計章數",
    "plan_label_volumes": "卷數",
    "plan_label_pov": "視角",
    "plan_label_tags": "標籤",
    "plan_label_one_line": "一句話梗概",
    "plan_label_beginning": "起",
    "plan_label_middle": "承",
    "plan_label_end": "合",
    "plan_label_characters": "主要角色",
    "confirm_plan": "\n👤 對這個策劃方案滿意嗎？(y/修改建議): ",
    "adjusting_plan": "\n⏳ 正在根據你的意見調整方案...",
    "plan_confirmed": "✅ 策劃方案已確認並儲存！",
    "rename_dir_prompt": "\n📁 小說標題為「{title}」，但專案資料夾為「{dir}」。",
    "rename_dir_confirm": "   是否將專案資料夾重新命名為「{title}」？(y/n): ",
    "rename_dir_done": "  ✅ 專案資料夾已重新命名為: {path}",
    "rename_dir_exists": "  ⚠️ 目錄已存在: {path}",
    "rename_dir_failed": "  ❌ 重新命名失敗: {error}",
    "phase_world_title": "\n🌍 階段二：世界觀構建 & 風格指南（並行生成中...）",
    "world_done": "✅ 世界觀設定已生成（{count}個文檔）",
    "world_failed": "❌ 世界觀生成失敗: {error}",
    "style_done": "✅ 風格指南已生成",
    "style_failed": "❌ 風格指南生成失敗: {error}",
    "phase_outline_title": "\n📋 階段三：總大綱生成",
    "generating_outline": "⏳ 正在生成總大綱...",
    "outline_done": "✅ 總大綱已生成",
    "outline_review": "\n📖 總大綱已儲存到 plot/master_outline.md，請查閱。",
    "press_enter_continue": "👤 按Enter繼續生成第一卷細綱...",
    "generating_volume": "📑 正在生成第{num}卷細綱...",
    "volume_done": "✅ 第{num}卷細綱已生成",
    "phase_writing_title": "\n✍️ 階段五：開始寫作",
    "checkpoint_resume": "[斷點續跑] 檢測到已完成{count}章，從第{next}章開始",
    "volume_not_found": "⚠️ 未找到第{num}卷細綱，正在生成...",
    "generating_volume_outline": "⏳ 正在生成第{num}卷細綱...",
    "writing_chapter": "📖 正在寫作第{num}章...",
    "chapter_done": "  ✅ 第{num}章寫作完成（約{words}字）",
    "post_processing": "  ⏳ 正在分析並更新元資訊...",
    "post_done": "  ✅ 第{num}章後處理完成",
    "post_failed": "  ⚠️ 第{num}章後處理分析失敗，跳過更新",
    "chapter_error": "  ❌ 第{num}章寫作出錯: {error}",
    "retry_prompt": "  是否重試？(y/n): ",
    "skip_chapter": "  跳過第{num}章，繼續下一章",
    "pause_prompt": "\n📊 已完成{num}章，按Enter繼續，或輸入'stop'暫停",
    "pause_input": "👤 ",
    "paused": "⏸️ 已暫停，下次可以從第{next}章繼續",
    "writing_complete": "🎉 寫作階段完成！",
    "planning_incomplete": "策劃階段未完成，退出。",
    "no_plan_found": "未找到策劃方案，從頭開始...",
    "resume_checking": "🔄 正在檢查專案狀態...",
    "resume_completed": "已完成{count}章，繼續寫作...",
    "no_style_guide": "未找到風格指南，正在生成...",
    "no_outline": "未找到總大綱，正在生成...",
    "plan_not_found_error": "未找到策劃方案檔案 plan.json，請先執行策劃階段",
    "worldbuilding_start": "[世界觀Agent] 開始並行生成 {count} 個設定文檔...",
    "doc_done": "  ✅ {filename} 生成完成",
    "doc_failed": "  ❌ {filename} 生成失敗",
    "doc_error": "  ❌ {filename} 生成出錯: {error}",
    "llm_error_retry": "抱歉，我出了點問題，請再說一次~",
    "info_enough": "資訊已經足夠啦！讓我來為你整理一份完整的小說策劃方案... 🎯",
    "continue_input": "請繼續告訴我更多關於你想創作的小說的資訊~",
    "config_loaded": "[配置] 已從 {file} 載入配置: {keys}",
    "novel_config_loaded": "[配置] 已從專案配置 {file} 載入: {keys}",
    "novel_config_skipped": "  ⚠️ 已跳過 {file} 中的 API/路徑配置（請使用全域配置）: {keys}",
    "novel_config_auto_created": "[配置] 已自動建立 {file}（可編輯此檔案自訂本小說的參數）",
"config_not_found": "[配置] 未找到 {file}，將使用預設值；API Key 需在執行時手動輸入",
    "config_hint": "[配置] 可參考 user_config.example.json 建立 {file}",
    "project_initialized": "[專案] 目錄已初始化: {path}",
    "openai_initialized": "[LLM-OpenAI] 已初始化，模型: {model}, Base URL: {url}",
    "openai_need_package": "使用 OpenAI 後端需要安裝 openai 套件: pip install openai",
"openai_no_key": "OPENAI_API_KEY 未配置，請在 user_config.json 中填寫或執行時輸入",
    "openai_attempt_failed": "[LLM-OpenAI] 第{n}次呼叫失敗: {error}",
    "openai_retry_wait": "[LLM-OpenAI] {wait}秒後重試...",
    "openai_max_retries": "[LLM-OpenAI] 已達最大重試次數({max})，放棄",
    "local_initialized": "[LLM-Local] 已初始化，URL: {url}, 模型標記: {marker}",
    "local_need_package": "使用本地後端需要安裝 requests 套件: pip install requests",
"local_no_url": "LOCAL_API_URL 未配置，請在 user_config.json 中填寫",
    "local_attempt_failed": "[LLM-Local] 第{n}次呼叫失敗: {error}",
    "local_retry_wait": "[LLM-Local] {wait}秒後重試...",
    "local_max_retries": "[LLM-Local] 已達最大重試次數({max})，放棄",
    "cannot_load_openai": "無法載入 OpenAI 後端: {error}\n請確保 llm_openai.py 存在且已安裝 openai 套件",
    "cannot_load_local": "無法載入本地後端: {error}\n請確保 llm_local.py 存在且已安裝 requests 套件",
    "unsupported_api_mode": "不支援的API模式: {mode}，可選值: 'openai', 'local'",
    "file_written": "[儲存] 已寫入: {path}",

    # -- Feature #1: 多方案大綱對比 --
    "outline_multi_draft_title": "\n📋 階段三：總大綱生成（多方案對比）",
    "generating_draft": "  ⏳ 正在生成大綱方案 {num}/{total}（風格：{style}）...",
    "draft_done": "  ✅ 方案{num}完成",
    "draft_failed": "  ❌ 方案{num}失敗: {error}",
    "draft_comparison_title": "\n📊 大綱方案對比",
    "draft_header": "\n{'─' * 40}\n📄 方案{num} — 風格：{style}\n{'─' * 40}",
    "draft_select_prompt": "\n👤 選擇使用哪個方案（1-{max}），或輸入'm'合併各方案精華: ",
    "draft_merging": "⏳ 正在合併各方案的精華...",
    "draft_selected": "✅ 已選擇方案{num}作為總大綱",
    "draft_merged": "✅ 合併大綱已生成",
    "outline_drafts_truncating": "   ⚠️ 大綱草稿過長（預估 {total} tokens，預算 {budget}），將等比例截斷各草稿...",
    "draft_invalid": "無效選擇，請輸入1-{max}或'm'",
    "parallel_review_title": "  🔍 正在運行並行品質審查...",
    "review_consistency": "[一致性審查員]",
    "review_style": "[文風審查員]",
    "review_foreshadowing": "[伏筆審查員]",
    "review_done": "  ✅ {reviewer}: 發現{count}個問題（置信度≥{threshold}）",
    "review_failed": "  ⚠️ {reviewer} 審查失敗: {error}",
    "review_no_issues": "  ✅ 所有審查員通過 — 沒有顯著問題！",
    "review_issues_found": "  ⚠️ 所有審查員共發現{count}個問題:",
    "review_issue_item": "    [{severity}] ({reviewer}, 置信度: {confidence}) {description}",
    "review_critical_prompt": "  🚨 發現嚴重問題。是否重寫本章？(y/n): ",
    "polish_start": "  ✨ 開始潤色循環（最多{max_iter}輪）...",
    "polish_iteration": "  ✨ 潤色第{iter}/{max_iter}輪...",
    "polish_score": "  📊 品質評分: {score}/10（閾值: {threshold}）",
    "polish_passed": "  ✅ 達到品質閾值！退出潤色循環。",
    "polish_improving": "  ⏳ 評分未達標，正在改進...",
    "polish_max_reached": "  ⚠️ 已達最大潤色輪次。使用最佳版本（評分: {score}/10）。",
    "polish_failed": "  ⚠️ 潤色評估失敗，保留當前版本。",
    "volume_checkpoint_title": "\n📍 第{num}卷檢查點",
    "volume_checkpoint_summary": "  當前進度: 已完成{completed}章，約{words}字",
    "volume_checkpoint_prompt": "\n👤 即將開始第{num}卷。繼續？(y / adjust / stop): ",
    "volume_checkpoint_adjust": "👤 請輸入調整意見: ",
    "volume_checkpoint_adjusting": "⏳ 正在根據你的回饋調整卷大綱...",
    "volume_checkpoint_stopped": "⏸️ 在第{num}卷前停止。下次從第{next}章繼續。",
    "severity_critical": "嚴重",
    "severity_major": "重要",
    "severity_minor": "輕微",
    "severity_info": "提示",
    "final_summary_title": "\n📊 正在生成全書總結報告...",
    "final_summary_done": "✅ 全書總結報告已生成並儲存！",
    "final_summary_failed": "⚠️ 全書總結報告生成失敗: {error}",

    # -- 寫作參數確認 --
    "writing_params_title": "\n⚙️ 寫作參數確認",
    "ask_chapter_min_words": "   每章最少字數（目前: {current}，直接按 Enter 保持不變）: ",
    "ask_chapter_max_words": "   每章最多字數（目前: {current}，直接按 Enter 保持不變）: ",
    "writing_params_swapped": "   ⚠️ 最小值大於最大值，已自動交換。",
    "ask_word_count_check": "   是否啟用字數檢查？（目前: {status}，y/n，直接按 Enter 保持不變）: ",
    "ask_lazy_mode": "   是否啟用懶人模式（自動確認一切）？（目前: {status}，y/n，直接按 Enter 保持不變）: ",
    "writing_params_summary": "   ✅ 寫作參數: {min}-{max} 字/章, 字數檢查: {check}, 懶人模式: {lazy}",

    # -- 引號偏好 --
    "quote_style_title": "\n💬 對話引號風格設定",
    "quote_style_prompt": "\n👤 請選擇小說中對話使用的引號風格 (1-{max}): ",
    "quote_style_invalid": "無效選擇，請輸入 1-{max}",
    "quote_style_selected": "✅ 對話引號風格已設定為: {style}",
    "quote_style_option_curly": '\u201c\u201d 彎引號（如：\u201c你好！\u201d）',
    "quote_style_option_corner": '\u300c\u300d 直角引號（如：\u300c你好！\u300d）',
    "quote_style_option_guillemet": '\u00ab\u00bb 書名號式引號（如：\u00ab你好！\u00bb）',
    "quote_style_option_dash": '\u2014 破折號式對話（如：\u2014\u2014你好！）',
    "quote_style_option_straight": '"" 直引號（如："你好！"）',

    # -- 心理活動引號風格 --
    "inner_quote_title": "\n💭 心理活動/內心獨白引號風格設定",
    "inner_quote_prompt": "\n👤 請選擇小說中心理活動使用的引號風格 (1-{max}): ",
    "inner_quote_invalid": "無效選擇，請輸入 1-{max}",
    "inner_quote_selected": "✅ 心理活動引號風格已設定為: {style}",
    "inner_quote_option_corner_double": '『』雙直角引號（如：『我必須小心』）',
    "inner_quote_option_corner": '「」直角引號（如：「我必須小心」）',
    "inner_quote_option_curly_single": '\u2018\u2019 單彎引號（如：\u2018我必須小心\u2019）',
    "inner_quote_option_italic": '*斜體* 標記心理活動（如：*我必須小心*）',
    "inner_quote_option_dash": '——雙破折號（如：——我必須小心——）',
    "inner_quote_option_paren": '（）全形括號（如：（我必須小心））',
    "inner_quote_option_same": '與對話引號相同',
    "inner_quote_option_none": '不使用特殊標記（用敘述方式描寫心理活動）',

    # -- 引號規則（注入風格指南/寫作提示詞中） --
    "quote_rules_heading": "引號風格規則",
    "quote_rule_dialogue_curly": '所有對話使用\u201c\u201d（彎雙引號）。示例：\u201c你好！\u201d',
    "quote_rule_dialogue_corner": '所有對話使用「」（直角引號）。示例：「你好！」',
    "quote_rule_dialogue_guillemet": '所有對話使用«»（書名號式引號）。示例：«你好！»',
    "quote_rule_dialogue_dash": '使用——（破折號）引出對話。示例：——你好！',
    "quote_rule_dialogue_straight": '所有對話使用""（直引號）。示例："你好！"',
    "quote_rule_inner_corner_double": '心理活動/內心獨白使用『』（雙直角引號）。示例：『我必須小心』',
    "quote_rule_inner_corner": '心理活動/內心獨白使用「」（直角引號）。示例：「我必須小心」',
    "quote_rule_inner_curly_single": '心理活動/內心獨白使用\u2018\u2019（單彎引號）。示例：\u2018我必須小心\u2019',
    "quote_rule_inner_italic": '心理活動/內心獨白使用*斜體*標記。示例：*我必須小心*',
    "quote_rule_inner_dash": '心理活動/內心獨白使用——（雙破折號）。示例：——我必須小心——',
    "quote_rule_inner_paren": '心理活動/內心獨白使用（）（全形括號）。示例：（我必須小心）',
    "quote_rule_inner_none": '心理活動不使用任何特殊引號標記，改用敘述方式描寫。',
    "quote_rule_inner_same": '心理活動/內心獨白使用與對話相同的引號風格。',

    # -- 懶人模式 --
    "lazy_mode_enabled": "🛋️ 懶人模式已開啟 — 確定大綱後將全自動運行，無需任何操作！",
    "lazy_auto_merge": "🛋️ [懶人] 自動合併所有大綱草稿...",
    "lazy_auto_select": "🛋️ [懶人] 僅一個草稿可用，已自動選擇。",
    "lazy_auto_continue": "🛋️ [懶人] 自動繼續...",
    "lazy_auto_retry": "🛋️ [懶人] 自動重試...",
    "lazy_auto_skip": "🛋️ [懶人] 自動跳過...",
    "lazy_auto_volume_continue": "🛋️ [懶人] 自動繼續第{num}卷...",

    # -- 審查重試 --
    "review_retry_feedback": """⚠️ 重要：這是第{attempt}/{max_attempts}次重寫。上一版本存在以下嚴重/重要問題，必須修正：
{issues}

請從頭重寫完整章節，確保修正以上所有問題，同時保持整體故事、基調和結構不變。""",
    "review_max_retries_reached": "  ⚠️ 第{num}章已達最大審查重試次數（{max}次），保存當前版本繼續。",


    # -- 字數校驗 --
    "wordcount_check_start": "  📏 字數校驗：{words}字（目標：{min}-{max}）",
    "wordcount_too_short": "  ⚠️ 章節過短（{words}字，最少{min}字），正在擴充...",
    "wordcount_too_long": "  ⚠️ 章節過長（{words}字，最多{max}字），正在壓縮...",
    "wordcount_split_needed": "  📑 章節嚴重超長（{words}字，≥{threshold}%上限），將拆分為兩章...",
    "wordcount_expand_done": "  ✅ 擴充完成：{words}字",
    "wordcount_compress_done": "  ✅ 壓縮完成：{words}字",
    "wordcount_split_done": "  ✅ 拆分完成：第{num_a}章（{words_a}字）+ 第{num_b}章（{words_b}字）",
    "wordcount_retry": "  🔄 字數校驗重試 {attempt}/{max_attempts}...",
    "wordcount_give_up": "  ⚠️ 經過{max_attempts}次重試仍未達標，使用當前版本（{words}字）。",
    "wordcount_ok": "  ✅ 字數合格：{words}字",
    "wordcount_split_renumber": "  📝 注意：拆分後的後續章節將自動重新編號。",

    # -- Feature #1: Multi-draft outline styles --
    "outline_style_dramatic": "戲劇張力型",
    "outline_style_literary": "文學深度型",
    "outline_style_commercial": "商業節奏型",

    # -- Continue from existing chapters --
    "ask_existing_chapters": "\n📝 您是否已經手動寫好了一些章節？(y/n): ",
    "ask_chapter_count": "📚 您寫了幾章？請輸入數字: ",
    "ask_chapter_count_invalid": "❌ 請輸入一個有效的正整數。",
    "created_empty_chapters": "\n📂 已在以下路徑創建 {count} 個空白章節檔案:\n   {path}\n",
    "created_empty_chapter_item": "   📄 {filename}",
    "wait_fill_chapters": "\n✏️ 請將您已寫好的章節內容貼到上述檔案中，完成後按Enter繼續...",
    "checking_filled_chapters": "\n🔍 正在檢查已填入的章節檔案...",
    "filled_chapter_ok": "   ✅ 第{num}章：{words} 字",
    "filled_chapter_empty": "   ⚠️ 第{num}章：空白（將被跳過）",
    "all_chapters_empty": "❌ 所有章節檔案皆為空白。將以全新模式開始。",
    "continue_scanning": "\n🔍 正在掃描已有章節...",
    "continue_found_chapters": "📖 找到 {count} 個已有章節。",
    "continue_reading_chapters": "📚 正在讀取已有章節以建立上下文...",
    "continue_chapter_read": "   ✅ 第{num}章：{words} 字",
    "continue_summary_generating": "🤖 正在生成已有章節的摘要...",
    "continue_summary_done": "✅ 章節摘要已生成。開始基於已有內容進行規劃。",
    "continue_planning_title": "\n📝 規劃階段（基於已有 {count} 章）",
    "continue_outline_context": "\n📋 大綱將整合已有的 {count} 個章節內容。",
    "continue_writing_from": "\n✍️ 將從第 {next_chapter} 章開始寫作。",
    "skipping_chapter_writing": "\n⏩ 第{num}章：已撰寫，跳過創作...",
    "existing_chapters_processed": "\n✅ 已處理全部 {count} 個已有章節。AI將從第 {next} 章開始創作。",
    "running_post_process_existing": "   🔄 正在對第{num}章執行後處理（hook追蹤、摘要更新）...",
})

# ============================================================
# PROMPTS: LLM提示詞模板（繁體中文完整翻譯）
# ============================================================
from locales.en import PROMPTS as _BASE_PROMPTS, TEMPLATES as _BASE_TEMPLATES

PROMPTS = dict(_BASE_PROMPTS)
PROMPTS.update({
    # -- 策劃Agent --
    "planner_system": """你是一位資深小說策劃編輯，擅長從零開始構思一部小說的核心設定。
你的任務是透過和使用者對話，蒐集足夠的資訊來確定以下小說核心要素：

1. **題材/類型**：玄幻、都市、懸疑、言情、科幻等
2. **核心主題**：小說要表達什麼
3. **目標字數和章節規劃**：總字數、每章字數、預計章數、卷數
4. **敘述視角**：第一人稱/第三人稱
5. **核心標籤**：3-5個關鍵標籤
6. **一句話梗概**：能概括全書的一句話
7. **三段式梗概**：起承合的劇情概要
8. **文風要求**：寫作風格、基調、參考作品
9. **禁忌事項**：不能出現的內容
10. **主要角色**：至少男主/女主的基本設定
11. **世界觀框架**：故事發生的世界背景

你需要主動提問使用者來獲取這些資訊。對於使用者不想自己決定的部分，由你來創造性地補充。
當你認為資訊已經足夠時，輸出最終的小說策劃方案。

注意：
- 每次只問2-3個相關聯的問題，不要一次性問太多
- 根據使用者的回答靈活調整後續問題
- 對於每個要素，要明確詢問使用者是想自己指定還是交由你來創造
- 保持友好、專業的對話風格""",

    "planner_first_question": """你好！我是你的小說策劃助手~ 🎉

在開始創作之前，我需要了解你的想法。讓我們一步步來：

**首先，最基本的問題：**
1. 你想寫什麼**題材/類型**的小說？（比如：玄幻、都市、懸疑、科幻、言情、歷史等）
2. 你心目中有沒有大致的**故事方向**或**核心創意**？哪怕只是一個模糊的念頭也行
3. 這些基礎設定你想自己指定，還是更希望由我來幫你頭腦風暴？

請隨意聊聊你的想法~""",

    "planner_check_enough": """請分析目前蒐集到的所有資訊，判斷是否已經足夠開始創作規劃。

需要檢查的核心要素清單:
1. 題材/類型 - {has_genre}
2. 核心主題 - {has_theme}
3. 目標字數和章節規劃 - {has_structure}
4. 敘述視角 - {has_pov}
5. 核心標籤 - {has_tags}
6. 一句話梗概 - {has_summary}
7. 文風要求 - {has_style}
8. 主要角色（至少有主角概念）- {has_characters}
9. 世界觀框架 - {has_world}

**重要**：當使用者讓你來決定某些項時（如「體裁你來定」、「風格隨你」、「至於女主，你自己決定」，或直接說「你來決定」），應將這些項視為**已滿足**，不要列入「missing_items」。只有使用者既未指定、也未委託給你的項才算真正缺失。若所有項都已被使用者指定或委託，則將「is_enough」設為true。

請用JSON格式回覆:
{{
    "is_enough": true/false,
    "missing_items": ["缺少的要素列表"],
    "next_questions": "如果資訊不夠，你接下來要問使用者的問題（2-3個）"
}}

只返回JSON，不要其他內容。""",

    "planner_summarize": """根據以下使用者對話中蒐集到的資訊，生成完整的小說策劃方案。
對於使用者沒有明確指定的部分，請你創造性地補充，使整體方案連貫且有吸引力。

請嚴格按照以下JSON格式輸出，不要輸出其他內容：
{{
    "title": "書名",
    "genre": "類型/題材",
    "theme": "核心主題（一段話）",
    "target_words": "目標總字數",
    "chapter_words": "每章字數範圍",
    "total_chapters": "預計總章數",
    "volumes": "卷數和劃分",
    "pov": "敘述視角",
    "tags": "核心標籤（逗號分隔）",
    "one_line_summary": "一句話梗概",
    "three_act_summary": {{
        "beginning": "起（開端概要）",
        "middle": "承（發展概要）",
        "end": "合（結局概要）"
    }},
    "style_guide": "文風要求和寫作規範",
    "taboos": "禁忌事項",
    "main_characters": [
        {{
            "name": "名字",
            "role": "角色定位（男主/女主/配角等）",
            "age": "年齡",
            "appearance": "外貌描述",
            "personality": "性格描述",
            "background": "背景故事",
            "motivation": "核心動機",
            "arc": "人物弧光/成長軌跡"
        }}
    ],
    "world_setting": "世界觀框架描述",
    "synopsis": "小說簡介（用於發佈）"
}}""",

    # -- 大綱Agent --
    "outline_system": """你是一位經驗豐富的小說大綱規劃師。你將基於給定的小說策劃方案，建立詳細的劇情大綱。

你需要輸出：
1. 全書的卷級大綱（每卷的主線、核心衝突、關鍵事件、卷末高潮和懸念）
2. 角色關係圖譜的文字描述

輸出格式為Markdown。請確保：
- 每卷大綱包含清晰的主線和關鍵事件列表
- 卷與卷之間有明確的因果銜接
- 角色的成長弧線貫穿始終
- 伏筆和懸念的設計合理
- 節奏有張有弛""",

    "volume_outline_system": """你是一位擅長細化劇情的小說大綱師。
你將基於總大綱中某一卷的概述，建立該卷的詳細章節級大綱。

輸出格式為Markdown，每章需要包含：
- 章節標題
- 主要事件（3-5個關鍵點）
- 出場角色
- 情感基調/氛圍
- 伏筆（埋/填）
- 承上啟下的銜接點""",

    # -- 世界觀Agent --
    "worldbuilding_system": """你是一位專業的世界觀構建師。基於給定的小說策劃方案，你需要建立詳細的世界設定文件。

輸出格式為Markdown，需要涵蓋：
1. 世界觀總設定（時代背景、社會結構、科技/魔法水準等）
2. 地理/空間設定（重要地點及其特徵）
3. 特殊體系設定（修仙體系/魔法體系/科技體系等，根據題材而定）
4. 時間線大事記（故事開始前的重要歷史事件）

確保設定之間互相一致，不矛盾。""",

    "character_system": """你是一位擅長人物塑造的角色設計師。基於給定的小說策劃方案和世界設定，你需要建立詳細的人物檔案。

每個角色需要包含：
- 基本資訊（名字、年齡、外貌等）
- 性格描寫（多層次，包含外在表現和內在性格）
- 背景故事
- 能力/特長
- 目標/動機
- 說話風格/口癖
- 人物弧光（成長軌跡）
- 角色關係

輸出格式為Markdown。確保角色之間有化學反應，性格互補或衝突。""",

    # -- 寫作Agent --
    "writer_system": """你是一位才華橫溢的網路小說作家。
你將根據提供的設定、大綱和上下文，撰寫小說正文。

寫作要求：
{style_guide}

結構要求：
- 每章 {min_words}-{max_words} 字
- 章節需要有鉤子開頭（承接上章或製造新懸念）
- 核心劇情推進（至少一個關鍵事件）
- 結尾留鉤（吸引讀者繼續閱讀）

嚴格遵守以下格式：
- 章節標題格式：第X章 標題
- 直接輸出正文內容，不要輸出任何元資訊或備註""",

    "writer_chapter_prompt": """請根據以下資訊撰寫第{chapter_num}章的正文。

## 本章大綱
{chapter_outline}

## 最近章節摘要（用於保持連貫性）
{recent_briefs}

## 當前人物狀態
{character_status}

## 需要注意的伏筆
{hooks_info}

## 角色檔案（權威設定——姓名必須嚴格一致）
{character_profiles}

## 世界觀與地點設定（權威設定——所有地名、勢力名等必須嚴格一致）
{world_setting}

⚠️ 嚴重警告：所有角色姓名、地點名稱、門派/勢力名稱及專有名詞，必須與上方的角色檔案和世界觀設定完全一致。嚴禁自行創造、修改或替換任何名稱。

請直接輸出完整的章節正文（{min_words}-{max_words}字），以「第{chapter_num}章」開頭。""",

    # -- 後處理Agent --
    "post_write_system": """你是一位細心的小說編輯助理。你的任務是在每章寫完後，分析章節內容並生成以下更新資訊。

請以JSON格式輸出:
{{
    "chapter_brief": {{
        "chapter_num": 章節號,
        "title": "章節標題",
        "word_count": 約字數,
        "main_events": ["主要事件1", "主要事件2", ...],
        "character_changes": ["角色狀態變更1", ...],
        "hooks_planted": ["新埋的伏筆1", ...],
        "hooks_resolved": ["填上的伏筆ID1", ...],
        "next_chapter_hook": "留給下一章的鉤子"
    }},
    "progress_update": {{
        "latest_chapter": "第X章·標題",
        "total_words": 約累計總字數,
        "character_status": {{
            "角色名": "當前狀態描述"
        }}
    }}
}}

只返回JSON，不要其他內容。""",

    # -- 風格指南Agent --
    "style_guide_system": """你是一位文學顧問，專門負責制定小說的文風規範。
根據給定的小說策劃方案，生成詳細的文風指南文件。

輸出格式為Markdown，需要包含：
1. 敘述視角規範
2. 文風要求（整體基調、內心獨白風格、對外表現風格等）
3. 章節結構規範
4. 對話規範（對話格式、角色說話風格）
5. 描寫規範（戰鬥/情感/環境等各類描寫的要求）
6. 節奏控制建議
7. 核心寫作原則
8. 禁忌事項""",

    # -- 世界觀任務提示詞 --
    "task_world_setting": """基於以下小說策劃方案，建立世界觀總設定文件（Markdown格式）。
包含：時代背景、社會結構、重要勢力/組織等基礎世界觀。

策劃方案：
{plan_text}""",

    "task_characters": """基於以下小說策劃方案，建立詳細的人物檔案文件（Markdown格式）。
參考格式要求：每個角色包含姓名、年齡、外貌、性格（多層次）、背景、能力、動機、口癖、人物弧光。
最後附上角色關係圖譜（文字描述）。

策劃方案：
{plan_text}""",

    "task_locations": """基於以下小說策劃方案，建立重要地點/場景設定文件（Markdown格式）。
包含所有故事中會出現的重要地點及其特徵描述。

策劃方案：
{plan_text}""",

    "task_timeline": """基於以下小說策劃方案，建立時間線大事記文件（Markdown格式）。
包含故事開始前的重要歷史事件和故事進行中的時間線規劃。

策劃方案：
{plan_text}""",

    "task_power_system": """基於以下小說策劃方案，建立力量/修煉體系設定文件（Markdown格式）。
包含：等級劃分、修煉方式、特殊能力體系等詳細設定。

策劃方案：
{plan_text}""",

    "task_tech_system": """基於以下小說策劃方案，建立科技體系設定文件（Markdown格式）。
包含：科技水準、關鍵技術、特殊裝置等詳細設定。

策劃方案：
{plan_text}""",

    # -- 大綱生成提示詞 --
    "master_outline_prompt": """請基於以下小說策劃方案，建立全書的總大綱。

## 小說策劃方案
{plan_json}

請生成包含所有卷的總大綱（Markdown格式），每卷需要包含：
- 主線描述
- 核心衝突
- 關鍵事件（編號列表）
- 主要角色狀態
- 卷末高潮
- 卷末懸念
- 與下一卷的銜接""",

    "volume_outline_prompt": """請基於以下資訊，建立第{volume_num}卷的詳細章節級大綱。

## 小說策劃方案摘要
- 書名：{title}
- 類型：{genre}
- 每章字數：{chapter_words}

## 卷定位提示
{volume_info}

## 總大綱（完整 — 請從中找到第{volume_num}卷的內容作為基礎）
{master_outline}

請為這一卷生成詳細的章節級大綱，每章包含：
- 章節編號和標題
- 主要事件（3-5個）
- 出場角色
- 情感基調
- 伏筆（埋/填）
- 銜接點""",

    # -- 後處理提示詞 --
    "analyze_chapter_prompt": """請分析以下小說章節，生成摘要和更新資訊。

## 章節大綱（參考）
{chapter_outline}

## 章節正文
{chapter_text}

請嚴格按照指定的JSON格式輸出。""",

    # -- 修改方案 --
    "plan_revision_request": "我對策劃方案有以下修改意見：{feedback}\n請據此調整方案。",

    # -- 題材偵測關鍵詞 --
    "genre_fantasy_keywords": ["玄幻", "修仙", "仙俠", "魔法", "奇幻"],
    "genre_scifi_keywords": ["科幻", "未來", "賽博", "太空", "科技"],


    "outline_merge_prompt": """以下是同一部小說的{count}個不同風格的總大綱方案。

請建立一份**合併總大綱**，要求：
1. 從各方案中取最強的結構性元素
2. 融合最佳的情節創意和角色弧線
3. 保持全篇邏輯一致性
4. 保留最精彩的伏筆設計和高潮安排

{drafts_text}

以Markdown格式輸出合併後的總大綱。""",

    # -- Feature #2: 並行審查系統提示詞 --
    "consistency_reviewer_system": """你是一位細緻入微的小說連續性編輯。
你的任務是審查章節內容與前文、大綱以及提供的角色檔案的一致性。

檢查以下內容：
1. **角色姓名準確性**：將章節中出現的每一個角色名字與角色檔案逐一比對。標記任何與檔案不完全一致的名字（拼寫錯誤、名字錯誤、名字互換、稱呼不一致）。這是最高優先級的檢查項。
2. **角色特徵一致性**：驗證每個角色的行為、說話風格、能力和性格是否與其檔案匹配。
3. 時間線和時序準確性
4. 場景/地點一致性
5. 情節連續性（引用的事件必須確實發生過）
6. 角色認知一致性（角色不應知道他們尚未了解的事情）

對發現的每個問題，給出置信度評分（0-100）：
- 0-25: 不確定，可能是有意為之
- 26-50: 可能有問題，但也可能是主觀判斷
- 51-75: 很可能是錯誤，需要驗證
- 76-100: 確定是錯誤，已與原文對照驗證

以JSON格式輸出：
{{
    "issues": [
        {{
            "type": "consistency",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "問題描述",
            "location": "章節中的大致位置",
            "suggestion": "修復建議"
        }}
    ],
    "overall_consistency_score": 1-10
}}

只返回JSON，不要其他內容。""",

    "style_reviewer_system": """你是一位文學風格審查專家。
你的任務是審查章節內容是否符合寫作風格指南。

檢查以下內容：
1. 敘述視角一致性（無意外的視角切換）
2. 語氣和氛圍與風格指南的契合度
3. 對話風格與角色檔案的一致性
4. 節奏問題（太倉促或太拖沓）
5. 文筆品質（彆扭的措辭、重複用詞等）

對發現的每個問題，給出置信度評分（0-100）。

以JSON格式輸出：
{{
    "issues": [
        {{
            "type": "style",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "問題描述",
            "location": "章節中的大致位置",
            "suggestion": "修復建議"
        }}
    ],
    "overall_style_score": 1-10
}}

只返回JSON，不要其他內容。""",

    "foreshadowing_reviewer_system": """你是一位伏筆和情節連貫性專家。
你的任務是審查章節中伏筆元素的處理情況。

檢查以下內容：
1. 埋設的伏筆是否足夠隱蔽（不會太明顯）？
2. 之前埋下的鉤子是否在適當時機推進或解決？
3. 根據大綱，是否有被遺漏的伏筆機會？
4. 已解決的伏筆是否令人滿意？
5. 章節結尾是否為下一章創造了足夠的懸念？

對發現的每個問題，給出置信度評分（0-100）。

以JSON格式輸出：
{{
    "issues": [
        {{
            "type": "foreshadowing",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "問題描述",
            "location": "章節中的大致位置",
            "suggestion": "修復建議"
        }}
    ],
    "overall_foreshadowing_score": 1-10
}}

只返回JSON，不要其他內容。""",

    "review_chapter_prompt": """請審查以下章節。

## 角色檔案（權威參考，用於核對姓名和特徵）
{character_profiles}

## 風格指南
{style_guide}

## 章節大綱
{chapter_outline}

## 最近章節摘要
{recent_briefs}

## 伏筆追蹤
{hooks_info}

## 章節正文
{chapter_text}

重要：請將章節正文中的所有角色名字與上方的角色檔案逐一比對。任何名字不匹配都是嚴重問題。

請按照指定的JSON格式輸出審查結果。""",

    # -- Feature #3: 潤色循環提示詞 --
    "polish_evaluate_system": """你是一位資深小說編輯。請對以下章節的品質進行1-10分的評估。

評估維度：
1. 文筆品質和可讀性
2. 角色聲音一致性
3. 節奏和流暢度
4. 情感衝擊力
5. 鉤子強度（開頭和結尾）
6. 與大綱的契合度

以JSON格式輸出：
{{
    "score": 1-10,
    "strengths": ["優點1", "優點2"],
    "weaknesses": ["不足1", "不足2"],
    "specific_improvements": [
        {{
            "location": "文中位置",
            "current": "當前問題文字（簡述）",
            "suggested": "改進建議"
        }}
    ]
}}

只返回JSON，不要其他內容。""",

    "polish_evaluate_prompt": """請評估這一章的品質。

## 風格指南
{style_guide}

## 章節大綱
{chapter_outline}

## 章節正文
{chapter_text}

請以JSON格式輸出評估結果。""",

    "polish_improve_system": """你是一位才華橫溢的小說作家，正在進行修訂。
你將收到一章內容以及編輯給出的具體改進建議。
請重寫**完整章節**，將改進建議融入其中，同時保持整體故事、基調和結構不變。

不要新增任何元評論——只輸出修訂後的章節正文。""",

    "polish_improve_prompt": """請根據編輯的回饋修訂以下章節。

## 編輯回饋
不足之處：{weaknesses}

具體改進建議：
{improvements}

## 當前章節正文
{chapter_text}

請輸出完整的修訂後章節正文。""",

    # -- Feature #4: 卷間檢查點調整 --
    "volume_adjust_prompt": """讀者對第{volume_num}卷提出了以下回饋/調整意見。

回饋：{feedback}

當前卷大綱：
{volume_outline}

請修改卷大綱以融入讀者的回饋，同時保持與總大綱的一致性。

以Markdown格式輸出修改後的卷大綱。""",

    # -- 字數校驗提示詞 --
    "expand_chapter_system": """你是一位才華橫溢的小說作家。你將收到一個字數不足的章節，需要對其進行擴充。
在保持品質的前提下擴充章節以達到目標字數。不要用注水內容來湊字數。

擴充策略：
- 增加更多細節描寫（環境、情緒、感官細節）
- 擴展對話交流，增加自然的對話往來
- 添加角色內心獨白和反應
- 細化動作場景，增加更生動的描述
- 添加烘托氛圍的過渡場景

重要：只輸出完整的擴充後章節正文，不要輸出任何元資訊或備註。""",

    "expand_chapter_prompt": """以下章節字數不足（{current_words}字），請將其擴充至約{target_words}字。

## 風格指南
{style_guide}

## 章節大綱
{chapter_outline}

## 當前章節正文（過短）
{chapter_text}

請輸出完整的擴充後章節正文（{target_words}字以上）。""",

    "compress_chapter_system": """你是一位經驗豐富的小說編輯。你將收到一個字數過多的章節，需要對其進行壓縮。
在保留所有關鍵情節點和角色時刻的前提下壓縮章節。

壓縮策略：
- 精簡文筆，去除冗餘描寫
- 合併重複對話
- 概括不太重要的過渡場景
- 去除不推動情節的注水內容
- 精簡動作場景

重要：所有關鍵情節事件、角色發展和伏筆必須保留。
只輸出完整的壓縮後章節正文，不要輸出任何元資訊或備註。""",

    "compress_chapter_prompt": """以下章節字數過多（{current_words}字），請將其壓縮至約{target_words}字。

## 風格指南
{style_guide}

## 章節大綱（保留所有關鍵事件）
{chapter_outline}

## 當前章節正文（過長）
{chapter_text}

請輸出完整的壓縮後章節正文（約{target_words}字），保留所有關鍵情節點。""",

    "split_chapter_system": """你是一位經驗豐富的小說編輯。你將收到一個嚴重超長的章節，需要將其拆分為兩章。
找到一個自然的敘事斷點來拆分章節。拆分後的每一章需要：
- 有自己的戲劇弧線（鋪墊 → 發展 → 鉤子結尾）
- 長度大致相等
- 在自然的懸念點或過渡點結束

輸出格式：使用精確的分隔行 "===CHAPTER_SPLIT===" 分隔兩章。
每章以章節標題行開頭。

重要：只輸出由 ===CHAPTER_SPLIT=== 分隔的兩章正文，不要輸出任何元資訊或備註。""",

    "split_chapter_prompt": """以下章節嚴重超長（{current_words}字，每章目標：{min_words}-{max_words}字），請將其拆分為兩章。

## 風格指南
{style_guide}

## 原章節大綱
{chapter_outline}

## 當前章節正文（待拆分）
{chapter_text}

將此章拆分為兩個結構完整的章節，使用 "===CHAPTER_SPLIT===" 作為分隔。
第{chapter_num_a}章為前半部分，第{chapter_num_b}章為後半部分。
每章約{target_words}字。""",

    # -- Feature #6: 完結總結提示詞 --
    "final_summary_system": """你是一位文學分析師。為一部已完成的小說生成全面的總結報告。

以Markdown格式輸出，包含：
1. **小說概覽** — 書名、類型、最終字數、章數
2. **情節綜述** — 完整故事梗概（含劇透）
3. **角色弧線分析** — 每位主要角色的成長變化
4. **主題分析** — 核心主題及其展開方式
5. **數據統計** — 每章字數、平均字數、最長/最短章節
6. **伏筆解決報告** — 哪些伏筆被埋設和解決
7. **寫作品質評注** — 整體文筆品質、亮點場景
8. **續集潛力線索** — 可以延續的開放線索""",

    "final_summary_prompt": """為這部已完成的小說生成全面的完結總結。

## 小說策劃方案
{plan_json}

## 章節摘要
{all_briefs}

## 角色檔案
{characters}

## 伏筆追蹤
{hooks_info}

## 統計數據
- 總章數：{total_chapters}
- 總字數：約{total_words}字

請以Markdown格式生成完整的總結報告。""",

    # -- Language enforcement instruction --
    "language_instruction": (
        "**重要——語言要求**："
        "你必須使用{native_name}（{english_name}）撰寫所有輸出內容。"
        "每一句話、每一段、每個標題和標籤都必須使用{native_name}。"
        "除非是引用專有名詞或術語，否則不要混入其他語言。"
    ),

    # -- Continue from existing chapters --
    "planner_continue_system": """你是一位資深小說策劃編輯。用戶已經寫好了小說的部分章節。
你的任務是理解已有內容，幫助用戶規劃後續的故事發展。

你已獲得已有章節的摘要。基於這些已有內容，你需要：
1. 理解已確立的角色、世界觀、基調和情節走向
2. 與用戶討論故事接下來的發展方向
3. 幫助填寫一份與已有內容保持一致的完整小說計劃
4. 尊重已有內容——不得與已確立的設定產生矛盾

需要確定的核心要素（部分可能已從已有章節中明確）：
1. **類型/題材**：可能已從已有內容中顯而易見
2. **核心主題**：小說想要表達的主旨
3. **目標字數與結構**：總字數、每章字數、預計總章數、卷數
4. **敘事視角**：應與已有章節保持一致
5. **核心標籤**：3-5個關鍵標籤
6. **一句話概括**：一句話總結全書
7. **三幕概要**：開篇（已部分完成）、發展、結局概述
8. **寫作風格**：應與已有章節保持一致
9. **禁忌事項**：不得出現的內容
10. **主要角色**：從已有章節中提取 + 規劃新角色
11. **世界框架**：從已有章節中提取 + 擴展

注意事項：
- 每次只問2-3個相關問題
- 指出你從已有章節中了解到的內容
- 將問題聚焦在已有內容中尚未明確的方面
- 保持友好、專業的對話風格""",
    "planner_continue_first_question": """你好！我已經閱讀了你已有的 {chapter_count} 章內容的摘要。🎉

以下是我目前了解到的資訊：
{existing_summary}

現在，讓我們來規劃後續內容！我有幾個問題：

1. 你計劃這部小說總共寫多少章？
2. 對於接下來的情節，你有什麼具體的想法或方向嗎？
3. 你希望保持目前的敘事節奏，還是想做一些改變？""",
    "planner_continue_summarize": """基於已有章節的摘要和我們對話中收集到的資訊，生成一份完整的小說計劃。
計劃必須與已有章節保持一致。對於three_act_summary.beginning，描述已有章節中實際發生的事情。

已有章節摘要：
{chapter_summaries}

請嚴格按照以下JSON格式輸出，不要有其他內容：
{{
    "title": "書名",
    "genre": "類型/題材",
    "theme": "核心主題（一段話）",
    "target_words": "目標總字數",
    "chapter_words": "每章字數範圍",
    "total_chapters": "預計總章數（包括已寫的）",
    "volumes": "卷數和分卷",
    "pov": "敘事視角（必須與已有章節一致）",
    "tags": "核心標籤（逗號分隔）",
    "one_line_summary": "一句話概括",
    "three_act_summary": {{
        "beginning": "開篇（總結已有章節中已發生的事情）",
        "middle": "發展（中間部分概述）",
        "end": "結局（結局概述）"
    }},
    "style_guide": "寫作風格要求和規範（匹配已有章節）",
    "taboos": "禁忌事項",
    "main_characters": [
        {{
            "name": "名字",
            "role": "角色定位（主角/反派/配角等）",
            "age": "年齡（必須從已有章節推斷——如果是高中生則應為~15-18歲，不得隨意編造）",
            "appearance": "外貌描述",
            "personality": "性格描述",
            "background": "背景故事",
            "motivation": "核心動機",
            "arc": "角色弧線/成長軌跡"
        }}
    ],
    "world_setting": "世界框架描述",
    "synopsis": "小說簡介（用於出版）"
}}""",
    "chapter_summary_prompt": """請閱讀以下章節文本並生成一份簡潔的摘要。

## 第 {chapter_num} 章
{chapter_text}

請輸出 JSON 摘要：
{{
    "chapter_num": {chapter_num},
    "title": "簡短標題",
    "summary": "2-3 句情節摘要",
    "characters": ["出場角色名"],
    "setting": "場景/地點（如：高中校園、中世紀城堡、太空站）",
    "time_period": "時代/年齡背景（如：現代高中生約16歲、古代王朝、未來2200年代）。如能辨別請註明角色年齡範圍。",
    "key_events": ["關鍵事件1", "關鍵事件2"],
    "unresolved_hooks": ["未解決的伏筆/懸念"],
    "pov": "視角角色或敘述方式",
    "tone": "本章的整體基調/氛圍"
}}

只輸出 JSON，不要其他內容。""",
    "master_outline_continue_prompt": """請基於以下小說計劃為整本書創建總綱。
重要：前{existing_count}章已經寫好。大綱必須與已有章節內容保持一致，不得產生矛盾。

## 小說計劃
{plan_json}

## 已有章節摘要
{chapter_summaries}

請生成覆蓋所有卷的總綱（Markdown格式）。每卷需要包含：
- 主線劇情描述
- 核心衝突
- 關鍵事件（編號列表）
- 主要角色狀態
- 本卷高潮
- 本卷懸念
- 與下一卷的銜接

確保前面章節的大綱準確反映已有內容。""",
})

# ============================================================
# TEMPLATES: Markdown模板（繁體中文完整翻譯）
# ============================================================
TEMPLATES = dict(_BASE_TEMPLATES)
TEMPLATES.update({
    "readme": """# 📖 長篇小說創作專案

## 小說基本資訊
- **書名**：《{title}》
- **類型**：{genre}
- **目標字數**：{target_words}
- **每章字數**：{min_words}-{max_words}字
- **預計總章數**：{total_chapters}
- **卷數劃分**：{volumes}
- **敘述視角**：{pov}
- **核心標籤**：{tags}

## 一句話梗概
{one_line_summary}

## 📁 目錄結構說明

```
{title}/
├── README.md              # 專案總綱
├── meta/                  # 元資訊管理
│   ├── progress.md        # 寫作進度追蹤
│   ├── style_guide.md     # 文風和寫作規範
│   └── hooks_tracker.md   # 伏筆/鉤子追蹤表
├── worldbuilding/         # 世界觀設定
│   ├── characters.md      # 人物檔案
│   ├── world_setting.md   # 世界觀總設定
│   └── ...                # 其他設定檔案
├── plot/                  # 劇情管理
│   ├── master_outline.md  # 總大綱
│   ├── volume_XX.md       # 每卷細綱
│   └── chapter_briefs.md  # 章節摘要記錄
└── chapters/              # 正文輸出
    ├── chapter_001.txt    # 第一章正文
    └── ...
```

## 🔄 寫作流程
1. 讀取 progress.md → 了解當前進度
2. 讀取 chapter_briefs.md → 回顧最近章節
3. 參考當前卷細綱 → 確認本章內容
4. 檢查 hooks_tracker.md → 看伏筆狀態
5. 查閱 characters.md → 確認人物狀態
6. 輸出正文到 chapters/
7. 更新 progress.md、chapter_briefs.md 等
""",

    "progress": """# 📊 寫作進度追蹤

## 當前狀態
- **最新完成章節**：尚未開始
- **當前正在寫**：待定
- **當前卷**：第一卷
- **總字數**：0
- **上次更新時間**：-

## 下一步計畫
> 1. ~~確定小說題材/類型~~ ✅
> 2. ~~核心設定和主角~~ ✅
> 3. ~~總大綱~~ ✅
> 4. **完成第一卷細綱** ← 當前
> 5. 開始正文創作

## 已完成章節一覽

| 章節 | 標題 | 約字數 | 核心事件 |
|------|------|--------|---------|

## 當前角色狀態速查
（待更新）

## 待處理事項
- [x] 確定小說題材
- [x] 完成世界觀設定
- [x] 完成人物設定
- [x] 完成總大綱
- [ ] 完成第一卷細綱
- [ ] 第1章正文
""",

    "hooks_tracker": """# 🎣 伏筆/鉤子追蹤表

> 記錄所有埋下的伏筆和懸念，追蹤其狀態
> 狀態：🔴 已埋未填 | 🟡 部分揭示 | 🟢 已填坑 | ⚪ 計畫中

---

## 長線伏筆（跨卷）

| ID | 伏筆內容 | 埋設章節 | 計畫填坑 | 狀態 | 備註 |
|----|---------|---------|---------|------|------|

## 短線伏筆（本卷內）

| ID | 伏筆內容 | 埋設章節 | 計畫填坑 | 狀態 | 備註 |
|----|---------|---------|---------|------|------|

## 已填坑記錄

| ID | 伏筆內容 | 埋設章節 | 填坑章節 | 備註 |
|----|---------|---------|---------|------|
""",

    "chapter_briefs": """# 📝 章節摘要記錄

> 每章寫完後記錄摘要，用於快速回顧劇情
> 格式：章節號 | 標題 | 字數 | 主要事件 | 角色狀態變化 | 伏筆/懸念

---
""",

    "synopsis_title": "# 小說簡介\n\n",

    "chapter_brief_entry": """
### 第{chapter_num}章 · {title}（約{word_count}字）
**主要事件**：
""",
    "character_changes_header": "\n**角色狀態變更**：\n",
    "hooks_planted_header": "\n**新埋伏筆**：\n",
    "next_hook_prefix": "\n**下章鉤子**：",

    "progress_update_entry": """
---
### 第{chapter_num}章完成更新
- **最新完成**：{latest_chapter}
- **累計字數**：約{total_words}字
""",
    "character_status_header": "\n**角色狀態速查**：\n",

    "final_summary_filename": "meta/final_summary.md",
})

"""
简体中文语言包
"""
from locales.en import UI as _BASE_UI, PROMPTS as _BASE_PROMPTS, TEMPLATES as _BASE_TEMPLATES

# ============================================================
# UI: 用户界面文本（继承英语基础 + 中文覆写）
# ============================================================
UI = dict(_BASE_UI)
UI.update({
    # -- main.py --
    "welcome_title": "📖 小说Agent工作流 v1.0",
    "welcome_subtitle": "   AI驱动的自动小说创作系统",
    "no_backend": "\n❌ 没有可用的LLM后端！",
    "no_backend_hint": "   请确保 llm_openai.py 或 llm_local.py 至少有一个存在",
    "select_api_mode": "\n🔌 请选择LLM API模式：",
    "api_openai_desc": "OpenAI 标准格式（需要配置API Key）",
    "api_local_desc": "本地 stream-server API",
    "auto_selected": "\n  （仅检测到 {desc}，已自动选择）",
    "input_choice": "\n👤 请输入选择 (1-{max}): ",
    "invalid_choice": "无效选择，请输入 1-{max}",
    "input_openai_key": "请输入 OpenAI API Key: ",
    "api_key_empty": "API Key 不能为空！",
    "input_base_url": "API Base URL (回车使用默认: {default}): ",
    "input_model": "模型名称 (回车使用默认: {default}): ",
    "input_local_url": "请输入本地API地址: ",
    "api_url_empty": "API 地址不能为空！",
    "input_api_key": "请输入 API Key (回车跳过): ",
    "input_wsid": "请输入 WSID (回车跳过): ",
    "input_model_marker": "请输入模型标记 (回车跳过): ",
    "project_setup": "\n📁 项目设置",
    "input_novel_name": "👤 请输入小说项目名（用于创建文件夹）: ",
    "scan_projects_header": "\n📂 检测到以下已有项目：",
    "no_existing_projects": "\n📂 未检测到已有项目。",
    "project_status_chapters": "{count}章",
    "project_status_plan": "计划",
    "project_status_meta": "元数据",
    "project_status_plot": "大纲",
    "or_input_manually": "手动输入项目名...",
    "select_project_prompt": "\n👤 请选择项目 (1-{max}): ",
    "select_operation": "\n🎯 请选择操作：",
    "op_full": "  1. 从头开始创作（完整流程）",
    "op_resume": "  2. 从断点继续写作",
    "op_planning": "  3. 仅执行策划阶段",
    "op_worldbuilding": "  4. 仅生成世界观和风格指南",
    "op_outline": "  5. 仅生成大纲",
    "op_writing": "  6. 仅执行写作（需要已有大纲）",
    "op_batch": "  7. 批量模式（连续生成多部小说）",
    "input_op_choice": "\n👤 请输入选择 (1-7): ",
    "invalid_op": "无效选择，请输入 1-7",
    "input_volume_num": "要生成哪一卷的细纲？(输入卷号，或回车跳过): ",
    "input_start_chapter": "从第几章开始？(回车从第1章开始): ",
    "input_end_chapter": "写到第几章？(回车写到末尾): ",
    "interrupted": "\n\n⏸️ 用户中断，已保存当前进度。下次可以选择'从断点继续'来恢复。",
    "error_occurred": "\n❌ 发生错误: {error}",
    "goodbye": "\n👋 再见！",

    # -- 批量模式 --
    "batch_input_names": "\n📚 请输入多个小说名称，用英文逗号分隔（如：小说A, 小说B, 小说C）：",
    "batch_empty": "❌ 未提供小说名称，返回主菜单。",
    "batch_select_op": "\n🎯 选择每部小说要执行的操作：",
    "batch_start": "\n🚀 批量模式：将按顺序生成 {total} 部小说：{names}",
    "batch_progress": "📖 [{current}/{total}] 开始生成小说：{name}",
    "batch_novel_done": "✅ 小说「{name}」已完成！",
    "batch_interrupted": "\n⏸️ 在写作「{name}」时被中断，还剩 {remaining} 部小说未完成。",
    "batch_continue_prompt": "是否继续生成剩余小说？(y/n): ",
    "batch_stopped": "🛑 批量生成已停止。",
    "batch_novel_error": "\n❌ 生成小说「{name}」时出错：{error}",
    "batch_all_done": "\n🎉 批量完成！共 {total} 部小说全部生成完毕。",

    # -- Language selection --
    "select_language": "\n🌐 请选择小说使用的语言：",
    "lang_choice_prompt": "\n👤 请输入选择 (1-{max}): ",

    # -- workflow.py --
    "phase_planning_title": "\n📝 阶段一：小说策划",
    "planner_prefix": "\n🤖 策划助手：\n",
    "user_prefix": "👤 你：",
    "input_empty_hint": "（请输入你的回答）",
    "multiline_hint": "（支持多行输入，输入空行结束；输入 /paste 进入粘贴模式）",
    "multiline_paste_hint": "（已进入粘贴模式，可自由粘贴含空行的内容，输入 /end 结束）",
    "quit_planning": "已退出策划阶段。",
    "force_done": "好的，让我来整理策划方案...",
    "generating_plan": "\n⏳ 正在生成完整的小说策划方案...",
    "plan_display_title": "\n📋 小说策划方案",
    "plan_label_title": "书名",
    "plan_label_genre": "类型",
    "plan_label_theme": "核心主题",
    "plan_label_target_words": "目标字数",
    "plan_label_total_chapters": "预计章数",
    "plan_label_volumes": "卷数",
    "plan_label_pov": "视角",
    "plan_label_tags": "标签",
    "plan_label_one_line": "一句话梗概",
    "plan_label_beginning": "起",
    "plan_label_middle": "承",
    "plan_label_end": "合",
    "plan_label_characters": "主要角色",
    "confirm_plan": "\n👤 对这个策划方案满意吗？(y/修改建议): ",
    "adjusting_plan": "\n⏳ 正在根据你的意见调整方案...",
    "plan_confirmed": "✅ 策划方案已确认并保存！",
    "rename_dir_prompt": "\n📁 小说标题为「{title}」，但项目文件夹为「{dir}」。",
    "rename_dir_confirm": "   是否将项目文件夹重命名为「{title}」？(y/n): ",
    "rename_dir_done": "  ✅ 项目文件夹已重命名为: {path}",
    "rename_dir_exists": "  ⚠️ 目录已存在: {path}",
    "rename_dir_failed": "  ❌ 重命名失败: {error}",
    "phase_world_title": "\n🌍 阶段二：世界观构建 & 风格指南（并行生成中...）",
    "world_done": "✅ 世界观设定已生成（{count}个文档）",
    "world_failed": "❌ 世界观生成失败: {error}",
    "style_done": "✅ 风格指南已生成",
    "style_failed": "❌ 风格指南生成失败: {error}",
    "phase_outline_title": "\n📋 阶段三：总大纲生成",
    "generating_outline": "⏳ 正在生成总大纲...",
    "outline_done": "✅ 总大纲已生成",
    "outline_review": "\n📖 总大纲已保存到 plot/master_outline.md，请查阅。",
    "press_enter_continue": "👤 按回车继续生成第一卷细纲...",
    "generating_volume": "📑 正在生成第{num}卷细纲...",
    "volume_done": "✅ 第{num}卷细纲已生成",
    "phase_writing_title": "\n✍️ 阶段五：开始写作",
    "checkpoint_resume": "[断点续跑] 检测到已完成{count}章，从第{next}章开始",
    "volume_not_found": "⚠️ 未找到第{num}卷细纲，正在生成...",
    "generating_volume_outline": "⏳ 正在生成第{num}卷细纲...",
    "writing_chapter": "📖 正在写作第{num}章...",
    "chapter_done": "  ✅ 第{num}章写作完成（约{words}字）",
    "post_processing": "  ⏳ 正在分析并更新元信息...",
    "post_done": "  ✅ 第{num}章后处理完成",
    "post_failed": "  ⚠️ 第{num}章后处理分析失败，跳过更新",
    "chapter_error": "  ❌ 第{num}章写作出错: {error}",
    "retry_prompt": "  是否重试？(y/n): ",
    "skip_chapter": "  跳过第{num}章，继续下一章",
    "pause_prompt": "\n📊 已完成{num}章，按回车继续，或输入'stop'暂停",
    "pause_input": "👤 ",
    "paused": "⏸️ 已暂停，下次可以从第{next}章继续",
    "writing_complete": "🎉 写作阶段完成！",
    "planning_incomplete": "策划阶段未完成，退出。",
    "no_plan_found": "未找到策划方案，从头开始...",
    "resume_checking": "🔄 正在检查项目状态...",
    "resume_completed": "已完成{count}章，继续写作...",
    "no_style_guide": "未找到风格指南，正在生成...",
    "no_outline": "未找到总大纲，正在生成...",
    "plan_not_found_error": "未找到策划方案文件 plan.json，请先执行策划阶段",

    # -- agents.py --
    "worldbuilding_start": "[世界观Agent] 开始并行生成 {count} 个设定文档...",
    "doc_done": "  ✅ {filename} 生成完成",
    "doc_failed": "  ❌ {filename} 生成失败",
    "doc_error": "  ❌ {filename} 生成出错: {error}",
    "llm_error_retry": "抱歉，我出了点问题，请再说一次~",
    "info_enough": "信息已经足够啦！让我来为你整理一份完整的小说策划方案... 🎯",
    "continue_input": "请继续告诉我更多关于你想创作的小说的信息~",

    # -- config.py --
    "config_loaded": "[配置] 已从 {file} 加载配置: {keys}",
    "novel_config_loaded": "[配置] 已从项目配置 {file} 加载: {keys}",
    "novel_config_skipped": "  ⚠️ 已跳过 {file} 中的 API/路径配置（请使用全局配置）: {keys}",
    "novel_config_auto_created": "[配置] 已自动创建 {file}（可编辑此文件定制本小说的参数）",
"config_not_found": "[配置] 未找到 {file}，将使用默认值；API Key 需在运行时手动输入",
    "config_hint": "[配置] 可参考 user_config.example.json 创建 {file}",
    "project_initialized": "[项目] 目录已初始化: {path}",

    # -- llm backends --
    "openai_initialized": "[LLM-OpenAI] 已初始化，模型: {model}, Base URL: {url}",
    "openai_need_package": "使用 OpenAI 后端需要安装 openai 包: pip install openai",
"openai_no_key": "OPENAI_API_KEY 未配置，请在 user_config.json 中填写或运行时输入",
    "openai_attempt_failed": "[LLM-OpenAI] 第{n}次调用失败: {error}",
    "openai_retry_wait": "[LLM-OpenAI] {wait}秒后重试...",
    "openai_max_retries": "[LLM-OpenAI] 已达最大重试次数({max})，放弃",
    "local_initialized": "[LLM-Local] 已初始化，URL: {url}, 模型标记: {marker}",
    "local_need_package": "使用本地后端需要安装 requests 包: pip install requests",
"local_no_url": "LOCAL_API_URL 未配置，请在 user_config.json 中填写",
    "local_attempt_failed": "[LLM-Local] 第{n}次调用失败: {error}",
    "local_retry_wait": "[LLM-Local] {wait}秒后重试...",
    "local_max_retries": "[LLM-Local] 已达最大重试次数({max})，放弃",
    "cannot_load_openai": "无法加载 OpenAI 后端: {error}\n请确保 llm_openai.py 存在且已安装 openai 包 (pip install openai)",
    "cannot_load_local": "无法加载本地后端: {error}\n请确保 llm_local.py 存在且已安装 requests 包 (pip install requests)",
    "unsupported_api_mode": "不支持的API模式: {mode}，可选值: 'openai', 'local'",

    # -- storage.py --
    "file_written": "[存储] 已写入: {path}",

    # -- Feature #1: 多方案大纲对比 --
    "outline_multi_draft_title": "\n📋 阶段三：总大纲生成（多方案对比）",
    "generating_draft": "  ⏳ 正在生成大纲方案 {num}/{total}（风格：{style}）...",
    "draft_done": "  ✅ 方案{num}完成",
    "draft_failed": "  ❌ 方案{num}失败: {error}",
    "draft_comparison_title": "\n📊 大纲方案对比",
    "draft_header": "\n{'─' * 40}\n📄 方案{num} — 风格：{style}\n{'─' * 40}",
    "draft_select_prompt": "\n👤 选择使用哪个方案（1-{max}），或输入'm'合并各方案精华: ",
    "draft_merging": "⏳ 正在合并各方案的精华...",
    "draft_selected": "✅ 已选择方案{num}作为总大纲",
    "draft_merged": "✅ 合并大纲已生成",
    "outline_drafts_truncating": "   ⚠️ 大纲草稿过长（预估 {total} tokens，预算 {budget}），将等比例截断各草稿...",
    "draft_invalid": "无效选择，请输入1-{max}或'm'",

    # -- Feature #2: 并行质量审查 --
    "parallel_review_title": "  🔍 正在运行并行质量审查...",
    "review_consistency": "[一致性审查员]",
    "review_style": "[文风审查员]",
    "review_foreshadowing": "[伏笔审查员]",
    "review_done": "  ✅ {reviewer}: 发现{count}个问题（置信度≥{threshold}）",
    "review_failed": "  ⚠️ {reviewer} 审查失败: {error}",
    "review_no_issues": "  ✅ 所有审查员通过 — 没有显著问题！",
    "review_issues_found": "  ⚠️ 所有审查员共发现{count}个问题:",
    "review_issue_item": "    [{severity}] ({reviewer}, 置信度: {confidence}) {description}",
    "review_critical_prompt": "  🚨 发现严重问题。是否重写本章？(y/n): ",

    # -- Feature #3: 润色循环 --
    "polish_start": "  ✨ 开始润色循环（最多{max_iter}轮）...",
    "polish_iteration": "  ✨ 润色第{iter}/{max_iter}轮...",
    "polish_score": "  📊 质量评分: {score}/10（阈值: {threshold}）",
    "polish_passed": "  ✅ 达到质量阈值！退出润色循环。",
    "polish_improving": "  ⏳ 评分未达标，正在改进...",
    "polish_max_reached": "  ⚠️ 已达最大润色轮次。使用最佳版本（评分: {score}/10）。",
    "polish_failed": "  ⚠️ 润色评估失败，保留当前版本。",

    # -- Feature #4: 卷间检查点 --
    "volume_checkpoint_title": "\n📍 第{num}卷检查点",
    "volume_checkpoint_summary": "  当前进度: 已完成{completed}章，约{words}字",
    "volume_checkpoint_prompt": "\n👤 即将开始第{num}卷。继续？(y / adjust / stop): ",
    "volume_checkpoint_adjust": "👤 请输入调整意见: ",
    "volume_checkpoint_adjusting": "⏳ 正在根据你的反馈调整卷大纲...",
    "volume_checkpoint_stopped": "⏸️ 在第{num}卷前停止。下次从第{next}章继续。",

    # -- Feature #5: 置信度分级 --
    "severity_critical": "严重",
    "severity_major": "重要",
    "severity_minor": "轻微",
    "severity_info": "提示",

    # -- Feature #6: 完结总结 --
    "final_summary_title": "\n📊 正在生成全书总结报告...",
    "final_summary_done": "✅ 全书总结报告已生成并保存！",
    "final_summary_failed": "⚠️ 全书总结报告生成失败: {error}",

    # -- 写作参数确认 --
    "writing_params_title": "\n⚙️ 写作参数确认",
    "ask_chapter_min_words": "   每章最少字数（当前: {current}，直接回车保持不变）: ",
    "ask_chapter_max_words": "   每章最多字数（当前: {current}，直接回车保持不变）: ",
    "writing_params_swapped": "   ⚠️ 最小值大于最大值，已自动交换。",
    "ask_word_count_check": "   是否启用字数检查？（当前: {status}，y/n，直接回车保持不变）: ",
    "ask_lazy_mode": "   是否启用懒人模式（自动确认一切）？（当前: {status}，y/n，直接回车保持不变）: ",
    "writing_params_summary": "   ✅ 写作参数: {min}-{max} 字/章, 字数检查: {check}, 懒人模式: {lazy}",

    # -- 引号偏好 --
    "quote_style_title": "\n💬 对话引号风格设置",
    "quote_style_prompt": "\n👤 请选择小说中对话使用的引号风格 (1-{max}): ",
    "quote_style_invalid": "无效选择，请输入 1-{max}",
    "quote_style_selected": "✅ 对话引号风格已设置为: {style}",
    "quote_style_option_curly": '\u201c\u201d 弯引号（如：\u201c你好！\u201d）',
    "quote_style_option_corner": '\u300c\u300d 直角引号（如：\u300c你好！\u300d）',
    "quote_style_option_guillemet": '\u00ab\u00bb 书名号式引号（如：\u00ab你好！\u00bb）',
    "quote_style_option_dash": '\u2014 破折号式对话（如：\u2014\u2014你好！）',
    "quote_style_option_straight": '"" 直引号（如："你好！"）',

    # -- 心理活动引号风格 --
    "inner_quote_title": "\n💭 心理活动/内心独白引号风格设置",
    "inner_quote_prompt": "\n👤 请选择小说中心理活动使用的引号风格 (1-{max}): ",
    "inner_quote_invalid": "无效选择，请输入 1-{max}",
    "inner_quote_selected": "✅ 心理活动引号风格已设置为: {style}",
    "inner_quote_option_corner_double": '『』双直角引号（如：『我必须小心』）',
    "inner_quote_option_corner": '「」直角引号（如：「我必须小心」）',
    "inner_quote_option_curly_single": '\u2018\u2019 单弯引号（如：\u2018我必须小心\u2019）',
    "inner_quote_option_italic": '*斜体* 标记心理活动（如：*我必须小心*）',
    "inner_quote_option_dash": '——双破折号（如：——我必须小心——）',
    "inner_quote_option_paren": '（）全角括号（如：（我必须小心））',
    "inner_quote_option_same": '与对话引号相同',
    "inner_quote_option_none": '不使用特殊标记（用叙述方式描写心理活动）',

    # -- 引号规则（注入风格指南/写作提示词中） --
    "quote_rules_heading": "引号风格规则",
    "quote_rule_dialogue_curly": '所有对话使用\u201c\u201d（弯双引号）。示例：\u201c你好！\u201d',
    "quote_rule_dialogue_corner": '所有对话使用「」（直角引号）。示例：「你好！」',
    "quote_rule_dialogue_guillemet": '所有对话使用«»（书名号式引号）。示例：«你好！»',
    "quote_rule_dialogue_dash": '使用——（破折号）引出对话。示例：——你好！',
    "quote_rule_dialogue_straight": '所有对话使用""（直引号）。示例："你好！"',
    "quote_rule_inner_corner_double": '心理活动/内心独白使用『』（双直角引号）。示例：『我必须小心』',
    "quote_rule_inner_corner": '心理活动/内心独白使用「」（直角引号）。示例：「我必须小心」',
    "quote_rule_inner_curly_single": '心理活动/内心独白使用\u2018\u2019（单弯引号）。示例：\u2018我必须小心\u2019',
    "quote_rule_inner_italic": '心理活动/内心独白使用*斜体*标记。示例：*我必须小心*',
    "quote_rule_inner_dash": '心理活动/内心独白使用——（双破折号）。示例：——我必须小心——',
    "quote_rule_inner_paren": '心理活动/内心独白使用（）（全角括号）。示例：（我必须小心）',
    "quote_rule_inner_none": '心理活动不使用任何特殊引号标记，改用叙述方式描写。',
    "quote_rule_inner_same": '心理活动/内心独白使用与对话相同的引号风格。',

    # -- 懒人模式 --
    "lazy_mode_enabled": "🛋️ 懒人模式已开启 — 确定大纲后将全自动运行，无需任何操作！",
    "lazy_auto_merge": "🛋️ [懒人] 自动合并所有大纲草稿...",
    "lazy_auto_select": "🛋️ [懒人] 仅一个草稿可用，已自动选择。",
    "lazy_auto_continue": "🛋️ [懒人] 自动继续...",
    "lazy_auto_retry": "🛋️ [懒人] 自动重试...",
    "lazy_auto_skip": "🛋️ [懒人] 自动跳过...",
    "lazy_auto_volume_continue": "🛋️ [懒人] 自动继续第{num}卷...",

    # -- 审查重试 --
    "review_retry_feedback": """⚠️ 重要：这是第{attempt}/{max_attempts}次重写。上一版本存在以下严重/重要问题，必须修正：
{issues}

请从头重写完整章节，确保修正以上所有问题，同时保持整体故事、基调和结构不变。""",
    "review_max_retries_reached": "  ⚠️ 第{num}章已达最大审查重试次数（{max}次），保存当前版本继续。",

    # -- 字数校验 --
    "wordcount_check_start": "  📏 字数校验：{words}字（目标：{min}-{max}）",
    "wordcount_too_short": "  ⚠️ 章节过短（{words}字，最少{min}字），正在扩充...",
    "wordcount_too_long": "  ⚠️ 章节过长（{words}字，最多{max}字），正在压缩...",
    "wordcount_split_needed": "  📑 章节严重超长（{words}字，≥{threshold}%上限），将拆分为两章...",
    "wordcount_expand_done": "  ✅ 扩充完成：{words}字",
    "wordcount_compress_done": "  ✅ 压缩完成：{words}字",
    "wordcount_split_done": "  ✅ 拆分完成：第{num_a}章（{words_a}字）+ 第{num_b}章（{words_b}字）",
    "wordcount_retry": "  🔄 字数校验重试 {attempt}/{max_attempts}...",
    "wordcount_give_up": "  ⚠️ 经过{max_attempts}次重试仍未达标，使用当前版本（{words}字）。",
    "wordcount_ok": "  ✅ 字数合格：{words}字",
    "wordcount_split_renumber": "  📝 注意：拆分后的后续章节将自动重新编号。",

    # -- Feature #1: 多方案大纲风格 --
    "outline_style_dramatic": "戏剧张力型",
    "outline_style_literary": "文学深度型",
    "outline_style_commercial": "商业节奏型",
})

# ============================================================
# PROMPTS: LLM提示词模板（继承英语基础 + 中文覆写）
# ============================================================
PROMPTS = dict(_BASE_PROMPTS)
PROMPTS.update({
    # -- 策划Agent --
    "planner_system": """你是一位资深小说策划编辑，擅长从零开始构思一部小说的核心设定。
你的任务是通过和用户对话，收集足够的信息来确定以下小说核心要素：

1. **题材/类型**：玄幻、都市、悬疑、言情、科幻等
2. **核心主题**：小说要表达什么
3. **目标字数和章节规划**：总字数、每章字数、预计章数、卷数
4. **叙述视角**：第一人称/第三人称
5. **核心标签**：3-5个关键标签
6. **一句话梗概**：能概括全书的一句话
7. **三段式梗概**：起承合的剧情概要
8. **文风要求**：写作风格、基调、参考作品
9. **禁忌事项**：不能出现的内容
10. **主要角色**：至少男主/女主的基本设定
11. **世界观框架**：故事发生的世界背景

你需要主动提问用户来获取这些信息。对于用户不想自己决定的部分，由你来创造性地补充。
当你认为信息已经足够时，输出最终的小说策划方案。

注意：
- 每次只问2-3个相关联的问题，不要一次性问太多
- 根据用户的回答灵活调整后续问题
- 对于每个要素，要明确询问用户是想自己指定还是交由你来创造
- 保持友好、专业的对话风格""",

    "planner_first_question": """你好！我是你的小说策划助手~ 🎉

在开始创作之前，我需要了解你的想法。让我们一步步来：

**首先，最基本的问题：**
1. 你想写什么**题材/类型**的小说？（比如：玄幻、都市、悬疑、科幻、言情、历史等）
2. 你心目中有没有大致的**故事方向**或**核心创意**？哪怕只是一个模糊的念头也行
3. 这些基础设定你想自己指定，还是更希望由我来帮你头脑风暴？

请随意聊聊你的想法~""",

    "planner_check_enough": """请分析目前收集到的所有信息，判断是否已经足够开始创作规划。

需要检查的核心要素清单:
1. 题材/类型 - {has_genre}
2. 核心主题 - {has_theme}
3. 目标字数和章节规划 - {has_structure}
4. 叙述视角 - {has_pov}
5. 核心标签 - {has_tags}
6. 一句话梗概 - {has_summary}
7. 文风要求 - {has_style}
8. 主要角色（至少有主角概念）- {has_characters}
9. 世界观框架 - {has_world}

请用JSON格式回复:
{{
    "is_enough": true/false,
    "missing_items": ["缺少的要素列表"],
    "next_questions": "如果信息不够，你接下来要问用户的问题（2-3个）"
}}

只返回JSON，不要其他内容。""",

    "planner_summarize": """根据以下用户对话中收集到的信息，生成完整的小说策划方案。
对于用户没有明确指定的部分，请你创造性地补充，使整体方案连贯且有吸引力。

请严格按照以下JSON格式输出，不要输出其他内容：
{{
    "title": "书名",
    "genre": "类型/题材",
    "theme": "核心主题（一段话）",
    "target_words": "目标总字数",
    "chapter_words": "每章字数范围",
    "total_chapters": "预计总章数",
    "volumes": "卷数和划分",
    "pov": "叙述视角",
    "tags": "核心标签（逗号分隔）",
    "one_line_summary": "一句话梗概",
    "three_act_summary": {{
        "beginning": "起（开端概要）",
        "middle": "承（发展概要）",
        "end": "合（结局概要）"
    }},
    "style_guide": "文风要求和写作规范",
    "taboos": "禁忌事项",
    "main_characters": [
        {{
            "name": "名字",
            "role": "角色定位（男主/女主/配角等）",
            "age": "年龄",
            "appearance": "外貌描述",
            "personality": "性格描述",
            "background": "背景故事",
            "motivation": "核心动机",
            "arc": "人物弧光/成长轨迹"
        }}
    ],
    "world_setting": "世界观框架描述",
    "synopsis": "小说简介（用于发布）"
}}""",

    # -- 大纲Agent --
    "outline_system": """你是一位经验丰富的小说大纲规划师。你将基于给定的小说策划方案，创建详细的剧情大纲。

你需要输出：
1. 全书的卷级大纲（每卷的主线、核心冲突、关键事件、卷末高潮和悬念）
2. 角色关系图谱的文字描述

输出格式为Markdown。请确保：
- 每卷大纲包含清晰的主线和关键事件列表
- 卷与卷之间有明确的因果衔接
- 角色的成长弧线贯穿始终
- 伏笔和悬念的设计合理
- 节奏有张有弛""",

    "volume_outline_system": """你是一位擅长细化剧情的小说大纲师。
你将基于总大纲中某一卷的概述，创建该卷的详细章节级大纲。

输出格式为Markdown，每章需要包含：
- 章节标题
- 主要事件（3-5个关键点）
- 出场角色
- 情感基调/氛围
- 伏笔（埋/填）
- 承上启下的衔接点""",

    # -- 世界观Agent --
    "worldbuilding_system": """你是一位专业的世界观构建师。基于给定的小说策划方案，你需要创建详细的世界设定文档。

输出格式为Markdown，需要覆盖：
1. 世界观总设定（时代背景、社会结构、科技/魔法水平等）
2. 地理/空间设定（重要地点及其特征）
3. 特殊体系设定（修仙体系/魔法体系/科技体系等，根据题材而定）
4. 时间线大事记（故事开始前的重要历史事件）

确保设定之间互相一致，不矛盾。""",

    "character_system": """你是一位擅长人物塑造的角色设计师。基于给定的小说策划方案和世界设定，你需要创建详细的人物档案。

每个角色需要包含：
- 基本信息（名字、年龄、外貌等）
- 性格描写（多层次，包含外在表现和内在性格）
- 背景故事
- 能力/特长
- 目标/动机
- 说话风格/口癖
- 人物弧光（成长轨迹）
- 角色关系

输出格式为Markdown。确保角色之间有化学反应，性格互补或冲突。""",

    # -- 写作Agent --
    "writer_system": """你是一位才华横溢的网络小说作家。
你将根据提供的设定、大纲和上下文，撰写小说正文。

写作要求：
{style_guide}

结构要求：
- 每章 {min_words}-{max_words} 字
- 章节需要有钩子开头（承接上章或制造新悬念）
- 核心剧情推进（至少一个关键事件）
- 结尾留钩（吸引读者继续阅读）

严格遵守以下格式：
- 章节标题格式：第X章 标题
- 直接输出正文内容，不要输出任何元信息或备注""",

    "writer_chapter_prompt": """请根据以下信息撰写第{chapter_num}章的正文。

## 本章大纲
{chapter_outline}

## 最近章节摘要（用于保持连贯性）
{recent_briefs}

## 当前人物状态
{character_status}

## 需要注意的伏笔
{hooks_info}

## 角色档案（权威设定——姓名必须严格一致）
{character_profiles}

## 世界观与地点设定（权威设定——所有地名、势力名等必须严格一致）
{world_setting}

⚠️ 严重警告：所有角色姓名、地点名称、门派/势力名称及专有名词，必须与上方的角色档案和世界观设定完全一致。严禁自行创造、修改或替换任何名称。

请直接输出完整的章节正文（{min_words}-{max_words}字），以"第{chapter_num}章"开头。""",

    # -- 后处理Agent --
    "post_write_system": """你是一位细心的小说编辑助理。你的任务是在每章写完后，分析章节内容并生成以下更新信息。

请以JSON格式输出:
{{
    "chapter_brief": {{
        "chapter_num": 章节号,
        "title": "章节标题",
        "word_count": 约字数,
        "main_events": ["主要事件1", "主要事件2", ...],
        "character_changes": ["角色状态变更1", ...],
        "hooks_planted": ["新埋的伏笔1", ...],
        "hooks_resolved": ["填上的伏笔ID1", ...],
        "next_chapter_hook": "留给下一章的钩子"
    }},
    "progress_update": {{
        "latest_chapter": "第X章·标题",
        "total_words": 约累计总字数,
        "character_status": {{
            "角色名": "当前状态描述"
        }}
    }}
}}

只返回JSON，不要其他内容。""",

    # -- 风格指南Agent --
    "style_guide_system": """你是一位文学顾问，专门负责制定小说的文风规范。
根据给定的小说策划方案，生成详细的文风指南文档。

输出格式为Markdown，需要包含：
1. 叙述视角规范
2. 文风要求（整体基调、内心独白风格、对外表现风格等）
3. 章节结构规范
4. 对话规范（对话格式、角色说话风格）
5. 描写规范（战斗/情感/环境等各类描写的要求）
6. 节奏控制建议
7. 核心写作原则
8. 禁忌事项""",

    # -- 世界观任务提示词 --
    "task_world_setting": """基于以下小说策划方案，创建世界观总设定文档（Markdown格式）。
包含：时代背景、社会结构、重要势力/组织等基础世界观。

策划方案：
{plan_text}""",

    "task_characters": """基于以下小说策划方案，创建详细的人物档案文档（Markdown格式）。
参考格式要求：每个角色包含姓名、年龄、外貌、性格（多层次）、背景、能力、动机、口癖、人物弧光。
最后附上角色关系图谱（文字描述）。

策划方案：
{plan_text}""",

    "task_locations": """基于以下小说策划方案，创建重要地点/场景设定文档（Markdown格式）。
包含所有故事中会出现的重要地点及其特征描述。

策划方案：
{plan_text}""",

    "task_timeline": """基于以下小说策划方案，创建时间线大事记文档（Markdown格式）。
包含故事开始前的重要历史事件和故事进行中的时间线规划。

策划方案：
{plan_text}""",

    "task_power_system": """基于以下小说策划方案，创建力量/修炼体系设定文档（Markdown格式）。
包含：等级划分、修炼方式、特殊能力体系等详细设定。

策划方案：
{plan_text}""",

    "task_tech_system": """基于以下小说策划方案，创建科技体系设定文档（Markdown格式）。
包含：科技水平、关键技术、特殊设备等详细设定。

策划方案：
{plan_text}""",

    # -- 大纲生成提示词 --
    "master_outline_prompt": """请基于以下小说策划方案，创建全书的总大纲。

## 小说策划方案
{plan_json}

请生成包含所有卷的总大纲（Markdown格式），每卷需要包含：
- 主线描述
- 核心冲突
- 关键事件（编号列表）
- 主要角色状态
- 卷末高潮
- 卷末悬念
- 与下一卷的衔接""",

    "volume_outline_prompt": """请基于以下信息，创建第{volume_num}卷的详细章节级大纲。

## 小说策划方案摘要
- 书名：{title}
- 类型：{genre}
- 每章字数：{chapter_words}

## 该卷在总大纲中的描述
{volume_info}

## 总大纲（完整，用于把握全局）
{master_outline}

请为这一卷生成详细的章节级大纲，每章包含：
- 章节编号和标题
- 主要事件（3-5个）
- 出场角色
- 情感基调
- 伏笔（埋/填）
- 衔接点""",

    # -- 后处理提示词 --
    "analyze_chapter_prompt": """请分析以下小说章节，生成摘要和更新信息。

## 章节大纲（参考）
{chapter_outline}

## 章节正文
{chapter_text}

请严格按照指定的JSON格式输出。""",

    # -- 修改方案 --
    "plan_revision_request": "我对策划方案有以下修改意见：{feedback}\n请据此调整方案。",

    # -- 题材检测关键词 --
    "genre_fantasy_keywords": ["玄幻", "修仙", "仙侠", "魔法", "奇幻"],
    "genre_scifi_keywords": ["科幻", "未来", "赛博", "太空", "科技"],

    "outline_merge_prompt": """以下是同一部小说的
请创建一份**合并总大纲**，要求：
1. 从各方案中取最强的结构性元素
2. 融合最佳的情节创意和角色弧线
3. 保持全篇逻辑一致性
4. 保留最精彩的伏笔设计和高潮安排

{drafts_text}

以Markdown格式输出合并后的总大纲。""",

    # -- Feature #2: 并行审查系统提示词 --
    "consistency_reviewer_system": """你是一位细致入微的小说连续性编辑。
你的任务是审查章节内容与前文、大纲以及提供的角色档案的一致性。

检查以下内容：
1. **角色姓名准确性**：将章节中出现的每一个角色名字与角色档案进行逐一比对。标记任何与档案不完全一致的名字（拼写错误、名字错误、名字互换、称呼不一致）。这是最高优先级的检查项。
2. **角色特征一致性**：验证每个角色的行为、说话风格、能力和性格是否与其档案匹配。
3. 时间线和时序准确性
4. 场景/地点一致性
5. 情节连续性（引用的事件必须确实发生过）
6. 角色认知一致性（角色不应知道他们尚未了解的事情）

对发现的每个问题，给出置信度评分（0-100）：
- 0-25: 不确定，可能是有意为之
- 26-50: 可能有问题，但也可能是主观判断
- 51-75: 很可能是错误，需要验证
- 76-100: 确定是错误，已与原文对照验证

以JSON格式输出：
{{
    "issues": [
        {{
            "type": "consistency",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "问题描述",
            "location": "章节中的大致位置",
            "suggestion": "修复建议"
        }}
    ],
    "overall_consistency_score": 1-10
}}

只返回JSON，不要其他内容。""",

    "style_reviewer_system": """你是一位文学风格审查专家。
你的任务是审查章节内容是否符合写作风格指南。

检查以下内容：
1. 叙述视角一致性（无意外的视角切换）
2. 语气和氛围与风格指南的契合度
3. 对话风格与角色档案的一致性
4. 节奏问题（太仓促或太拖沓）
5. 文笔质量（别扭的措辞、重复用词等）

对发现的每个问题，给出置信度评分（0-100）。

以JSON格式输出：
{{
    "issues": [
        {{
            "type": "style",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "问题描述",
            "location": "章节中的大致位置",
            "suggestion": "修复建议"
        }}
    ],
    "overall_style_score": 1-10
}}

只返回JSON，不要其他内容。""",

    "foreshadowing_reviewer_system": """你是一位伏笔和情节连贯性专家。
你的任务是审查章节中伏笔元素的处理情况。

检查以下内容：
1. 埋设的伏笔是否足够隐蔽（不会太明显）？
2. 之前埋下的钩子是否在适当时机推进或解决？
3. 根据大纲，是否有被遗漏的伏笔机会？
4. 已解决的伏笔是否令人满意？
5. 章节结尾是否为下一章创造了足够的悬念？

对发现的每个问题，给出置信度评分（0-100）。

以JSON格式输出：
{{
    "issues": [
        {{
            "type": "foreshadowing",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "问题描述",
            "location": "章节中的大致位置",
            "suggestion": "修复建议"
        }}
    ],
    "overall_foreshadowing_score": 1-10
}}

只返回JSON，不要其他内容。""",

    "review_chapter_prompt": """请审查以下章节。

## 角色档案（权威参考，用于核对姓名和特征）
{character_profiles}

## 风格指南
{style_guide}

## 章节大纲
{chapter_outline}

## 最近章节摘要
{recent_briefs}

## 伏笔追踪
{hooks_info}

## 章节正文
{chapter_text}

重要：请将章节正文中的所有角色名字与上方的角色档案逐一比对。任何名字不匹配都是严重问题。

请按照指定的JSON格式输出审查结果。""",

    # -- Feature #3: 润色循环提示词 --
    "polish_evaluate_system": """你是一位资深小说编辑。请对以下章节的质量进行1-10分的评估。

评估维度：
1. 文笔质量和可读性
2. 角色声音一致性
3. 节奏和流畅度
4. 情感冲击力
5. 钩子强度（开头和结尾）
6. 与大纲的契合度

以JSON格式输出：
{{
    "score": 1-10,
    "strengths": ["优点1", "优点2"],
    "weaknesses": ["不足1", "不足2"],
    "specific_improvements": [
        {{
            "location": "文中位置",
            "current": "当前问题文本（简述）",
            "suggested": "改进建议"
        }}
    ]
}}

只返回JSON，不要其他内容。""",

    "polish_evaluate_prompt": """请评估这一章的质量。

## 风格指南
{style_guide}

## 章节大纲
{chapter_outline}

## 章节正文
{chapter_text}

请以JSON格式输出评估结果。""",

    "polish_improve_system": """你是一位才华横溢的小说作家，正在进行修订。
你将收到一章内容以及编辑给出的具体改进建议。
请重写**完整章节**，将改进建议融入其中，同时保持整体故事、基调和结构不变。

不要添加任何元评论——只输出修订后的章节正文。""",

    "polish_improve_prompt": """请根据编辑的反馈修订以下章节。

## 编辑反馈
不足之处：{weaknesses}

具体改进建议：
{improvements}

## 当前章节正文
{chapter_text}

请输出完整的修订后章节正文。""",

    # -- Feature #4: 卷间检查点调整 --
    "volume_adjust_prompt": """读者对第{volume_num}卷提出了以下反馈/调整意见。

反馈：{feedback}

当前卷大纲：
{volume_outline}

请修改卷大纲以融入读者的反馈，同时保持与总大纲的一致性。

以Markdown格式输出修改后的卷大纲。""",

    # -- 字数校验提示词 --
    "expand_chapter_system": """你是一位才华横溢的小说作家。你将收到一个字数不足的章节，需要对其进行扩充。
在保持质量的前提下扩充章节以达到目标字数。不要用注水内容来凑字数。

扩充策略：
- 增加更多细节描写（环境、情绪、感官细节）
- 扩展对话交流，增加自然的对话往来
- 添加角色内心独白和反应
- 细化动作场景，增加更生动的描述
- 添加烘托氛围的过渡场景

重要：只输出完整的扩充后章节正文，不要输出任何元信息或备注。""",

    "expand_chapter_prompt": """以下章节字数不足（{current_words}字），请将其扩充至约{target_words}字。

## 风格指南
{style_guide}

## 章节大纲
{chapter_outline}

## 当前章节正文（过短）
{chapter_text}

请输出完整的扩充后章节正文（{target_words}字以上）。""",

    "compress_chapter_system": """你是一位经验丰富的小说编辑。你将收到一个字数过多的章节，需要对其进行压缩。
在保留所有关键情节点和角色时刻的前提下压缩章节。

压缩策略：
- 精简文笔，去除冗余描写
- 合并重复对话
- 概括不太重要的过渡场景
- 去除不推动情节的注水内容
- 精简动作场景

重要：所有关键情节事件、角色发展和伏笔必须保留。
只输出完整的压缩后章节正文，不要输出任何元信息或备注。""",

    "compress_chapter_prompt": """以下章节字数过多（{current_words}字），请将其压缩至约{target_words}字。

## 风格指南
{style_guide}

## 章节大纲（保留所有关键事件）
{chapter_outline}

## 当前章节正文（过长）
{chapter_text}

请输出完整的压缩后章节正文（约{target_words}字），保留所有关键情节点。""",

    "split_chapter_system": """你是一位经验丰富的小说编辑。你将收到一个严重超长的章节，需要将其拆分为两章。
找到一个自然的叙事断点来拆分章节。拆分后的每一章需要：
- 有自己的戏剧弧线（铺垫 → 发展 → 钩子结尾）
- 长度大致相等
- 在自然的悬念点或过渡点结束

输出格式：使用精确的分隔行 "===CHAPTER_SPLIT===" 分隔两章。
每章以章节标题行开头。

重要：只输出由 ===CHAPTER_SPLIT=== 分隔的两章正文，不要输出任何元信息或备注。""",

    "split_chapter_prompt": """以下章节严重超长（{current_words}字，每章目标：{min_words}-{max_words}字），请将其拆分为两章。

## 风格指南
{style_guide}

## 原章节大纲
{chapter_outline}

## 当前章节正文（待拆分）
{chapter_text}

将此章拆分为两个结构完整的章节，使用 "===CHAPTER_SPLIT===" 作为分隔。
第{chapter_num_a}章为前半部分，第{chapter_num_b}章为后半部分。
每章约{target_words}字。""",

    # -- Feature #6: 完结总结提示词 --
    "final_summary_system": """你是一位文学分析师。为一部已完成的小说生成全面的总结报告。

以Markdown格式输出，包含：
1. **小说概览** — 书名、类型、最终字数、章数
2. **情节综述** — 完整故事梗概（含剧透）
3. **角色弧线分析** — 每位主要角色的成长变化
4. **主题分析** — 核心主题及其展开方式
5. **数据统计** — 每章字数、平均字数、最长/最短章节
6. **伏笔解决报告** — 哪些伏笔被埋设和解决
7. **写作质量评注** — 整体文笔质量、亮点场景
8. **续集潜力线索** — 可以延续的开放线索""",

    "final_summary_prompt": """为这部已完成的小说生成全面的完结总结。

## 小说策划方案
{plan_json}

## 章节摘要
{all_briefs}

## 角色档案
{characters}

## 伏笔追踪
{hooks_info}

## 统计数据
- 总章数：{total_chapters}
- 总字数：约{total_words}字

请以Markdown格式生成完整的总结报告。""",

    # -- Language enforcement instruction --
    "language_instruction": (
        "**重要——语言要求**："
        "你必须使用{native_name}（{english_name}）撰写所有输出内容。"
        "每一句话、每一段、每个标题和标签都必须使用{native_name}。"
        "除非是引用专有名词或术语，否则不要混入其他语言。"
    ),
})

# ============================================================
# TEMPLATES: Markdown模板（继承英语基础 + 中文覆写）
# ============================================================
TEMPLATES = dict(_BASE_TEMPLATES)
TEMPLATES.update({
    "readme": """# 📖 长篇小说创作项目

## 小说基本信息
- **书名**：《{title}》
- **类型**：{genre}
- **目标字数**：{target_words}
- **每章字数**：{min_words}-{max_words}字
- **预计总章数**：{total_chapters}
- **卷数划分**：{volumes}
- **叙述视角**：{pov}
- **核心标签**：{tags}

## 一句话梗概
{one_line_summary}

## 📁 目录结构说明

```
{title}/
├── README.md              # 项目总纲
├── meta/                  # 元信息管理
│   ├── progress.md        # 写作进度追踪
│   ├── style_guide.md     # 文风和写作规范
│   └── hooks_tracker.md   # 伏笔/钩子追踪表
├── worldbuilding/         # 世界观设定
│   ├── characters.md      # 人物档案
│   ├── world_setting.md   # 世界观总设定
│   └── ...                # 其他设定文件
├── plot/                  # 剧情管理
│   ├── master_outline.md  # 总大纲
│   ├── volume_XX.md       # 每卷细纲
│   └── chapter_briefs.md  # 章节摘要记录
└── chapters/              # 正文输出
    ├── chapter_001.txt    # 第一章正文
    └── ...
```

## 🔄 写作流程
1. 读取 progress.md → 了解当前进度
2. 读取 chapter_briefs.md → 回顾最近章节
3. 参考当前卷细纲 → 确认本章内容
4. 检查 hooks_tracker.md → 看伏笔状态
5. 查阅 characters.md → 确认人物状态
6. 输出正文到 chapters/
7. 更新 progress.md、chapter_briefs.md 等
""",

    "progress": """# 📊 写作进度追踪

## 当前状态
- **最新完成章节**：尚未开始
- **当前正在写**：待定
- **当前卷**：第一卷
- **总字数**：0
- **上次更新时间**：-

## 下一步计划
> 1. ~~确定小说题材/类型~~ ✅
> 2. ~~核心设定和主角~~ ✅
> 3. ~~总大纲~~ ✅
> 4. **完成第一卷细纲** ← 当前
> 5. 开始正文创作

## 已完成章节一览

| 章节 | 标题 | 约字数 | 核心事件 |
|------|------|--------|---------|

## 当前角色状态速查
（待更新）

## 待处理事项
- [x] 确定小说题材
- [x] 完成世界观设定
- [x] 完成人物设定
- [x] 完成总大纲
- [ ] 完成第一卷细纲
- [ ] 第1章正文
""",

    "hooks_tracker": """# 🎣 伏笔/钩子追踪表

> 记录所有埋下的伏笔和悬念，追踪其状态
> 状态：🔴 已埋未填 | 🟡 部分揭示 | 🟢 已填坑 | ⚪ 计划中

---

## 长线伏笔（跨卷）

| ID | 伏笔内容 | 埋设章节 | 计划填坑 | 状态 | 备注 |
|----|---------|---------|---------|------|------|

## 短线伏笔（本卷内）

| ID | 伏笔内容 | 埋设章节 | 计划填坑 | 状态 | 备注 |
|----|---------|---------|---------|------|------|

## 已填坑记录

| ID | 伏笔内容 | 埋设章节 | 填坑章节 | 备注 |
|----|---------|---------|---------|------|
""",

    "chapter_briefs": """# 📝 章节摘要记录

> 每章写完后记录摘要，用于快速回顾剧情
> 格式：章节号 | 标题 | 字数 | 主要事件 | 角色状态变化 | 伏笔/悬念

---
""",

    "synopsis_title": "# 小说简介\n\n",

    # -- 后处理更新模板 --
    "chapter_brief_entry": """
### 第{chapter_num}章 · {title}（约{word_count}字）
**主要事件**：
""",
    "character_changes_header": "\n**角色状态变更**：\n",
    "hooks_planted_header": "\n**新埋伏笔**：\n",
    "next_hook_prefix": "\n**下章钩子**：",

    "progress_update_entry": """
---
### 第{chapter_num}章完成更新
- **最新完成**：{latest_chapter}
- **累计字数**：约{total_words}字
""",
    "character_status_header": "\n**角色状态速查**：\n",

    # -- Feature #6: 完结总结模板 --
    "final_summary_filename": "meta/final_summary.md",
})

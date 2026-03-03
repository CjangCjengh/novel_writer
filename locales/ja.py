"""
日本語ロケール
"""
from locales.en import UI as _BASE_UI, PROMPTS as _BASE_PROMPTS, TEMPLATES as _BASE_TEMPLATES

# ============================================================
# UI: ユーザーインターフェース文字列（英語をベースに日本語で上書き）
# ============================================================
UI = dict(_BASE_UI)
UI.update({
    "welcome_title": "📖 小説Agentワークフロー v1.0",
    "welcome_subtitle": "   AI駆動の自動小説創作システム",
    "no_backend": "\n❌ 利用可能なLLMバックエンドがありません！",
    "no_backend_hint": "   llm_openai.py または llm_local.py の少なくとも一つが存在することを確認してください",
    "select_api_mode": "\n🔌 LLM APIモードを選択してください：",
    "api_openai_desc": "OpenAI標準フォーマット（APIキーが必要）",
    "api_local_desc": "ローカル stream-server API",
    "auto_selected": "\n  （{desc}のみ検出、自動選択されました）",
    "input_choice": "\n👤 選択を入力してください (1-{max}): ",
    "invalid_choice": "無効な選択です。1-{max}を入力してください",
    "input_openai_key": "OpenAI APIキーを入力してください: ",
    "api_key_empty": "APIキーは空にできません！",
    "input_base_url": "API Base URL (デフォルト使用はEnter: {default}): ",
    "input_model": "モデル名 (デフォルト使用はEnter: {default}): ",
    "input_local_url": "ローカルAPIアドレスを入力してください: ",
    "api_url_empty": "APIアドレスは空にできません！",
    "input_api_key": "APIキーを入力してください (スキップはEnter): ",
    "input_wsid": "WSIDを入力してください (スキップはEnter): ",
    "input_model_marker": "モデルマーカーを入力してください (スキップはEnter): ",
    "project_setup": "\n📁 プロジェクト設定",
    "input_novel_name": "👤 小説プロジェクト名を入力してください（フォルダ作成用）: ",
    "scan_projects_header": "\n📂 既存のプロジェクトが見つかりました：",
    "no_existing_projects": "\n📂 既存のプロジェクトは見つかりませんでした。",
    "project_status_chapters": "{count}章",
    "project_status_plan": "計画",
    "project_status_meta": "メタ",
    "project_status_plot": "アウトライン",
    "or_input_manually": "プロジェクト名を手動入力...",
    "select_project_prompt": "\n👤 プロジェクトを選択してください (1-{max}): ",
    "select_operation": "\n🎯 操作を選択してください：",
    "op_full": "  1. 最初から作成（フルワークフロー）",
    "op_resume": "  2. チェックポイントから再開",
    "op_planning": "  3. 企画フェーズのみ",
    "op_worldbuilding": "  4. 世界観＆スタイルガイドの生成のみ",
    "op_outline": "  5. アウトラインの生成のみ",
    "op_writing": "  6. 執筆のみ（既存のアウトラインが必要）",
    "op_batch": "  7. バッチモード（複数の小説を連続生成）",
    "input_op_choice": "\n👤 選択を入力してください (1-7): ",
    "invalid_op": "無効な選択です。1-7を入力してください",
    "input_volume_num": "どの巻のアウトラインを生成しますか？(番号を入力、またはEnterでスキップ): ",
    "input_start_chapter": "何章から開始しますか？(Enter で第1章から): ",
    "input_end_chapter": "何章まで書きますか？(Enterで最後まで): ",
    "interrupted": "\n\n⏸️ ユーザーによる中断。進捗は保存されました。次回「チェックポイントから再開」を選択してください。",
    "error_occurred": "\n❌ エラーが発生しました: {error}",
    "goodbye": "\n👋 さようなら！",

    # -- バッチモード --
    "batch_input_names": "\n📚 小説名をカンマ区切りで入力してください（例：小説A, 小説B, 小説C）：",
    "batch_empty": "❌ 小説名が入力されていません。メインメニューに戻ります。",
    "batch_select_op": "\n🎯 各小説に対する操作を選択してください：",
    "batch_start": "\n🚀 バッチモード：{total} 作品を順番に生成します：{names}",
    "batch_progress": "📖 [{current}/{total}] 小説を開始：{name}",
    "batch_novel_done": "✅ 小説『{name}』が完了しました！",
    "batch_interrupted": "\n⏸️ 『{name}』の執筆中に中断されました。残り {remaining} 作品が未完了です。",
    "batch_continue_prompt": "残りの小説の生成を続けますか？(y/n): ",
    "batch_stopped": "🛑 バッチ処理を停止しました。",
    "batch_novel_error": "\n❌ 小説『{name}』の生成中にエラー：{error}",
    "batch_all_done": "\n🎉 バッチ完了！全 {total} 作品の生成が完了しました。",

    "select_language": "\n🌐 小説で使用する言語を選択してください：",
    "lang_choice_prompt": "\n👤 選択を入力してください (1-{max}): ",
    "phase_planning_title": "\n📝 フェーズ1：小説企画",
    "planner_prefix": "\n🤖 企画アシスタント：\n",
    "user_prefix": "👤 あなた：",
    "input_empty_hint": "（回答を入力してください）",
    "multiline_hint": "（複数行入力可能・空行で入力終了。/paste で貼り付けモード）",
    "multiline_paste_hint": "（貼り付けモード：空行を含む内容を自由に貼り付け可能。/end で終了）",
    "quit_planning": "企画フェーズを終了しました。",
    "force_done": "了解しました、企画書をまとめます...",
    "generating_plan": "\n⏳ 完全な小説企画書を生成中...",
    "plan_display_title": "\n📋 小説企画書",
    "plan_label_title": "タイトル",
    "plan_label_genre": "ジャンル",
    "plan_label_theme": "核心テーマ",
    "plan_label_target_words": "目標文字数",
    "plan_label_total_chapters": "予想章数",
    "plan_label_volumes": "巻数",
    "plan_label_pov": "視点",
    "plan_label_tags": "タグ",
    "plan_label_one_line": "一行あらすじ",
    "plan_label_beginning": "起",
    "plan_label_middle": "承",
    "plan_label_end": "結",
    "plan_label_characters": "主要キャラクター",
    "confirm_plan": "\n👤 この企画書に満足していますか？(y/修正意見): ",
    "adjusting_plan": "\n⏳ ご意見に基づいて企画書を調整中...",
    "plan_confirmed": "✅ 企画書が確認され保存されました！",
    "rename_dir_prompt": "\n📁 小説タイトルは「{title}」ですが、プロジェクトディレクトリは「{dir}」です。",
    "rename_dir_confirm": "   プロジェクトディレクトリを「{title}」にリネームしますか？ (y/n): ",
    "rename_dir_done": "  ✅ プロジェクトディレクトリをリネームしました: {path}",
    "rename_dir_exists": "  ⚠️ ディレクトリが既に存在します: {path}",
    "rename_dir_failed": "  ❌ リネームに失敗しました: {error}",
    "phase_world_title": "\n🌍 フェーズ2：世界観構築＆スタイルガイド（並列生成中...）",
    "world_done": "✅ 世界観設定の生成完了（{count}個のドキュメント）",
    "world_failed": "❌ 世界観生成に失敗: {error}",
    "style_done": "✅ スタイルガイドの生成完了",
    "style_failed": "❌ スタイルガイド生成に失敗: {error}",
    "phase_outline_title": "\n📋 フェーズ3：マスターアウトライン生成",
    "generating_outline": "⏳ マスターアウトラインを生成中...",
    "outline_done": "✅ マスターアウトラインの生成完了",
    "outline_review": "\n📖 マスターアウトラインが plot/master_outline.md に保存されました。ご確認ください。",
    "press_enter_continue": "👤 Enterを押して第1巻アウトラインの生成を続行...",
    "generating_volume": "📑 第{num}巻のアウトラインを生成中...",
    "volume_done": "✅ 第{num}巻のアウトライン生成完了",
    "phase_writing_title": "\n✍️ フェーズ5：執筆開始",
    "checkpoint_resume": "[チェックポイント] {count}章の完了を検出、第{next}章から再開",
    "volume_not_found": "⚠️ 第{num}巻のアウトラインが見つかりません、生成中...",
    "generating_volume_outline": "⏳ 第{num}巻のアウトラインを生成中...",
    "writing_chapter": "📖 第{num}章を執筆中...",
    "chapter_done": "  ✅ 第{num}章の執筆完了（約{words}文字）",
    "post_processing": "  ⏳ メタデータを分析・更新中...",
    "post_done": "  ✅ 第{num}章の後処理完了",
    "post_failed": "  ⚠️ 第{num}章の後処理分析に失敗、更新をスキップ",
    "chapter_error": "  ❌ 第{num}章の執筆でエラー: {error}",
    "retry_prompt": "  リトライしますか？(y/n): ",
    "skip_chapter": "  第{num}章をスキップ、次の章へ",
    "pause_prompt": "\n📊 {num}章が完了。Enterで続行、'stop'で一時停止",
    "pause_input": "👤 ",
    "paused": "⏸️ 一時停止しました。次回は第{next}章から再開できます",
    "writing_complete": "🎉 執筆フェーズ完了！",
    "planning_incomplete": "企画フェーズが未完了のため、終了します。",
    "no_plan_found": "企画書が見つかりません。最初から開始します...",
    "resume_checking": "🔄 プロジェクトの状態を確認中...",
    "resume_completed": "{count}章が完了しています。執筆を続行...",
    "no_style_guide": "スタイルガイドが見つかりません。生成中...",
    "no_outline": "マスターアウトラインが見つかりません。生成中...",
    "plan_not_found_error": "企画書ファイル plan.json が見つかりません。まず企画フェーズを実行してください",
    "worldbuilding_start": "[世界観エージェント] {count}個の設定ドキュメントを並列生成開始...",
    "doc_done": "  ✅ {filename} 生成完了",
    "doc_failed": "  ❌ {filename} 生成失敗",
    "doc_error": "  ❌ {filename} エラー: {error}",
    "llm_error_retry": "すみません、問題が発生しました。もう一度お願いします~",
    "info_enough": "情報は十分です！完全な小説企画書をまとめます... 🎯",
    "continue_input": "あなたが書きたい小説についてもっと教えてください~",
    "config_loaded": "[設定] {file} から設定を読み込みました: {keys}",
    "novel_config_loaded": "[設定] 作品別設定 {file} を読み込みました: {keys}",
    "novel_config_skipped": "  ⚠️ {file} のAPI/パスキーをスキップしました（グローバル設定を使用）: {keys}",
    "novel_config_auto_created": "[設定] テンプレートから {file} を自動作成しました（この作品の設定をカスタマイズできます）",
    "config_not_found": "[設定] {file} が見つかりません。機密情報は実行時に手動入力が必要です",
"config_hint": "[設定] user_config.example.json を参考に {file} を作成してください",
    "project_initialized": "[プロジェクト] ディレクトリ初期化完了: {path}",
    "openai_initialized": "[LLM-OpenAI] 初期化完了、モデル: {model}, Base URL: {url}",
    "openai_need_package": "OpenAIバックエンドにはopenaiパッケージが必要です: pip install openai",
"openai_no_key": "OPENAI_API_KEY が未設定です。user_config.json に記入するか実行時に入力してください",
    "openai_attempt_failed": "[LLM-OpenAI] 試行{n}回目失敗: {error}",
    "openai_retry_wait": "[LLM-OpenAI] {wait}秒後にリトライ...",
    "openai_max_retries": "[LLM-OpenAI] 最大リトライ回数({max})に達しました。中止します",
    "local_initialized": "[LLM-Local] 初期化完了、URL: {url}, モデルマーカー: {marker}",
    "local_need_package": "ローカルバックエンドにはrequestsパッケージが必要です: pip install requests",
"local_no_url": "LOCAL_API_URL が未設定です。user_config.json に記入してください",
    "local_attempt_failed": "[LLM-Local] 試行{n}回目失敗: {error}",
    "local_retry_wait": "[LLM-Local] {wait}秒後にリトライ...",
    "local_max_retries": "[LLM-Local] 最大リトライ回数({max})に達しました。中止します",
    "cannot_load_openai": "OpenAIバックエンドを読み込めません: {error}\nllm_openai.py が存在し、openai がインストールされていることを確認してください",
    "cannot_load_local": "ローカルバックエンドを読み込めません: {error}\nllm_local.py が存在し、requests がインストールされていることを確認してください",
    "unsupported_api_mode": "サポートされていないAPIモード: {mode}。選択肢: 'openai', 'local'",
    "file_written": "[ストレージ] 書き込み完了: {path}",
    "outline_multi_draft_title": "\n📋 フェーズ3：マスターアウトライン生成（マルチドラフト比較）",
    "generating_draft": "  ⏳ アウトラインドラフト {num}/{total} を生成中（スタイル：{style}）...",
    "draft_done": "  ✅ ドラフト{num}完了",
    "draft_failed": "  ❌ ドラフト{num}失敗: {error}",
    "draft_comparison_title": "\n📊 アウトラインドラフト比較",
    "draft_header": "\n{'─' * 40}\n📄 ドラフト{num} — スタイル：{style}\n{'─' * 40}",
    "draft_select_prompt": "\n👤 使用するドラフトを選択 (1-{max})、または'm'で各ドラフトの精髄を統合: ",
    "draft_merging": "⏳ 各ドラフトの精髄を統合中...",
    "draft_selected": "✅ ドラフト{num}をマスターアウトラインとして選択",
    "draft_merged": "✅ 統合アウトラインが生成されました",
    "outline_drafts_truncating": "   ⚠️ アウトライン草稿が長すぎます（推定 {total} tokens、予算 {budget}）、各草稿を均等に切り詰めます...",
    "draft_invalid": "無効な選択です。1-{max}または'm'を入力してください",
    "parallel_review_title": "  🔍 並列品質レビューを実行中...",
    "review_consistency": "[一貫性レビュアー]",
    "review_style": "[文体レビュアー]",
    "review_foreshadowing": "[伏線レビュアー]",
    "review_done": "  ✅ {reviewer}: {count}件の問題を発見（信頼度≥{threshold}）",
    "review_failed": "  ⚠️ {reviewer} レビュー失敗: {error}",
    "review_no_issues": "  ✅ 全レビュアー通過 — 重大な問題はありません！",
    "review_issues_found": "  ⚠️ 全レビュアーで合計{count}件の問題を発見:",
    "review_issue_item": "    [{severity}] ({reviewer}, 信頼度: {confidence}) {description}",
    "review_critical_prompt": "  🚨 重大な問題が見つかりました。この章を再執筆しますか？(y/n): ",
    "polish_start": "  ✨ 推敲ループ開始（最大{max_iter}回）...",
    "polish_iteration": "  ✨ 推敲 {iter}/{max_iter}回目...",
    "polish_score": "  📊 品質スコア: {score}/10（閾値: {threshold}）",
    "polish_passed": "  ✅ 品質閾値を達成！推敲ループを終了。",
    "polish_improving": "  ⏳ スコアが閾値未満、改善中...",
    "polish_max_reached": "  ⚠️ 最大推敲回数に達しました。最良版を使用（スコア: {score}/10）。",
    "polish_failed": "  ⚠️ 推敲評価失敗、現在の版を保持。",
    "volume_checkpoint_title": "\n📍 第{num}巻チェックポイント",
    "volume_checkpoint_summary": "  現在の進捗: {completed}章完了、約{words}文字",
    "volume_checkpoint_prompt": "\n👤 第{num}巻を開始します。続行しますか？(y / adjust / stop): ",
    "volume_checkpoint_adjust": "👤 調整メモを入力してください: ",
    "volume_checkpoint_adjusting": "⏳ フィードバックに基づいて巻アウトラインを調整中...",
    "volume_checkpoint_stopped": "⏸️ 第{num}巻の前で停止。次回は第{next}章から再開。",
    "severity_critical": "重大",
    "severity_major": "主要",
    "severity_minor": "軽微",
    "severity_info": "情報",
    "final_summary_title": "\n📊 最終小説サマリーを生成中...",
    "final_summary_done": "✅ 最終サマリーが生成・保存されました！",
    "final_summary_failed": "⚠️ 最終サマリー生成失敗: {error}",

    # -- 執筆パラメータ確認 --
    "writing_params_title": "\n⚙️ 執筆パラメータ確認",
    "ask_chapter_min_words": "   章あたり最小文字数（現在: {current}、Enterでそのまま）: ",
    "ask_chapter_max_words": "   章あたり最大文字数（現在: {current}、Enterでそのまま）: ",
    "writing_params_swapped": "   ⚠️ 最小値 > 最大値のため、値を入れ替えました。",
    "ask_word_count_check": "   文字数チェックを有効にしますか？（現在: {status}、y/n、Enterでそのまま）: ",
    "ask_lazy_mode": "   お任せモード（全自動確認）を有効にしますか？（現在: {status}、y/n、Enterでそのまま）: ",
    "writing_params_summary": "   ✅ 執筆パラメータ: {min}〜{max}文字/章、文字数チェック: {check}、お任せモード: {lazy}",

    # -- 対話の引用符スタイル --
    "quote_style_title": "\n💬 対話の引用符スタイル設定",
    "quote_style_prompt": "\n👤 小説の対話に使用する引用符スタイルを選択してください (1-{max}): ",
    "quote_style_invalid": "無効な選択です。1-{max}を入力してください",
    "quote_style_selected": "✅ 対話の引用符スタイルを設定しました: {style}",
    "quote_style_option_curly": '\u201c\u201d ダブルカーリークォート（例：\u201cこんにちは！\u201d）',
    "quote_style_option_corner": '「」 鉤括弧（例：「こんにちは！」）',
    "quote_style_option_guillemet": '«» ギュメ（例：«こんにちは！»）',
    "quote_style_option_dash": '— ダッシュ式対話（例：— こんにちは！）',
    "quote_style_option_straight": '"" ストレートクォート（例："こんにちは！"）',

    # -- 心理活動の引用符スタイル --
    "inner_quote_title": "\n💭 心理活動・内心独白の引用符スタイル設定",
    "inner_quote_prompt": "\n👤 小説の心理描写に使用するスタイルを選択してください (1-{max}): ",
    "inner_quote_invalid": "無効な選択です。1-{max}を入力してください",
    "inner_quote_selected": "✅ 心理活動の引用符スタイルを設定しました: {style}",
    "inner_quote_option_corner_double": '『』 二重鉤括弧（例：『気をつけなければ』）',
    "inner_quote_option_corner": '「」 鉤括弧（例：「気をつけなければ」）',
    "inner_quote_option_curly_single": '\u2018\u2019 シングルカーリークォート（例：\u2018気をつけなければ\u2019）',
    "inner_quote_option_italic": '*イタリック*で心理描写（例：*気をつけなければ*）',
    "inner_quote_option_dash": '——ダッシュ（例：——気をつけなければ——）',
    "inner_quote_option_paren": '（）全角括弧（例：（気をつけなければ））',
    "inner_quote_option_same": '対話と同じスタイル',
    "inner_quote_option_none": '特殊な記号なし（地の文で心理を描写）',

    # -- 引用符規則（スタイルガイド/ライタープロンプトに注入） --
    "quote_rules_heading": "引用符スタイル規則",
    "quote_rule_dialogue_curly": '全ての対話に\u201c\u201d（ダブルカーリークォート）を使用すること。例：\u201cこんにちは！\u201d',
    "quote_rule_dialogue_corner": '全ての対話に「」（鉤括弧）を使用すること。例：「こんにちは！」',
    "quote_rule_dialogue_guillemet": '全ての対話に«»（ギュメ）を使用すること。例：«こんにちは！»',
    "quote_rule_dialogue_dash": '対話にはダッシュ（—）を使用すること。例：— こんにちは！',
    "quote_rule_dialogue_straight": '全ての対話に""（ストレートクォート）を使用すること。例："こんにちは！"',
    "quote_rule_inner_corner_double": '心理描写/内心独白には『』（二重鉤括弧）を使用すること。例：『気をつけなければ』',
    "quote_rule_inner_corner": '心理描写/内心独白には「」（鉤括弧）を使用すること。例：「気をつけなければ」',
    "quote_rule_inner_curly_single": '心理描写/内心独白には\u2018\u2019（シングルカーリークォート）を使用すること。例：\u2018気をつけなければ\u2019',
    "quote_rule_inner_italic": '心理描写/内心独白には*イタリック*を使用すること。例：*気をつけなければ*',
    "quote_rule_inner_dash": '心理描写/内心独白には——（二重ダッシュ）を使用すること。例：——気をつけなければ——',
    "quote_rule_inner_paren": '心理描写/内心独白には（）（全角括弧）を使用すること。例：（気をつけなければ）',
    "quote_rule_inner_none": '心理描写に特殊な引用符を使用しないこと。地の文で心理を描写すること。',
    "quote_rule_inner_same": '心理描写/内心独白にも対話と同じ引用符を使用すること。',

    # -- おまかせモード --
    "lazy_mode_enabled": "🛋️ おまかせモードON — 大綱確定後は全自動で進行します！",
    "lazy_auto_merge": "🛋️ [おまかせ] 全大綱草稿を自動統合中...",
    "lazy_auto_select": "🛋️ [おまかせ] 草稿が1つのみ、自動選択しました。",
    "lazy_auto_continue": "🛋️ [おまかせ] 自動続行中...",
    "lazy_auto_retry": "🛋️ [おまかせ] 自動リトライ中...",
    "lazy_auto_skip": "🛋️ [おまかせ] 自動スキップ中...",
    "lazy_auto_volume_continue": "🛋️ [おまかせ] 第{num}巻へ自動続行中...",

    # -- レビュー再試行 --
    "review_retry_feedback": """⚠️ 重要：これは{attempt}/{max_attempts}回目の書き直しです。前回のバージョンには以下の重大/主要な問題があり、必ず修正してください：
{issues}

章全体を最初から書き直し、上記のすべての問題を修正しつつ、全体のストーリー、トーン、構成を維持してください。""",
    "review_max_retries_reached": "  ⚠️ 第{num}章のレビュー再試行回数が上限（{max}回）に達しました。現在のバージョンを保存して続行します。",

    # -- 文字数検証 --
    "wordcount_check_start": "  📏 文字数検証：{words}文字（目標：{min}～{max}）",
    "wordcount_too_short": "  ⚠️ 章が短すぎます（{words}文字、最低{min}文字）。拡張中...",
    "wordcount_too_long": "  ⚠️ 章が長すぎます（{words}文字、最大{max}文字）。圧縮中...",
    "wordcount_split_needed": "  📑 章が大幅に超過（{words}文字、≧{threshold}%上限）。2章に分割中...",
    "wordcount_expand_done": "  ✅ 拡張完了：{words}文字",
    "wordcount_compress_done": "  ✅ 圧縮完了：{words}文字",
    "wordcount_split_done": "  ✅ 分割完了：第{num_a}章（{words_a}文字）+ 第{num_b}章（{words_b}文字）",
    "wordcount_retry": "  🔄 文字数検証リトライ {attempt}/{max_attempts}...",
    "wordcount_give_up": "  ⚠️ {max_attempts}回リトライ後も未達。現行版を使用（{words}文字）。",
    "wordcount_ok": "  ✅ 文字数OK：{words}文字",
    "wordcount_split_renumber": "  📝 注意：分割後の後続章は自動的に再番号付けされます。",


    # -- Feature #1: Multi-draft outline styles --
    "outline_style_dramatic": "ドラマチック・高テンション型",
    "outline_style_literary": "文学・キャラクター重視型",
    "outline_style_commercial": "商業・テンポ重視型",
})

# ============================================================
# PROMPTS: LLMプロンプトテンプレート（日本語完全翻訳）
# ============================================================
PROMPTS = dict(_BASE_PROMPTS)
PROMPTS.update({
    # -- 企画エージェント --
    "planner_system": """あなたは経験豊富な小説企画編集者です。ゼロから小説の核心設定を構想することに長けています。
ユーザーとの会話を通じて、以下の小説の核心要素を決定するための十分な情報を収集することが任務です：

1. **ジャンル/タイプ**：ファンタジー、現代、ミステリー、恋愛、SF等
2. **核心テーマ**：小説が何を表現するか
3. **目標文字数と構成**：総文字数、各章の文字数、予想章数、巻数
4. **語りの視点**：一人称/三人称
5. **核心タグ**：3-5個のキーワード
6. **一行あらすじ**：全書を要約する一文
7. **三幕構成あらすじ**：起承結の概要
8. **文体要件**：文体、基調、参考作品
9. **禁忌事項**：含めてはならない内容
10. **主要キャラクター**：少なくとも主人公の基本設定
11. **世界観フレームワーク**：物語が展開する世界の背景

ユーザーに積極的に質問してこれらの情報を集めてください。ユーザーが自分で決めたくない部分は、あなたが創造的に補完してください。
情報が十分だと判断したら、最終的な小説企画書を出力してください。

注意：
- 一度に2-3個の関連する質問のみ
- ユーザーの回答に基づいて柔軟にフォローアップ
- 各要素について、ユーザーが自分で指定したいか、あなたに任せたいか明確に確認
- フレンドリーでプロフェッショナルな会話スタイルを維持""",

    "planner_first_question": """こんにちは！小説企画アシスタントです~ 🎉

創作を始める前に、あなたのアイデアを聞かせてください。一歩ずつ進めましょう：

**まず、最も基本的な質問：**
1. どの**ジャンル/タイプ**の小説を書きたいですか？（例：ファンタジー、現代、ミステリー、SF、恋愛、歴史等）
2. 大まかな**ストーリーの方向性**や**核心アイデア**はありますか？漠然とした考えでも大丈夫です
3. これらの基本設定はご自分で指定しますか、それとも私にブレインストーミングをお任せしますか？

お気軽にお話しください~""",

    "planner_check_enough": """これまでに収集した全情報を分析し、企画を開始するのに十分かどうか判断してください。

核心要素チェックリスト：
1. ジャンル/タイプ - {has_genre}
2. 核心テーマ - {has_theme}
3. 目標文字数と構成 - {has_structure}
4. 語りの視点 - {has_pov}
5. 核心タグ - {has_tags}
6. 一行あらすじ - {has_summary}
7. 文体要件 - {has_style}
8. 主要キャラクター（少なくとも主人公の概念）- {has_characters}
9. 世界観フレームワーク - {has_world}

JSON形式で回答してください：
{{
    "is_enough": true/false,
    "missing_items": ["不足している要素のリスト"],
    "next_questions": "情報が不足している場合、次にユーザーに質問する内容（2-3個）"
}}

JSONのみ返答してください。""",

    "planner_summarize": """以下の会話で収集した情報に基づいて、完全な小説企画書を生成してください。
ユーザーが明示的に指定していない部分は、創造的に補完し、全体の企画が一貫して魅力的になるようにしてください。

以下のJSON形式で厳密に出力してください。他の内容は不要です：
{{
    "title": "書名",
    "genre": "ジャンル/タイプ",
    "theme": "核心テーマ（一段落）",
    "target_words": "目標総文字数",
    "chapter_words": "各章の文字数範囲",
    "total_chapters": "予想総章数",
    "volumes": "巻数と分割",
    "pov": "語りの視点",
    "tags": "核心タグ（カンマ区切り）",
    "one_line_summary": "一行あらすじ",
    "three_act_summary": {{
        "beginning": "起（開始の概要）",
        "middle": "承（展開の概要）",
        "end": "結（結末の概要）"
    }},
    "style_guide": "文体要件と執筆規範",
    "taboos": "禁忌事項",
    "main_characters": [
        {{
            "name": "名前",
            "role": "役割（主人公/敵役/脇役等）",
            "age": "年齢",
            "appearance": "外見描写",
            "personality": "性格描写",
            "background": "背景ストーリー",
            "motivation": "核心動機",
            "arc": "キャラクターアーク/成長軌跡"
        }}
    ],
    "world_setting": "世界観フレームワーク描写",
    "synopsis": "小説あらすじ（公開用）"
}}""",

    # -- アウトラインエージェント --
    "outline_system": """あなたは経験豊富な小説アウトラインプランナーです。与えられた小説企画書に基づいて、詳細なプロットアウトラインを作成します。

出力内容：
1. 全書の巻レベルアウトライン（各巻の主要プロット、核心対立、主要イベント、クライマックスと引き）
2. キャラクター関係図のテキスト描写

Markdown形式で出力してください。以下を確保：
- 各巻のアウトラインに明確な主要プロットと主要イベントリストを含む
- 巻と巻の間に明確な因果関係の接続がある
- キャラクターの成長アークが全体を貫く
- 伏線とサスペンスが合理的に設計されている
- テンポに緩急がある""",

    "volume_outline_system": """あなたはプロットの詳細化に長けた小説アウトライン専門家です。
マスターアウトラインの巻の概要に基づいて、詳細な章レベルのアウトラインを作成します。

Markdown形式で出力してください。各章に必要な内容：
- 章タイトル
- 主要イベント（3-5個の重要ポイント）
- 登場キャラクター
- 感情のトーン/雰囲気
- 伏線（設置/回収）
- 前後のつながり""",

    # -- 世界観エージェント --
    "worldbuilding_system": """あなたはプロの世界観構築専門家です。与えられた小説企画書に基づいて、詳細な世界設定ドキュメントを作成する必要があります。

Markdown形式で出力してください。カバーすべき内容：
1. 世界の全体設定（時代背景、社会構造、技術/魔法レベル等）
2. 地理/空間設定（重要な場所とその特徴）
3. 特殊システム設定（修行体系/魔法体系/技術体系等、ジャンルに応じて）
4. 大事件年表（物語開始前の重要な歴史的事件）

設定が相互に一貫し、矛盾がないことを確保してください。""",

    "character_system": """あなたはキャラクター造形に長けたキャラクターデザイン専門家です。与えられた小説企画書と世界設定に基づいて、詳細なキャラクタープロフィールを作成する必要があります。

各キャラクターに必要な内容：
- 基本情報（名前、年齢、外見等）
- 性格描写（多層的、外面の行動と内面の性格を含む）
- 背景ストーリー
- 能力/特技
- 目標/動機
- 話し方/口癖
- キャラクターアーク（成長軌跡）
- キャラクター関係

Markdown形式で出力してください。キャラクター間に化学反応があり、性格が補完または対立するようにしてください。""",

    # -- 執筆エージェント --
    "writer_system": """あなたは才能豊かなWeb小説作家です。
提供された設定、アウトライン、コンテキストに基づいて、小説本文を執筆します。

執筆要件：
{style_guide}

構成要件：
- 各章 {min_words}-{max_words} 文字
- 章にはフック開始が必要（前章との接続や新たなサスペンスの創出）
- 核心プロットの推進（少なくとも1つの主要イベント）
- 結末のフック（読者を引き続き読ませるため）

以下の形式を厳守してください：
- 章タイトル形式：第X章 タイトル
- 本文を直接出力し、メタ情報やノートは出力しないでください""",

    "writer_chapter_prompt": """以下の情報に基づいて、第{chapter_num}章の本文を執筆してください。

## 本章のアウトライン
{chapter_outline}

## 最近の章の要約（連続性の維持のため）
{recent_briefs}

## 現在のキャラクター状態
{character_status}

## 注意すべき伏線
{hooks_info}

## キャラクタープロフィール（公式設定 — 名前は必ず正確に一致させてください）
{character_profiles}

## 世界観と場所の設定（公式設定 — 全ての地名、勢力名等は必ず正確に一致させてください）
{world_setting}

⚠️ 重要警告：全てのキャラクター名、地名、勢力/門派名、及び固有名詞は、上記のキャラクタープロフィールと世界観設定に完全に一致させてください。いかなる名前も勝手に創作、変更、代替しないでください。

完全な章の本文（{min_words}-{max_words}文字）を「第{chapter_num}章」から始めて出力してください。""",

    # -- 後処理エージェント --
    "post_write_system": """あなたは細心の小説編集アシスタントです。各章の執筆後に、章の内容を分析し、以下の更新情報を生成することが任務です。

JSON形式で出力してください：
{{
    "chapter_brief": {{
        "chapter_num": 章番号,
        "title": "章タイトル",
        "word_count": 概算文字数,
        "main_events": ["主要イベント1", "主要イベント2", ...],
        "character_changes": ["キャラクター状態変更1", ...],
        "hooks_planted": ["新たに設置した伏線1", ...],
        "hooks_resolved": ["回収した伏線ID1", ...],
        "next_chapter_hook": "次章へのフック"
    }},
    "progress_update": {{
        "latest_chapter": "第X章·タイトル",
        "total_words": 概算累計文字数,
        "character_status": {{
            "キャラクター名": "現在の状態描写"
        }}
    }}
}}

JSONのみ返答してください。""",

    # -- スタイルガイドエージェント --
    "style_guide_system": """あなたは文体ガイドラインの策定を専門とする文学コンサルタントです。
与えられた小説企画書に基づいて、詳細な文体ガイドドキュメントを生成します。

Markdown形式で出力してください。含めるべき内容：
1. 語りの視点ガイドライン
2. 文体要件（全体的な基調、内面独白のスタイル、外面表現のスタイル等）
3. 章構成ガイドライン
4. 対話ガイドライン（対話形式、キャラクターの話し方）
5. 描写ガイドライン（戦闘/感情/環境等各種描写の要件）
6. テンポ制御の提案
7. 核心執筆原則
8. 禁忌事項""",

    # -- 世界観タスクプロンプト --
    "task_world_setting": """以下の小説企画書に基づいて、世界の全体設定ドキュメントを作成してください（Markdown形式）。
含めるべき内容：時代背景、社会構造、重要な勢力/組織等の基礎的な世界観。

企画書：
{plan_text}""",

    "task_characters": """以下の小説企画書に基づいて、詳細なキャラクタープロフィールドキュメントを作成してください（Markdown形式）。
参考形式要件：各キャラクターに名前、年齢、外見、性格（多層的）、背景、能力、動機、口癖、キャラクターアークを含む。
最後にキャラクター関係図（テキスト描写）を付けてください。

企画書：
{plan_text}""",

    "task_locations": """以下の小説企画書に基づいて、重要な場所/シーン設定ドキュメントを作成してください（Markdown形式）。
物語に登場する全ての重要な場所とその特徴描写を含めてください。

企画書：
{plan_text}""",

    "task_timeline": """以下の小説企画書に基づいて、大事件年表ドキュメントを作成してください（Markdown形式）。
物語開始前の重要な歴史的事件と、物語中のタイムライン計画を含めてください。

企画書：
{plan_text}""",

    "task_power_system": """以下の小説企画書に基づいて、力/修行体系設定ドキュメントを作成してください（Markdown形式）。
含めるべき内容：等級区分、修行方法、特殊能力体系等の詳細設定。

企画書：
{plan_text}""",

    "task_tech_system": """以下の小説企画書に基づいて、技術体系設定ドキュメントを作成してください（Markdown形式）。
含めるべき内容：技術レベル、主要技術、特殊装置等の詳細設定。

企画書：
{plan_text}""",

    # -- アウトライン生成プロンプト --
    "master_outline_prompt": """以下の小説企画書に基づいて、全書のマスターアウトラインを作成してください。

## 小説企画書
{plan_json}

全巻を網羅するマスターアウトライン（Markdown形式）を生成してください。各巻に必要な内容：
- 主要プロットの描写
- 核心対立
- 主要イベント（番号付きリスト）
- 主要キャラクターの状態
- 巻のクライマックス
- 巻の引き
- 次巻との接続""",

    "volume_outline_prompt": """以下の情報に基づいて、第{volume_num}巻の詳細な章レベルアウトラインを作成してください。

## 小説企画書要約
- タイトル：{title}
- ジャンル：{genre}
- 各章の文字数：{chapter_words}

## マスターアウトラインにおけるこの巻の描写
{volume_info}

## マスターアウトライン（完全版、全体把握用）
{master_outline}

この巻の詳細な章レベルアウトラインを生成してください。各章に含むべき内容：
- 章番号とタイトル
- 主要イベント（3-5個）
- 登場キャラクター
- 感情のトーン
- 伏線（設置/回収）
- 前後のつながり""",

    # -- 後処理プロンプト --
    "analyze_chapter_prompt": """以下の小説の章を分析し、要約と更新情報を生成してください。

## 章のアウトライン（参考）
{chapter_outline}

## 章の本文
{chapter_text}

指定されたJSON形式で厳密に出力してください。""",

    # -- 企画修正 --
    "plan_revision_request": "企画書に対して以下の修正意見があります：{feedback}\nこれに基づいて企画書を調整してください。",

    # -- ジャンル検出キーワード --
    "genre_fantasy_keywords": ["ファンタジー", "修行", "仙術", "魔法", "異世界"],
    "genre_scifi_keywords": ["SF", "未来", "サイバー", "宇宙", "テクノロジー"],


    "outline_merge_prompt": """以下は同じ小説の{count}個の異なるスタイルのマスターアウトラインです。

以下の要件で**統合マスターアウトライン**を作成してください：
1. 各ドラフトから最も強い構造的要素を取り入れる
2. 最良のプロットアイデアとキャラクターアークを融合する
3. 全体を通じて論理的一貫性を維持する
4. 最も魅力的な伏線設計とクライマックス配置を保持する

{drafts_text}

Markdown形式で統合後のマスターアウトラインを出力してください。""",

    # -- 機能 #2: 並列レビューシステムプロンプト --
    "consistency_reviewer_system": """あなたは小説の緻密な連続性エディターです。
あなたの任務は、章の内容が前の章、アウトライン、および提供されたキャラクタープロフィールと一貫しているかを審査することです。

チェック項目：
1. **キャラクター名の正確性**：章中に登場するすべてのキャラクター名をキャラクタープロフィールと照合してください。プロフィールと完全に一致しない名前（誤字、名前の間違い、名前の入れ替え、呼称の不一致）をすべてフラグしてください。これは最優先のチェック項目です。
2. **キャラクター特性の一貫性**：各キャラクターの行動、話し方、能力、性格がプロフィールと一致しているか検証してください。
3. タイムラインと時系列の正確性
4. 場面/場所の一貫性
5. プロットの連続性（参照されたイベントが実際に起こったか）
6. キャラクター知識の一貫性（キャラクターがまだ知らないはずの情報を知っていないか）

発見した問題ごとに、確信度スコア（0-100）を付けてください：
- 0-25: 不確実、意図的かもしれない
- 26-50: 問題の可能性あり、主観的判断かもしれない
- 51-75: おそらくエラー、要確認
- 76-100: 確実なエラー、原典と照合済み

JSON形式で出力：
{{
    "issues": [
        {{
            "type": "consistency",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "問題の説明",
            "location": "章内のおおよその位置",
            "suggestion": "修正方法"
        }}
    ],
    "overall_consistency_score": 1-10
}}

JSONのみ返答してください。""",

    "style_reviewer_system": """あなたは文学スタイル審査の専門家です。
あなたの任務は、章の内容が文体ガイドに準拠しているかを審査することです。

チェック項目：
1. 視点の一貫性（意図しない視点の切り替えがないか）
2. トーンとムードがスタイルガイドと一致しているか
3. 対話スタイルがキャラクタープロフィールと一致しているか
4. テンポの問題（急ぎすぎ、またはだらだらしすぎ）
5. 文章の品質（ぎこちない表現、重複する言葉等）

発見した問題ごとに、確信度スコア（0-100）を付けてください。

JSON形式で出力：
{{
    "issues": [
        {{
            "type": "style",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "問題の説明",
            "location": "章内のおおよその位置",
            "suggestion": "修正方法"
        }}
    ],
    "overall_style_score": 1-10
}}

JSONのみ返答してください。""",

    "foreshadowing_reviewer_system": """あなたは伏線とプロット連続性の専門家です。
あなたの任務は、章における伏線要素の取り扱いを審査することです。

チェック項目：
1. 設置された伏線が十分に巧みか（あからさますぎないか）？
2. 以前に設置したフックが適切なタイミングで進展または回収されているか？
3. アウトラインに基づき、見逃されている伏線の機会はないか？
4. 回収された伏線は満足感があるか？
5. 章の結末は次章への十分なサスペンスを生み出しているか？

発見した問題ごとに、確信度スコア（0-100）を付けてください。

JSON形式で出力：
{{
    "issues": [
        {{
            "type": "foreshadowing",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "問題の説明",
            "location": "章内のおおよその位置",
            "suggestion": "修正方法"
        }}
    ],
    "overall_foreshadowing_score": 1-10
}}

JSONのみ返答してください。""",

    "review_chapter_prompt": """以下の章を審査してください。

## キャラクタープロフィール（名前と特徴の照合用権威参照）
{character_profiles}

## スタイルガイド
{style_guide}

## 章のアウトライン
{chapter_outline}

## 最近の章の要約
{recent_briefs}

## 伏線トラッカー
{hooks_info}

## 章の本文
{chapter_text}

重要：章の本文中のすべてのキャラクター名を上記のキャラクタープロフィールと照合してください。名前の不一致は重大な問題です。

指定されたJSON形式で審査結果を出力してください。""",
    # -- 機能 #3: 推敲ループプロンプト --
    "polish_evaluate_system": """あなたは上級小説編集者です。以下の章の品質を1-10で評価してください。

評価基準：
1. 文章の品質と読みやすさ
2. キャラクターの声の一貫性
3. テンポと流れ
4. 感情的インパクト
5. フックの強さ（開始と結末）
6. アウトラインとの整合性

JSON形式で出力：
{{
    "score": 1-10,
    "strengths": ["長所1", "長所2"],
    "weaknesses": ["短所1", "短所2"],
    "specific_improvements": [
        {{
            "location": "テキスト内の場所",
            "current": "現在の問題テキスト（概要）",
            "suggested": "改善方法"
        }}
    ]
}}

JSONのみ返答してください。""",

    "polish_evaluate_prompt": """この章の品質を評価してください。

## スタイルガイド
{style_guide}

## 章のアウトライン
{chapter_outline}

## 章の本文
{chapter_text}

JSON形式で評価結果を出力してください。""",

    "polish_improve_system": """あなたは才能豊かな小説作家で、改訂を行っています。
章とエディターからの具体的な改善提案を受け取ります。
改善を取り入れて章全体を書き直してください。全体のストーリー、トーン、構成は保持してください。

メタコメントは一切追加しないでください — 改訂後の章の本文のみを出力してください。""",

    "polish_improve_prompt": """エディターのフィードバックに基づいて、以下の章を改訂してください。

## エディターのフィードバック
短所：{weaknesses}

具体的な改善提案：
{improvements}

## 現在の章の本文
{chapter_text}

完全な改訂後の章の本文を出力してください。""",

    # -- 機能 #4: 巻間チェックポイント調整 --
    "volume_adjust_prompt": """読者が第{volume_num}巻に対して以下のフィードバック/調整を提出しました。

フィードバック：{feedback}

現在の巻アウトライン：
{volume_outline}

読者のフィードバックを取り入れつつ、マスターアウトラインとの一貫性を維持して巻アウトラインを修正してください。

Markdown形式で修正後の巻アウトラインを出力してください。""",

    # -- 文字数検証プロンプト --
    "expand_chapter_system": """あなたは才能豊かな小説家です。文字数が不足している章を受け取り、拡充する必要があります。
品質を維持しながら、目標文字数に達するよう章を拡充してください。水増し的な内容は入れないでください。

拡充戦略：
- より詳細な描写を追加（環境、感情、五感の描写）
- 会話のやり取りを拡張し、自然な対話を増やす
- キャラクターの内面独白や反応を追加
- アクションシーンをより詳細に、生き生きと描写
- 雰囲気を醸成する場面転換を追加

重要：完成した拡充後の章の本文のみを出力してください。メタ情報やコメントは出力しないでください。""",

    "expand_chapter_prompt": """以下の章は文字数が不足しています（{current_words}文字）。約{target_words}文字に拡充してください。

## 文体ガイド
{style_guide}

## 章のアウトライン
{chapter_outline}

## 現在の章の本文（短すぎ）
{chapter_text}

完成した拡充後の章の本文（{target_words}文字以上）を出力してください。""",

    "compress_chapter_system": """あなたは経験豊富な小説編集者です。文字数が超過している章を受け取り、圧縮する必要があります。
すべての重要なプロットポイントとキャラクターの瞬間を保持しながら章を圧縮してください。

圧縮戦略：
- 文章を洗練させ、冗長な描写を除去
- 重複する会話を統合
- 重要でない場面転換を要約
- プロットを進展させない内容を除去
- アクションシーンを簡潔にする

重要：すべての重要なプロットイベント、キャラクター発展、伏線は必ず保持してください。
完成した圧縮後の章の本文のみを出力してください。メタ情報やコメントは出力しないでください。""",

    "compress_chapter_prompt": """以下の章は文字数が超過しています（{current_words}文字）。約{target_words}文字に圧縮してください。

## 文体ガイド
{style_guide}

## 章のアウトライン（すべての重要イベントを保持）
{chapter_outline}

## 現在の章の本文（長すぎ）
{chapter_text}

完成した圧縮後の章の本文（約{target_words}文字）を出力してください。すべての重要なプロットポイントを保持してください。""",

    "split_chapter_system": """あなたは経験豊富な小説編集者です。大幅に超過した章を受け取り、二つの章に分割する必要があります。
自然な物語の区切りを見つけて章を分割してください。分割後の各章は：
- 独自のドラマチックアーク（導入 → 展開 → フック的結末）を持つこと
- 大体同じ長さであること
- 自然なクリフハンガーや転換点で終わること

出力形式：二つの章の間に正確に "===CHAPTER_SPLIT===" という区切り行を使用。
各章は章タイトル行で始めること。

重要：===CHAPTER_SPLIT=== で区切られた二つの章の本文のみを出力してください。メタコメントは不要です。""",

    "split_chapter_prompt": """以下の章は大幅に超過しています（{current_words}文字、章ごとの目標：{min_words}〜{max_words}文字）。二つの章に分割してください。

## 文体ガイド
{style_guide}

## 元の章のアウトライン
{chapter_outline}

## 現在の章の本文（分割対象）
{chapter_text}

構造が完全な二つの章に分割してください。"===CHAPTER_SPLIT===" を区切りとして使用。
第{chapter_num_a}章が前半、第{chapter_num_b}章が後半です。
各章約{target_words}文字。""",

    # -- 機能 #6: 最終サマリープロンプト --
    "final_summary_system": """あなたは文学アナリストです。完成した小説の包括的なサマリーレポートを生成してください。

Markdown形式で出力してください。含めるべき内容：
1. **小説概要** — タイトル、ジャンル、最終文字数、章数
2. **プロット要約** — 完全なストーリー概要（ネタバレあり）
3. **キャラクターアーク分析** — 各主要キャラクターの成長変化
4. **テーマ分析** — 核心テーマとその展開方法
5. **統計概要** — 各章の文字数、平均文字数、最長/最短章
6. **伏線回収レポート** — どの伏線が設置され回収されたか
7. **執筆品質メモ** — 全体的な文章品質、注目すべきシーン
8. **続編の可能性** — 継続可能なオープンスレッド""",

    "final_summary_prompt": """この完成した小説の包括的な最終サマリーを生成してください。

## 小説企画書
{plan_json}

## 章の要約
{all_briefs}

## キャラクタープロフィール
{characters}

## 伏線トラッカー
{hooks_info}

## 統計データ
- 総章数：{total_chapters}
- 総文字数：約{total_words}文字

Markdown形式で完全なサマリーレポートを生成してください。""",
})

# ============================================================
# TEMPLATES: Markdownテンプレート（日本語完全翻訳）
# ============================================================
TEMPLATES = dict(_BASE_TEMPLATES)
TEMPLATES.update({
    "readme": """# 📖 長編小説創作プロジェクト

## 基本情報
- **タイトル**：「{title}」
- **ジャンル**：{genre}
- **目標文字数**：{target_words}
- **各章の文字数**：{min_words}-{max_words}文字
- **予想総章数**：{total_chapters}
- **巻数**：{volumes}
- **語りの視点**：{pov}
- **核心タグ**：{tags}

## 一行あらすじ
{one_line_summary}

## 📁 ディレクトリ構成

```
{title}/
├── README.md              # プロジェクト概要
├── meta/                  # メタ情報管理
│   ├── progress.md        # 執筆進捗トラッカー
│   ├── style_guide.md     # 文体ガイド
│   └── hooks_tracker.md   # 伏線トラッカー
├── worldbuilding/         # 世界観設定
│   ├── characters.md      # キャラクタープロフィール
│   ├── world_setting.md   # 世界観設定概要
│   └── ...                # その他の設定ファイル
├── plot/                  # プロット管理
│   ├── master_outline.md  # マスターアウトライン
│   ├── volume_XX.md       # 各巻アウトライン
│   └── chapter_briefs.md  # 章要約記録
└── chapters/              # 本文出力
    ├── chapter_001.txt    # 第1章
    └── ...
```

## 🔄 執筆ワークフロー
1. progress.md を読む → 現在の進捗確認
2. chapter_briefs.md を読む → 最近の章を振り返る
3. 現在の巻アウトラインを参照 → 本章の内容を確認
4. hooks_tracker.md を確認 → 伏線の状態を確認
5. characters.md を参照 → キャラクターの状態を確認
6. 本文を chapters/ に出力
7. progress.md、chapter_briefs.md 等を更新
""",

    "progress": """# 📊 執筆進捗トラッカー

## 現在の状態
- **最新完了章**：まだ開始していません
- **現在執筆中**：未定
- **現在の巻**：第1巻
- **総文字数**：0
- **最終更新**：-

## 次のステップ
> 1. ~~小説のジャンル/タイプを決定~~ ✅
> 2. ~~核心設定と主人公~~ ✅
> 3. ~~マスターアウトライン~~ ✅
> 4. **第1巻アウトラインを完成** ← 現在
> 5. 本文執筆開始

## 完了章一覧

| 章 | タイトル | 約文字数 | 核心イベント |
|---|---------|---------|------------|

## 現在のキャラクター状態クイックリファレンス
（更新待ち）

## TODO
- [x] 小説のジャンルを決定
- [x] 世界観設定を完成
- [x] キャラクター設定を完成
- [x] マスターアウトラインを完成
- [ ] 第1巻アウトラインを完成
- [ ] 第1章本文
""",

    "hooks_tracker": """# 🎣 伏線/フックトラッカー

> すべての伏線とサスペンスを記録し、状態を追跡
> 状態：🔴 設置済み未回収 | 🟡 一部開示 | 🟢 回収済み | ⚪ 計画中

---

## 長期伏線（巻をまたぐ）

| ID | 内容 | 設置章 | 回収予定 | 状態 | メモ |
|----|------|--------|---------|------|------|

## 短期伏線（現在の巻内）

| ID | 内容 | 設置章 | 回収予定 | 状態 | メモ |
|----|------|--------|---------|------|------|

## 回収記録

| ID | 内容 | 設置章 | 回収章 | メモ |
|----|------|--------|--------|------|
""",

    "chapter_briefs": """# 📝 章要約記録

> 各章執筆後に要約を記録、プロットの素早い振り返り用
> 形式：章 | タイトル | 文字数 | 主要イベント | キャラクター変化 | 伏線

---
""",

    "synopsis_title": "# 小説あらすじ\n\n",

    "chapter_brief_entry": """
### 第{chapter_num}章 · {title}（約{word_count}文字）
**主要イベント**：
""",
    "character_changes_header": "\n**キャラクター状態変更**：\n",
    "hooks_planted_header": "\n**新規伏線**：\n",
    "next_hook_prefix": "\n**次章へのフック**：",

    "progress_update_entry": """
---
### 第{chapter_num}章完了更新
- **最新完了**：{latest_chapter}
- **累計文字数**：約{total_words}文字
""",
    "character_status_header": "\n**キャラクター状態クイックリファレンス**：\n",

    "final_summary_filename": "meta/final_summary.md",
})

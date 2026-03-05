"""
Tiếng Việt locale
"""
from locales.en import UI as _BASE_UI, PROMPTS as _BASE_PROMPTS, TEMPLATES as _BASE_TEMPLATES

UI = dict(_BASE_UI)
UI.update({
    "welcome_title": "📖 Novel Agent Workflow v1.0",
    "welcome_subtitle": "   Hệ thống viết tiểu thuyết tự động bằng AI",
    "no_backend": "\n❌ Không có backend LLM nào khả dụng!",
    "no_backend_hint": "   Hãy đảm bảo ít nhất một trong llm_openai.py hoặc llm_local.py tồn tại",
    "select_api_mode": "\n🔌 Chọn chế độ LLM API:",
    "api_openai_desc": "Định dạng chuẩn OpenAI (cần API Key)",
    "api_local_desc": "API stream-server cục bộ",
    "auto_selected": "\n  (Chỉ phát hiện {desc}, đã tự động chọn)",
    "input_choice": "\n👤 Nhập lựa chọn (1-{max}): ",
    "invalid_choice": "Lựa chọn không hợp lệ, vui lòng nhập 1-{max}",
    "input_openai_key": "Nhập OpenAI API Key: ",
    "api_key_empty": "API Key không được để trống!",
    "input_base_url": "API Base URL (nhấn Enter dùng mặc định: {default}): ",
    "input_model": "Tên model (nhấn Enter dùng mặc định: {default}): ",
    "input_local_url": "Nhập địa chỉ API cục bộ: ",
    "api_url_empty": "Địa chỉ API không được để trống!",
    "input_api_key": "Nhập API Key (nhấn Enter để bỏ qua): ",
    "input_wsid": "Nhập WSID (nhấn Enter để bỏ qua): ",
    "input_model_marker": "Nhập model marker (nhấn Enter để bỏ qua): ",
    "project_setup": "\n📁 Thiết lập dự án",
    "input_novel_name": "👤 Nhập tên dự án tiểu thuyết (dùng để tạo thư mục): ",
    "scan_projects_header": "\n📂 Phát hiện các dự án hiện có:",
    "no_existing_projects": "\n📂 Không tìm thấy dự án nào.",
    "project_status_chapters": "{count} chương",
    "project_status_plan": "kế hoạch",
    "project_status_meta": "metadata",
    "project_status_plot": "đề cương",
    "or_input_manually": "Nhập tên dự án thủ công...",
    "select_project_prompt": "\n👤 Chọn dự án (1-{max}): ",
    "select_operation": "\n🎯 Chọn thao tác:",
    "op_full": "  1. Bắt đầu từ đầu (quy trình đầy đủ)",
    "op_resume": "  2. Tiếp tục từ điểm dừng",
    "op_planning": "  3. Chỉ giai đoạn lập kế hoạch",
    "op_worldbuilding": "  4. Chỉ tạo thế giới quan & hướng dẫn phong cách",
    "op_outline": "  5. Chỉ tạo đề cương",
    "op_writing": "  6. Chỉ viết (cần có đề cương sẵn)",
    "op_batch": "  7. Chế độ hàng loạt (tạo nhiều tiểu thuyết liên tiếp)",
    "input_op_choice": "\n👤 Nhập lựa chọn (1-7): ",
    "invalid_op": "Lựa chọn không hợp lệ, vui lòng nhập 1-7",
    "input_volume_num": "Tạo đề cương chi tiết cho tập mấy? (nhập số, hoặc Enter để bỏ qua): ",
    "input_start_chapter": "Bắt đầu từ chương mấy? (Enter từ chương 1): ",
    "input_end_chapter": "Viết đến chương mấy? (Enter viết đến hết): ",
    "interrupted": "\n\n⏸️ Người dùng đã ngắt. Tiến trình đã được lưu. Lần sau chọn 'Tiếp tục từ điểm dừng'.",
    "error_occurred": "\n❌ Đã xảy ra lỗi: {error}",
    "goodbye": "\n👋 Tạm biệt!",

    # -- Chế độ hàng loạt --
    "batch_input_names": "\n📚 Nhập tên các tiểu thuyết, phân cách bằng dấu phẩy (ví dụ: truyenA, truyenB, truyenC):",
    "batch_empty": "❌ Không có tên tiểu thuyết nào, quay về menu chính.",
    "batch_select_op": "\n🎯 Chọn thao tác cho mỗi tiểu thuyết:",
    "batch_start": "\n🚀 Chế độ hàng loạt: sẽ tạo {total} tiểu thuyết theo thứ tự: {names}",
    "batch_progress": "📖 [{current}/{total}] Bắt đầu tiểu thuyết: {name}",
    "batch_novel_done": "✅ Tiểu thuyết '{name}' hoàn thành!",
    "batch_interrupted": "\n⏸️ Bị gián đoạn khi viết '{name}'. Còn {remaining} tiểu thuyết chưa hoàn thành.",
    "batch_continue_prompt": "Tiếp tục với các tiểu thuyết còn lại? (y/n): ",
    "batch_stopped": "🛑 Đã dừng chế độ hàng loạt.",
    "batch_novel_error": "\n❌ Lỗi khi tạo tiểu thuyết '{name}': {error}",
    "batch_all_done": "\n🎉 Hoàn tất! Tất cả {total} tiểu thuyết đã được tạo xong.",

    "select_language": "\n🌐 Chọn ngôn ngữ cho tiểu thuyết:",
    "lang_choice_prompt": "\n👤 Nhập lựa chọn (1-{max}): ",
    # -- Continue from existing chapters (integrated in option 1) --
    "ask_existing_chapters": "\n\U0001f4dd Bạn đã viết sẵn chương nào chưa? (y/n, Enter = chưa): ",
    "ask_chapter_count": "📚 Bạn đã viết bao nhiêu chương? Nhập số: ",
    "ask_chapter_count_invalid": "❌ Vui lòng nhập số nguyên dương hợp lệ.",
    "created_empty_chapters": "\n\U0001f4c2 Đã tạo {count} file chương trống tại:\n   {path}\n",
    "created_empty_chapter_item": "   📄 {filename}",
    "checking_filled_chapters": "\n\U0001f50d Đang kiểm tra các file chương đã điền...",
    "filled_chapter_ok": "   ✅ Chương {num}: {words} từ",
    "filled_chapter_empty": "   ⚠️ Chương {num}: trống (sẽ bỏ qua)",
    "all_chapters_empty": "❌ Tất cả file chương đều trống. Tiếp tục theo quy trình bình thường.",
    "skipping_chapter_writing": "\n⏩ Chương {num}: đã có sẵn, bỏ qua việc viết...",
    "running_post_process_existing": "   🔄 Đang chạy hậu xử lý (theo dõi mạch truyện, cập nhật tóm tắt) cho chương {num}...",
    "existing_chapters_processed": "\n✅ Đã xử lý xong {count} chương đã có. Bắt đầu viết AI từ chương {next}.",
    "wait_fill_chapters": "\n✍️ Hãy dán nội dung các chương đã viết vào các file trên.\n   Khi xong, nhấn Enter để tiếp tục...",

    "phase_planning_title": "\n📝 Giai đoạn 1: Lập kế hoạch tiểu thuyết",
    "planner_prefix": "\n🤖 Trợ lý kế hoạch:\n",
    "user_prefix": "👤 Bạn: ",
    "input_empty_hint": "(Vui lòng nhập câu trả lời)",
    "multiline_hint": "(Hỗ trợ nhập nhiều dòng, nhập dòng trống để kết thúc. Gõ /paste để vào chế độ dán)",
    "multiline_paste_hint": "(Chế độ dán: tự do dán nội dung có dòng trống, gõ /end để kết thúc)",
    "quit_planning": "Đã thoát giai đoạn lập kế hoạch.",
    "force_done": "Được rồi, để tôi tổng hợp kế hoạch...",
    "generating_plan": "\n⏳ Đang tạo kế hoạch tiểu thuyết hoàn chỉnh...",
    "plan_display_title": "\n📋 Kế hoạch tiểu thuyết",
    "plan_label_title": "Tên sách",
    "plan_label_genre": "Thể loại",
    "plan_label_theme": "Chủ đề cốt lõi",
    "plan_label_target_words": "Số từ mục tiêu",
    "plan_label_total_chapters": "Số chương dự kiến",
    "plan_label_volumes": "Số tập",
    "plan_label_pov": "Góc nhìn",
    "plan_label_tags": "Thẻ",
    "plan_label_one_line": "Tóm tắt một câu",
    "plan_label_beginning": "Mở đầu",
    "plan_label_middle": "Phát triển",
    "plan_label_end": "Kết thúc",
    "plan_label_characters": "Nhân vật chính",
    "confirm_plan": "\n👤 Bạn hài lòng với kế hoạch này? (y/ghi chú chỉnh sửa): ",
    "adjusting_plan": "\n⏳ Đang điều chỉnh kế hoạch theo ý kiến của bạn...",
    "plan_confirmed": "✅ Kế hoạch đã được xác nhận và lưu!",
    "rename_dir_prompt": "\n📁 Tên tiểu thuyết là \"{title}\", nhưng thư mục dự án là \"{dir}\".",
    "rename_dir_confirm": "   Đổi tên thư mục dự án thành \"{title}\"? (y/n): ",
    "rename_dir_done": "  ✅ Đã đổi tên thư mục dự án: {path}",
    "rename_dir_exists": "  ⚠️ Thư mục đã tồn tại: {path}",
    "rename_dir_failed": "  ❌ Đổi tên thất bại: {error}",
    "phase_world_title": "\n🌍 Giai đoạn 2: Xây dựng thế giới & Hướng dẫn phong cách (đang tạo song song...)",
    "world_done": "✅ Thiết lập thế giới hoàn tất ({count} tài liệu)",
    "world_failed": "❌ Tạo thế giới thất bại: {error}",
    "style_done": "✅ Hướng dẫn phong cách đã được tạo",
    "style_failed": "❌ Tạo hướng dẫn phong cách thất bại: {error}",
    "phase_outline_title": "\n📋 Giai đoạn 3: Tạo đề cương tổng thể",
    "generating_outline": "⏳ Đang tạo đề cương tổng thể...",
    "outline_done": "✅ Đề cương tổng thể đã được tạo",
    "outline_review": "\n📖 Đề cương tổng thể đã lưu tại plot/master_outline.md. Vui lòng xem xét.",
    "press_enter_continue": "👤 Nhấn Enter để tiếp tục tạo đề cương tập 1...",
    "generating_volume": "📑 Đang tạo đề cương tập {num}...",
    "volume_done": "✅ Đề cương tập {num} đã được tạo",
    "phase_writing_title": "\n✍️ Giai đoạn 5: Bắt đầu viết",
    "checkpoint_resume": "[Điểm dừng] Phát hiện {count} chương đã hoàn thành, tiếp tục từ chương {next}",
    "volume_not_found": "⚠️ Không tìm thấy đề cương tập {num}, đang tạo...",
    "generating_volume_outline": "⏳ Đang tạo đề cương tập {num}...",
    "writing_chapter": "📖 Đang viết chương {num}...",
    "chapter_done": "  ✅ Chương {num} hoàn thành (~{words} từ)",
    "post_processing": "  ⏳ Đang phân tích và cập nhật metadata...",
    "post_done": "  ✅ Xử lý hậu kỳ chương {num} hoàn tất",
    "post_failed": "  ⚠️ Phân tích hậu kỳ chương {num} thất bại, bỏ qua cập nhật",
    "chapter_error": "  ❌ Lỗi khi viết chương {num}: {error}",
    "retry_prompt": "  Thử lại? (y/n): ",
    "skip_chapter": "  Bỏ qua chương {num}, tiếp tục chương tiếp theo",
    "pause_prompt": "\n📊 Đã hoàn thành {num} chương. Nhấn Enter để tiếp tục, hoặc gõ 'stop' để tạm dừng",
    "pause_input": "👤 ",
    "paused": "⏸️ Đã tạm dừng. Lần sau có thể tiếp tục từ chương {next}",
    "writing_complete": "🎉 Giai đoạn viết hoàn tất!",
    "planning_incomplete": "Giai đoạn lập kế hoạch chưa hoàn thành, thoát.",
    "no_plan_found": "Không tìm thấy kế hoạch, bắt đầu từ đầu...",
    "resume_checking": "🔄 Đang kiểm tra trạng thái dự án...",
    "resume_completed": "Đã hoàn thành {count} chương, tiếp tục viết...",
    "no_style_guide": "Không tìm thấy hướng dẫn phong cách, đang tạo...",
    "no_outline": "Không tìm thấy đề cương tổng thể, đang tạo...",
    "plan_not_found_error": "Không tìm thấy file kế hoạch plan.json. Vui lòng chạy giai đoạn lập kế hoạch trước",
    "worldbuilding_start": "[Worldbuilding Agent] Bắt đầu tạo song song {count} tài liệu thiết lập...",
    "doc_done": "  ✅ {filename} đã tạo xong",
    "doc_failed": "  ❌ {filename} tạo thất bại",
    "doc_error": "  ❌ {filename} lỗi: {error}",
    "llm_error_retry": "Xin lỗi, có lỗi xảy ra. Vui lòng nói lại~",
    "info_enough": "Thông tin đã đủ rồi! Để tôi tổng hợp kế hoạch tiểu thuyết hoàn chỉnh... 🎯",
    "continue_input": "Hãy cho tôi biết thêm về tiểu thuyết bạn muốn viết~",
    "config_loaded": "[Cấu hình] Đã tải cấu hình từ {file}: {keys}",
    "novel_config_loaded": "[Cấu hình] Đã tải cấu hình riêng của tiểu thuyết từ {file}: {keys}",
    "novel_config_skipped": "  ⚠️ Đã bỏ qua khóa API/đường dẫn trong {file} (sử dụng cấu hình toàn cục): {keys}",
    "novel_config_auto_created": "[Cấu hình] Đã tự động tạo {file} từ mẫu (chỉnh sửa để tùy chỉnh cài đặt tiểu thuyết này)",
    "config_not_found": "[Cấu hình] Không tìm thấy {file}. Thông tin nhạy cảm cần nhập thủ công khi chạy",
"config_hint": "[Cấu hình] Tham khảo user_config.example.json để tạo {file}",
    "project_initialized": "[Dự án] Đã khởi tạo thư mục: {path}",
    "openai_initialized": "[LLM-OpenAI] Đã khởi tạo, model: {model}, Base URL: {url}",
    "openai_need_package": "Backend OpenAI cần package openai: pip install openai",
"openai_no_key": "OPENAI_API_KEY chưa được cấu hình. Vui lòng điền trong user_config.json hoặc nhập khi chạy",
    "openai_attempt_failed": "[LLM-OpenAI] Lần thử {n} thất bại: {error}",
    "openai_retry_wait": "[LLM-OpenAI] Thử lại sau {wait}s...",
    "openai_max_retries": "[LLM-OpenAI] Đã đạt số lần thử tối đa ({max}), bỏ cuộc",
    "local_initialized": "[LLM-Local] Đã khởi tạo, URL: {url}, model marker: {marker}",
    "local_need_package": "Backend cục bộ cần package requests: pip install requests",
"local_no_url": "LOCAL_API_URL chưa được cấu hình. Vui lòng điền trong user_config.json",
    "local_attempt_failed": "[LLM-Local] Lần thử {n} thất bại: {error}",
    "local_retry_wait": "[LLM-Local] Thử lại sau {wait}s...",
    "local_max_retries": "[LLM-Local] Đã đạt số lần thử tối đa ({max}), bỏ cuộc",
    "cannot_load_openai": "Không thể tải backend OpenAI: {error}\nĐảm bảo llm_openai.py tồn tại và openai đã được cài đặt",
    "cannot_load_local": "Không thể tải backend cục bộ: {error}\nĐảm bảo llm_local.py tồn tại và requests đã được cài đặt",
    "unsupported_api_mode": "Chế độ API không được hỗ trợ: {mode}. Có sẵn: 'openai', 'local'",
    "file_written": "[Lưu trữ] Đã ghi: {path}",

    # -- Feature #1: So sánh nhiều bản thảo đề cương --
    "outline_multi_draft_title": "\n📋 Giai đoạn 3: Tạo đề cương tổng thể (So sánh nhiều bản thảo)",
    "generating_draft": "  ⏳ Đang tạo bản thảo đề cương {num}/{total} (phong cách: {style})...",
    "draft_done": "  ✅ Bản thảo {num} hoàn tất",
    "draft_failed": "  ❌ Bản thảo {num} thất bại: {error}",
    "draft_comparison_title": "\n📊 So sánh bản thảo đề cương",
    "draft_header": "\n{'─' * 40}\n📄 Bản thảo {num} — Phong cách: {style}\n{'─' * 40}",
    "draft_select_prompt": "\n👤 Chọn bản thảo sử dụng (1-{max}), hoặc gõ 'm' để hợp nhất tinh hoa: ",
    "draft_merging": "⏳ Đang hợp nhất tinh hoa từ các bản thảo...",
    "draft_selected": "✅ Đã chọn bản thảo {num} làm đề cương chính",
    "draft_merged": "✅ Đề cương hợp nhất đã được tạo",
    "outline_drafts_truncating": "   ⚠️ Bản thảo đề cương quá dài (ước tính {total} token, ngân sách {budget}), cắt ngắn tỷ lệ...",
    "draft_invalid": "Lựa chọn không hợp lệ, vui lòng nhập 1-{max} hoặc 'm'",
    "parallel_review_title": "  🔍 Đang chạy đánh giá chất lượng song song...",
    "review_consistency": "[Người đánh giá tính nhất quán]",
    "review_style": "[Người đánh giá phong cách]",
    "review_foreshadowing": "[Người đánh giá phục bút]",
    "review_done": "  ✅ {reviewer}: Phát hiện {count} vấn đề (độ tin cậy≥{threshold})",
    "review_failed": "  ⚠️ {reviewer} đánh giá thất bại: {error}",
    "review_no_issues": "  ✅ Tất cả đánh giá đạt — không có vấn đề đáng kể!",
    "review_issues_found": "  ⚠️ Tổng cộng {count} vấn đề từ tất cả người đánh giá:",
    "review_issue_item": "    [{severity}] ({reviewer}, độ tin cậy: {confidence}) {description}",
    "review_critical_prompt": "  🚨 Phát hiện vấn đề nghiêm trọng. Viết lại chương này? (y/n): ",
    "polish_start": "  ✨ Bắt đầu vòng chỉnh sửa (tối đa {max_iter} lần)...",
    "polish_iteration": "  ✨ Chỉnh sửa lần {iter}/{max_iter}...",
    "polish_score": "  📊 Điểm chất lượng: {score}/10 (ngưỡng: {threshold})",
    "polish_passed": "  ✅ Đạt ngưỡng chất lượng! Kết thúc vòng chỉnh sửa.",
    "polish_improving": "  ⏳ Điểm chưa đạt ngưỡng, đang cải thiện...",
    "polish_max_reached": "  ⚠️ Đã đạt số lần chỉnh sửa tối đa. Sử dụng bản tốt nhất (điểm: {score}/10).",
    "polish_failed": "  ⚠️ Đánh giá chỉnh sửa thất bại, giữ bản hiện tại.",
    "volume_checkpoint_title": "\n📍 Điểm kiểm tra tập {num}",
    "volume_checkpoint_summary": "  Tiến độ hiện tại: {completed} chương hoàn thành, ~{words} từ",
    "volume_checkpoint_prompt": "\n👤 Sắp bắt đầu tập {num}. Tiếp tục? (y / adjust / stop): ",
    "volume_checkpoint_adjust": "👤 Nhập ghi chú điều chỉnh: ",
    "volume_checkpoint_adjusting": "⏳ Đang điều chỉnh đề cương tập theo phản hồi...",
    "volume_checkpoint_stopped": "⏸️ Dừng trước tập {num}. Lần sau tiếp tục từ chương {next}.",
    "severity_critical": "NGHIÊM TRỌNG",
    "severity_major": "QUAN TRỌNG",
    "severity_minor": "NHỎ",
    "severity_info": "THÔNG TIN",
    "final_summary_title": "\n📊 Đang tạo báo cáo tổng kết cuối cùng...",
    "final_summary_done": "✅ Báo cáo tổng kết đã được tạo và lưu!",
    "final_summary_failed": "⚠️ Tạo báo cáo tổng kết thất bại: {error}",

    # -- Xác nhận thông số viết --
    "writing_params_title": "\n⚙️ Xác nhận thông số viết",
    "ask_chapter_min_words": "   Số từ tối thiểu mỗi chương (hiện tại: {current}, Enter để giữ nguyên): ",
    "ask_chapter_max_words": "   Số từ tối đa mỗi chương (hiện tại: {current}, Enter để giữ nguyên): ",
    "writing_params_swapped": "   ⚠️ Min > Max, đã hoán đổi giá trị.",
    "ask_word_count_check": "   Bật kiểm tra số từ? (hiện tại: {status}, y/n, Enter để giữ nguyên): ",
    "ask_lazy_mode": "   Bật chế độ tự động (tự xác nhận mọi thứ)? (hiện tại: {status}, y/n, Enter để giữ nguyên): ",
    "writing_params_summary": "   ✅ Thông số viết: {min}-{max} từ/chương, kiểm tra số từ: {check}, chế độ tự động: {lazy}",

    # -- Phong cách dấu ngoặc kép hội thoại --
    "quote_style_title": "\n💬 Phong cách dấu ngoặc kép hội thoại",
    "quote_style_prompt": "\n👤 Chọn phong cách dấu ngoặc kép cho hội thoại (1-{max}): ",
    "quote_style_invalid": "Lựa chọn không hợp lệ, vui lòng nhập 1-{max}",
    "quote_style_selected": "✅ Đã đặt phong cách dấu ngoặc kép: {style}",
    "quote_style_option_curly": '\u201c\u201d ngoặc kép cong (ví dụ: \u201cXin chào!\u201d)',
    "quote_style_option_corner": '「」 ngoặc vuông (ví dụ: 「Xin chào!」)',
    "quote_style_option_guillemet": '«» ngoặc kép kiểu Pháp (ví dụ: «Xin chào!»)',
    "quote_style_option_dash": '— gạch ngang cho hội thoại (ví dụ: — Xin chào!)',
    "quote_style_option_straight": '"" ngoặc kép thẳng (ví dụ: "Xin chào!")',

    # -- Phong cách dấu ngoặc nội tâm --
    "inner_quote_title": "\n💭 Phong cách dấu ngoặc nội tâm / độc thoại nội tâm",
    "inner_quote_prompt": "\n👤 Chọn phong cách cho nội tâm trong tiểu thuyết (1-{max}): ",
    "inner_quote_invalid": "Lựa chọn không hợp lệ, vui lòng nhập 1-{max}",
    "inner_quote_selected": "✅ Đã đặt phong cách nội tâm: {style}",
    "inner_quote_option_corner_double": '『』 ngoặc vuông kép (ví dụ: 『Phải cẩn thận mới được』)',
    "inner_quote_option_corner": '「」 ngoặc vuông (ví dụ: 「Phải cẩn thận mới được」)',
    "inner_quote_option_curly_single": '\u2018\u2019 ngoặc đơn cong (ví dụ: \u2018Phải cẩn thận mới được\u2019)',
    "inner_quote_option_italic": '*in nghiêng* cho nội tâm (ví dụ: *Phải cẩn thận mới được*)',
    "inner_quote_option_dash": '——gạch ngang kép (ví dụ: ——Phải cẩn thận mới được——)',
    "inner_quote_option_paren": '（） ngoặc đơn toàn độ rộng (ví dụ: （Phải cẩn thận mới được）)',
    "inner_quote_option_same": 'Giống như hội thoại',
    "inner_quote_option_none": 'Không dùng ký hiệu đặc biệt (miêu tả bằng lời kể)',

    # -- Quy tắc dấu ngoặc kép (chèn vào hướng dẫn phong cách/prompt) --
    "quote_rules_heading": "Quy tắc phong cách dấu ngoặc kép",
    "quote_rule_dialogue_curly": 'Dùng \u201c\u201d (ngoặc kép cong) cho tất cả hội thoại. Ví dụ: \u201cXin chào!\u201d',
    "quote_rule_dialogue_corner": 'Dùng 「」 (ngoặc vuông) cho tất cả hội thoại. Ví dụ: 「Xin chào!」',
    "quote_rule_dialogue_guillemet": 'Dùng «» (ngoặc kép kiểu Pháp) cho tất cả hội thoại. Ví dụ: «Xin chào!»',
    "quote_rule_dialogue_dash": 'Dùng — (gạch ngang) để dẫn hội thoại. Ví dụ: — Xin chào!',
    "quote_rule_dialogue_straight": 'Dùng "" (ngoặc kép thẳng) cho tất cả hội thoại. Ví dụ: "Xin chào!"',
    "quote_rule_inner_corner_double": 'Nội tâm/độc thoại nội tâm dùng 『』 (ngoặc vuông kép). Ví dụ: 『Phải cẩn thận mới được』',
    "quote_rule_inner_corner": 'Nội tâm/độc thoại nội tâm dùng 「」 (ngoặc vuông). Ví dụ: 「Phải cẩn thận mới được」',
    "quote_rule_inner_curly_single": 'Nội tâm/độc thoại nội tâm dùng \u2018\u2019 (ngoặc đơn cong). Ví dụ: \u2018Phải cẩn thận mới được\u2019',
    "quote_rule_inner_italic": 'Nội tâm/độc thoại nội tâm dùng *in nghiêng*. Ví dụ: *Phải cẩn thận mới được*',
    "quote_rule_inner_dash": 'Nội tâm/độc thoại nội tâm dùng ——(gạch ngang kép). Ví dụ: ——Phải cẩn thận mới được——',
    "quote_rule_inner_paren": 'Nội tâm/độc thoại nội tâm dùng （）(ngoặc đơn toàn độ rộng). Ví dụ: （Phải cẩn thận mới được）',
    "quote_rule_inner_none": 'Không dùng ký hiệu đặc biệt cho nội tâm. Miêu tả bằng lời kể.',
    "quote_rule_inner_same": 'Nội tâm/độc thoại nội tâm dùng cùng phong cách với hội thoại.',

    # -- Chế độ tự động --
    "welcome_title": "📖 Hệ thống viết tiểu thuyết AI v1.0",
    "lazy_mode_enabled": "🛋️ Chế độ tự động BẬT — mọi thao tác sau đề cương sẽ tự động!",
    "lazy_auto_merge": "🛋️ [Tự động] Đang tự động hợp nhất tất cả bản nháp đề cương...",
    "lazy_auto_select": "🛋️ [Tự động] Chỉ có một bản nháp, đã tự động chọn.",
    "lazy_auto_continue": "🛋️ [Tự động] Tự động tiếp tục...",
    "lazy_auto_retry": "🛋️ [Tự động] Tự động thử lại...",
    "lazy_auto_skip": "🛋️ [Tự động] Tự động bỏ qua...",
    "lazy_auto_volume_continue": "🛋️ [Tự động] Tự động tiếp tục tập {num}...",

    # -- Thử lại đánh giá --
    "review_retry_feedback": """⚠️ QUAN TRỌNG: Đây là lần viết lại thứ {attempt}/{max_attempts}. Phiên bản trước có các vấn đề nghiêm trọng/quan trọng sau cần phải sửa:
{issues}

Vui lòng viết lại TOÀN BỘ chương từ đầu, đảm bảo sửa TẤT CẢ các vấn đề trên đồng thời giữ nguyên cốt truyện, giọng văn và cấu trúc.""",
    "review_max_retries_reached": "  ⚠️ Chương {num} đã đạt số lần thử lại đánh giá tối đa ({max}). Lưu phiên bản hiện tại và tiếp tục.",



    # -- Kiểm tra số từ --
    "wordcount_check_start": "  📏 Kiểm tra số từ: {words} từ (mục tiêu: {min}-{max})",
    "wordcount_too_short": "  ⚠️ Chương quá ngắn ({words} từ, tối thiểu {min}). Đang mở rộng...",
    "wordcount_too_long": "  ⚠️ Chương quá dài ({words} từ, tối đa {max}). Đang rút gọn...",
    "wordcount_split_needed": "  📑 Chương vượt quá nghiêm trọng ({words} từ, ≥{threshold}% giới hạn). Đang tách thành hai chương...",
    "wordcount_expand_done": "  ✅ Mở rộng hoàn tất: {words} từ",
    "wordcount_compress_done": "  ✅ Rút gọn hoàn tất: {words} từ",
    "wordcount_split_done": "  ✅ Tách hoàn tất: Chương {num_a} ({words_a} từ) + Chương {num_b} ({words_b} từ)",
    "wordcount_retry": "  🔄 Kiểm tra số từ thử lại {attempt}/{max_attempts}...",
    "wordcount_give_up": "  ⚠️ Sau {max_attempts} lần thử vẫn chưa đạt, dùng bản hiện tại ({words} từ).",
    "wordcount_ok": "  ✅ Số từ đạt yêu cầu: {words} từ",
    "wordcount_split_renumber": "  📝 Lưu ý: Các chương sau khi tách sẽ được đánh số lại tự động.",

    # -- Feature #1: Multi-draft outline styles --
    "outline_style_dramatic": "Kịch tính & Căng thẳng cao",
    "outline_style_literary": "Văn học & Nhân vật là trọng tâm",
    "outline_style_commercial": "Thương mại & Nhịp nhanh",

    # -- Tiếp tục từ chương đã viết --
    "ask_existing_chapters": "\n📝 Bạn đã viết sẵn một số chương chưa? (y/n): ",
    "created_empty_chapter_item": "   📄 {filename}",
    "continue_scanning": "\n🔍 Đang quét các chương đã có...",
    "continue_found_chapters": "📖 Tìm thấy {count} chương đã có.",
    "continue_reading_chapters": "📚 Đang đọc các chương đã có để xây dựng ngữ cảnh...",
    "continue_chapter_read": "   ✅ Chương {num}: {words} từ",
    "continue_summary_generating": "🤖 Đang tạo tóm tắt các chương đã có...",
    "continue_summary_done": "✅ Đã tạo tóm tắt các chương. Bắt đầu lập kế hoạch dựa trên nội dung đã có.",
    "continue_planning_title": "\n📝 Lập kế hoạch (dựa trên {count} chương đã có)",
    "continue_outline_context": "\n📋 Đề cương sẽ tích hợp {count} chương đã có.",
    "continue_writing_from": "\n✍️ Sẽ bắt đầu viết từ chương {next_chapter}.",
})

PROMPTS = dict(_BASE_PROMPTS)
PROMPTS.update({
    # -- Planner Agent --
    "planner_system": """Bạn là một biên tập viên lập kế hoạch tiểu thuyết giàu kinh nghiệm, giỏi trong việc xây dựng cốt lõi tiểu thuyết từ con số không.
Nhiệm vụ của bạn là thu thập đủ thông tin qua cuộc trò chuyện với người dùng để xác định các yếu tố cốt lõi sau:

1. **Thể loại/Loại hình**: Fantasy, Hiện đại, Trinh thám, Ngôn tình, Sci-Fi, v.v.
2. **Chủ đề cốt lõi**: Tiểu thuyết muốn truyền tải điều gì
3. **Số từ mục tiêu & Cấu trúc**: Tổng số từ, số từ mỗi chương, số chương dự kiến, số tập
4. **Góc nhìn kể chuyện**: Ngôi thứ nhất / Ngôi thứ ba
5. **Thẻ cốt lõi**: 3-5 từ khóa
6. **Tóm tắt một câu**: Một câu khái quát toàn bộ cuốn sách
7. **Tóm tắt ba hồi**: Mở đầu, phát triển, kết thúc
8. **Yêu cầu phong cách**: Phong cách, giọng điệu, tác phẩm tham khảo
9. **Điều cấm kỵ**: Nội dung không được phép xuất hiện
10. **Nhân vật chính**: Ít nhất thiết lập cơ bản cho nhân vật chính
11. **Khung thế giới**: Bối cảnh thế giới nơi câu chuyện diễn ra

Bạn cần chủ động hỏi người dùng để thu thập thông tin. Những phần người dùng không muốn tự quyết định, hãy sáng tạo bổ sung.
Khi bạn cho rằng đã có đủ thông tin, hãy xuất bản kế hoạch tiểu thuyết hoàn chỉnh.

Lưu ý:
- Mỗi lần chỉ hỏi 2-3 câu hỏi liên quan
- Linh hoạt điều chỉnh câu hỏi tiếp theo dựa trên câu trả lời
- Với mỗi yếu tố, hỏi rõ người dùng muốn tự chỉ định hay để bạn quyết định
- Duy trì phong cách trò chuyện thân thiện và chuyên nghiệp""",

    "planner_first_question": """Xin chào! Tôi là trợ lý lập kế hoạch tiểu thuyết của bạn~ 🎉

Trước khi bắt đầu sáng tác, tôi cần hiểu ý tưởng của bạn. Hãy tiến hành từng bước:

**Đầu tiên, những câu hỏi cơ bản nhất:**
1. Bạn muốn viết tiểu thuyết **thể loại** gì? (ví dụ: Fantasy, Hiện đại, Trinh thám, Sci-Fi, Ngôn tình, Lịch sử, v.v.)
2. Bạn có **hướng đi câu chuyện** hoặc **ý tưởng cốt lõi** nào trong đầu không? Dù chỉ là ý tưởng mơ hồ cũng được
3. Bạn muốn tự chỉ định các thiết lập cơ bản này, hay muốn tôi giúp brainstorm?

Hãy thoải mái chia sẻ suy nghĩ của bạn~""",

    "planner_check_enough": """Hãy phân tích tất cả thông tin đã thu thập và xác định xem đã đủ để bắt đầu lập kế hoạch chưa.

Danh sách kiểm tra yếu tố cốt lõi:
1. Thể loại/Loại hình - {has_genre}
2. Chủ đề cốt lõi - {has_theme}
3. Số từ mục tiêu & Cấu trúc - {has_structure}
4. Góc nhìn kể chuyện - {has_pov}
5. Thẻ cốt lõi - {has_tags}
6. Tóm tắt một câu - {has_summary}
7. Yêu cầu phong cách - {has_style}
8. Nhân vật chính (ít nhất ý tưởng về nhân vật chính) - {has_characters}
9. Khung thế giới - {has_world}

**QUAN TRỌNG**: Khi người dùng yêu cầu BẠN quyết định một số mục nhất định (ví dụ: "thể loại bạn tự chọn", "bối cảnh tùy bạn", "nhân vật nữ chính bạn tự quyết định", hoặc đơn giản là "bạn tự quyết định"), hãy coi các mục đó là **đã đủ** và KHÔNG liệt kê vào "missing_items". Chỉ những mục mà người dùng không chỉ định và cũng không ủy thác cho bạn mới thực sự thiếu. Nếu tất cả mục đều đã được chỉ định hoặc ủy thác, đặt "is_enough" thành true.

Hãy trả lời bằng định dạng JSON:
{{
    "is_enough": true/false,
    "missing_items": ["danh sách yếu tố còn thiếu"],
    "next_questions": "Nếu chưa đủ, câu hỏi tiếp theo cho người dùng (2-3 câu)"
}}

Chỉ trả về JSON.""",

    "planner_summarize": """Dựa trên thông tin thu thập được trong cuộc trò chuyện sau, hãy tạo bản kế hoạch tiểu thuyết hoàn chỉnh.
Những phần người dùng chưa chỉ định rõ ràng, hãy sáng tạo bổ sung để toàn bộ kế hoạch nhất quán và hấp dẫn.

Hãy xuất nghiêm ngặt theo định dạng JSON sau:
{{
    "title": "Tên sách",
    "genre": "Thể loại/Loại hình",
    "theme": "Chủ đề cốt lõi (một đoạn văn)",
    "target_words": "Tổng số từ mục tiêu",
    "chapter_words": "Phạm vi số từ mỗi chương",
    "total_chapters": "Tổng số chương dự kiến",
    "volumes": "Số tập và cách phân chia",
    "pov": "Góc nhìn kể chuyện",
    "tags": "Thẻ cốt lõi (phân cách bằng dấu phẩy)",
    "one_line_summary": "Tóm tắt một câu",
    "three_act_summary": {{
        "beginning": "Mở đầu (tổng quan phần khởi đầu)",
        "middle": "Phát triển (tổng quan phần giữa)",
        "end": "Kết thúc (tổng quan phần kết)"
    }},
    "style_guide": "Yêu cầu phong cách viết và quy tắc",
    "taboos": "Điều cấm kỵ",
    "main_characters": [
        {{
            "name": "Tên",
            "role": "Vai trò (nhân vật chính/phản diện/phụ, v.v.)",
            "age": "Tuổi",
            "appearance": "Mô tả ngoại hình",
            "personality": "Mô tả tính cách",
            "background": "Câu chuyện nền",
            "motivation": "Động lực cốt lõi",
            "arc": "Cung phát triển nhân vật"
        }}
    ],
    "world_setting": "Mô tả khung thế giới",
    "synopsis": "Tóm tắt tiểu thuyết (bản công khai)"
}}""",

    # -- Outline Agent --
    "outline_system": """Bạn là một người lập kế hoạch đề cương tiểu thuyết giàu kinh nghiệm. Dựa trên kế hoạch tiểu thuyết được cung cấp, bạn sẽ tạo đề cương cốt truyện chi tiết.

Nội dung cần xuất:
1. Đề cương cấp tập cho toàn bộ sách (mỗi tập: cốt truyện chính, xung đột cốt lõi, sự kiện chính, cao trào và điểm hấp dẫn)
2. Mô tả bằng văn bản về bản đồ mối quan hệ nhân vật

Xuất bằng định dạng Markdown. Đảm bảo:
- Mỗi đề cương tập có cốt truyện chính rõ ràng và danh sách sự kiện
- Có mối liên hệ nhân quả rõ ràng giữa các tập
- Cung phát triển nhân vật xuyên suốt
- Phục bút và hồi hộp được thiết kế hợp lý
- Nhịp truyện có lúc căng lúc chùng""",

    "volume_outline_system": """Bạn là chuyên gia đề cương tiểu thuyết, giỏi chi tiết hóa cốt truyện.
Dựa trên tổng quan của một tập từ đề cương tổng thể, bạn sẽ tạo đề cương chi tiết cấp chương.

Xuất bằng Markdown. Mỗi chương cần:
- Tiêu đề chương
- Sự kiện chính (3-5 điểm then chốt)
- Nhân vật xuất hiện
- Giọng điệu cảm xúc/bầu không khí
- Phục bút (gieo/thu hồi)
- Điểm chuyển tiếp""",

    # -- Worldbuilding Agent --
    "worldbuilding_system": """Bạn là chuyên gia xây dựng thế giới chuyên nghiệp. Dựa trên kế hoạch tiểu thuyết, bạn cần tạo tài liệu thiết lập thế giới chi tiết.

Xuất bằng Markdown, bao gồm:
1. Thiết lập thế giới tổng thể (bối cảnh thời đại, cấu trúc xã hội, trình độ công nghệ/phép thuật, v.v.)
2. Thiết lập địa lý/không gian (các địa điểm quan trọng và đặc điểm)
3. Thiết lập hệ thống đặc biệt (hệ thống tu luyện/phép thuật/công nghệ, tùy thể loại)
4. Niên biểu sự kiện lớn (các sự kiện lịch sử quan trọng trước khi câu chuyện bắt đầu)

Đảm bảo các thiết lập nhất quán với nhau và không mâu thuẫn.""",

    "character_system": """Bạn là chuyên gia thiết kế nhân vật. Dựa trên kế hoạch tiểu thuyết và thiết lập thế giới, bạn cần tạo hồ sơ nhân vật chi tiết.

Mỗi nhân vật cần:
- Thông tin cơ bản (tên, tuổi, ngoại hình, v.v.)
- Mô tả tính cách (đa tầng, bao gồm hành vi bên ngoài và tính cách bên trong)
- Câu chuyện nền
- Khả năng/sở trường
- Mục tiêu/động lực
- Cách nói chuyện/thói quen ngôn ngữ
- Cung phát triển nhân vật
- Mối quan hệ nhân vật

Xuất bằng Markdown. Đảm bảo các nhân vật có sự tương tác hóa học, tính cách bổ sung hoặc đối lập.""",

    # -- Writer Agent --
    "writer_system": """Bạn là một nhà văn tiểu thuyết tài năng.
Bạn sẽ viết các chương tiểu thuyết dựa trên thiết lập, đề cương và ngữ cảnh được cung cấp.

Yêu cầu viết:
{style_guide}

Yêu cầu cấu trúc:
- Mỗi chương {min_words}-{max_words} từ
- Chương cần mở đầu hấp dẫn (kết nối với chương trước hoặc tạo hồi hộp mới)
- Đẩy cốt truyện chính (ít nhất một sự kiện then chốt)
- Kết thúc có điểm nhấn (để thu hút người đọc tiếp tục)

Tuân thủ nghiêm ngặt định dạng:
- Định dạng tiêu đề: Chương X Tiêu đề
- Xuất trực tiếp nội dung chương, không có ghi chú hay thông tin meta""",

    "writer_chapter_prompt": """Hãy viết toàn bộ nội dung Chương {chapter_num} dựa trên thông tin sau.

## Đề cương chương này
{chapter_outline}

## Tóm tắt các chương gần đây (để duy trì tính liên tục)
{recent_briefs}

## Trạng thái nhân vật hiện tại
{character_status}

## Lưu ý về phục bút
{hooks_info}

## Hồ sơ nhân vật (CHÍNH THỨC — tên phải khớp chính xác)
{character_profiles}

## Bối cảnh thế giới & Địa danh (CHÍNH THỨC — tất cả địa danh, tên phe phái, v.v. phải khớp chính xác)
{world_setting}

⚠️ CẢNH BÁO QUAN TRỌNG: Tất cả tên nhân vật, địa danh, tên phe phái/môn phái và thuật ngữ riêng PHẢI khớp chính xác với hồ sơ nhân vật và bối cảnh thế giới ở trên. KHÔNG được tự tạo, thay đổi hoặc thay thế bất kỳ tên nào.

Hãy xuất toàn bộ nội dung chương ({min_words}-{max_words} từ), bắt đầu bằng "Chương {chapter_num}".""",

    # -- Post-write Agent --
    "post_write_system": """Bạn là một trợ lý biên tập tiểu thuyết tỉ mỉ. Nhiệm vụ của bạn là phân tích nội dung chương sau khi viết xong và tạo thông tin cập nhật.

Xuất bằng định dạng JSON:
{{
    "chapter_brief": {{
        "chapter_num": số chương,
        "title": "Tiêu đề chương",
        "word_count": số từ ước tính,
        "main_events": ["Sự kiện chính 1", "Sự kiện chính 2", ...],
        "character_changes": ["Thay đổi trạng thái nhân vật 1", ...],
        "hooks_planted": ["Phục bút mới 1", ...],
        "hooks_resolved": ["ID phục bút đã thu hồi 1", ...],
        "next_chapter_hook": "Điểm nhấn cho chương tiếp theo"
    }},
    "progress_update": {{
        "latest_chapter": "Chương X · Tiêu đề",
        "total_words": tổng số từ tích lũy ước tính,
        "character_status": {{
            "Tên nhân vật": "Mô tả trạng thái hiện tại"
        }}
    }}
}}

Chỉ trả về JSON.""",

    # -- Style Guide Agent --
    "style_guide_system": """Bạn là cố vấn văn học chuyên về hướng dẫn phong cách viết.
Dựa trên kế hoạch tiểu thuyết, tạo tài liệu hướng dẫn phong cách chi tiết.

Xuất bằng Markdown, bao gồm:
1. Hướng dẫn góc nhìn kể chuyện
2. Yêu cầu phong cách viết (giọng điệu tổng thể, phong cách độc thoại nội tâm, biểu hiện bên ngoài, v.v.)
3. Hướng dẫn cấu trúc chương
4. Hướng dẫn đối thoại (định dạng đối thoại, phong cách nói của nhân vật)
5. Hướng dẫn miêu tả (chiến đấu/cảm xúc/cảnh quan, v.v.)
6. Đề xuất kiểm soát nhịp truyện
7. Nguyên tắc viết cốt lõi
8. Điều cấm kỵ""",

    # -- Worldbuilding task prompts --
    "task_world_setting": """Dựa trên kế hoạch tiểu thuyết sau, hãy tạo tài liệu thiết lập thế giới tổng thể (Markdown).
Bao gồm: bối cảnh thời đại, cấu trúc xã hội, các thế lực/tổ chức quan trọng và nền tảng thế giới.

Kế hoạch:
{plan_text}""",

    "task_characters": """Dựa trên kế hoạch tiểu thuyết sau, hãy tạo tài liệu hồ sơ nhân vật chi tiết (Markdown).
Yêu cầu: mỗi nhân vật bao gồm tên, tuổi, ngoại hình, tính cách (đa tầng), nền, khả năng, động lực, thói quen nói, cung phát triển.
Cuối cùng đính kèm bản đồ quan hệ nhân vật (mô tả bằng văn bản).

Kế hoạch:
{plan_text}""",

    "task_locations": """Dựa trên kế hoạch tiểu thuyết sau, hãy tạo tài liệu thiết lập địa điểm/cảnh quan quan trọng (Markdown).
Bao gồm tất cả địa điểm quan trọng xuất hiện trong truyện và mô tả đặc điểm.

Kế hoạch:
{plan_text}""",

    "task_timeline": """Dựa trên kế hoạch tiểu thuyết sau, hãy tạo tài liệu niên biểu sự kiện lớn (Markdown).
Bao gồm các sự kiện lịch sử quan trọng trước khi câu chuyện bắt đầu và kế hoạch thời gian trong truyện.

Kế hoạch:
{plan_text}""",

    "task_power_system": """Dựa trên kế hoạch tiểu thuyết sau, hãy tạo tài liệu thiết lập hệ thống sức mạnh/tu luyện (Markdown).
Bao gồm: phân cấp, phương pháp tu luyện, hệ thống năng lực đặc biệt và thiết lập chi tiết.

Kế hoạch:
{plan_text}""",

    "task_tech_system": """Dựa trên kế hoạch tiểu thuyết sau, hãy tạo tài liệu thiết lập hệ thống công nghệ (Markdown).
Bao gồm: trình độ công nghệ, công nghệ then chốt, thiết bị đặc biệt và thiết lập chi tiết.

Kế hoạch:
{plan_text}""",

    # -- Outline generation prompts --
    "master_outline_prompt": """Hãy tạo đề cương tổng thể cho toàn bộ sách dựa trên kế hoạch sau.

## Kế hoạch tiểu thuyết
{plan_json}

Tạo đề cương tổng thể (Markdown) bao phủ tất cả các tập. Mỗi tập cần:
- Mô tả cốt truyện chính
- Xung đột cốt lõi
- Sự kiện chính (danh sách đánh số)
- Trạng thái nhân vật chính
- Cao trào của tập
- Điểm hấp dẫn cuối tập
- Kết nối với tập tiếp theo""",

    "volume_outline_prompt": """Hãy tạo đề cương chi tiết cấp chương cho Tập {volume_num}.

## Tóm tắt kế hoạch tiểu thuyết
- Tên: {title}
- Thể loại: {genre}
- Số từ mỗi chương: {chapter_words}

## Gợi ý vị trí tập
{volume_info}

## Đề cương tổng thể (bản đầy đủ — tìm phần Tập {volume_num} làm cơ sở)
{master_outline}

Tạo đề cương chi tiết cấp chương. Mỗi chương bao gồm:
- Số chương và tiêu đề
- Sự kiện chính (3-5)
- Nhân vật xuất hiện
- Giọng điệu cảm xúc
- Phục bút (gieo/thu hồi)
- Điểm chuyển tiếp""",

    # -- Post-write prompts --
    "analyze_chapter_prompt": """Hãy phân tích chương tiểu thuyết sau và tạo tóm tắt cùng thông tin cập nhật.

## Đề cương chương (tham khảo)
{chapter_outline}

## Nội dung chương
{chapter_text}

Xuất nghiêm ngặt theo định dạng JSON đã chỉ định.""",

    # -- Plan revision --
    "plan_revision_request": "Tôi có ý kiến chỉnh sửa sau cho kế hoạch: {feedback}\nHãy điều chỉnh kế hoạch theo đó.",

    # -- Genre detection keywords --
    "genre_fantasy_keywords": ["fantasy", "tu tiên", "tiên hiệp", "ma thuật", "dị giới"],
    "genre_scifi_keywords": ["sci-fi", "tương lai", "cyber", "không gian", "công nghệ"],


    "outline_merge_prompt": """Dưới đây là {count} đề cương tổng thể với phong cách khác nhau cho cùng một tiểu thuyết.

Hãy tạo một **đề cương tổng thể hợp nhất** với yêu cầu:
1. Lấy yếu tố cấu trúc mạnh nhất từ mỗi bản thảo
2. Kết hợp ý tưởng cốt truyện và cung nhân vật tốt nhất
3. Duy trì tính nhất quán logic xuyên suốt
4. Giữ lại thiết kế phục bút và cao trào hấp dẫn nhất

{drafts_text}

Xuất đề cương hợp nhất bằng Markdown.""",

    # -- Feature #2: Parallel reviewer system prompts --
    "consistency_reviewer_system": """Bạn là biên tập viên kiểm tra tính liên tục tỉ mỉ cho tiểu thuyết.
Nhiệm vụ: kiểm tra xem nội dung chương có nhất quán với các chương trước, đề cương và hồ sơ nhân vật được cung cấp không.

Kiểm tra:
1. **Độ chính xác tên nhân vật**: Đối chiếu TẤT CẢ tên nhân vật trong chương với hồ sơ nhân vật. Đánh dấu BẤT KỲ tên nào không khớp chính xác với hồ sơ (lỗi chính tả, tên sai, hoán đổi tên, xưng hô không nhất quán). Đây là kiểm tra ƯU TIÊN CAO NHẤT.
2. **Nhất quán đặc điểm nhân vật**: Xác minh hành vi, cách nói, năng lực và tính cách của mỗi nhân vật có khớp với hồ sơ không.
3. Độ chính xác của dòng thời gian và trình tự sự kiện
4. Nhất quán bối cảnh/địa điểm
5. Tính liên tục cốt truyện (sự kiện được đề cập phải đã thực sự xảy ra)
6. Nhất quán kiến thức nhân vật (nhân vật không biết điều họ chưa học được)

Với mỗi vấn đề, gán điểm tin cậy (0-100):- 0-25: Không chắc chắn, có thể là cố ý
- 26-50: Có thể là vấn đề nhưng có thể chủ quan
- 51-75: Có khả năng là lỗi, cần xác minh
- 76-100: Chắc chắn là lỗi, đã đối chiếu nguồn

Xuất JSON:
{{
    "issues": [
        {{
            "type": "consistency",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "Mô tả vấn đề",
            "location": "Vị trí ước tính trong chương",
            "suggestion": "Cách sửa"
        }}
    ],
    "overall_consistency_score": 1-10
}}

Chỉ trả về JSON.""",

    "style_reviewer_system": """Bạn là chuyên gia đánh giá phong cách văn học.
Nhiệm vụ: kiểm tra chương có tuân thủ hướng dẫn phong cách không.

Kiểm tra:
1. Nhất quán góc nhìn (không chuyển đổi góc nhìn ngoài ý muốn)
2. Giọng điệu và bầu không khí phù hợp với hướng dẫn phong cách
3. Phong cách đối thoại nhất quán với hồ sơ nhân vật
4. Vấn đề nhịp truyện (quá vội hoặc quá chậm)
5. Chất lượng văn phong (diễn đạt vụng, từ lặp lại, v.v.)

Với mỗi vấn đề, gán điểm tin cậy (0-100).

Xuất JSON:
{{
    "issues": [
        {{
            "type": "style",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "Mô tả vấn đề",
            "location": "Vị trí ước tính trong chương",
            "suggestion": "Cách sửa"
        }}
    ],
    "overall_style_score": 1-10
}}

Chỉ trả về JSON.""",

    "foreshadowing_reviewer_system": """Bạn là chuyên gia về phục bút và tính liên tục cốt truyện.
Nhiệm vụ: kiểm tra cách xử lý yếu tố phục bút trong chương.

Kiểm tra:
1. Phục bút được gieo có đủ tinh tế không (không quá lộ liễu)?
2. Các điểm nhấn đã gieo trước có được phát triển hoặc thu hồi đúng thời điểm?
3. Có bỏ lỡ cơ hội phục bút nào dựa trên đề cương?
4. Phục bút được thu hồi có thỏa mãn không?
5. Kết thúc chương có tạo đủ hồi hộp cho chương tiếp theo?

Với mỗi vấn đề, gán điểm tin cậy (0-100).

Xuất JSON:
{{
    "issues": [
        {{
            "type": "foreshadowing",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "Mô tả vấn đề",
            "location": "Vị trí ước tính trong chương",
            "suggestion": "Cách sửa"
        }}
    ],
    "overall_foreshadowing_score": 1-10
}}

Chỉ trả về JSON.""",

    "review_chapter_prompt": """Hãy đánh giá chương sau.

## Hồ sơ nhân vật (Tham chiếu chính thức để đối chiếu tên và đặc điểm)
{character_profiles}

## Hướng dẫn phong cách
{style_guide}

## Đề cương chương
{chapter_outline}

## Tóm tắt các chương gần đây
{recent_briefs}

## Bảng theo dõi phục bút
{hooks_info}

## Nội dung chương
{chapter_text}

QUAN TRỌNG: Đối chiếu TẤT CẢ tên nhân vật trong chương với Hồ sơ nhân vật ở trên. Bất kỳ tên nào không khớp đều là vấn đề NGHIÊM TRỌNG.

Xuất kết quả đánh giá theo định dạng JSON đã chỉ định.""",
    # -- Feature #3: Polish loop prompts --
    "polish_evaluate_system": """Bạn là biên tập viên cao cấp. Đánh giá chất lượng chương theo thang 1-10.

Tiêu chí:
1. Chất lượng văn phong và độ dễ đọc
2. Nhất quán giọng nói nhân vật
3. Nhịp truyện và sự trôi chảy
4. Tác động cảm xúc
5. Sức hút điểm nhấn (mở đầu và kết thúc)
6. Phù hợp với đề cương

Xuất JSON:
{{
    "score": 1-10,
    "strengths": ["điểm mạnh 1", "điểm mạnh 2"],
    "weaknesses": ["điểm yếu 1", "điểm yếu 2"],
    "specific_improvements": [
        {{
            "location": "vị trí trong văn bản",
            "current": "văn bản có vấn đề hiện tại (tóm tắt)",
            "suggested": "cách cải thiện"
        }}
    ]
}}

Chỉ trả về JSON.""",

    "polish_evaluate_prompt": """Đánh giá chất lượng chương này.

## Hướng dẫn phong cách
{style_guide}

## Đề cương chương
{chapter_outline}

## Nội dung chương
{chapter_text}

Xuất kết quả đánh giá bằng JSON.""",

    "polish_improve_system": """Bạn là nhà văn tài năng đang thực hiện chỉnh sửa.
Bạn sẽ nhận được chương cùng với đề xuất cải thiện cụ thể từ biên tập viên.
Viết lại TOÀN BỘ chương, tích hợp các cải thiện nhưng giữ nguyên câu chuyện, giọng điệu và cấu trúc.

KHÔNG thêm bình luận meta — chỉ xuất nội dung chương đã chỉnh sửa.""",

    "polish_improve_prompt": """Hãy chỉnh sửa chương sau dựa trên phản hồi của biên tập viên.

## Phản hồi biên tập viên
Điểm yếu: {weaknesses}

Đề xuất cải thiện cụ thể:
{improvements}

## Nội dung chương hiện tại
{chapter_text}

Xuất toàn bộ nội dung chương đã chỉnh sửa.""",

    # -- Feature #4: Volume checkpoint adjustment --
    "volume_adjust_prompt": """Độc giả đã gửi phản hồi/điều chỉnh sau cho Tập {volume_num}.

Phản hồi: {feedback}

Đề cương tập hiện tại:
{volume_outline}

Hãy chỉnh sửa đề cương tập để tích hợp phản hồi, đồng thời duy trì nhất quán với đề cương tổng thể.

Xuất đề cương tập đã chỉnh sửa bằng Markdown.""",


    # -- Kiểm tra số từ prompts --
    "expand_chapter_system": """Bạn là một nhà văn tiểu thuyết tài năng. Bạn sẽ nhận được một chương quá ngắn cần mở rộng.
Mở rộng chương để đạt số từ mục tiêu mà vẫn giữ chất lượng. KHÔNG thêm nội dung lấp chỗ.

Chiến lược mở rộng:
- Thêm miêu tả chi tiết hơn (môi trường, cảm xúc, chi tiết giác quan)
- Mở rộng trao đổi đối thoại tự nhiên
- Thêm độc thoại nội tâm và phản ứng nhân vật
- Chi tiết hóa cảnh hành động sinh động hơn
- Thêm cảnh chuyển tiếp tạo bầu không khí

QUAN TRỌNG: Chỉ xuất nội dung chương đã mở rộng. Không bình luận meta.""",

    "expand_chapter_prompt": """Chương sau quá ngắn ({current_words} từ). Hãy mở rộng đến khoảng {target_words} từ.

## Hướng dẫn phong cách
{style_guide}

## Đề cương chương
{chapter_outline}

## Nội dung chương hiện tại (quá ngắn)
{chapter_text}

Xuất nội dung chương đã mở rộng ({target_words}+ từ).""",

    "compress_chapter_system": """Bạn là biên tập viên tiểu thuyết giàu kinh nghiệm. Bạn sẽ nhận được một chương quá dài cần rút gọn.
Rút gọn chương mà vẫn giữ tất cả điểm cốt truyện và khoảnh khắc nhân vật quan trọng.

Chiến lược rút gọn:
- Tinh gọn văn phong, loại bỏ miêu tả thừa
- Gộp đối thoại lặp lại
- Tóm tắt cảnh chuyển tiếp ít quan trọng
- Loại bỏ nội dung không đẩy cốt truyện
- Tinh gọn cảnh hành động

QUAN TRỌNG: Tất cả sự kiện cốt truyện, phát triển nhân vật và phục bút phải được giữ lại.
Chỉ xuất nội dung chương đã rút gọn. Không bình luận meta.""",

    "compress_chapter_prompt": """Chương sau quá dài ({current_words} từ). Hãy rút gọn xuống khoảng {target_words} từ.

## Hướng dẫn phong cách
{style_guide}

## Đề cương chương (giữ tất cả sự kiện chính)
{chapter_outline}

## Nội dung chương hiện tại (quá dài)
{chapter_text}

Xuất nội dung chương đã rút gọn (~{target_words} từ). Giữ TẤT CẢ điểm cốt truyện.""",

    "split_chapter_system": """Bạn là biên tập viên tiểu thuyết giàu kinh nghiệm. Bạn sẽ nhận được một chương quá dài nghiêm trọng cần tách thành hai.
Tìm điểm ngắt tự nhiên để tách chương. Mỗi chương sau khi tách:
- Có cung kịch riêng (thiết lập → phát triển → kết thúc hấp dẫn)
- Độ dài tương đương
- Kết thúc tại điểm hồi hộp hoặc chuyển tiếp tự nhiên

Định dạng: Dùng dòng "===CHAPTER_SPLIT===" giữa hai chương.
Mỗi chương bắt đầu bằng dòng tiêu đề.

QUAN TRỌNG: Chỉ xuất hai chương phân cách bằng ===CHAPTER_SPLIT===. Không bình luận.""",

    "split_chapter_prompt": """Chương sau quá dài nghiêm trọng ({current_words} từ, mục tiêu: {min_words}-{max_words} từ). Hãy tách thành hai chương.

## Hướng dẫn phong cách
{style_guide}

## Đề cương chương gốc
{chapter_outline}

## Nội dung chương hiện tại (cần tách)
{chapter_text}

Tách thành hai chương hoàn chỉnh. Dùng "===CHAPTER_SPLIT===" làm dấu phân cách.
Chương {chapter_num_a} là nửa đầu, Chương {chapter_num_b} là nửa sau.
Mỗi chương khoảng {target_words} từ.""",

    # -- Feature #6: Final summary prompts --
    "final_summary_system": """Bạn là nhà phân tích văn học. Tạo báo cáo tổng kết toàn diện cho tiểu thuyết hoàn thành.

Xuất bằng Markdown, bao gồm:
1. **Tổng quan tiểu thuyết** — Tên, thể loại, tổng số từ, số chương
2. **Tóm tắt cốt truyện** — Tóm tắt câu chuyện đầy đủ (có spoiler)
3. **Phân tích cung nhân vật** — Sự phát triển của từng nhân vật chính
4. **Phân tích chủ đề** — Chủ đề cốt lõi và cách triển khai
5. **Tổng quan thống kê** — Số từ mỗi chương, trung bình, chương dài/ngắn nhất
6. **Báo cáo thu hồi phục bút** — Phục bút nào đã gieo và thu hồi
7. **Ghi chú chất lượng** — Chất lượng văn phong tổng thể, cảnh đáng chú ý
8. **Tiềm năng phần tiếp theo** — Các tuyến mở có thể tiếp tục""",

    "final_summary_prompt": """Tạo báo cáo tổng kết cuối cùng cho tiểu thuyết hoàn thành.

## Kế hoạch tiểu thuyết
{plan_json}

## Tóm tắt các chương
{all_briefs}

## Hồ sơ nhân vật
{characters}

## Bảng theo dõi phục bút
{hooks_info}

## Thống kê
- Tổng số chương: {total_chapters}
- Tổng số từ: ~{total_words}

Tạo báo cáo đầy đủ bằng Markdown.""",

    # -- Language enforcement instruction --
    "language_instruction": (
        "**QUAN TRỌNG — YÊU CẦU NGÔN NGỮ**: "
        "Bạn PHẢI viết TẤT CẢ nội dung bằng {native_name} ({english_name}). "
        "Mọi câu, đoạn văn, tiêu đề và nhãn phải được viết bằng {native_name}. "
        "KHÔNG trộn lẫn các ngôn ngữ khác trừ khi trích dẫn danh từ riêng hoặc thuật ngữ chuyên môn."
    ),

    # -- Tiếp tục từ chương đã viết --
    "planner_continue_system": """Bạn là một biên tập viên kế hoạch tiểu thuyết cấp cao. Người dùng đã viết một số chương tiểu thuyết của họ.
Nhiệm vụ của bạn là hiểu nội dung hiện có và giúp người dùng lên kế hoạch tiếp tục câu chuyện.

Bạn đã được cung cấp bản tóm tắt các chương hiện có. Dựa trên nội dung hiện có này, bạn cần:
1. Hiểu các nhân vật, bối cảnh thế giới, giọng điệu và hướng cốt truyện đã được thiết lập
2. Thảo luận với người dùng về hướng đi tiếp theo của câu chuyện
3. Giúp hoàn thiện kế hoạch tiểu thuyết đầy đủ nhất quán với nội dung đã viết
4. Tôn trọng nội dung hiện có — không mâu thuẫn với những gì đã được thiết lập

Các yếu tố cốt lõi cần xác định (một số có thể đã rõ ràng từ các chương hiện có):
1. **Thể loại**: Có thể đã rõ ràng từ nội dung hiện có
2. **Chủ đề cốt lõi**: Điều tiểu thuyết muốn thể hiện
3. **Số từ mục tiêu & Cấu trúc**: Tổng số từ, số từ mỗi chương, số chương ước tính, số quyển
4. **Ngôi kể**: Phải khớp với các chương hiện có
5. **Thẻ cốt lõi**: 3-5 thẻ chính
6. **Tóm tắt một dòng**: Một câu tóm gọn toàn bộ sách
7. **Tóm tắt ba hồi**: Mở đầu (đã viết một phần), phát triển, kết thúc tổng quan
8. **Phong cách viết**: Phải khớp với các chương hiện có
9. **Điều cấm kỵ**: Nội dung không được xuất hiện
10. **Nhân vật chính**: Trích từ hiện có + lên kế hoạch nhân vật mới
11. **Khung thế giới**: Trích từ hiện có + mở rộng

Lưu ý:
- Chỉ hỏi 2-3 câu hỏi liên quan mỗi lượt
- Thể hiện những gì bạn đã nắm được từ các chương hiện có
- Tập trung câu hỏi vào những điều chưa rõ ràng từ nội dung hiện có
- Duy trì phong cách hội thoại thân thiện, chuyên nghiệp""",
    "planner_continue_first_question": """Xin chào! Tôi đã đọc tóm tắt {chapter_count} chương đã có. 🎉

Đây là những gì tôi đã nắm được:
{existing_summary}

Bây giờ hãy lên kế hoạch phần tiếp theo! Tôi có vài câu hỏi:

1. Bạn dự định viết tổng cộng bao nhiêu chương?
2. Bạn có ý tưởng cụ thể nào cho phần tiếp theo không?
3. Bạn muốn giữ nhịp kể chuyện hiện tại hay muốn thay đổi?""",
    "planner_continue_summarize": """Dựa trên bản tóm tắt các chương hiện có và thông tin thu thập trong cuộc trò chuyện, tạo kế hoạch tiểu thuyết hoàn chỉnh.
Kế hoạch phải nhất quán với các chương hiện có. Đối với three_act_summary.beginning, mô tả những gì đã thực sự xảy ra trong các chương hiện có.

Tóm tắt các chương hiện có:
{chapter_summaries}

Xuất ra nghiêm ngặt theo định dạng JSON sau, không có nội dung khác:
{{
    "title": "Tên sách",
    "genre": "Thể loại",
    "theme": "Chủ đề cốt lõi (một đoạn)",
    "target_words": "Tổng số từ mục tiêu",
    "chapter_words": "Phạm vi số từ mỗi chương",
    "total_chapters": "Số chương ước tính (bao gồm đã viết)",
    "volumes": "Số và cách chia quyển",
    "pov": "Ngôi kể (phải khớp với các chương hiện có)",
    "tags": "Thẻ cốt lõi (phân cách bằng dấu phẩy)",
    "one_line_summary": "Tóm tắt một dòng",
    "three_act_summary": {{
        "beginning": "Mở đầu (tóm tắt những gì đã xảy ra trong các chương hiện có)",
        "middle": "Phát triển (tổng quan phần giữa)",
        "end": "Kết thúc (tổng quan kết thúc)"
    }},
    "style_guide": "Yêu cầu và quy chuẩn phong cách viết (khớp với các chương hiện có)",
    "taboos": "Điều cấm kỵ",
    "main_characters": [
        {{
    "main_characters": [
        {{
            "name": "Tên",
            "role": "Vai trò (nhân vật chính/phản diện/phụ v.v.)",
            "age": "Tuổi (BẮT BUỘC suy luận từ các chương hiện có — vd: nếu là học sinh cấp 3 thì tuổi phải ~15-18, KHÔNG được đặt tùy tiện)",
            "appearance": "Mô tả ngoại hình",
            "personality": "Mô tả tính cách",
            "background": "Câu chuyện nền",
            "motivation": "Động lực cốt lõi",
            "arc": "Vòng cung nhân vật/quỹ đạo phát triển"
        }}
    ],
    "world_setting": "Mô tả khung thế giới",
    "synopsis": "Tóm tắt tiểu thuyết (để xuất bản)"
}}""",
    "chapter_summary_prompt": """Đọc chương sau và tạo tóm tắt ngắn gọn.

## Chương {chapter_num}
{chapter_text}

Xuất JSON:
{{
    "chapter_num": {chapter_num},
    "title": "tiêu đề ngắn",
    "summary": "tóm tắt 2-3 câu",
    "characters": ["nhân vật"],
    "setting": "Bối cảnh/địa điểm (vd: trường cấp 3, lâu đài, trạm vũ trụ)",
    "time_period": "Thời đại/độ tuổi nhân vật (vd: học sinh cấp 3 ~16 tuổi, thời phong kiến, tương lai 2200s). Ghi rõ khoảng tuổi nếu nhận biết được.",
    "key_events": ["sự kiện"],
    "unresolved_hooks": ["mồi câu chưa giải"],
    "pov": "góc nhìn",
    "tone": "giọng điệu"
}}

Chỉ xuất JSON.""",
    "master_outline_continue_prompt": """Hãy tạo đề cương tổng thể cho toàn bộ sách dựa trên kế hoạch tiểu thuyết sau.
Quan trọng: {existing_count} chương đầu tiên đã được viết xong. Đề cương phải nhất quán với nội dung hiện có, không được mâu thuẫn.

## Kế hoạch tiểu thuyết
{plan_json}

## Tóm tắt các chương hiện có
{chapter_summaries}

Tạo đề cương tổng thể bao quát tất cả các quyển (định dạng Markdown). Mỗi quyển cần có:
- Mô tả cốt truyện chính
- Xung đột cốt lõi
- Sự kiện chính (danh sách đánh số)
- Trạng thái nhân vật chính
- Cao trào của quyển
- Điểm treo của quyển
- Kết nối với quyển tiếp theo

Đảm bảo đề cương các chương đầu phản ánh chính xác nội dung đã viết.""",
})

# ============================================================
# TEMPLATES: Mẫu Markdown (tiếng Việt đầy đủ)
# ============================================================
TEMPLATES = dict(_BASE_TEMPLATES)
TEMPLATES.update({
    "readme": """# 📖 Dự án Viết Tiểu Thuyết

## Thông tin cơ bản
- **Tên sách**: "{title}"
- **Thể loại**: {genre}
- **Số từ mục tiêu**: {target_words}
- **Số từ mỗi chương**: {min_words}-{max_words}
- **Số chương dự kiến**: {total_chapters}
- **Số tập**: {volumes}
- **Góc nhìn**: {pov}
- **Thẻ cốt lõi**: {tags}

## Tóm tắt một câu
{one_line_summary}

## 📁 Cấu trúc thư mục

```
{title}/
├── README.md              # Tổng quan dự án
├── meta/                  # Quản lý thông tin meta
│   ├── progress.md        # Theo dõi tiến độ viết
│   ├── style_guide.md     # Hướng dẫn phong cách
│   └── hooks_tracker.md   # Theo dõi phục bút
├── worldbuilding/         # Thiết lập thế giới
│   ├── characters.md      # Hồ sơ nhân vật
│   ├── world_setting.md   # Tổng quan thế giới
│   └── ...                # Các tệp thiết lập khác
├── plot/                  # Quản lý cốt truyện
│   ├── master_outline.md  # Đề cương tổng thể
│   ├── volume_XX.md       # Đề cương từng tập
│   └── chapter_briefs.md  # Tóm tắt chương
└── chapters/              # Nội dung chương
    ├── chapter_001.txt    # Chương 1
    └── ...
```

## 🔄 Quy trình viết
1. Đọc progress.md → Kiểm tra tiến độ
2. Đọc chapter_briefs.md → Xem lại các chương gần đây
3. Tham khảo đề cương tập hiện tại → Xác nhận nội dung chương
4. Kiểm tra hooks_tracker.md → Xem trạng thái phục bút
5. Tham khảo characters.md → Xác nhận trạng thái nhân vật
6. Xuất nội dung chương vào chapters/
7. Cập nhật progress.md, chapter_briefs.md, v.v.
""",

    "progress": """# 📊 Theo dõi Tiến độ Viết

## Trạng thái hiện tại
- **Chương hoàn thành gần nhất**: Chưa bắt đầu
- **Đang viết**: Chưa xác định
- **Tập hiện tại**: Tập 1
- **Tổng số từ**: 0
- **Cập nhật lần cuối**: -

## Bước tiếp theo
> 1. ~~Xác định thể loại~~ ✅
> 2. ~~Thiết lập cốt lõi và nhân vật chính~~ ✅
> 3. ~~Đề cương tổng thể~~ ✅
> 4. **Hoàn thành đề cương Tập 1** ← Hiện tại
> 5. Bắt đầu viết

## Danh sách chương đã hoàn thành

| Chương | Tiêu đề | ~Số từ | Sự kiện chính |
|--------|---------|--------|---------------|

## Trạng thái nhân vật hiện tại
(Chờ cập nhật)

## Việc cần làm
- [x] Xác định thể loại
- [x] Hoàn thành xây dựng thế giới
- [x] Hoàn thành hồ sơ nhân vật
- [x] Hoàn thành đề cương tổng thể
- [ ] Hoàn thành đề cương Tập 1
- [ ] Nội dung Chương 1
""",

    "hooks_tracker": """# 🎣 Theo dõi Phục bút/Điểm nhấn

> Ghi lại tất cả phục bút và hồi hộp, theo dõi trạng thái
> Trạng thái: 🔴 Đã gieo chưa thu | 🟡 Tiết lộ một phần | 🟢 Đã thu hồi | ⚪ Đã lên kế hoạch

---

## Phục bút dài hạn (xuyên tập)

| ID | Nội dung | Gieo ở chương | Thu hồi dự kiến | Trạng thái | Ghi chú |
|----|----------|---------------|-----------------|------------|---------|

## Phục bút ngắn hạn (trong tập hiện tại)

| ID | Nội dung | Gieo ở chương | Thu hồi dự kiến | Trạng thái | Ghi chú |
|----|----------|---------------|-----------------|------------|---------|

## Lịch sử thu hồi

| ID | Nội dung | Gieo ở chương | Thu ở chương | Ghi chú |
|----|----------|---------------|-------------|---------|
""",

    "chapter_briefs": """# 📝 Tóm tắt Chương

> Ghi tóm tắt sau mỗi chương, dùng để xem lại nhanh
> Định dạng: Chương | Tiêu đề | Số từ | Sự kiện chính | Thay đổi nhân vật | Phục bút

---
""",

    "synopsis_title": "# Tóm tắt Tiểu thuyết\n\n",

    "chapter_brief_entry": """
### Chương {chapter_num} · {title} (~{word_count} từ)
**Sự kiện chính**:
""",
    "character_changes_header": "\n**Thay đổi trạng thái nhân vật**:\n",
    "hooks_planted_header": "\n**Phục bút mới**:\n",
    "next_hook_prefix": "\n**Điểm nhấn chương sau**: ",

    "progress_update_entry": """
---
### Cập nhật hoàn thành Chương {chapter_num}
- **Hoàn thành gần nhất**: {latest_chapter}
- **Tổng từ tích lũy**: ~{total_words}
""",
    "character_status_header": "\n**Trạng thái nhân vật nhanh**:\n",

    "final_summary_filename": "meta/final_summary.md",
})

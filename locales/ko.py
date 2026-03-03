"""
한국어 언어 파일
"""
from locales.en import UI as _BASE_UI, PROMPTS as _BASE_PROMPTS, TEMPLATES as _BASE_TEMPLATES

# ============================================================
# UI: 사용자 인터페이스 문자열 (영어 기반 + 한국어 덮어쓰기)
# ============================================================
UI = dict(_BASE_UI)
UI.update({
    "welcome_title": "📖 소설 창작 도우미 v1.0",
    "welcome_subtitle": "   AI 기반 자동 소설 창작 시스템",
    "no_backend": "\n❌ 사용 가능한 LLM 연결 방식이 없습니다!",
    "no_backend_hint": "   llm_openai.py 또는 llm_local.py 중 하나 이상이 존재하는지 확인하세요",
    "select_api_mode": "\n🔌 LLM API 연결 방식을 선택하세요:",
    "api_openai_desc": "OpenAI 표준 형식 (API 키 필요)",
    "api_local_desc": "로컬 서버 API",
    "auto_selected": "\n  ({desc}만 감지됨, 자동 선택)",
    "input_choice": "\n👤 선택을 입력하세요 (1-{max}): ",
    "invalid_choice": "잘못된 선택입니다. 1-{max}을 입력하세요",
    "input_openai_key": "OpenAI API 키를 입력하세요: ",
    "api_key_empty": "API 키는 비워둘 수 없습니다!",
    "input_base_url": "API Base URL (기본값 사용시 Enter: {default}): ",
    "input_model": "모델 이름 (기본값 사용시 Enter: {default}): ",
    "input_local_url": "로컬 API 주소를 입력하세요: ",
    "api_url_empty": "API 주소는 비워둘 수 없습니다!",
    "input_api_key": "API 키를 입력하세요 (건너뛰려면 Enter): ",
    "input_wsid": "WSID를 입력하세요 (건너뛰려면 Enter): ",
    "input_model_marker": "모델 식별자를 입력하세요 (건너뛰려면 Enter): ",
    "project_setup": "\n📁 프로젝트 설정",
    "input_novel_name": "👤 소설 프로젝트 이름을 입력하세요 (폴더 생성용): ",
    "scan_projects_header": "\n📂 기존 프로젝트 발견:",
    "no_existing_projects": "\n📂 기존 프로젝트가 없습니다.",
    "project_status_chapters": "{count}장",
    "project_status_plan": "계획",
    "project_status_meta": "메타",
    "project_status_plot": "개요",
    "or_input_manually": "프로젝트 이름 직접 입력...",
    "select_project_prompt": "\n👤 프로젝트를 선택하세요 (1-{max}): ",
    "select_operation": "\n🎯 작업을 선택하세요:",
    "op_full": "  1. 처음부터 시작 (전체 흐름)",
    "op_resume": "  2. 중단된 곳에서 이어쓰기",
    "op_planning": "  3. 기획 단계만",
    "op_worldbuilding": "  4. 세계관 & 문체 지침 작성만",
    "op_outline": "  5. 개요 생성만",
    "op_writing": "  6. 집필만 (기존 개요 필요)",
    "op_batch": "  7. 배치 모드 (여러 소설 연속 생성)",
    "input_op_choice": "\n👤 선택을 입력하세요 (1-7): ",
    "invalid_op": "잘못된 선택입니다. 1-7을 입력하세요",
    "input_volume_num": "몇 권의 세부 줄거리를 만드시겠습니까? (번호 입력, 또는 Enter로 건너뛰기): ",
    "input_start_chapter": "몇 장부터 시작하시겠습니까? (Enter로 1장부터): ",
    "input_end_chapter": "몇 장까지 쓰시겠습니까? (Enter로 끝까지): ",
    "interrupted": "\n\n⏸️ 사용자가 중단했습니다. 진행 상황이 저장되었습니다. 다음에 '중단된 곳에서 이어쓰기'를 선택하세요.",
    "error_occurred": "\n❌ 오류 발생: {error}",
    "goodbye": "\n👋 안녕히 가세요!",

    # -- 배치 모드 --
    "batch_input_names": "\n📚 소설 이름을 쉼표로 구분하여 입력하세요 (예: 소설A, 소설B, 소설C):",
    "batch_empty": "❌ 소설 이름이 입력되지 않았습니다. 메인 메뉴로 돌아갑니다.",
    "batch_select_op": "\n🎯 각 소설에 대한 작업을 선택하세요:",
    "batch_start": "\n🚀 배치 모드: {total}편의 소설을 순서대로 생성합니다: {names}",
    "batch_progress": "📖 [{current}/{total}] 소설 시작: {name}",
    "batch_novel_done": "✅ 소설 '{name}' 완료!",
    "batch_interrupted": "\n⏸️ '{name}' 집필 중 중단됨. 나머지 {remaining}편 미완료.",
    "batch_continue_prompt": "나머지 소설을 계속 생성하시겠습니까? (y/n): ",
    "batch_stopped": "🛑 배치 처리가 중지되었습니다.",
    "batch_novel_error": "\n❌ 소설 '{name}' 생성 중 오류: {error}",
    "batch_all_done": "\n🎉 배치 완료! 총 {total}편의 소설이 모두 생성되었습니다.",

    "select_language": "\n🌐 소설에 사용할 언어를 선택하세요:",
    "lang_choice_prompt": "\n👤 선택을 입력하세요 (1-{max}): ",
    "phase_planning_title": "\n📝 1단계: 소설 구상",
    "planner_prefix": "\n🤖 기획 도우미:\n",
    "user_prefix": "👤 당신: ",
    "input_empty_hint": "(답변을 입력하세요)",
    "multiline_hint": "(여러 줄 입력 가능, 빈 줄로 완료. /paste 로 붙여넣기 모드)",
    "multiline_paste_hint": "(붙여넣기 모드: 빈 줄 포함 자유롭게 붙여넣기 가능, /end 로 완료)",
    "quit_planning": "구상 단계를 종료했습니다.",
    "force_done": "알겠습니다, 기획안을 정리하겠습니다...",
    "generating_plan": "\n⏳ 완전한 소설 기획안을 작성 중...",
    "plan_display_title": "\n📋 소설 기획안",
    "plan_label_title": "제목",
    "plan_label_genre": "장르",
    "plan_label_theme": "핵심 주제",
    "plan_label_target_words": "목표 분량",
    "plan_label_total_chapters": "예상 장 수",
    "plan_label_volumes": "권 수",
    "plan_label_pov": "시점",
    "plan_label_tags": "태그",
    "plan_label_one_line": "한 줄 줄거리",
    "plan_label_beginning": "발단",
    "plan_label_middle": "전개",
    "plan_label_end": "결말",
    "plan_label_characters": "주요 캐릭터",
    "confirm_plan": "\n👤 이 기획안에 만족하십니까? (y/수정 의견): ",
    "adjusting_plan": "\n⏳ 의견에 따라 기획안을 수정 중...",
    "plan_confirmed": "✅ 기획안이 확정되어 저장되었습니다!",
    "rename_dir_prompt": "\n📁 소설 제목은 \"{title}\"이지만 프로젝트 디렉터리는 \"{dir}\"입니다.",
    "rename_dir_confirm": "   프로젝트 디렉터리를 \"{title}\"으로 이름을 바꾸시겠습니까? (y/n): ",
    "rename_dir_done": "  ✅ 프로젝트 디렉터리 이름 변경 완료: {path}",
    "rename_dir_exists": "  ⚠️ 디렉터리가 이미 존재합니다: {path}",
    "rename_dir_failed": "  ❌ 이름 변경 실패: {error}",
    "phase_world_title": "\n🌍 2단계: 세계관 구축 & 문체 지침 (동시 생성 중...)",
    "world_done": "✅ 세계관 설정 완료 ({count}개 문서)",
    "world_failed": "❌ 세계관 생성 실패: {error}",
    "style_done": "✅ 문체 지침 작성 완료",
    "style_failed": "❌ 문체 지침 생성 실패: {error}",
    "phase_outline_title": "\n📋 3단계: 전체 줄거리 작성",
    "generating_outline": "⏳ 전체 줄거리를 작성 중...",
    "outline_done": "✅ 전체 줄거리 작성 완료",
    "outline_review": "\n📖 전체 줄거리가 plot/master_outline.md에 저장되었습니다. 확인해 주세요.",
    "press_enter_continue": "👤 Enter를 눌러 제1권 세부 줄거리 생성을 계속...",
    "generating_volume": "📑 제{num}권 세부 줄거리를 작성 중...",
    "volume_done": "✅ 제{num}권 세부 줄거리 작성 완료",
    "phase_writing_title": "\n✍️ 5단계: 집필 시작",
    "checkpoint_resume": "[이어쓰기] {count}장 완료 확인, 제{next}장부터 재개",
    "volume_not_found": "⚠️ 제{num}권 세부 줄거리를 찾을 수 없습니다, 작성 중...",
    "generating_volume_outline": "⏳ 제{num}권 세부 줄거리를 작성 중...",
    "writing_chapter": "📖 제{num}장 집필 중...",
    "chapter_done": "  ✅ 제{num}장 집필 완료 (~{words}자)",
    "post_processing": "  ⏳ 정보 정리 및 갱신 중...",
    "post_done": "  ✅ 제{num}장 뒷정리 완료",
    "post_failed": "  ⚠️ 제{num}장 뒷정리 분석 실패, 갱신 건너뜀",
    "chapter_error": "  ❌ 제{num}장 집필 오류: {error}",
    "retry_prompt": "  재시도하시겠습니까? (y/n): ",
    "skip_chapter": "  제{num}장을 건너뛰고 다음 장으로",
    "pause_prompt": "\n📊 제{num}장 완료. Enter로 계속, 'stop'으로 일시 정지",
    "pause_input": "👤 ",
    "paused": "⏸️ 일시 정지됨. 다음에 제{next}장부터 이어쓰기 가능",
    "writing_complete": "🎉 집필 단계 완료!",
    "planning_incomplete": "구상 단계가 완료되지 않아 종료합니다.",
    "no_plan_found": "기획안을 찾을 수 없습니다. 처음부터 시작합니다...",
    "resume_checking": "🔄 프로젝트 상태 확인 중...",
    "resume_completed": "{count}장 완료됨, 집필 계속...",
    "no_style_guide": "문체 지침을 찾을 수 없습니다. 작성 중...",
    "no_outline": "전체 줄거리를 찾을 수 없습니다. 작성 중...",
    "plan_not_found_error": "기획안 파일 plan.json을 찾을 수 없습니다. 먼저 구상 단계를 실행하세요",
    "worldbuilding_start": "[세계관 도우미] {count}개 설정 문서 동시 생성 시작...",
    "doc_done": "  ✅ {filename} 생성 완료",
    "doc_failed": "  ❌ {filename} 생성 실패",
    "doc_error": "  ❌ {filename} 오류: {error}",
    "llm_error_retry": "죄송합니다, 문제가 발생했습니다. 다시 말씀해 주세요~",
    "info_enough": "정보가 충분합니다! 완전한 소설 기획서를 정리하겠습니다... 🎯",
    "continue_input": "쓰고 싶은 소설에 대해 더 알려주세요~",
    "config_loaded": "[설정] {file}에서 설정을 불러왔습니다: {keys}",
    "novel_config_loaded": "[설정] 소설별 설정 {file}에서 불러왔습니다: {keys}",
    "novel_config_skipped": "  ⚠️ {file}의 API/경로 키를 건너뛰었습니다 (전역 설정 사용): {keys}",
    "novel_config_auto_created": "[설정] 템플릿에서 {file}을 자동 생성했습니다 (이 소설의 설정을 편집할 수 있습니다)",
    "config_not_found": "[설정] {file}을 찾을 수 없습니다. 비밀 정보는 실행 시 직접 입력해야 합니다",
"config_hint": "[설정] user_config.example.json을 참고하여 {file}을 만들어 주세요",
    "project_initialized": "[프로젝트] 폴더 준비 완료: {path}",
    "openai_initialized": "[LLM-OpenAI] 연결 완료, 모델: {model}, 주소: {url}",
    "openai_need_package": "OpenAI 연결에는 openai 패키지가 필요합니다: pip install openai",
"openai_no_key": "OPENAI_API_KEY가 설정되지 않았습니다. user_config.json에 적어두거나 실행 시 입력하세요",
    "openai_attempt_failed": "[LLM-OpenAI] {n}번째 시도 실패: {error}",
    "openai_retry_wait": "[LLM-OpenAI] {wait}초 후 재시도...",
    "openai_max_retries": "[LLM-OpenAI] 최대 재시도 횟수({max})에 도달, 포기",
    "local_initialized": "[LLM-Local] 연결 완료, 주소: {url}, 모델 식별자: {marker}",
    "local_need_package": "로컬 연결에는 requests 패키지가 필요합니다: pip install requests",
"local_no_url": "LOCAL_API_URL이 설정되지 않았습니다. user_config.json에 적어두세요",
    "local_attempt_failed": "[LLM-Local] {n}번째 시도 실패: {error}",
    "local_retry_wait": "[LLM-Local] {wait}초 후 재시도...",
    "local_max_retries": "[LLM-Local] 최대 재시도 횟수({max})에 도달, 포기",
    "cannot_load_openai": "OpenAI 연결을 불러올 수 없습니다: {error}\nllm_openai.py가 존재하고 openai가 설치되어 있는지 확인하세요",
    "cannot_load_local": "로컬 연결을 불러올 수 없습니다: {error}\nllm_local.py가 존재하고 requests가 설치되어 있는지 확인하세요",
    "unsupported_api_mode": "지원되지 않는 API 연결 방식: {mode}. 선택 가능: 'openai', 'local'",
    "file_written": "[저장소] 기록 완료: {path}",
    "outline_multi_draft_title": "\n📋 3단계: 전체 줄거리 작성 (여러 초안 비교)",
    "generating_draft": "  ⏳ 줄거리 초안 {num}/{total} 작성 중 (유형: {style})...",
    "draft_done": "  ✅ 초안 {num} 완료",
    "draft_failed": "  ❌ 초안 {num} 실패: {error}",
    "draft_comparison_title": "\n📊 줄거리 초안 비교",
    "draft_header": "\n{'─' * 40}\n📄 초안 {num} — 유형: {style}\n{'─' * 40}",
    "draft_select_prompt": "\n👤 사용할 초안을 선택하세요 (1-{max}), 또는 'm'으로 장점만 모아 합치기: ",
    "draft_merging": "⏳ 모든 초안의 장점을 모아 합치는 중...",
    "draft_selected": "✅ 초안 {num}을 전체 줄거리로 채택",
    "draft_merged": "✅ 합친 줄거리가 완성되었습니다",
    "outline_drafts_truncating": "   ⚠️ 줄거리 초안이 너무 깁니다 (추정 {total} 토큰, 예산 {budget}), 각 초안을 균등하게 잘라냅니다...",
    "draft_invalid": "잘못된 선택입니다. 1-{max} 또는 'm'을 입력하세요",
    "parallel_review_title": "  🔍 품평 진행 중 (세 방향 동시 검토)...",
    "review_consistency": "[앞뒤 일관성 검토]",
    "review_style": "[문체 검토]",
    "review_foreshadowing": "[복선 검토]",
    "review_done": "  ✅ {reviewer}: {count}건의 지적 사항 (확신도≥{threshold})",
    "review_failed": "  ⚠️ {reviewer} 검토 실패: {error}",
    "review_no_issues": "  ✅ 모든 검토 통과 — 주요 문제 없음!",
    "review_issues_found": "  ⚠️ 전체 검토에서 총 {count}건의 지적 사항:",
    "review_issue_item": "    [{severity}] ({reviewer}, 확신도: {confidence}) {description}",
    "review_critical_prompt": "  🚨 심각한 문제가 발견되었습니다. 이 장을 다시 쓰시겠습니까? (y/n): ",
    "polish_start": "  ✨ 다듬기 시작 (최대 {max_iter}회 반복)...",
    "polish_iteration": "  ✨ 다듬기 {iter}/{max_iter}회차...",
    "polish_score": "  📊 품질 점수: {score}/10 (기준: {threshold})",
    "polish_passed": "  ✅ 기준 점수 달성! 다듬기 완료.",
    "polish_improving": "  ⏳ 점수가 기준 미만, 개선 중...",
    "polish_max_reached": "  ⚠️ 최대 다듬기 횟수에 도달. 가장 나은 판본 사용 (점수: {score}/10).",
    "polish_failed": "  ⚠️ 다듬기 평가 실패, 현재 판본 유지.",
    "volume_checkpoint_title": "\n📍 제{num}권 중간 점검",
    "volume_checkpoint_summary": "  현재 진행: {completed}장 완료, 약 {words}자",
    "volume_checkpoint_prompt": "\n👤 제{num}권을 시작합니다. 계속하시겠습니까? (y / adjust / stop): ",
    "volume_checkpoint_adjust": "👤 수정 의견을 입력하세요: ",
    "volume_checkpoint_adjusting": "⏳ 의견에 따라 권별 줄거리를 수정 중...",
    "volume_checkpoint_stopped": "⏸️ 제{num}권 앞에서 정지. 다음에 제{next}장부터 이어쓰기.",
    "severity_critical": "심각",
    "severity_major": "주요",
    "severity_minor": "경미",
    "severity_info": "정보",
    "final_summary_title": "\n📊 완결 보고서 작성 중...",
    "final_summary_done": "✅ 완결 보고서가 작성되어 저장되었습니다!",
    "final_summary_failed": "⚠️ 완결 보고서 작성 실패: {error}",

    # -- 집필 매개변수 확인 --
    "writing_params_title": "\n⚙️ 집필 매개변수 확인",
    "ask_chapter_min_words": "   장당 최소 글자 수 (현재: {current}, Enter로 유지): ",
    "ask_chapter_max_words": "   장당 최대 글자 수 (현재: {current}, Enter로 유지): ",
    "writing_params_swapped": "   ⚠️ 최솟값 > 최댓값이므로 값을 교환했습니다.",
    "ask_word_count_check": "   글자 수 검사를 활성화할까요? (현재: {status}, y/n, Enter로 유지): ",
    "ask_lazy_mode": "   자동 모드(모두 자동 확인)를 활성화할까요? (현재: {status}, y/n, Enter로 유지): ",
    "writing_params_summary": "   ✅ 집필 매개변수: {min}~{max}자/장, 글자 수 검사: {check}, 자동 모드: {lazy}",

    # -- 대화 인용부호 스타일 --
    "quote_style_title": "\n💬 대화 인용부호 스타일 설정",
    "quote_style_prompt": "\n👤 소설의 대화에 사용할 인용부호 스타일을 선택하세요 (1-{max}): ",
    "quote_style_invalid": "잘못된 선택입니다. 1-{max}을 입력하세요",
    "quote_style_selected": "✅ 대화 인용부호 스타일 설정 완료: {style}",
    "quote_style_option_curly": '\u201c\u201d 큰따옴표 (예: \u201c안녕하세요!\u201d)',
    "quote_style_option_corner": '「」 낫표 (예: 「안녕하세요!」)',
    "quote_style_option_guillemet": '«» 겹화살괄호 (예: «안녕하세요!»)',
    "quote_style_option_dash": '— 줄표 대화 (예: — 안녕하세요!)',
    "quote_style_option_straight": '"" 곧은따옴표 (예: "안녕하세요!")',

    # -- 심리 활동 인용부호 스타일 --
    "inner_quote_title": "\n💭 심리 활동/내면 독백 인용부호 스타일 설정",
    "inner_quote_prompt": "\n👤 소설의 심리 묘사에 사용할 스타일을 선택하세요 (1-{max}): ",
    "inner_quote_invalid": "잘못된 선택입니다. 1-{max}을 입력하세요",
    "inner_quote_selected": "✅ 심리 활동 인용부호 스타일 설정 완료: {style}",
    "inner_quote_option_corner_double": '『』 겹낫표 (예: 『조심해야 해』)',
    "inner_quote_option_corner": '「」 낫표 (예: 「조심해야 해」)',
    "inner_quote_option_curly_single": '\u2018\u2019 작은따옴표 (예: \u2018조심해야 해\u2019)',
    "inner_quote_option_italic": '*이탤릭체* 심리 묘사 (예: *조심해야 해*)',
    "inner_quote_option_dash": '——줄표 (예: ——조심해야 해——)',
    "inner_quote_option_paren": '（） 전각 괄호 (예: （조심해야 해）)',
    "inner_quote_option_same": '대화와 동일한 스타일',
    "inner_quote_option_none": '특수 기호 없음 (서술로 심리 묘사)',

    # -- 인용부호 규칙 (스타일 가이드/작성 프롬프트에 삽입) --
    "quote_rules_heading": "인용부호 스타일 규칙",
    "quote_rule_dialogue_curly": '모든 대화에 \u201c\u201d (큰따옴표)를 사용하세요. 예: \u201c안녕하세요!\u201d',
    "quote_rule_dialogue_corner": '모든 대화에 「」 (낫표)를 사용하세요. 예: 「안녕하세요!」',
    "quote_rule_dialogue_guillemet": '모든 대화에 «» (겹화살괄호)를 사용하세요. 예: «안녕하세요!»',
    "quote_rule_dialogue_dash": '대화에 — (줄표)를 사용하세요. 예: — 안녕하세요!',
    "quote_rule_dialogue_straight": '모든 대화에 "" (곧은따옴표)를 사용하세요. 예: "안녕하세요!"',
    "quote_rule_inner_corner_double": '심리 묘사/내면 독백에 『』 (겹낫표)를 사용하세요. 예: 『조심해야 해』',
    "quote_rule_inner_corner": '심리 묘사/내면 독백에 「」 (낫표)를 사용하세요. 예: 「조심해야 해」',
    "quote_rule_inner_curly_single": '심리 묘사/내면 독백에 \u2018\u2019 (작은따옴표)를 사용하세요. 예: \u2018조심해야 해\u2019',
    "quote_rule_inner_italic": '심리 묘사/내면 독백에 *이탤릭*을 사용하세요. 예: *조심해야 해*',
    "quote_rule_inner_dash": '심리 묘사/내면 독백에 ——(줄표)를 사용하세요. 예: ——조심해야 해——',
    "quote_rule_inner_paren": '심리 묘사/내면 독백에 （）(전각 괄호)를 사용하세요. 예: （조심해야 해）',
    "quote_rule_inner_none": '심리 묘사에 특수 인용부호를 사용하지 마세요. 서술로 심리를 표현하세요.',
    "quote_rule_inner_same": '심리 묘사/내면 독백에도 대화와 동일한 인용부호를 사용하세요.',

    # -- 자동 모드 --
    "lazy_mode_enabled": "🛋️ 자동 모드 ON — 개요 확정 후 모두 자동으로 진행됩니다!",
    "lazy_auto_merge": "🛋️ [자동] 모든 개요 초안 자동 통합 중...",
    "lazy_auto_select": "🛋️ [자동] 초안이 하나뿐이므로 자동 선택했습니다.",
    "lazy_auto_continue": "🛋️ [자동] 자동 계속...",
    "lazy_auto_retry": "🛋️ [자동] 자동 재시도...",
    "lazy_auto_skip": "🛋️ [자동] 자동 건너뛰기...",
    "lazy_auto_volume_continue": "🛋️ [자동] 제{num}권으로 자동 계속...",

    # -- 심사 재시도 --
    "review_retry_feedback": """⚠️ 중요: {attempt}/{max_attempts}번째 재작성입니다. 이전 버전에 다음과 같은 심각/주요 문제가 있었으며 반드시 수정해야 합니다:
{issues}

전체 장을 처음부터 다시 작성하여 위의 모든 문제를 수정하되, 전체 스토리, 톤, 구조는 유지해 주세요.""",
    "review_max_retries_reached": "  ⚠️ 제{num}장 최대 심사 재시도 횟수({max}회)에 도달했습니다. 현재 버전을 저장하고 계속합니다.",



    # -- 글자 수 검증 --
    "wordcount_check_start": "  📏 글자 수 검증: {words}자 (목표: {min}-{max})",
    "wordcount_too_short": "  ⚠️ 장이 너무 짧습니다 ({words}자, 최소 {min}자). 확장 중...",
    "wordcount_too_long": "  ⚠️ 장이 너무 깁니다 ({words}자, 최대 {max}자). 압축 중...",
    "wordcount_split_needed": "  📑 장이 심각하게 초과됨 ({words}자, ≥{threshold}% 상한). 두 장으로 분할 중...",
    "wordcount_expand_done": "  ✅ 확장 완료: {words}자",
    "wordcount_compress_done": "  ✅ 압축 완료: {words}자",
    "wordcount_split_done": "  ✅ 분할 완료: 제{num_a}장 ({words_a}자) + 제{num_b}장 ({words_b}자)",
    "wordcount_retry": "  🔄 글자 수 검증 재시도 {attempt}/{max_attempts}...",
    "wordcount_give_up": "  ⚠️ {max_attempts}회 재시도 후에도 미달, 현재 버전 사용 ({words}자).",
    "wordcount_ok": "  ✅ 글자 수 적합: {words}자",
    "wordcount_split_renumber": "  📝 참고: 분할 후 이후 장 번호가 자동으로 재조정됩니다.",

    # -- Feature #1: Multi-draft outline styles --
    "outline_style_dramatic": "극적 긴장형",
    "outline_style_literary": "문학·캐릭터 중심형",
    "outline_style_commercial": "상업·빠른 전개형",
})

# ============================================================
# PROMPTS: LLM 프롬프트 템플릿 (한국어 완전 번역)
# ============================================================
PROMPTS = dict(_BASE_PROMPTS)
PROMPTS.update({
    # -- 기획 에이전트 --
    "planner_system": """당신은 경험이 풍부한 소설 기획 편집자입니다. 처음부터 소설의 핵심 설정을 구상하는 데 능숙합니다.
사용자와의 대화를 통해 다음 소설 핵심 요소를 결정하기 위한 충분한 정보를 수집하는 것이 당신의 임무입니다:

1. **장르/유형**: 판타지, 현대, 미스터리, 로맨스, SF 등
2. **핵심 주제**: 소설이 표현하고자 하는 것
3. **목표 분량과 구조**: 총 분량, 장당 분량, 예상 장 수, 권 수
4. **서술 시점**: 1인칭/3인칭
5. **핵심 태그**: 3-5개 키워드
6. **한 줄 줄거리**: 전체 책을 요약하는 한 문장
7. **삼막 줄거리**: 발단, 전개, 결말 개요
8. **문체 요구사항**: 문체, 톤, 참고 작품
9. **금기 사항**: 포함되어서는 안 되는 내용
10. **주요 캐릭터**: 최소한 주인공의 기본 설정
11. **세계관 프레임워크**: 이야기가 전개되는 세계 배경

사용자에게 적극적으로 질문하여 정보를 수집하세요. 사용자가 직접 결정하고 싶지 않은 부분은 창의적으로 보완하세요.
정보가 충분하다고 판단되면 최종 소설 기획서를 출력하세요.

주의:
- 한 번에 2-3개의 관련 질문만
- 사용자 답변에 따라 유연하게 후속 질문 조정
- 각 요소에 대해 사용자가 직접 지정할지 당신에게 맡길지 명확히 확인
- 친근하고 전문적인 대화 스타일 유지""",

    "planner_first_question": """안녕하세요! 소설 기획 어시스턴트입니다~ 🎉

창작을 시작하기 전에, 당신의 아이디어를 듣고 싶습니다. 단계적으로 진행하겠습니다:

**먼저, 가장 기본적인 질문:**
1. 어떤 **장르/유형**의 소설을 쓰고 싶으신가요? (예: 판타지, 현대, 미스터리, SF, 로맨스, 역사 등)
2. 대략적인 **스토리 방향**이나 **핵심 아이디어**가 있으신가요? 모호한 생각이라도 괜찮습니다
3. 이런 기본 설정을 직접 지정하시겠습니까, 아니면 제가 브레인스토밍을 도와드릴까요?

편하게 이야기해 주세요~""",

    "planner_check_enough": """지금까지 수집된 모든 정보를 분석하고 기획을 시작하기에 충분한지 판단하세요.

핵심 요소 체크리스트:
1. 장르/유형 - {has_genre}
2. 핵심 주제 - {has_theme}
3. 목표 분량과 구조 - {has_structure}
4. 서술 시점 - {has_pov}
5. 핵심 태그 - {has_tags}
6. 한 줄 줄거리 - {has_summary}
7. 문체 요구사항 - {has_style}
8. 주요 캐릭터 (최소한 주인공 개념) - {has_characters}
9. 세계관 프레임워크 - {has_world}

JSON 형식으로 답하세요:
{{
    "is_enough": true/false,
    "missing_items": ["부족한 요소 목록"],
    "next_questions": "정보가 부족할 경우, 사용자에게 물어볼 다음 질문들 (2-3개)"
}}

JSON만 반환하세요.""",

    "planner_summarize": """다음 대화에서 수집된 정보를 바탕으로 완전한 소설 기획서를 생성하세요.
사용자가 명시적으로 지정하지 않은 부분은 창의적으로 보완하여 전체 기획이 일관되고 매력적이 되도록 하세요.

다음 JSON 형식으로 엄밀하게 출력하세요:
{{
    "title": "책 제목",
    "genre": "장르/유형",
    "theme": "핵심 주제 (한 문단)",
    "target_words": "목표 총 글자 수",
    "chapter_words": "장당 글자 수 범위",
    "total_chapters": "예상 총 장 수",
    "volumes": "권 수와 분할",
    "pov": "서술 시점",
    "tags": "핵심 태그 (쉼표 구분)",
    "one_line_summary": "한 줄 줄거리",
    "three_act_summary": {{
        "beginning": "발단 (시작 개요)",
        "middle": "전개 (발전 개요)",
        "end": "결말 (해결 개요)"
    }},
    "style_guide": "문체 요구사항과 집필 규범",
    "taboos": "금기 사항",
    "main_characters": [
        {{
            "name": "이름",
            "role": "역할 (주인공/적대자/조연 등)",
            "age": "나이",
            "appearance": "외모 묘사",
            "personality": "성격 묘사",
            "background": "배경 이야기",
            "motivation": "핵심 동기",
            "arc": "캐릭터 아크/성장 궤적"
        }}
    ],
    "world_setting": "세계관 프레임워크 묘사",
    "synopsis": "소설 시놉시스 (공개용)"
}}""",

    # -- 줄거리 에이전트 --
    "outline_system": """당신은 경험이 풍부한 소설 줄거리 기획자입니다. 주어진 소설 기획서를 바탕으로 상세한 플롯 줄거리를 작성합니다.

출력 내용:
1. 전체 책의 권별 줄거리 (각 권의 주요 플롯, 핵심 갈등, 주요 사건, 클라이맥스와 끌림)
2. 캐릭터 관계도 텍스트 묘사

마크다운 형식으로 출력하세요. 확인 사항:
- 각 권 줄거리에 명확한 주요 플롯과 주요 사건 목록 포함
- 권과 권 사이에 명확한 인과관계 연결
- 캐릭터의 성장 아크가 전체를 관통
- 복선과 서스펜스의 합리적 설계
- 완급 조절이 적절""",

    "volume_outline_system": """당신은 플롯 상세화에 능숙한 소설 줄거리 전문가입니다.
전체 줄거리에서 한 권의 개요를 바탕으로 상세한 장별 줄거리를 작성합니다.

마크다운 형식으로 출력하세요. 각 장에 필요한 내용:
- 장 제목
- 주요 사건 (3-5개 핵심 포인트)
- 등장 캐릭터
- 감정의 톤/분위기
- 복선 (설치/회수)
- 전후 연결점""",

    # -- 세계관 에이전트 --
    "worldbuilding_system": """당신은 전문적인 세계관 구축 전문가입니다. 주어진 소설 기획서를 바탕으로 상세한 세계 설정 문서를 작성해야 합니다.

마크다운 형식으로 출력하세요. 포함해야 할 내용:
1. 세계 전체 설정 (시대 배경, 사회 구조, 기술/마법 수준 등)
2. 지리/공간 설정 (중요한 장소와 그 특징)
3. 특수 체계 설정 (수련 체계/마법 체계/기술 체계 등, 장르에 따라)
4. 주요 사건 연표 (이야기 시작 전의 중요한 역사적 사건)

설정 간에 상호 일관성이 있고 모순이 없도록 하세요.""",

    "character_system": """당신은 캐릭터 조형에 능숙한 캐릭터 디자인 전문가입니다. 주어진 소설 기획서와 세계 설정을 바탕으로 상세한 캐릭터 프로필을 작성해야 합니다.

각 캐릭터에 필요한 내용:
- 기본 정보 (이름, 나이, 외모 등)
- 성격 묘사 (다층적, 외면의 행동과 내면의 성격 포함)
- 배경 이야기
- 능력/특기
- 목표/동기
- 말투/말버릇
- 캐릭터 아크 (성장 궤적)
- 캐릭터 관계

마크다운 형식으로 출력하세요. 캐릭터 간에 케미가 있고, 성격이 보완적이거나 충돌하도록 하세요.""",

    # -- 집필 에이전트 --
    "writer_system": """당신은 재능 있는 웹소설 작가입니다.
제공된 설정, 줄거리, 맥락을 바탕으로 소설 본문을 집필합니다.

집필 요구사항:
{style_guide}

구조 요구사항:
- 각 장 {min_words}-{max_words} 글자
- 장에는 훅 시작이 필요 (이전 장과의 연결 또는 새로운 서스펜스 생성)
- 핵심 플롯 진행 (최소 하나의 주요 사건)
- 결말 훅 (독자가 계속 읽도록 유도)

다음 형식을 엄격히 따르세요:
- 장 제목 형식: 제X장 제목
- 본문을 직접 출력하고, 메타 정보나 노트는 출력하지 마세요""",

    "writer_chapter_prompt": """다음 정보를 바탕으로 제{chapter_num}장의 본문을 집필하세요.

## 본 장의 줄거리
{chapter_outline}

## 최근 장 요약 (연속성 유지용)
{recent_briefs}

## 현재 캐릭터 상태
{character_status}

## 주의할 복선
{hooks_info}

## 캐릭터 프로필 (공식 설정 — 이름은 반드시 정확히 일치해야 합니다)
{character_profiles}

## 세계관 및 장소 설정 (공식 설정 — 모든 지명, 세력명 등은 반드시 정확히 일치해야 합니다)
{world_setting}

⚠️ 중요 경고: 모든 캐릭터 이름, 장소 이름, 세력/문파 이름 및 고유명사는 위의 캐릭터 프로필 및 세계관 설정과 정확히 일치해야 합니다. 어떤 이름도 임의로 만들거나 변경하거나 대체하지 마세요.

완전한 장 본문 ({min_words}-{max_words}글자)을 "제{chapter_num}장"으로 시작하여 출력하세요.""",

    # -- 후처리 에이전트 --
    "post_write_system": """당신은 꼼꼼한 소설 편집 어시스턴트입니다. 각 장 집필 후 장의 내용을 분석하고 다음 갱신 정보를 생성하는 것이 임무입니다.

JSON 형식으로 출력하세요:
{{
    "chapter_brief": {{
        "chapter_num": 장 번호,
        "title": "장 제목",
        "word_count": 대략적 글자 수,
        "main_events": ["주요 사건1", "주요 사건2", ...],
        "character_changes": ["캐릭터 상태 변경1", ...],
        "hooks_planted": ["새로 설치한 복선1", ...],
        "hooks_resolved": ["회수한 복선 ID1", ...],
        "next_chapter_hook": "다음 장으로의 훅"
    }},
    "progress_update": {{
        "latest_chapter": "제X장·제목",
        "total_words": 대략적 누적 글자 수,
        "character_status": {{
            "캐릭터 이름": "현재 상태 묘사"
        }}
    }}
}}

JSON만 반환하세요.""",

    # -- 문체 지침 에이전트 --
    "style_guide_system": """당신은 집필 문체 지침 수립을 전문으로 하는 문학 컨설턴트입니다.
주어진 소설 기획서를 바탕으로 상세한 문체 지침 문서를 생성합니다.

마크다운 형식으로 출력하세요. 포함할 내용:
1. 서술 시점 지침
2. 문체 요구사항 (전체적인 톤, 내면 독백 스타일, 외적 표현 스타일 등)
3. 장 구조 지침
4. 대화 지침 (대화 형식, 캐릭터 말투)
5. 묘사 지침 (전투/감정/환경 등 각종 묘사 요구사항)
6. 완급 조절 제안
7. 핵심 집필 원칙
8. 금기 사항""",

    # -- 세계관 작업 프롬프트 --
    "task_world_setting": """다음 소설 기획서를 바탕으로 세계 전체 설정 문서를 작성하세요 (마크다운 형식).
포함: 시대 배경, 사회 구조, 중요한 세력/조직 등 기초 세계관.

기획서:
{plan_text}""",

    "task_characters": """다음 소설 기획서를 바탕으로 상세한 캐릭터 프로필 문서를 작성하세요 (마크다운 형식).
참고 형식 요구사항: 각 캐릭터에 이름, 나이, 외모, 성격(다층적), 배경, 능력, 동기, 말버릇, 캐릭터 아크를 포함.
마지막에 캐릭터 관계도(텍스트 묘사)를 첨부하세요.

기획서:
{plan_text}""",

    "task_locations": """다음 소설 기획서를 바탕으로 중요 장소/장면 설정 문서를 작성하세요 (마크다운 형식).
이야기에 등장할 모든 중요한 장소와 그 특징 묘사를 포함하세요.

기획서:
{plan_text}""",

    "task_timeline": """다음 소설 기획서를 바탕으로 주요 사건 연표 문서를 작성하세요 (마크다운 형식).
이야기 시작 전의 중요한 역사적 사건과 이야기 중 타임라인 계획을 포함하세요.

기획서:
{plan_text}""",

    "task_power_system": """다음 소설 기획서를 바탕으로 힘/수련 체계 설정 문서를 작성하세요 (마크다운 형식).
포함: 등급 구분, 수련 방법, 특수 능력 체계 등 상세 설정.

기획서:
{plan_text}""",

    "task_tech_system": """다음 소설 기획서를 바탕으로 기술 체계 설정 문서를 작성하세요 (마크다운 형식).
포함: 기술 수준, 핵심 기술, 특수 장치 등 상세 설정.

기획서:
{plan_text}""",

    # -- 줄거리 생성 프롬프트 --
    "master_outline_prompt": """다음 소설 기획서를 바탕으로 전체 책의 전체 줄거리를 작성하세요.

## 소설 기획서
{plan_json}

모든 권을 포괄하는 전체 줄거리(마크다운 형식)를 생성하세요. 각 권에 필요한 내용:
- 주요 플롯 묘사
- 핵심 갈등
- 주요 사건 (번호 목록)
- 주요 캐릭터 상태
- 권의 클라이맥스
- 권의 끌림
- 다음 권과의 연결""",

    "volume_outline_prompt": """다음 정보를 바탕으로 제{volume_num}권의 상세한 장별 줄거리를 작성하세요.

## 소설 기획서 요약
- 제목: {title}
- 장르: {genre}
- 장당 글자 수: {chapter_words}

## 전체 줄거리에서의 이 권 묘사
{volume_info}

## 전체 줄거리 (완전본, 전체 파악용)
{master_outline}

이 권의 상세한 장별 줄거리를 생성하세요. 각 장에 포함할 내용:
- 장 번호와 제목
- 주요 사건 (3-5개)
- 등장 캐릭터
- 감정의 톤
- 복선 (설치/회수)
- 전후 연결점""",

    # -- 후처리 프롬프트 --
    "analyze_chapter_prompt": """다음 소설 장을 분석하고 요약과 갱신 정보를 생성하세요.

## 장 줄거리 (참고)
{chapter_outline}

## 장 본문
{chapter_text}

지정된 JSON 형식으로 엄밀하게 출력하세요.""",

    # -- 기획 수정 --
    "plan_revision_request": "기획서에 대한 수정 의견이 있습니다: {feedback}\n이에 따라 기획서를 조정해 주세요.",

    # -- 장르 감지 키워드 --
    "genre_fantasy_keywords": ["판타지", "수련", "선협", "마법", "이세계"],
    "genre_scifi_keywords": ["SF", "미래", "사이버", "우주", "테크놀로지"],


    "outline_merge_prompt": """아래는 같은 소설에 대한 {count}개의 서로 다른 스타일의 전체 줄거리입니다.

다음 요구사항으로 **통합 전체 줄거리**를 만드세요:
1. 각 초안에서 가장 강한 구조적 요소를 가져올 것
2. 최고의 플롯 아이디어와 캐릭터 아크를 융합할 것
3. 전체를 관통하는 논리적 일관성을 유지할 것
4. 가장 매력적인 복선 설계와 클라이맥스 배치를 보존할 것

{drafts_text}

마크다운 형식으로 통합된 전체 줄거리를 출력하세요.""",

    # -- 기능 #2: 병렬 검토 시스템 프롬프트 --
    "consistency_reviewer_system": """당신은 소설의 꼼꼼한 연속성 편집자입니다.
장의 내용이 이전 장, 줄거리, 그리고 제공된 캐릭터 프로필과 일치하는지 검토하는 것이 임무입니다.

확인 항목:
1. **캐릭터 이름 정확성**: 장에 등장하는 모든 캐릭터 이름을 캐릭터 프로필과 대조하세요. 프로필과 완전히 일치하지 않는 이름(오타, 잘못된 이름, 이름 바뀌, 호칭 불일치)을 모두 플래그하세요. 이것이 최우선 검토 항목입니다.
2. **캐릭터 특성 일관성**: 각 캐릭터의 행동, 말투, 능력, 성격이 프로필과 일치하는지 검증하세요.
3. 타임라인과 시간순서의 정확성
4. 장면/장소의 일관성
5. 플롯의 연속성 (참조된 사건이 실제로 일어났는지)
6. 캐릭터 지식의 일관성 (캐릭터가 아직 모를 정보를 알고 있지 않은지)

발견된 문제마다 확신도 점수(0-100)를 매기세요:
- 0-25: 불확실, 의도적일 수 있음
- 26-50: 문제 가능성 있으나 주관적 판단일 수 있음
- 51-75: 오류 가능성 높음, 확인 필요
- 76-100: 확실한 오류, 원문과 대조 확인됨

JSON 형식으로 출력:
{{
    "issues": [
        {{
            "type": "consistency",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "문제 설명",
            "location": "장 내 대략적 위치",
            "suggestion": "수정 방법"
        }}
    ],
    "overall_consistency_score": 1-10
}}

JSON만 반환하세요.""",

    "style_reviewer_system": """당신은 문학 스타일 검토 전문가입니다.
장의 내용이 문체 지침에 부합하는지 검토하는 것이 임무입니다.

확인 항목:
1. 시점의 일관성 (의도치 않은 시점 전환 없는지)
2. 톤과 분위기가 문체 지침과 일치하는지
3. 대화 스타일이 캐릭터 프로필과 일치하는지
4. 완급 문제 (너무 급하거나 너무 늘어지는지)
5. 문장 품질 (어색한 표현, 반복적인 단어 등)

발견된 문제마다 확신도 점수(0-100)를 매기세요.

JSON 형식으로 출력:
{{
    "issues": [
        {{
            "type": "style",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "문제 설명",
            "location": "장 내 대략적 위치",
            "suggestion": "수정 방법"
        }}
    ],
    "overall_style_score": 1-10
}}

JSON만 반환하세요.""",

    "foreshadowing_reviewer_system": """당신은 복선과 플롯 연속성 전문가입니다.
장에서의 복선 요소 처리를 검토하는 것이 임무입니다.

확인 항목:
1. 설치된 복선이 충분히 미묘한지 (너무 노골적이지 않은지)?
2. 이전에 설치한 훅이 적절한 타이밍에 진전 또는 회수되고 있는지?
3. 줄거리를 기준으로, 놓치고 있는 복선 기회가 없는지?
4. 회수된 복선이 만족스러운지?
5. 장의 결말이 다음 장을 위한 충분한 서스펜스를 만들고 있는지?

발견된 문제마다 확신도 점수(0-100)를 매기세요.

JSON 형식으로 출력:
{{
    "issues": [
        {{
            "type": "foreshadowing",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "문제 설명",
            "location": "장 내 대략적 위치",
            "suggestion": "수정 방법"
        }}
    ],
    "overall_foreshadowing_score": 1-10
}}

JSON만 반환하세요.""",

    "review_chapter_prompt": """다음 장을 검토하세요.

## 캐릭터 프로필 (이름과 특성 대조용 권위 참조)
{character_profiles}

## 문체 지침
{style_guide}

## 장 줄거리
{chapter_outline}

## 최근 장 요약
{recent_briefs}

## 복선 트래커
{hooks_info}

## 장 본문
{chapter_text}

중요: 장 본문의 모든 캐릭터 이름을 위의 캐릭터 프로필과 대조하세요. 이름 불일치는 심각한 문제입니다.

지정된 JSON 형식으로 검토 결과를 출력하세요.""",
    # -- 기능 #3: 다듬기 반복 프롬프트 --
    "polish_evaluate_system": """당신은 수석 소설 편집자입니다. 다음 장의 품질을 1-10으로 평가하세요.

평가 기준:
1. 문장의 품질과 가독성
2. 캐릭터 목소리의 일관성
3. 완급과 흐름
4. 감정적 임팩트
5. 훅의 강도 (시작과 결말)
6. 줄거리와의 정합성

JSON 형식으로 출력:
{{
    "score": 1-10,
    "strengths": ["장점1", "장점2"],
    "weaknesses": ["단점1", "단점2"],
    "specific_improvements": [
        {{
            "location": "텍스트 내 위치",
            "current": "현재 문제 텍스트 (요약)",
            "suggested": "개선 방법"
        }}
    ]
}}

JSON만 반환하세요.""",

    "polish_evaluate_prompt": """이 장의 품질을 평가하세요.

## 문체 지침
{style_guide}

## 장 줄거리
{chapter_outline}

## 장 본문
{chapter_text}

JSON 형식으로 평가 결과를 출력하세요.""",

    "polish_improve_system": """당신은 재능 있는 소설 작가로서 개정 작업을 수행하고 있습니다.
장과 편집자의 구체적인 개선 제안을 받게 됩니다.
개선 사항을 반영하여 장 전체를 다시 쓰세요. 전체적인 이야기, 톤, 구조는 유지하세요.

메타 코멘트는 절대 추가하지 마세요 — 개정된 장 본문만 출력하세요.""",

    "polish_improve_prompt": """편집자의 피드백에 따라 다음 장을 개정하세요.

## 편집자의 피드백
단점: {weaknesses}

구체적 개선 제안:
{improvements}

## 현재 장 본문
{chapter_text}

완전한 개정 장 본문을 출력하세요.""",

    # -- 기능 #4: 권간 중간점검 조정 --
    "volume_adjust_prompt": """독자가 제{volume_num}권에 대해 다음 피드백/조정 사항을 제출했습니다.

피드백: {feedback}

현재 권 줄거리:
{volume_outline}

독자의 피드백을 반영하면서 전체 줄거리와의 일관성을 유지하여 권 줄거리를 수정하세요.

마크다운 형식으로 수정된 권 줄거리를 출력하세요.""",


    # -- 글자 수 검증 프롬프트 --
    "expand_chapter_system": """당신은 재능 있는 소설 작가입니다. 글자 수가 부족한 장을 받게 되며, 이를 확장해야 합니다.
품질을 유지하면서 목표 글자 수에 도달하도록 장을 확장하세요. 분량 채우기용 내용은 넣지 마세요.

확장 전략:
- 더 상세한 묘사 추가 (환경, 감정, 감각적 디테일)
- 대화 교류 확장, 자연스러운 대화 왕래 추가
- 캐릭터 내면 독백과 반응 추가
- 액션 장면 세밀화, 더 생동감 있는 묘사
- 분위기를 조성하는 전환 장면 추가

중요: 완성된 확장 장 본문만 출력하세요. 메타 정보나 코멘트는 출력하지 마세요.""",

    "expand_chapter_prompt": """다음 장은 글자 수가 부족합니다 ({current_words}자). 약 {target_words}자로 확장해 주세요.

## 문체 지침
{style_guide}

## 장 줄거리
{chapter_outline}

## 현재 장 본문 (너무 짧음)
{chapter_text}

완성된 확장 장 본문 ({target_words}자 이상)을 출력하세요.""",

    "compress_chapter_system": """당신은 경험 풍부한 소설 편집자입니다. 글자 수가 초과된 장을 받게 되며, 이를 압축해야 합니다.
모든 핵심 플롯 포인트와 캐릭터 순간을 보존하면서 장을 압축하세요.

압축 전략:
- 문장을 다듬어 중복 묘사 제거
- 반복적인 대화 통합
- 덜 중요한 전환 장면 요약
- 플롯을 진전시키지 않는 내용 제거
- 액션 장면 간결화

중요: 모든 핵심 플롯 사건, 캐릭터 발전, 복선은 반드시 보존해야 합니다.
완성된 압축 장 본문만 출력하세요. 메타 정보나 코멘트는 출력하지 마세요.""",

    "compress_chapter_prompt": """다음 장은 글자 수가 초과되었습니다 ({current_words}자). 약 {target_words}자로 압축해 주세요.

## 문체 지침
{style_guide}

## 장 줄거리 (모든 핵심 사건 보존)
{chapter_outline}

## 현재 장 본문 (너무 긴)
{chapter_text}

완성된 압축 장 본문 (~{target_words}자)을 출력하세요. 모든 핵심 플롯 포인트를 보존하세요.""",

    "split_chapter_system": """당신은 경험 풍부한 소설 편집자입니다. 심각하게 초과된 장을 받게 되며, 두 장으로 분할해야 합니다.
자연스러운 서사적 구분점을 찾아 장을 분할하세요. 분할된 각 장은:
- 자체적인 극적 아크 보유 (설정 → 전개 → 훅 엔딩)
- 대략 비슷한 길이
- 자연스러운 클리프행어 또는 전환점에서 끝남

출력 형식: 두 장 사이에 정확히 "===CHAPTER_SPLIT===" 구분선 사용.
각 장은 장 제목 줄로 시작.

중요: ===CHAPTER_SPLIT===로 구분된 두 장의 본문만 출력하세요. 메타 코멘트 없음.""",

    "split_chapter_prompt": """다음 장은 심각하게 초과되었습니다 ({current_words}자, 장당 목표: {min_words}-{max_words}자). 두 장으로 분할해 주세요.

## 문체 지침
{style_guide}

## 원래 장 줄거리
{chapter_outline}

## 현재 장 본문 (분할 대상)
{chapter_text}

구조가 완전한 두 장으로 분할하세요. "===CHAPTER_SPLIT===" 를 구분선으로 사용.
제{chapter_num_a}장이 전반부, 제{chapter_num_b}장이 후반부입니다.
각 장 약 {target_words}자.""",

    # -- 기능 #6: 완결 보고서 프롬프트 --
    "final_summary_system": """당신은 문학 분석가입니다. 완성된 소설의 종합 보고서를 생성하세요.

마크다운 형식으로 출력하세요. 포함할 내용:
1. **소설 개요** — 제목, 장르, 최종 글자 수, 장 수
2. **플롯 요약** — 완전한 이야기 시놉시스 (스포일러 포함)
3. **캐릭터 아크 분석** — 각 주요 캐릭터의 성장 변화
4. **주제 분석** — 핵심 주제와 그 전개 방식
5. **통계 개요** — 장별 글자 수, 평균 글자 수, 가장 긴/짧은 장
6. **복선 회수 보고** — 어떤 복선이 설치되고 회수되었는지
7. **집필 품질 메모** — 전체 문장 품질, 주목할 장면
8. **후속작 가능성** — 이어질 수 있는 열린 실마리""",

    "final_summary_prompt": """이 완성된 소설의 종합 완결 보고서를 생성하세요.

## 소설 기획서
{plan_json}

## 장 요약
{all_briefs}

## 캐릭터 프로필
{characters}

## 복선 트래커
{hooks_info}

## 통계 데이터
- 총 장 수: {total_chapters}
- 총 글자 수: 약 {total_words}자

마크다운 형식으로 완전한 보고서를 생성하세요.""",

    # -- Language enforcement instruction --
    "language_instruction": (
        "**중요 — 언어 요구사항**: "
        "모든 출력을 반드시 {native_name}({english_name})로 작성하세요. "
        "모든 문장, 단락, 제목, 라벨은 {native_name}로 작성해야 합니다. "
        "고유명사나 전문용어를 인용하는 경우를 제외하고 다른 언어를 섞지 마세요."
    ),
})

# ============================================================
# TEMPLATES: 마크다운 템플릿 (한국어 완전 번역)
# ============================================================
TEMPLATES = dict(_BASE_TEMPLATES)
TEMPLATES.update({
    "readme": """# 📖 장편소설 창작 프로젝트

## 기본 정보
- **제목**: 「{title}」
- **장르**: {genre}
- **목표 분량**: {target_words}
- **장당 분량**: {min_words}-{max_words}자
- **예상 총 장 수**: {total_chapters}
- **권 수**: {volumes}
- **서술 시점**: {pov}
- **핵심 태그**: {tags}

## 한 줄 줄거리
{one_line_summary}

## 📁 디렉토리 구조

```
{title}/
├── README.md              # 프로젝트 개요
├── meta/                  # 메타 정보 관리
│   ├── progress.md        # 집필 진행 트래커
│   ├── style_guide.md     # 문체 지침
│   └── hooks_tracker.md   # 복선 트래커
├── worldbuilding/         # 세계관 설정
│   ├── characters.md      # 캐릭터 프로필
│   ├── world_setting.md   # 세계관 설정 개요
│   └── ...                # 기타 설정 파일
├── plot/                  # 플롯 관리
│   ├── master_outline.md  # 전체 줄거리
│   ├── volume_XX.md       # 권별 줄거리
│   └── chapter_briefs.md  # 장 요약 기록
└── chapters/              # 본문 출력
    ├── chapter_001.txt    # 제1장
    └── ...
```

## 🔄 집필 워크플로
1. progress.md 읽기 → 현재 진행 확인
2. chapter_briefs.md 읽기 → 최근 장 돌아보기
3. 현재 권 줄거리 참조 → 본 장 내용 확인
4. hooks_tracker.md 확인 → 복선 상태 확인
5. characters.md 참조 → 캐릭터 상태 확인
6. 본문을 chapters/에 출력
7. progress.md, chapter_briefs.md 등 갱신
""",

    "progress": """# 📊 집필 진행 트래커

## 현재 상태
- **최근 완료 장**: 아직 시작하지 않음
- **현재 집필 중**: 미정
- **현재 권**: 제1권
- **총 글자 수**: 0
- **최종 갱신**: -

## 다음 단계
> 1. ~~소설 장르/유형 결정~~ ✅
> 2. ~~핵심 설정과 주인공~~ ✅
> 3. ~~전체 줄거리~~ ✅
> 4. **제1권 줄거리 완성** ← 현재
> 5. 본문 집필 시작

## 완료 장 목록

| 장 | 제목 | 약 글자 수 | 핵심 사건 |
|----|------|-----------|----------|

## 현재 캐릭터 상태 요약
(갱신 대기 중)

## TODO
- [x] 소설 장르 결정
- [x] 세계관 설정 완성
- [x] 캐릭터 설정 완성
- [x] 전체 줄거리 완성
- [ ] 제1권 줄거리 완성
- [ ] 제1장 본문
""",

    "hooks_tracker": """# 🎣 복선/훅 트래커

> 모든 복선과 서스펜스를 기록하고 상태를 추적
> 상태: 🔴 설치 완료 미회수 | 🟡 일부 공개 | 🟢 회수 완료 | ⚪ 계획 중

---

## 장기 복선 (권을 넘는)

| ID | 내용 | 설치 장 | 회수 예정 | 상태 | 메모 |
|----|------|---------|----------|------|------|

## 단기 복선 (현재 권 내)

| ID | 내용 | 설치 장 | 회수 예정 | 상태 | 메모 |
|----|------|---------|----------|------|------|

## 회수 기록

| ID | 내용 | 설치 장 | 회수 장 | 메모 |
|----|------|---------|--------|------|
""",

    "chapter_briefs": """# 📝 장 요약 기록

> 각 장 집필 후 요약 기록, 플롯의 빠른 되돌아보기용
> 형식: 장 | 제목 | 글자 수 | 주요 사건 | 캐릭터 변화 | 복선

---
""",

    "synopsis_title": "# 소설 시놉시스\n\n",

    "chapter_brief_entry": """
### 제{chapter_num}장 · {title} (약 {word_count}자)
**주요 사건**:
""",
    "character_changes_header": "\n**캐릭터 상태 변경**:\n",
    "hooks_planted_header": "\n**새 복선**:\n",
    "next_hook_prefix": "\n**다음 장 훅**: ",

    "progress_update_entry": """
---
### 제{chapter_num}장 완료 갱신
- **최근 완료**: {latest_chapter}
- **누적 글자 수**: 약 {total_words}자
""",
    "character_status_header": "\n**캐릭터 상태 요약**:\n",

    "final_summary_filename": "meta/final_summary.md",
})

"""
Lingua Latina locale
"""
from locales.en import UI as _BASE_UI, PROMPTS as _BASE_PROMPTS, TEMPLATES as _BASE_TEMPLATES

UI = dict(_BASE_UI)
UI.update({
    "welcome_title": "📖 Officina Narrationum v1.0",
    "welcome_subtitle": "   Systema Automaticum Scribendi per Machinam Intellegentem",
    "no_backend": "\n❌ Nullum tergum machinae praesto est!",
    "no_backend_hint": "   Fac ut saltem unum ex llm_openai.py vel llm_local.py adsit",
    "select_api_mode": "\n🔌 Elige modum machinae:",
    "api_openai_desc": "OpenAI forma regularis (clavis necessaria)",
    "api_local_desc": "Machina localis stream-server",
    "auto_selected": "\n  (Solum {desc} inventum, automatice electum)",
    "input_choice": "\n👤 Electionem tuam scribe (1-{max}): ",
    "invalid_choice": "Electio invalida, scribe 1-{max}",
    "input_openai_key": "Clavem OpenAI API scribe: ",
    "api_key_empty": "Clavis vacua esse non potest!",
    "input_base_url": "API Base URL (Enter pro defectu: {default}): ",
    "input_model": "Nomen machinae (Enter pro defectu: {default}): ",
    "input_local_url": "Inscriptionem machinae localis scribe: ",
    "api_url_empty": "Inscriptio vacua esse non potest!",
    "input_api_key": "Clavem API scribe (Enter ut transeas): ",
    "input_wsid": "WSID scribe (Enter ut transeas): ",
    "input_model_marker": "Signum machinae scribe (Enter ut transeas): ",
    "project_setup": "\n📁 Praeparatio Operis",
    "input_novel_name": "👤 Nomen operis scribe (ad directorium creandum): ",
    "scan_projects_header": "\n📂 Opera iam exstantia inventa sunt:",
    "no_existing_projects": "\n📂 Nulla opera exstantia inventa sunt.",
    "project_status_chapters": "{count} cap.",
    "project_status_plan": "consilium",
    "project_status_meta": "meta",
    "project_status_plot": "synopsis",
    "or_input_manually": "Nomen operis manu scribere...",
    "select_project_prompt": "\n👤 Opus elige (1-{max}): ",
    "select_operation": "\n🎯 Elige operationem:",
    "op_full": "  1. Ab initio incipere (totum iter)",
    "op_resume": "  2. A puncto servato resumere",
    "op_planning": "  3. Solum consilium capere",
    "op_worldbuilding": "  4. Solum mundum et stylum fingere",
    "op_outline": "  5. Solum argumentum delineare",
    "op_writing": "  6. Solum scribere (argumentum prius necessarium)",
    "op_batch": "  7. Modus catervatim (plures narrationes seriatim creare)",
    "input_op_choice": "\n👤 Electionem tuam scribe (1-7): ",
    "invalid_op": "Electio invalida, scribe 1-7",
    "input_volume_num": "Cui volumini argumentum detaliatum vis? (numerum scribe, vel Enter ut transeas): ",
    "input_start_chapter": "A quo capite incipias? (Enter pro capite primo): ",
    "input_end_chapter": "Usque ad quod caput scribas? (Enter usque ad finem): ",
    "interrupted": "\n\n⏸️ Ab utente interruptum. Progressus servatus. Proxima vice 'A puncto servato resumere' elige.",
    "error_occurred": "\n❌ Error factus: {error}",
    "goodbye": "\n👋 Vale!",

    # -- Modus catervatim --
    "batch_input_names": "\n📚 Nomina narrationum commis separata scribe (exempli gratia: narratioA, narratioB, narratioC):",
    "batch_empty": "❌ Nulla nomina narrationum data sunt. Ad indicem principalem reditur.",
    "batch_select_op": "\n🎯 Elige operationem pro unaquaque narratione:",
    "batch_start": "\n🚀 Modus catervatim: {total} narrationes ordine creabuntur: {names}",
    "batch_progress": "📖 [{current}/{total}] Narratio incipit: {name}",
    "batch_novel_done": "✅ Narratio '{name}' perfecta est!",
    "batch_interrupted": "\n⏸️ Interruptum est dum '{name}' scribitur. {remaining} narrationes restant.",
    "batch_continue_prompt": "Pergisne cum reliquis narrationibus? (y/n): ",
    "batch_stopped": "🛑 Modus catervatim sistit.",
    "batch_novel_error": "\n❌ Error in narratione '{name}': {error}",
    "batch_all_done": "\n🎉 Omnes {total} narrationes perfectae sunt!",

    "select_language": "\n🌐 Elige linguam narrationis tuae:",
    "lang_choice_prompt": "\n👤 Electionem tuam scribe (1-{max}): ",
    "phase_planning_title": "\n📝 Gradus I: Consilium",
    "planner_prefix": "\n🤖 Consiliarius:\n",
    "user_prefix": "👤 Tu: ",
    "input_empty_hint": "(Responsum tuum scribe)",
    "multiline_hint": "(Plures versus licent; versum vacuum da ut finiatur. /paste pro modo glutinandi)",
    "multiline_paste_hint": "(Modus glutinandi: libere glutina cum versibus vacuis, /end ut finiatur)",
    "quit_planning": "Consilium relictum est.",
    "force_done": "Bene, consilium componam...",
    "generating_plan": "\n⏳ Consilium integrum narrationis creatur...",
    "plan_display_title": "\n📋 Consilium Narrationis",
    "plan_label_title": "Titulus",
    "plan_label_genre": "Genus",
    "plan_label_theme": "Thema",
    "plan_label_target_words": "Verba Proposita",
    "plan_label_total_chapters": "Capita Aestimata",
    "plan_label_volumes": "Volumina",
    "plan_label_pov": "Persona Narrantis",
    "plan_label_tags": "Notae",
    "plan_label_one_line": "Summa Uno Versu",
    "plan_label_beginning": "Protasis",
    "plan_label_middle": "Epitasis",
    "plan_label_end": "Catastrophe",
    "plan_label_characters": "Personae Principales",
    "confirm_plan": "\n👤 Hoc consilio contentus es? (y/emendationes): ",
    "adjusting_plan": "\n⏳ Consilium secundum notas tuas accommodatur...",
    "plan_confirmed": "✅ Consilium confirmatum et servatum!",
    "rename_dir_prompt": "\n📁 Titulus fabulae est \"{title}\", sed directorium est \"{dir}\".",
    "rename_dir_confirm": "   Directorium in \"{title}\" renominare vis? (y/n): ",
    "rename_dir_done": "  ✅ Directorium renominatum: {path}",
    "rename_dir_exists": "  ⚠️ Directorium iam exstat: {path}",
    "rename_dir_failed": "  ❌ Renominatio defecit: {error}",
    "phase_world_title": "\n🌍 Gradus II: Mundus et Styli Norma (paralleliter creatur...)",
    "world_done": "✅ Mundi descriptio perfecta ({count} documenta)",
    "world_failed": "❌ Mundi descriptio defecit: {error}",
    "style_done": "✅ Styli norma creata",
    "style_failed": "❌ Styli norma defecit: {error}",
    "phase_outline_title": "\n📋 Gradus III: Argumentum Principale",
    "generating_outline": "⏳ Argumentum principale creatur...",
    "outline_done": "✅ Argumentum principale perfectum",
    "outline_review": "\n📖 Argumentum principale servatum in plot/master_outline.md. Quaeso inspice.",
    "press_enter_continue": "👤 Enter preme ut argumentum Voluminis I creetur...",
    "generating_volume": "📑 Argumentum Voluminis {num} creatur...",
    "volume_done": "✅ Argumentum Voluminis {num} perfectum",
    "phase_writing_title": "\n✍️ Gradus V: Scriptio",
    "checkpoint_resume": "[Punctum] {count} capita perfecta inventa, a capite {next} resumitur",
    "volume_not_found": "⚠️ Argumentum Voluminis {num} non inventum, creatur...",
    "generating_volume_outline": "⏳ Argumentum Voluminis {num} creatur...",
    "writing_chapter": "📖 Caput {num} scribitur...",
    "chapter_done": "  ✅ Caput {num} perfectum (~{words} verba)",
    "post_processing": "  ⏳ Metadatae analyzantur et renovantur...",
    "post_done": "  ✅ Caput {num} post-processus perfectum",
    "post_failed": "  ⚠️ Caput {num} post-processus defecit, renovatio praetermissa",
    "chapter_error": "  ❌ Error in capite {num}: {error}",
    "retry_prompt": "  Iterumne tentes? (y/n): ",
    "skip_chapter": "  Caput {num} praetermittitur, ad proximum transitur",
    "pause_prompt": "\n📊 {num} capita perfecta. Enter ut pergatur, 'stop' ut pausetur",
    "pause_input": "👤 ",
    "paused": "⏸️ Pausatum. Proxima vice a capite {next} resume",
    "writing_complete": "🎉 Scriptio perfecta!",
    "planning_incomplete": "Consilium nondum perfectum, exeundum.",
    "no_plan_found": "Consilium non inventum, ab initio incipiendum...",
    "resume_checking": "🔄 Status operis inspicitur...",
    "resume_completed": "{count} capita perfecta, scriptio pergit...",
    "no_style_guide": "Styli norma non inventa, creatur...",
    "no_outline": "Argumentum principale non inventum, creatur...",
    "plan_not_found_error": "Documentum consilii plan.json non inventum. Primum consilium cape.",
    "worldbuilding_start": "[Agens Mundi] {count} documenta paralleliter creantur...",
    "doc_done": "  ✅ {filename} creatum",
    "doc_failed": "  ❌ {filename} defecit",
    "doc_error": "  ❌ {filename} defecit: {error}",
    "llm_error_retry": "Ignosce, difficultas orta est. Iterum dic quaeso~",
    "info_enough": "Satis informationis habeo! Consilium integrum componam... 🎯",
    "continue_input": "Dic mihi plus de narratione quam scribere vis~",
    "config_loaded": "[Config] Configuratio ex {file} lecta: {keys}",
    "novel_config_loaded": "[Config] Configuratio fabulae ex {file} lecta: {keys}",
    "novel_config_skipped": "  ⚠️ Claves API/itineris in {file} omissae (configuratione globali utere): {keys}",
    "novel_config_auto_created": "[Config] {file} ex exemplo automatice creatum (muta ad hanc fabulam configurandam)",
    "config_not_found": "[Config] {file} non inventum. Arcana tempore executionis scribenda.",
"config_hint": "[Config] Vide user_config.example.json ad {file} creandum",
    "project_initialized": "[Opus] Directorium initiatum: {path}",
    "openai_initialized": "[LLM-OpenAI] Initiatum, machina: {model}, URL: {url}",
    "openai_need_package": "Tergum OpenAI fasciculum openai requirit: pip install openai",
"openai_no_key": "OPENAI_API_KEY non configurata. In user_config.json scribe vel tempore executionis indica.",
    "openai_attempt_failed": "[LLM-OpenAI] Conatus {n} defecit: {error}",
    "openai_retry_wait": "[LLM-OpenAI] Post {wait}s iterum tentatur...",
    "openai_max_retries": "[LLM-OpenAI] Maximum conatuum ({max}) attactum, desistendum",
    "local_initialized": "[LLM-Local] Initiatum, URL: {url}, signum: {marker}",
    "local_need_package": "Tergum locale fasciculum requests requirit: pip install requests",
"local_no_url": "LOCAL_API_URL non configurata. In user_config.json scribe.",
    "local_attempt_failed": "[LLM-Local] Conatus {n} defecit: {error}",
    "local_retry_wait": "[LLM-Local] Post {wait}s iterum tentatur...",
    "local_max_retries": "[LLM-Local] Maximum conatuum ({max}) attactum, desistendum",
    "cannot_load_openai": "Tergum OpenAI onerari non potest: {error}\nFac ut llm_openai.py adsit et openai installatum sit",
    "cannot_load_local": "Tergum locale onerari non potest: {error}\nFac ut llm_local.py adsit et requests installatum sit",
    "unsupported_api_mode": "Modus API non sustentus: {mode}. Praesto: 'openai', 'local'",
    "file_written": "[Theca] Scriptum: {path}",

    # -- Feature #1: Comparatio plurium schematum --
    "outline_multi_draft_title": "\n📋 Gradus III: Argumentum Principale (Comparatio Plurium Schematum)",
    "generating_draft": "  ⏳ Schema argumenti {num}/{total} creatur (stylus: {style})...",
    "draft_done": "  ✅ Schema {num} perfectum",
    "draft_failed": "  ❌ Schema {num} defecit: {error}",
    "draft_comparison_title": "\n📊 Comparatio Schematum Argumenti",
    "draft_header": "\n{'─' * 40}\n📄 Schema {num} — Stylus: {style}\n{'─' * 40}",
    "draft_select_prompt": "\n👤 Elige schema (1-{max}), vel 'm' ad optima coniungenda: ",
    "draft_merging": "⏳ Optima ex omnibus schematis coniunguntur...",
    "draft_selected": "✅ Schema {num} ut argumentum principale electum",
    "draft_merged": "✅ Argumentum coniunctum creatum est",
    "outline_drafts_truncating": "   ⚠️ Argumenta nimis longa ({total} tokens aest., {budget} permissa), proportionaliter truncantur...",
    "draft_invalid": "Electio invalida, scribe 1-{max} vel 'm'",
    "parallel_review_title": "  🔍 Censura qualitatis parallela agitur...",
    "review_consistency": "[Censor Congruentiae]",
    "review_style": "[Censor Styli]",
    "review_foreshadowing": "[Censor Praefigurationis]",
    "review_done": "  ✅ {reviewer}: {count} quaestio(nes) inventae (fiducia≥{threshold})",
    "review_failed": "  ⚠️ {reviewer} censura defecit: {error}",
    "review_no_issues": "  ✅ Omnes censores transierunt — nullae quaestiones graves!",
    "review_issues_found": "  ⚠️ {count} quaestio(nes) ab omnibus censoribus inventae:",
    "review_issue_item": "    [{severity}] ({reviewer}, fiducia: {confidence}) {description}",
    "review_critical_prompt": "  🚨 Quaestiones graves inventae. Caput rescribere? (y/n): ",
    "polish_start": "  ✨ Cyclus limaturus inchoatur (max {max_iter} iterationes)...",
    "polish_iteration": "  ✨ Limatura {iter}/{max_iter}...",
    "polish_score": "  📊 Nota qualitatis: {score}/10 (limen: {threshold})",
    "polish_passed": "  ✅ Limen qualitatis attactum! Cyclus limaturus finitus.",
    "polish_improving": "  ⏳ Nota infra limen, melioramenta applicantur...",
    "polish_max_reached": "  ⚠️ Maximum iterationum attactum. Optima versio usurpatur (nota: {score}/10).",
    "polish_failed": "  ⚠️ Aestimatio limaturae defecit, versio praesens retinetur.",
    "volume_checkpoint_title": "\n📍 Punctum Inspectionis Voluminis {num}",
    "volume_checkpoint_summary": "  Progressus: {completed} capita perfecta, ~{words} verba",
    "volume_checkpoint_prompt": "\n👤 Volumen {num} incipiendum. Perge? (y / adjust / stop): ",
    "volume_checkpoint_adjust": "👤 Notas accommodationis scribe: ",
    "volume_checkpoint_adjusting": "⏳ Argumentum voluminis secundum notas tuas accommodatur...",
    "volume_checkpoint_stopped": "⏸️ Ante Volumen {num} substitum. Proxima vice a capite {next} resume.",
    "severity_critical": "GRAVE",
    "severity_major": "MAIUS",
    "severity_minor": "MINUS",
    "severity_info": "NOTITIA",
    "final_summary_title": "\n📊 Summa Finalis Narrationis creatur...",
    "final_summary_done": "✅ Summa finalis creata et servata!",
    "final_summary_failed": "⚠️ Summa finalis defecit: {error}",

    # -- Confirmatio parametrorum scripturae --
    "writing_params_title": "\n⚙️ Confirmatio Parametrorum Scripturae",
    "ask_chapter_min_words": "   Minima verba per capitulum (nunc: {current}, Enter ut retineas): ",
    "ask_chapter_max_words": "   Maxima verba per capitulum (nunc: {current}, Enter ut retineas): ",
    "writing_params_swapped": "   ⚠️ Minimum > Maximum, valores permutati sunt.",
    "ask_word_count_check": "   Numerum verborum verificare? (nunc: {status}, y/n, Enter ut retineas): ",
    "ask_lazy_mode": "   Modum automaticum activare? (nunc: {status}, y/n, Enter ut retineas): ",
    "writing_params_summary": "   ✅ Parametra: {min}–{max} verba/cap., verificatio: {check}, modus auto.: {lazy}",

    # -- Stilus signorum colloquii --
    "quote_style_title": "\n💬 Stilus Signorum Colloquii",
    "quote_style_prompt": "\n👤 Elige stilum signorum pro colloquio (1-{max}): ",
    "quote_style_invalid": "Electio invalida, scribe 1-{max}",
    "quote_style_selected": "✅ Stilus signorum colloquii constitutus: {style}",
    "quote_style_option_curly": '\u201c\u201d signa duplicia curva (e.g. \u201cSalve!\u201d)',
    "quote_style_option_corner": '「」 uncini angulares (e.g. 「Salve!」)',
    "quote_style_option_guillemet": '«» guillemeta (e.g. «Salve!»)',
    "quote_style_option_dash": '— linea longa pro colloquio (e.g. — Salve!)',
    "quote_style_option_straight": '"" signa recta (e.g. "Salve!")',

    # -- Stilus signorum cogitationis --
    "inner_quote_title": "\n💭 Stilus Signorum Cogitationis Internae",
    "inner_quote_prompt": "\n👤 Elige stilum pro cogitationibus internis (1-{max}): ",
    "inner_quote_invalid": "Electio invalida, scribe 1-{max}",
    "inner_quote_selected": "✅ Stilus cogitationis constitutus: {style}",
    "inner_quote_option_corner_double": '『』 uncini duplices (e.g. 『Cavendum est mihi』)',
    "inner_quote_option_corner": '「」 uncini angulares (e.g. 「Cavendum est mihi」)',
    "inner_quote_option_curly_single": '\u2018\u2019 signa singula curva (e.g. \u2018Cavendum est mihi\u2019)',
    "inner_quote_option_italic": '*litterae inclinatae* pro cogitationibus (e.g. *Cavendum est mihi*)',
    "inner_quote_option_dash": '——linea longa duplex (e.g. ——Cavendum est mihi——)',
    "inner_quote_option_paren": '（） parentheses plenae (e.g. （Cavendum est mihi）)',
    "inner_quote_option_same": 'Eodem stilo ac colloquia',    "inner_quote_option_none": 'Sine signis specialibus (cogitatio narratione describitur)',

    # -- Regulae signorum (in regulam stili/promptum iniectae) --
    "quote_rules_heading": "Regulae Signorum Citationis",
    "quote_rule_dialogue_curly": 'Omnia colloquia signis \u201c\u201d (duplicibus curvis) utantur. Exemplum: \u201cSalve!\u201d',
    "quote_rule_dialogue_corner": 'Omnia colloquia signis 「」 (uncinis angularibus) utantur. Exemplum: 「Salve!」',
    "quote_rule_dialogue_guillemet": 'Omnia colloquia signis «» (guillemeta) utantur. Exemplum: «Salve!»',
    "quote_rule_dialogue_dash": 'Colloquia linea longa (—) introducantur. Exemplum: — Salve!',
    "quote_rule_dialogue_straight": 'Omnia colloquia signis "" (rectis) utantur. Exemplum: "Salve!"',
    "quote_rule_inner_corner_double": 'Cogitationes internae signis 『』 (duplicibus uncinis) utantur. Exemplum: 『Cavendum est mihi』',
    "quote_rule_inner_corner": 'Cogitationes internae signis 「」 (uncinis angularibus) utantur. Exemplum: 「Cavendum est mihi」',
    "quote_rule_inner_curly_single": 'Cogitationes internae signis \u2018\u2019 (singulis curvis) utantur. Exemplum: \u2018Cavendum est mihi\u2019',
    "quote_rule_inner_italic": 'Cogitationes internae *litteris inclinatis* notentur. Exemplum: *Cavendum est mihi*',
    "quote_rule_inner_dash": 'Cogitationes internae lineis longis (——) notentur. Exemplum: ——Cavendum est mihi——',
    "quote_rule_inner_paren": 'Cogitationes internae parenthesibus plenis (（）) notentur. Exemplum: （Cavendum est mihi）',
    "quote_rule_inner_none": 'Ne signa specialia ad cogitationes internas adhibeantur. Narratione describatur.',
    "quote_rule_inner_same": 'Cogitationes internae eodem stilo ac colloquia signentur.',

    # -- Modus Piger --
    "lazy_mode_enabled": "🛋️ Modus piger activatus — post argumenti confirmationem omnia automatice procedent!",
    "lazy_auto_merge": "🛋️ [Piger] Omnes delineationes automatice coniunguntur...",
    "lazy_auto_select": "🛋️ [Piger] Una tantum delineatio, automatice selecta.",
    "lazy_auto_continue": "🛋️ [Piger] Automatice continuatur...",
    "lazy_auto_retry": "🛋️ [Piger] Automatice iteratur...",
    "lazy_auto_skip": "🛋️ [Piger] Automatice praetermittitur...",
    "lazy_auto_volume_continue": "🛋️ [Piger] Automatice ad volumen {num} continuatur...",

    # -- Recognitio iterata --
    "review_retry_feedback": """⚠️ GRAVE: Haec est rescriptio {attempt}/{max_attempts}. Versio prior has quaestiones graves habuit quae CORRIGENDAE sunt:
{issues}

Totum caput ab initio rescribe, omnes quaestiones supra dictas corrigens, dum fabula, tonus et structura servantur.""",
    "review_max_retries_reached": "  ⚠️ Caput {num}: maximum conatuum recognitionis ({max}) attactum. Versio praesens servatur.",



    # -- Verificatio verborum --
    "wordcount_check_start": "  📏 Verificatio verborum: {words} verba (propositum: {min}-{max})",
    "wordcount_too_short": "  ⚠️ Caput nimis breve ({words} verba, minimum {min}). Expanditur...",
    "wordcount_too_long": "  ⚠️ Caput nimis longum ({words} verba, maximum {max}). Comprimitur...",
    "wordcount_split_needed": "  📑 Caput multo longius ({words} verba, ≥{threshold}% limitis). In duo capita scinditur...",
    "wordcount_expand_done": "  ✅ Expansio perfecta: {words} verba",
    "wordcount_compress_done": "  ✅ Compressio perfecta: {words} verba",
    "wordcount_split_done": "  ✅ Scissio perfecta: Caput {num_a} ({words_a} verba) + Caput {num_b} ({words_b} verba)",
    "wordcount_retry": "  🔄 Verificatio iterata {attempt}/{max_attempts}...",
    "wordcount_give_up": "  ⚠️ Post {max_attempts} conatus nondum attactum. Versio praesens usurpatur ({words} verba).",
    "wordcount_ok": "  ✅ Numerus verborum acceptus: {words} verba",
    "wordcount_split_renumber": "  📝 Nota: Post scissionem capita sequentia automatice renumerantur.",

    # -- Feature #1: Multi-draft outline styles --
    "outline_style_dramatic": "Dramaticum et Tensum",
    "outline_style_literary": "Litterarium et Personarum",
    "outline_style_commercial": "Commerciale et Celeris Rhythmi",
})

PROMPTS = dict(_BASE_PROMPTS)
PROMPTS.update({
    "planner_system": """Tu es consiliarius narrationum peritus, qui ex nihilo nucleum fabulae concipere scit.
Officium tuum est per colloquium cum utente satis informationis colligere ad haec elementa nuclei determinanda:

1. **Genus/Typus**: Phantasia, Urbanum, Mysterium, Amor, Scientifica Fictio, etc.
2. **Thema Nuclei**: Quid narratio exprimere velit
3. **Verba Proposita et Structura**: Verba totalia, verba per caput, capita aestimata, volumina
4. **Persona Narrantis**: Prima persona / Tertia persona
5. **Notae Nuclei**: 3-5 claves
6. **Summa Uno Versu**: Una sententia quae totum librum comprehendat
7. **Summa Tripartita**: Protasis, epitasis, catastrophe
8. **Styli Norma**: Stylus, tonus, opera referenda
9. **Interdicta**: Quae contineri non debent
10. **Personae Principales**: Saltem fundamenta protagonistae
11. **Mundi Structura**: Mundus in quo fabula evenit

Debes utenti active quaerere has informationes. Partes quas utens ipse determinare non vult, creative supple.
Cum satis informationis habere te credis, consilium finale narrationis emitte.

Nota:
- Tantum 2-3 quaestiones cognatas simul quaere
- Secundum responsa utentis flexibiliter subsequentes quaestiones accommoda
- Pro quoque elemento, explicite quaere utrum utens ipse specificare velit an tibi relinquere
- Stilum colloquii amicum et professionalem serva""",

    "planner_first_question": """Salve! Consiliarius narrationum tuus sum~ 🎉

Antequam scribere incipiamus, ideas tuas cognoscere velim. Gradatim procedemus:

**Primum, quaestiones fundamentalissimae:**
1. Quod **genus/typum** narrationis scribere vis? (e.g., Phantasia, Urbanum, Mysterium, Scientifica Fictio, Amor, Historicum, etc.)
2. Habesne rudem **directionem fabulae** vel **ideam nuclei** in mente? Etiam vaga notio sufficit!
3. Visne haec fundamenta ipse specificare, an mihi cogitationem committere?

Libere dic~""",

    "planner_check_enough": """Omnes informationes hactenus collectas analysa et determina num sufficientes sint ad consilium inchoandum.

Index elementorum nuclei:
1. Genus/Typus - {has_genre}
2. Thema Nuclei - {has_theme}
3. Verba Proposita et Structura - {has_structure}
4. Persona Narrantis - {has_pov}
5. Notae Nuclei - {has_tags}
6. Summa Uno Versu - {has_summary}
7. Styli Norma - {has_style}
8. Personae Principales (saltem conceptus protagonistae) - {has_characters}
9. Mundi Structura - {has_world}

Responde in forma JSON:
{{
    "is_enough": true/false,
    "missing_items": ["elementa quae desunt"],
    "next_questions": "Si non satis, quaestiones proximae utenti ponendae (2-3)"
}}

Solum JSON redde.""",

    "planner_summarize": """Ex informationibus in hoc colloquio collectis, consilium narrationis completum genera.
Partes quas utens non explicite specificavit, creative supple ut totum consilium cohaereat et alliciat.

Stricte in hac forma JSON emitte:
{{
    "title": "Titulus libri",
    "genre": "Genus/Typus",
    "theme": "Thema nuclei (uno paragrapho)",
    "target_words": "Verba totalia proposita",
    "chapter_words": "Verba per caput",
    "total_chapters": "Capita totalia aestimata",
    "volumes": "Numerus et divisio voluminum",
    "pov": "Persona narrantis",
    "tags": "Notae nuclei (virgula separatae)",
    "one_line_summary": "Summa uno versu",
    "three_act_summary": {{
        "beginning": "Protasis (initii conspectus)",
        "middle": "Epitasis (progressionis conspectus)",
        "end": "Catastrophe (conclusionis conspectus)"
    }},
    "style_guide": "Requisita stili et normae scribendi",
    "taboos": "Interdicta",
    "main_characters": [
        {{
            "name": "Nomen",
            "role": "Munus (protagonista/antagonista/adiutor etc.)",
            "age": "Aetas",
            "appearance": "Species",
            "personality": "Indoles",
            "background": "Historia",
            "motivation": "Causa principalis",
            "arc": "Iter personae"
        }}
    ],
    "world_setting": "Descriptio mundi",
    "synopsis": "Synopsis narrationis (ad publicandum)"
}}""",

    # -- Argumenti Compositor --
    "outline_system": """Tu es compositor argumenti peritus. Ex consilio narrationis dato, argumentum detallatum compone.

Emittenda:
1. Argumentum per volumina (cuiusque voluminis: fabula principalis, conflictus nuclei, eventus maiores, culmen et attractio)
2. Descriptio nexuum personarum (textu)

Formato Markdown emitte. Cura ut:
- Quodque volumen fabulam principalem claram et eventuum indicem habeat
- Inter volumina nexus causales sint
- Iter personarum per totum opus currat
- Praesagia et suspensiones bene dispositae sint
- Rhythmus variatus sit""",

    "volume_outline_system": """Tu es peritus argumenti qui singula elaborare scit.
Ex summa unius voluminis in argumento totali, argumentum per capita detallatum compone.

Formato Markdown. Quodque caput:
- Titulum capitis
- Eventus principales (3-5 puncta)
- Personae praesentes
- Tonus emotionalis
- Praesagia (ponere/colligere)
- Puncta connexionis""",

    # -- Mundi Aedificator --
    "worldbuilding_system": """Tu es peritus mundi aedificandi. Ex consilio narrationis, documentum constitutionis mundi detallatum compone.

Formato Markdown, continens:
1. Constitutio mundi generalis (aetas, structura socialis, gradus technologiae/magiae, etc.)
2. Geographia/Spatium (loca importantia et characteristica)
3. Systema speciale (exercitatio/magia/technologia, secundum genus)
4. Chronologia eventuum maiorum (eventus historici ante narrationem)

Cura ut constitutiones inter se cohaereant nec contradicant.""",

    "character_system": """Tu es peritus personarum creandi. Ex consilio et constitutione mundi, tabulas personarum detallatas compone.

Quaeque persona:
- Informationes fundamentales (nomen, aetas, species, etc.)
- Indolis descriptio (multiplex, includens comportamentum externum et animum internum)
- Historia
- Facultates/Artes
- Fines/Causae
- Modus loquendi/Habitus verborum
- Iter personae
- Nexus personarum

Formato Markdown. Personae chymicam inter se habeant.""",

    # -- Scriptor --
    "writer_system": """Tu es scriptor narrationum talentatus.
Ex constitutionibus, argumento et contextu datis, capita narrationis compone.

Requisita scribendi:
{style_guide}

Requisita structurae:
- Quodque caput {min_words}-{max_words} verba
- Caput incipit attractione (connexio cum praecedenti vel nova suspensio)
- Progressus fabulae principalis (saltem unus eventus maior)
- Finis capitis cum attractione (ut lector pergere velit)

Stricte hunc formatum serva:
- Titulus: Caput X Titulus
- Textum directe emitte, sine notis vel metainformationibus""",

    "writer_chapter_prompt": """Textum completum Capitis {chapter_num} compone ex informationibus sequentibus.

## Argumentum huius capitis
{chapter_outline}

## Summae capitum recentium (ad continuitatem)
{recent_briefs}

## Status personarum actualis
{character_status}

## Praesagia notanda
{hooks_info}

## Tabulae personarum (AUCTORITAS — nomina exacte congruere debent)
{character_profiles}

## Mundi descriptio et loca (AUCTORITAS — omnia nomina locorum, factionum, etc. exacte congruere debent)
{world_setting}

⚠️ MONITUM GRAVE: Omnia nomina personarum, locorum, factionum et vocabula propria DEBENT exacte congruere cum tabulis personarum et mundi descriptione supra. NOLI nomina fingere, mutare, vel substituere.

Textum completum capitis ({min_words}-{max_words} verba) emitte, incipiens "Caput {chapter_num}".""",

    # -- Post-Scriptionem --
    "post_write_system": """Tu es adiutor editoris diligens. Post quodque caput scriptum, contentum analysa et informationes renovationis genera.

Formato JSON emitte:
{{
    "chapter_brief": {{
        "chapter_num": numerus capitis,
        "title": "Titulus capitis",
        "word_count": numerus verborum approximatus,
        "main_events": ["Eventus 1", "Eventus 2", ...],
        "character_changes": ["Mutatio personae 1", ...],
        "hooks_planted": ["Praesagium novum 1", ...],
        "hooks_resolved": ["ID praesagii resoluti 1", ...],
        "next_chapter_hook": "Attractio pro capite proximo"
    }},
    "progress_update": {{
        "latest_chapter": "Caput X · Titulus",
        "total_words": verba totalia cumulata approximata,
        "character_status": {{
            "Nomen personae": "Status actualis"
        }}
    }}
}}

Solum JSON redde.""",

    # -- Styli Norma --
    "style_guide_system": """Tu es consiliarius litterarius stili normas specians.
Ex consilio narrationis, documentum normae stili detallatum genera.

Formato Markdown, continens:
1. Normae perspectivae narrationis
2. Requisita stili scribendi (tonus generalis, stilus monologi interni, etc.)
3. Normae structurae capitis
4. Normae dialogorum (formatus, stilus loquendi personarum)
5. Normae descriptionum (pugna/emotiones/natura)
6. Consilia de rhythmo
7. Principia fundamentalia scribendi
8. Interdicta""",

    # -- Officia mundi aedificandi --
    "task_world_setting": """Ex consilio narrationis sequenti, documentum constitutionis mundi generalis compone (Markdown).
Continens: aetas, structura socialis, factiones maiores, fundamenta mundi.

Consilium:
{plan_text}""",

    "task_characters": """Ex consilio sequenti, documentum tabularum personarum detallatarum compone (Markdown).
Quaeque persona: nomen, aetas, species, indoles (multiplex), historia, facultates, causae, modus loquendi, iter.
In fine chartam nexuum personarum adde (textu descriptam).

Consilium:
{plan_text}""",

    "task_locations": """Ex consilio sequenti, documentum locorum importantium compone (Markdown).
Omnia loca importantia in narratione et characteristica eorum.

Consilium:
{plan_text}""",

    "task_timeline": """Ex consilio sequenti, documentum chronologiae eventuum maiorum compone (Markdown).
Eventus historici ante narrationem et temporum ratio in narratione.

Consilium:
{plan_text}""",

    "task_power_system": """Ex consilio sequenti, documentum systematis potentiae/exercitationis compone (Markdown).
Continens: gradus, methodi exercitationis, systema facultatum specialium.

Consilium:
{plan_text}""",

    "task_tech_system": """Ex consilio sequenti, documentum systematis technologici compone (Markdown).
Continens: gradus technologiae, technologiae principales, instrumenta specialia.

Consilium:
{plan_text}""",

    # -- Argumenti generatio --
    "master_outline_prompt": """Ex consilio sequenti, argumentum totale totius libri compone.

## Consilium Narrationis
{plan_json}

Argumentum totale (Markdown) omnia volumina complectens genera. Quodque volumen:
- Descriptio fabulae principalis
- Conflictus nuclei
- Eventus maiores (index numeratus)
- Status personarum principalium
- Culmen voluminis
- Attractio finis voluminis
- Connexio cum volumine proximo""",

    "volume_outline_prompt": """Argumentum detallatum per capita Voluminis {volume_num} compone.

## Summa Consilii
- Titulus: {title}
- Genus: {genre}
- Verba per caput: {chapter_words}

## Hoc Volumen in Argumento Totali
{volume_info}

## Argumentum Totale (completum)
{master_outline}

Argumentum detallatum per capita compone. Quodque caput:
- Numerus et titulus capitis
- Eventus principales (3-5)
- Personae praesentes
- Tonus emotionalis
- Praesagia (ponere/colligere)
- Puncta connexionis""",

    # -- Post-scriptionem --
    "analyze_chapter_prompt": """Caput narrationis sequens analysa et summam cum informationibus renovationis genera.

## Argumentum Capitis (referentia)
{chapter_outline}

## Textus Capitis
{chapter_text}

Stricte in formato JSON designato emitte.""",

    # -- Revisio consilii --
    "plan_revision_request": "Notas revisionis consilii habeo: {feedback}\nConsilium secundum haec accommoda.",

    # -- Verba clavalia generis --
    "genre_fantasy_keywords": ["phantasia", "magia", "draco", "incantatio", "mundus alter"],
    "genre_scifi_keywords": ["scientia", "futurum", "machina", "spatium", "technologia"],

    "outline_merge_prompt": """Infra sunt {count} argumenta totalia diversorum stilorum pro eadem narratione.

**Argumentum totale unitum** compone quod:
1. Fortissima elementa structuralia ex quoque specimine sumat
2. Optimas ideas fabulae et itinera personarum fundat
3. Cohaerentia logica per totum servet
4. Optima praesagia et culmina retineat

{drafts_text}

Formato Markdown argumentum unitum emitte.""",

    # -- Censores paralleli --
    "consistency_reviewer_system": """Tu es editor continuitatis diligens.
Officium: inspice num contentus capitis cum capitibus praecedentibus, argumento, ET tabulis personarum praebitis congruat.

Inspice:
1. **Accuratio nominum personarum**: Omne nomen personae in capite cum tabulis personarum confer. Quodcumque nomen quod non exacte cum tabulis congruit (errores orthographiae, nomina falsa, permutationes nominum, appellationes incongruae) signa. Hoc est inspectio MAXIMAE prioritatis.
2. **Constantia characteristicorum personarum**: Verifica utrum comportamentum, stilus loquendi, facultates et indoles cuiusque personae cum tabulis congruant.
3. Accuratio chronologiae et ordinis eventuum
4. Constantia locorum/scaenarum
5. Continuitas fabulae (eventus citati revera evenerunt)
6. Constantia cognitionis personarum (personae non sciant quae nondum didicerunt)

Cuique problemati gradum fiduciae (0-100) attribue:
- 0-25: Incertum, fortasse intentionale
- 26-50: Fortasse problema sed subiectivum
- 51-75: Probabiliter error, confirmatio necessaria
- 76-100: Certe error, cum fonte collatum

JSON emitte:
{{
    "issues": [
        {{
            "type": "consistency",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "Descriptio problematis",
            "location": "Locus approximatus in capite",
            "suggestion": "Modus corrigendi"
        }}
    ],
    "overall_consistency_score": 1-10
}}

Solum JSON redde.""",

    "style_reviewer_system": """Tu es peritus inspectionis stili litterarii.
Officium: inspice num caput regulis stili correspondeat.

Inspice:
1. Constantia perspectivae (nulla mutatio inexpectata)
2. Tonus et atmosphaera congruunt cum regulis stili
3. Stilus dialogorum congruit cum tabulis personarum
4. Rhythmus (nimis celer vel nimis lentus)
5. Qualitas prosae (locutiones ineptae, verba repetita, etc.)

Cuique problemati gradum fiduciae (0-100) attribue.

JSON emitte:
{{
    "issues": [
        {{
            "type": "style",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "Descriptio",
            "location": "Locus in capite",
            "suggestion": "Modus corrigendi"
        }}
    ],
    "overall_style_score": 1-10
}}

Solum JSON redde.""",

    "foreshadowing_reviewer_system": """Tu es peritus praesagiorum et continuitatis fabulae.
Officium: inspice tractationem praesagiorum in capite.

Inspice:
1. Praesagia posita satis subtilia sunt (non nimis aperta)?
2. Attractiones antea positae tempore opportuno progrediuntur vel resolvuntur?
3. Secundum argumentum, sunt occasiones praesagiorum omissae?
4. Praesagia resoluta satisfaciunt?
5. Finis capitis satis suspensionis pro capite proximo creat?

Cuique problemati gradum fiduciae (0-100) attribue.

JSON emitte:
{{
    "issues": [
        {{
            "type": "foreshadowing",
            "severity": "critical|major|minor|info",
            "confidence": 0-100,
            "description": "Descriptio",
            "location": "Locus in capite",
            "suggestion": "Modus corrigendi"
        }}
    ],
    "overall_foreshadowing_score": 1-10
}}

Solum JSON redde.""",

    "review_chapter_prompt": """Caput sequens inspice.

## Tabulae Personarum (Referentia auctoritativa pro nominibus et characteristicis)
{character_profiles}

## Normae Stili
{style_guide}

## Argumentum Capitis
{chapter_outline}

## Summae Capitum Recentium
{recent_briefs}

## Index Praesagiorum
{hooks_info}

## Textus Capitis
{chapter_text}

IMPORTANS: Omnia nomina personarum in textu capitis cum Tabulis Personarum supra confer. Quaelibet nominis discrepantia est quaestio GRAVIS.

In formato JSON designato resultatus inspectionis emitte.""",
    # -- Limatura --
    "polish_evaluate_system": """Tu es editor senex. Qualitatem capitis 1-10 aestima.

Criteria:
1. Qualitas prosae et legibilitas
2. Constantia vocis personarum
3. Rhythmus et fluxus
4. Impactus emotionalis
5. Fortitudo attractionum (initium et finis)
6. Congruentia cum argumento

JSON emitte:
{{
    "score": 1-10,
    "strengths": ["virtus 1", "virtus 2"],
    "weaknesses": ["vitium 1", "vitium 2"],
    "specific_improvements": [
        {{
            "location": "locus in textu",
            "current": "textus problematicus (breviter)",
            "suggested": "modus meliorandi"
        }}
    ]
}}

Solum JSON redde.""",

    "polish_evaluate_prompt": """Qualitatem huius capitis aestima.

## Normae Stili
{style_guide}

## Argumentum Capitis
{chapter_outline}

## Textus Capitis
{chapter_text}

JSON formato resultatus aestimationis emitte.""",

    "polish_improve_system": """Tu es scriptor talentatus revisionem faciens.
Caput cum suggestionibus editoris accipies.
TOTUM caput rescribe, meliorationes incorporans sed fabulam, tonum et structuram servans.

Nullas notas meta adde — solum textum capitis revisum emitte.""",

    "polish_improve_prompt": """Caput sequens secundum notas editoris revide.

## Notae Editoris
Vitia: {weaknesses}

Suggestiones specificae:
{improvements}

## Textus Capitis Actualis
{chapter_text}

Textum capitis revisum completum emitte.""",

    # -- Punctum inspectionis voluminis --
    "volume_adjust_prompt": """Lector pro Volumine {volume_num} haec annotavit.

Annotationes: {feedback}

Argumentum voluminis actuale:
{volume_outline}

Argumentum voluminis accommoda, annotationes incorporans et cohaerentia cum argumento totali servata.

Formato Markdown argumentum accommodatum emitte.""",

    # -- Verba verificanda --
    "expand_chapter_system": """Tu es scriptor narrationis talento praeditus. Caput verbis deficiens accipies et expandendum est.
Caput expande ut numerum verborum propositum attingas, qualitate servata. Ne addas materiam inanem.

Ratio expandendi:
- Adde descriptiones uberiores (loci, affectus, sensuum)
- Expande colloquia, adde naturales sermonis vices
- Adde cogitationes intimas personarum et reactiones
- Scenas actionis accuratius et vividiore modo describe
- Adde scenas transitorias ad atmosphaeram creandam

Magni momenti: Solum textum capitis expansi integrum emitte. Nullas notas meta vel commentaria.""",

    "expand_chapter_prompt": """Hoc caput verbis deficit ({current_words} verba). Expande ad circa {target_words} verba.

## Norma stili
{style_guide}

## Argumentum capitis
{chapter_outline}

## Textus capitis praesens (nimis brevis)
{chapter_text}

Emitte textum capitis expansi integrum ({target_words}+ verba).""",

    "compress_chapter_system": """Tu es editor narrationis peritus. Caput verbis excedens accipies et comprimendum est.
Comprime caput, omnia puncta fabulae et momenta personarum essentialia servans.

Ratio comprimendi:
- Stylum poli, descriptiones redundantes remove
- Colloquia repetita coniunge
- Scenas transitorias minus graves summatim describe
- Materiam fabulam non promoventem remove
- Scenas actionis brevius narra

Magni momenti: Omnia eventa fabulae essentialia, progressus personarum et praefigurationes servanda sunt.
Solum textum capitis compressi integrum emitte. Nullas notas meta vel commentaria.""",

    "compress_chapter_prompt": """Hoc caput verbis excedit ({current_words} verba). Comprime ad circa {target_words} verba.

## Norma stili
{style_guide}

## Argumentum capitis (omnia eventa essentialia serva)
{chapter_outline}

## Textus capitis praesens (nimis longus)
{chapter_text}

Emitte textum capitis compressi integrum (~{target_words} verba). Omnia puncta fabulae essentialia serva.""",

    "split_chapter_system": """Tu es editor narrationis peritus. Caput multo longius accipies et in duo capita scindendum est.
Locum naturalem narrationis inveni ubi caput scindas. Utrumque caput scissum debet:
- Arcum dramaticum proprium habere (introductio → progressio → uncus finalis)
- Longitudinem fere aequalem habere
- In naturali suspenso vel puncto transitionis finire

Forma emittendi: Lineam "===CHAPTER_SPLIT===" inter duo capita praecise pone.
Unumquodque caput titulo capitis incipe.

Magni momenti: Solum duo capita ===CHAPTER_SPLIT=== separata emitte. Nulla commentaria meta.""",

    "split_chapter_prompt": """Hoc caput multo longius est ({current_words} verba, propositum per caput: {min_words}-{max_words} verba). In duo capita scinde.

## Norma stili
{style_guide}

## Argumentum capitis originale
{chapter_outline}

## Textus capitis praesens (scindendus)
{chapter_text}

In duo capita structura integra scinde. "===CHAPTER_SPLIT===" ut separatorem utere.
Caput {chapter_num_a} pars prior est, Caput {chapter_num_b} pars posterior.
Circa {target_words} verba per caput.""",

    # -- Summa finalis --
    "final_summary_system": """Tu es analystes litterarius. Relationem summae completam pro narratione perfecta genera.

Formato Markdown, continens:
1. **Conspectus Narrationis** — Titulus, genus, verba totalia, capita
2. **Summa Fabulae** — Synopsis completa (cum revelationibus)
3. **Analysis Itinerum Personarum** — Progressus cuiusque personae principalis
4. **Analysis Thematis** — Thema nuclei et modus tractandi
5. **Conspectus Statisticus** — Verba per caput, media, caput longissimum/brevissimum
6. **Relatio Praesagiorum** — Quae praesagia posita et resoluta
7. **Notae Qualitatis** — Qualitas generalis, scaenae notabiles
8. **Potentia Continuationis** — Fila aperta quae continuari possint""",

    "final_summary_prompt": """Relationem finalem summae pro hac narratione perfecta genera.

## Consilium Narrationis
{plan_json}

## Summae Capitum
{all_briefs}

## Tabulae Personarum
{characters}

## Index Praesagiorum
{hooks_info}

## Statisticae
- Capita totalia: {total_chapters}
- Verba totalia: ~{total_words}

Relationem completam formato Markdown genera.""",

    # -- Language enforcement instruction --
    "language_instruction": (
        "**MAGNI MOMENTI — REQUISITUM LINGUAE**: "
        "OMNIA scripta tua in {native_name} ({english_name}) scribenda sunt. "
        "Omnis sententia, paragraphus, titulus et inscriptio in {native_name} esse debet. "
        "Noli alias linguas miscere nisi nomina propria vel terminos technicos citans."
    ),
})

# ============================================================
# TEMPLATES: Formulae Markdown (Latine)
# ============================================================
TEMPLATES = dict(_BASE_TEMPLATES)
TEMPLATES.update({
    "readme": """# 📖 Opus Narrationis

## Informationes Fundamentales
- **Titulus**: «{title}»
- **Genus**: {genre}
- **Verba Proposita**: {target_words}
- **Verba per Caput**: {min_words}-{max_words}
- **Capita Aestimata**: {total_chapters}
- **Volumina**: {volumes}
- **Persona Narrantis**: {pov}
- **Notae Nuclei**: {tags}

## Summa Uno Versu
{one_line_summary}

## 📁 Structura Directorii

```
{title}/
├── README.md              # Conspectus operis
├── meta/                  # Metadatae
│   ├── progress.md        # Index progressus
│   ├── style_guide.md     # Norma stili
│   └── hooks_tracker.md   # Index praesagiorum
├── worldbuilding/         # Constitutio mundi
│   ├── characters.md      # Tabulae personarum
│   ├── world_setting.md   # Conspectus mundi
│   └── ...                # Alia documenta
├── plot/                  # Administratio fabulae
│   ├── master_outline.md  # Argumentum totale
│   ├── volume_XX.md       # Argumenta voluminum
│   └── chapter_briefs.md  # Summae capitum
└── chapters/              # Textus capitum
    ├── chapter_001.txt    # Caput I
    └── ...
```

## 🔄 Ordo Scribendi
1. Lege progress.md → Inspice progressum
2. Lege chapter_briefs.md → Recense capita recentia
3. Consulta argumentum voluminis actualis → Confirma contentum capitis
4. Inspice hooks_tracker.md → Inspice statum praesagiorum
5. Consulta characters.md → Confirma statum personarum
6. Emitte textum in chapters/
7. Renova progress.md, chapter_briefs.md, etc.
""",

    "progress": """# 📊 Index Progressus Scribendi

## Status Actualis
- **Caput Recentissimum**: Nondum inceptum
- **Nunc Scribens**: Indeterminatum
- **Volumen Actuale**: Volumen I
- **Verba Totalia**: 0
- **Ultima Renovatio**: -

## Gradus Proximi
> 1. ~~Genus narrationis determinare~~ ✅
> 2. ~~Constitutiones nuclei et protagonista~~ ✅
> 3. ~~Argumentum totale~~ ✅
> 4. **Argumentum Voluminis I perficere** ← Nunc
> 5. Scribere incipere

## Capita Perfecta

| Caput | Titulus | ~Verba | Eventus Principales |
|-------|---------|--------|---------------------|

## Status Personarum
(Renovationem expectans)

## Agenda
- [x] Genus narrationis determinare
- [x] Mundum aedificare
- [x] Personas definire
- [x] Argumentum totale perficere
- [ ] Argumentum Voluminis I perficere
- [ ] Caput I
""",

    "hooks_tracker": """# 🎣 Index Praesagiorum

> Omnia praesagia et suspensiones tracta, statum inspice
> Status: 🔴 Positum non resolutum | 🟡 Partim revelatum | 🟢 Resolutum | ⚪ Propositum

---

## Praesagia Longa (inter volumina)

| ID | Contentum | Positum In | Resolvendum | Status | Notae |
|----|-----------|-----------|-------------|--------|-------|

## Praesagia Brevia (intra volumen actuale)

| ID | Contentum | Positum In | Resolvendum | Status | Notae |
|----|-----------|-----------|-------------|--------|-------|

## Historia Resolutionum

| ID | Contentum | Positum In | Resolutum In | Notae |
|----|-----------|-----------|-------------|-------|
""",

    "chapter_briefs": """# 📝 Summae Capitum

> Post quodque caput summam scribe ad fabulam celeriter recensendam
> Formatus: Caput | Titulus | Verba | Eventus | Mutationes Personarum | Praesagia

---
""",

    "synopsis_title": "# Synopsis Narrationis\n\n",

    "chapter_brief_entry": """
### Caput {chapter_num} · {title} (~{word_count} verba)
**Eventus Principales**:
""",
    "character_changes_header": "\n**Mutationes Status Personarum**:\n",
    "hooks_planted_header": "\n**Praesagia Nova**:\n",
    "next_hook_prefix": "\n**Attractio Capitis Proximi**: ",

    "progress_update_entry": """
---
### Renovatio Capitis {chapter_num} Perfecti
- **Recentissimum Perfectum**: {latest_chapter}
- **Verba Cumulata**: ~{total_words}
""",
    "character_status_header": "\n**Status Personarum**:\n",

    "final_summary_filename": "meta/final_summary.md",
})

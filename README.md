<p align="center">
  <h1 align="center">📖 Novel Agent Workflow</h1>
  <p align="center">
    <strong>An AI-powered automatic novel writing system with full i18n support</strong>
  </p>
  <p align="center">
    <a href="docs/README_zh_CN.md">简体中文</a> •
    <a href="docs/README_zh_TW.md">繁體中文</a> •
    <a href="docs/README_ja.md">日本語</a> •
    <a href="docs/README_ko.md">한국어</a> •
    <a href="docs/README_vi.md">Tiếng Việt</a> •
    <a href="docs/README_th.md">ภาษาไทย</a> •
    <a href="docs/README_zh_CL.md">文言文</a> •
    <a href="docs/README_ja_CL.md">古語</a> •
    <a href="docs/README_la.md">Latina</a> •
    <a href="docs/README_sa.md">संस्कृतम्</a>
  </p>
</p>

---

## ✨ Features

- 🤖 **Multi-Agent Pipeline** — 9 specialized agents handle each phase: planning, worldbuilding, outlining, writing, reviewing, polishing, and summarizing
- 📋 **Multi-Draft Outline Comparison** — Generates multiple master outlines with different styles (dramatic, literary, commercial) for you to choose or merge
- 🔍 **Parallel Quality Review** — 3 parallel reviewers (consistency, style, foreshadowing) analyze each chapter with confidence-based severity scoring
- ✨ **Self-Polishing Loop** — Chapters are automatically evaluated and iteratively refined until they meet a configurable quality threshold
- 📍 **Mid-Volume Checkpoints** — Pause between volumes to review progress and adjust direction before continuing
- 📊 **Final Novel Summary** — Comprehensive report generated when the novel is complete: plot analysis, character arcs, statistics, and sequel hooks
- 🌐 **11+ Languages Built-in** — English, Simplified/Traditional Chinese, Japanese, Korean, Vietnamese, Thai, Classical Chinese, Classical Japanese, Latin, Sanskrit
- ➕ **Self-Extending i18n** — Add new language support on the fly! The agent uses its own LLM to translate and generate new locale files at runtime
- 🔌 **OpenAI-Compatible Backend** — Supports any OpenAI-compatible API (OpenAI, Azure, local proxies like LM Studio, Ollama, etc.)
- ⚡ **Parallel Execution** — Worldbuilding documents, style guides, outline drafts, and quality reviews all run concurrently
- 💾 **Checkpoint Resume** — Automatically detects completed chapters and resumes from where it left off
- 📝 **Rich Metadata Tracking** — Progress, chapter summaries, foreshadowing/hooks tracker, character status — all maintained in Markdown
- 🎨 **Customizable Parameters** — All hyperparameters (temperature, word count, retry count, etc.) are centralized in config; user-specific settings (including API keys) are stored in a separate `user_config.json` (git-ignored)
- 📂 **Per-Novel Config** — Each novel project can have its own `novel_config.json` to override writing parameters (word count, quality thresholds, quote style, etc.) without affecting global settings

## 📐 Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                         main.py                                │
│              (Language Selection → API Setup → Workflow)        │
└──────────────────────────┬─────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                       workflow.py                              │
│                  (Pipeline Orchestrator)                        │
│                                                                │
│   Planning ──▶ Worldbuilding + Style Guide ──▶ Master Outline  │
│                   (parallel)            (multi-draft compare)  │
│                                       ──▶ Volume Outline       │
│                                       ──▶ Chapter Writing      │
│                                           ├─ Polish Loop       │
│                                           ├─ Parallel Review   │
│                                           └─ Post-Processing   │
│                                       ──▶ Volume Checkpoint    │
│                                       ──▶ Final Summary        │
└──────┬──────────┬──────────┬──────────┬───────────────────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
   agents.py  storage.py  config.py  prompts.py
   (9 Agents) (File I/O)  (Params)   (Locale Bridge)
       │
       ▼
  llm_client.py  ──▶  llm_openai.py  (OpenAI-compatible)
```

### Agent Roles

| Agent | Responsibility |
|-------|---------------|
| **PlannerAgent** | Multi-turn dialogue with the user to collect novel requirements (genre, theme, structure, characters, etc.) |
| **WorldbuildingAgent** | Generates world settings, character profiles, locations, timeline, power/tech systems (parallel) |
| **StyleGuideAgent** | Creates a writing style guide based on the novel plan |
| **OutlineAgent** | Generates master outlines (single or multi-draft with style variants) and detailed volume-level outlines |
| **WriterAgent** | Writes chapter text following outlines, style guide, and continuity context |
| **PostWriteAgent** | Analyzes completed chapters, generates summaries, and updates progress/hooks metadata |
| **QualityReviewerAgent** | Runs 3 parallel reviews (consistency, style, foreshadowing) with confidence scoring |
| **PolishAgent** | Self-iterating refinement: evaluates quality → applies fixes → re-evaluates until threshold |
| **FinalSummaryAgent** | Generates a comprehensive novel completion report with statistics and analysis |

## 📁 Project Structure

```
novel_writer/
├── main.py                  # Entry point
├── workflow.py              # Pipeline orchestrator
├── agents.py                # All specialized agents
├── config.py                # Centralized configuration
├── llm_client.py            # Unified LLM interface
├── llm_openai.py            # OpenAI backend
├── prompts.py               # Locale-aware prompt bridge
├── storage.py               # File I/O management
├── locale_generator.py      # Self-extending locale generator
├── user_config.json         # 🔒 User settings + API keys (git-ignored)
├── user_config.example.json # Template for user_config.json
├── novel_config.example.json# Template for per-novel config
├── requirements.txt         # Python dependencies
├── locales/                 # i18n locale files
│   ├── __init__.py          # Locale loader + auto-discovery
│   ├── en.py                # English (base)
│   ├── zh_cn.py             # 简体中文
│   ├── zh_tw.py             # 繁體中文
│   ├── ja.py                # 日本語
│   ├── ko.py                # 한국어
│   ├── vi.py                # Tiếng Việt
│   ├── th.py                # ภาษาไทย
│   ├── zh_cl.py             # 文言文
│   ├── ja_cl.py             # 古典日本語
│   ├── la.py                # Latina
│   └── sa.py                # संस्कृतम्
├── docs/                    # Translated READMEs
│   ├── README_zh_CN.md
│   ├── README_zh_TW.md
│   ├── README_ja.md
│   ├── README_ko.md
│   ├── README_vi.md
│   ├── README_th.md
│   ├── README_zh_CL.md
│   ├── README_ja_CL.md
│   ├── README_la.md
│   └── README_sa.md
└── output/                  # 📂 Generated novels (git-ignored)
    └── <novel_name>/
        ├── README.md
        ├── plan.json
        ├── meta/
        │   ├── progress.md
        │   ├── style_guide.md
        │   ├── hooks_tracker.md
        │   └── synopsis.md
        ├── worldbuilding/
        │   ├── world_setting.md
        │   ├── characters.md
        │   ├── locations.md
        │   ├── timeline.md
        │   └── power_system.md / tech_system.md
        ├── plot/
        │   ├── master_outline.md
        │   ├── volume_01.md
        │   ├── chapter_briefs.md
        │   └── ...
        └── chapters/
        ├── chapter_001.txt
            ├── chapter_002.txt
            └── ...
        └── novel_config.json  # 📖 Per-novel config override (optional)
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `openai>=1.0.0`
- `tqdm>=4.65.0`

### 2. Configure Settings

Copy the example config file and fill in your credentials and preferences:

```bash
cp user_config.example.json user_config.json
```

Edit `user_config.json` — only include the fields you want to override:

```json
{
    "OPENAI_API_KEY": "sk-your-key-here",
    "OPENAI_BASE_URL": "https://api.openai.com/v1",
    "OPENAI_MODEL": "gpt-4o",
    "TEMPERATURE": 0.7,
    "CHAPTER_MIN_WORDS": 3000
}
```

> ⚠️ `user_config.json` is git-ignored. Never commit your API keys!
> See `user_config.example.json` for all available fields and defaults.

#### Per-Novel Configuration (Optional)

Each novel project can have its own `novel_config.json` to override writing-specific parameters:

```bash
cp novel_config.example.json output/your_novel_name/novel_config.json
```

Example — customize settings for a specific novel:

```json
{
    "CHAPTER_MIN_WORDS": 4000,
    "CHAPTER_MAX_WORDS": 6000,
    "QUOTE_STYLE": "corner",
    "REVIEW_CONFIDENCE_THRESHOLD": 85,
    "LAZY_MODE": true
}
```

> **Config loading order**: `config.py` defaults → `user_config.json` (global) → `novel_config.json` (per-novel)
>
> API-related keys (`OPENAI_API_KEY`, `API_MODE`, etc.) are **ignored** in `novel_config.json` for security — use the global `user_config.json` for those.
> See `novel_config.example.json` for all available per-novel fields.

### 3. Run

```bash
python main.py
```

You will be guided through:

1. **Language Selection** — Choose your novel's language (or add a new one!)
2. **Project Setup** — Name your novel project
3. **Operation Mode** — Full pipeline, resume, or run individual phases

### 4. Operation Modes

| Mode | Description |
|------|-------------|
| **Full Pipeline** | Run the complete flow from planning to final chapter |
| **Resume** | Continue from the last checkpoint |
| **Planning Only** | Interactive dialogue to design the novel |
| **Worldbuilding Only** | Generate world settings and style guide |
| **Outline Only** | Generate master and volume outlines |
| **Writing Only** | Write chapters (specify range) |
| **Batch Mode** | Generate multiple novels sequentially |

## 🔄 Enhanced Writing Pipeline

Each chapter goes through a sophisticated multi-stage pipeline:

```
┌─────────────────────────────────────────────────────────────┐
│                    Per-Chapter Pipeline                      │
│                                                             │
│   ① WriterAgent writes chapter draft                        │
│              │                                              │
│              ▼                                              │
│   ② PolishAgent evaluates quality (score 1-10)              │
│              │                                              │
│         score < threshold?                                  │
│          ╱         ╲                                        │
│        YES          NO                                      │
│         │            │                                      │
│    ③ PolishAgent     │                                      │
│    rewrites chapter  │                                      │
│         │            │                                      │
│    (loop back to ②)  │                                      │
│                      ▼                                      │
│   ④ Save chapter to file                                    │
│              │                                              │
│              ▼                                              │
│   ⑤ 3 Parallel Quality Reviewers                            │
│     ┌────────────┬──────────────┬────────────────┐          │
│     │Consistency │   Style      │ Foreshadowing  │          │
│     │ Reviewer   │  Reviewer    │   Reviewer     │          │
│     └─────┬──────┴──────┬───────┴────────┬───────┘          │
│           └─────────────┼────────────────┘                  │
│                         ▼                                   │
│   ⑥ Filter issues by confidence (≥80%)                      │
│     • CRITICAL → offer retry                                │
│     • MAJOR/MINOR → log for reference                       │
│              │                                              │
│              ▼                                              │
│   ⑦ PostWriteAgent updates metadata                         │
│     (briefs, progress, hooks tracker)                       │
└─────────────────────────────────────────────────────────────┘
```

> All features are individually toggleable via `config.py`. Set `ENABLE_POLISH_LOOP = False` or `ENABLE_PARALLEL_REVIEW = False` to skip those stages.

## 🌐 Adding a New Language

Novel Agent Workflow can **extend itself** to support any new language:

1. Select `➕ Add new language` from the language menu
2. Enter the language's English name, native name, and code
3. The LLM automatically translates all UI strings, prompts, and templates
4. The new locale file is generated and immediately available

You can also manually place a `.py` locale file in `locales/` — it will be auto-discovered on next startup.

### Locale File Format

Each locale file exports three dictionaries:

```python
UI = { ... }         # User interface strings (~120 entries)
PROMPTS = { ... }    # LLM prompt templates (~24 entries)
TEMPLATES = { ... }  # Markdown templates (~11 entries)
```

## ⚙️ Configuration

All hyperparameters are centralized in `config.py`:

### Core Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `TEMPERATURE` | 0.7 | LLM sampling temperature |
| `TOP_P` | 0.6 | Nucleus sampling threshold |
| `MAX_OUTPUT_TOKENS` | 32768 | Maximum tokens per LLM response |
| `CHAPTER_MIN_WORDS` | 3000 | Minimum words per chapter |
| `CHAPTER_MAX_WORDS` | 4000 | Maximum words per chapter |
| `MAX_PARALLEL_WORKERS` | 3 | Parallel task workers |
| `MAX_RETRIES` | 5 | API call retry attempts |
| `MAX_PLANNING_ROUNDS` | 20 | Maximum planning dialogue rounds |

### Advanced Features

| Parameter | Default | Description |
|-----------|---------|-------------|
| `OUTLINE_DRAFT_COUNT` | 3 | Number of outline variants to generate (set to 1 to disable multi-draft) |
| `ENABLE_PARALLEL_REVIEW` | True | Run 3 parallel quality reviewers after each chapter |
| `REVIEW_CONFIDENCE_THRESHOLD` | 80 | Minimum confidence (0-100) for an issue to be reported |
| `ENABLE_POLISH_LOOP` | True | Auto-refine chapters via evaluate→improve loop |
| `MAX_POLISH_ITERATIONS` | 2 | Maximum polish iterations per chapter |
| `POLISH_QUALITY_THRESHOLD` | 8 | Quality score (1-10) needed to exit polish loop |
| `ENABLE_VOLUME_CHECKPOINT` | True | Pause between volumes for user confirmation |
| `ENABLE_FINAL_SUMMARY` | True | Generate a comprehensive report when the novel is complete |

## 🔌 LLM Backends

### OpenAI-Compatible (`llm_openai.py`)

Works with any OpenAI-compatible API (OpenAI, Azure, local proxies like LM Studio, Ollama, etc.).

## 📜 License

MIT

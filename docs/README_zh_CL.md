
<p align="center">
  <h1 align="center">📖 綴文機樞 (Novel Agent Workflow)</h1>
  <p align="center">
    <strong>藉器械之巧，自動綴文。備諸國語言。</strong>
  </p>
  <p align="center">
    <a href="../README.md">English</a> •
    <a href="README_zh_CN.md">简体中文</a> •
    <a href="README_zh_TW.md">繁體中文</a> •
    <a href="README_ja.md">日本語</a> •
    <a href="README_ko.md">한국어</a> •
    <a href="README_vi.md">Tiếng Việt</a> •
    <a href="README_th.md">ภาษาไทย</a> •
    <a href="README_zh_CL.md">文言文</a> •
    <a href="README_ja_CL.md">古語</a> •
    <a href="README_la.md">Latina</a> •
    <a href="README_sa.md">संस्कृतम्</a>
  </p>
</p>

---

## ✨ 其能

- 🤖 **多機協作** — 九機各司其職：籌謀、營世界、擬綱、操觚、審覈、潤筆、總結
- 🌐 **內具十一餘語** — 英、簡繁中文、日、韓、越、泰、文言、古日、拉丁、梵
- ➕ **可自增語** — 運行之際，機自譯而生新語之檔
- 🔌 **OpenAI相容** — 凡OpenAI相容之口皆可用
- 📋 **多方大綱** — 數式並陳（劇力型/文深型/商節型），擇一或合之
- 🔍 **並行審覈** — 三員並審（前後一貫/文風/伏筆），附以信度
- ✨ **潤色循環** — 自評自改，至達品閾而止
- 📍 **卷間檢點** — 卷間暫歇，審度調向
- 📊 **完結總結** — 全書畢後自生報告：情節、人物弧線、統計、續集線索
- ⚡ **並行** — 營世界、定文風、擬多綱、審覈，皆並行
- 💾 **斷續可接** — 自察已成章，接續而行
- 📝 **元信備錄** — 進度、章旨、伏筆、人物，悉以Markdown存
- 🎨 **參數可調** — 集於 config；私設（含符牙）別存`user_config.json`（已 git-ignore）

## 📐 構造

```
┌──────────────────────────────────────────────┐
│                   main.py                    │
│            （擇語 → 設機 → 行流程）            │
└─────────────────────┬────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│                 workflow.py                  │
│                 （流程之樞）                  │
│                                              │
│  籌謀 ──▶ 營世界＋定文風 ──▶ 總綱            │
│             （並行）                          │
│                       ──▶ 分卷綱             │
│                       ──▶ 揮毫               │
│                            ├─ 潤色循環        │
│                            ├─ 並行審覈        │
│                            └─ 析理            │
│                       ──▶ 卷間檢點            │
│                       ──▶ 完結總結            │
└───┬───────┬───────┬───────┬──────────────────┘
    │       │       │       │
    ▼       ▼       ▼       ▼
 agents  storage  config  prompts
 （九機） （存取） （參數） （語橋）
    │
    ▼
 llm_client ──▶ llm_openai （OpenAI相容）
```

### 九機之職

| 機 | 職 |
|----|---|
| **PlannerAgent** | 多輪對語，集著書之需 |
| **WorldbuildingAgent** | 營天地、角色、地理、時序（並行） |
| **StyleGuideAgent** | 依策定文風 |
| **OutlineAgent** | 擬總綱及分卷之目 |
| **WriterAgent** | 循綱目文風以撰正文 |
| **PostWriteAgent** | 析已成章，出要，更元信 |
| **QualityReviewerAgent** | 三員並審（一貫/文風/伏筆），附信度分 |
| **PolishAgent** | 自迭潤色：評品→改善→再評，至達閾 |
| **FinalSummaryAgent** | 全書畢後出總結：統計、人物弧線、續集線索 |

## 🚀 速覽

### 一、裝

```bash
pip install -r requirements.txt
```

### 二、設符牙

```bash
cp user_config.example.json user_config.json
```

編`user_config.json`，入API之憑及所好之設。

> ⚠️ `user_config.json`已git-ignore。勿提交符牙！
> 可用欄位參見 `user_config.example.json`。

#### 書之獨設（可略）

每部書可置獨立 `novel_config.json`，覆其寫作之設：

```bash
cp novel_config.example.json output/書名/novel_config.json
```

> **設之載序**：`config.py` 預設 → `user_config.json`（通設） → `novel_config.json`（書之獨設）
>
> 安全故，`novel_config.json` 中API之設自略。API之設請於 `user_config.json` 中為之。
> 可用之書級欄位參見 `novel_config.example.json`。

### 三、行

```bash
python main.py
```

系統導之：

1. **擇語** — 擇書之語（或增新語）
2. **立卷** — 命名
3. **擇行** — 通貫、接續、或行某段

### 諸式

| 式 | 說 |
|---|---|
| **始末貫之** | 自謀至終章 |
| **踵續前功** | 自斷處續 |
| **惟事籌謀** | 對語以擬策 |
| **惟營世界** | 營天地文風 |
| **惟擬綱目** | 擬總綱分卷 |
| **惟事執筆** | 撰指定之章 |
| **諯著並行** | 依次生成多部 |

## 🌐 增新語

擇`➕ 增新語`，入語名，機自譯諸文字，即時生檔。

亦可手置`.py`於`locales/`，再啟自見。

## ⚙️ 參數

| 參 | 常 | 說 |
|----|---|---|
| `TEMPERATURE` | 0.7 | 採樣溫度 |
| `TOP_P` | 0.6 | 核採樣閾值 |
| `MAX_OUTPUT_TOKENS` | 32768 | 每答上限token |
| `CHAPTER_MIN_WORDS` | 3000 | 章最少字 |
| `CHAPTER_MAX_WORDS` | 4000 | 章最多字 |
| `MAX_PARALLEL_WORKERS` | 3 | 並行數 |
| `MAX_RETRIES` | 5 | 重試數 |

### 進階

| 參 | 常 | 說 |
|----|---|---|
| `OUTLINE_DRAFT_COUNT` | 3 | 綱方案數（設1則禁） |
| `ENABLE_PARALLEL_REVIEW` | True | 每章後並行三審 |
| `ENABLE_POLISH_LOOP` | True | 評→改循環自潤章 |
| `POLISH_QUALITY_THRESHOLD` | 8 | 退出潤色所需品分(1-10) |
| `ENABLE_VOLUME_CHECKPOINT` | True | 卷間暫歇以確認 |
| `ENABLE_FINAL_SUMMARY` | True | 全書畢後生報告 |

## 📜 許

MIT


<p align="center">
  <h1 align="center">📖 小說智能體工作流 (Novel Agent Workflow)</h1>
  <p align="center">
    <strong>AI 驅動的全自動小說寫作系統，支援完整的國際化</strong>
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

## ✨ 特色

- 🤖 **多智能體流水線** — 9 個專業化智能體分別負責：策劃、世界觀建構、大綱編寫、章節寫作、審查、潤色和總結
- 📋 **多方案大綱對比** — 生成多種風格（戲劇張力型/文學深度型/商業節奏型）的總大綱，供你選擇或合併
- 🔍 **平行品質審查** — 3 個平行審查員（一致性/文風/伏筆）分析每章，附帶置信度評分
- ✨ **自動潤色循環** — 章節自動評估並迭代改進，直到達到可配置的品質閾值
- 📍 **卷間檢查點** — 在卷之間暫停，審查進度並在繼續之前調整方向
- 📊 **完結總結報告** — 小說完成後自動生成完整報告：情節分析、角色弧線、統計資料和續集線索
- 🌐 **內建 11+ 語言** — 英語、簡/繁體中文、日語、韓語、越南語、泰語、文言文、古典日語、拉丁語、梵語
- ➕ **自擴展國際化** — 運行時即可新增語言！Agent 會利用 LLM 自動翻譯並產生新的語言檔案
- 🔌 **OpenAI 相容後端** — 支援任何 OpenAI 相容 API
- ⚡ **平行執行** — 世界觀設定、風格指南、大綱方案和品質審查全部平行運行
- 💾 **斷點續寫** — 自動偵測已完成章節，從中斷處繼續
- 📝 **豐富的中繼資料追蹤** — 進度、章節摘要、伏筆/懸念追蹤器、角色狀態
- 🎨 **可自訂參數** — 所有超參數集中管理在 config 中；用戶個人設定（含 API 金鑰）單獨存放於 `user_config.json`（已 git-ignore）
## 📐 架構

```
┌────────────────────────────────────────────────────────────────┐
│                         main.py                                │
│              (語言選擇 → API 設定 → 工作流)                      │
└──────────────────────────┬─────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                       workflow.py                              │
│                      (流水線編排器)                              │
│                                                                │
│   策劃 ──▶ 世界觀建構 + 風格指南 ──▶ 總大綱                       │
│               (平行)                                           │
│                              ──▶ 分卷大綱                       │
│                              ──▶ 章節寫作                       │
│                              ──▶ 後處理                         │
└──────┬──────────┬──────────┬──────────┬───────────────────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
   agents.py  storage.py  config.py  prompts.py
  (9 個智能體) (檔案讀寫)   (參數)    (語言橋接)
       │
       ▼
  llm_client.py  ──▶  llm_openai.py  (OpenAI 相容)
```

### 智能體角色

| 智能體 | 職責 |
|--------|------|
| **PlannerAgent** | 透過多輪對話收集小說需求（題材、主題、結構、角色等） |
| **WorldbuildingAgent** | 產生世界觀設定、角色檔案、地點、時間線、力量/科技體系（平行） |
| **StyleGuideAgent** | 基於小說方案建立寫作風格指南 |
| **OutlineAgent** | 產生總大綱（單方案或多風格方案對比）和分卷詳細大綱 |
| **WriterAgent** | 按照大綱、風格指南和連續性上下文寫作章節正文 |
| **PostWriteAgent** | 分析完成的章節，產生摘要，更新進度/伏筆中繼資料 |
| **QualityReviewerAgent** | 3 個平行審查員（一致性/文風/伏筆），帶置信度評分 |
| **PolishAgent** | 自迭代潤色：評估品質 → 改進 → 重新評估，直到達到閾值 |
| **FinalSummaryAgent** | 小說完成後生成完整報告：統計、角色弧線分析、續集線索 |

## 🚀 快速開始

### 1. 安裝相依套件

```bash
pip install -r requirements.txt
```

### 2. 設定配置

```bash
cp user_config.example.json user_config.json
```

編輯 `user_config.json`（只需保留想覆蓋的欄位），填入你的 API 憑證和偏好設定。

> ⚠️ `user_config.json` 已被 git-ignore，請勿提交你的 API 金鑰！
> 所有可用欄位參見 `user_config.example.json`。

#### 專案級配置（可選）

每部小說可擁有獨立的 `novel_config.json`，覆蓋寫作相關參數：

```bash
cp novel_config.example.json output/你的小說名/novel_config.json
```

> **配置載入順序**：`config.py` 預設值 → `user_config.json`（全域） → `novel_config.json`（專案級）
>
> 基於安全考量，`novel_config.json` 中的 API 相關配置會被 **自動忽略** — 這些請在全域 `user_config.json` 中設定。
> 所有可用的專案級欄位參見 `novel_config.example.json`。

### 3. 執行

```bash
python main.py
```

系統將引導你完成：

1. **選擇語言** — 選擇小說語言（或新增新語言！）
2. **專案設定** — 為小說專案命名
3. **選擇操作** — 完整流程、斷點續寫或單獨執行某個階段

### 操作模式

| 模式 | 說明 |
|------|------|
| **完整流程** | 從策劃到最終章節的完整流程 |
| **斷點續寫** | 從上次中斷處繼續 |
| **僅策劃** | 互動式對話設計小說方案 |
| **僅世界觀建構** | 產生世界觀設定和風格指南 |
| **僅大綱** | 產生總大綱和分卷大綱 |
| **僅寫作** | 寫作指定範圍的章節 |
| **批量模式** | 依次生成多部小說 |

## 🌐 新增語言

在語言選單中選擇 `➕ 新增語言`，輸入語言資訊，LLM 會自動翻譯所有 UI 字串、提示詞和範本，即時產生新的語言檔案。

你也可以手動將 `.py` 語言檔案放入 `locales/` 目錄 — 下次啟動時會自動發現。

## ⚙️ 設定參數

### 核心參數

| 參數 | 預設值 | 說明 |
|------|--------|------|
| `TEMPERATURE` | 0.7 | LLM 取樣溫度 |
| `TOP_P` | 0.6 | 核取樣閾值 |
| `MAX_OUTPUT_TOKENS` | 32768 | 每次 LLM 回覆的最大 token 數 |
| `CHAPTER_MIN_WORDS` | 3000 | 每章最少字數 |
| `CHAPTER_MAX_WORDS` | 4000 | 每章最多字數 |
| `MAX_PARALLEL_WORKERS` | 3 | 平行任務數 |
| `MAX_RETRIES` | 5 | API 呼叫重試次數 |

### 高級功能

| 參數 | 預設值 | 說明 |
|------|--------|------|
| `OUTLINE_DRAFT_COUNT` | 3 | 大綱方案數量（設為 1 停用多方案） |
| `ENABLE_PARALLEL_REVIEW` | True | 每章後運行 3 個平行品質審查 |
| `ENABLE_POLISH_LOOP` | True | 透過評估→改進循環自動精修章節 |
| `POLISH_QUALITY_THRESHOLD` | 8 | 退出潤色循環所需的品質分（1-10） |
| `ENABLE_VOLUME_CHECKPOINT` | True | 在卷之間暫停以確認用戶意見 |
| `ENABLE_FINAL_SUMMARY` | True | 小說完成後生成完整報告 |

## 📜 授權條款

MIT

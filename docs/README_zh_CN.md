<p align="center">
  <h1 align="center">📖 小说智能体工作流 (Novel Agent Workflow)</h1>
  <p align="center">
    <strong>AI 驱动的全自动小说写作系统，支持完整的国际化</strong>
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

## ✨ 特性

- 🤖 **多智能体流水线** — 9 个专业化智能体分别负责：策划、世界观构建、大纲编写、章节写作、审查、润色和总结
- 📋 **多方案大纲对比** — 生成多种风格（戏剧张力型/文学深度型/商业节奏型）的总大纲，供你选择或合并
- 🔍 **并行质量审查** — 3 个并行审查员（一致性/文风/伏笔）分析每章，附带置信度评分
- ✨ **自动润色循环** — 章节自动评估并迭代改进，直到达到可配置的质量阈值
- 📍 **卷间检查点** — 在卷之间暂停，审查进度并在继续之前调整方向
- 📊 **完结总结报告** — 小说完成后自动生成完整报告：情节分析、角色弧线、统计数据和续集线索
- 🌐 **内置 11+ 语言** — 英语、简/繁体中文、日语、韩语、越南语、泰语、文言文、古典日语、拉丁语、梵语
- ➕ **自扩展国际化** — 运行时即可添加新语言！Agent 会利用 LLM 自动翻译并生成新的语言文件
- 🔌 **OpenAI 兼容后端** — 支持任何 OpenAI 兼容 API（OpenAI, Azure, 以及 LM Studio, Ollama 等本地代理）
- ⚡ **并行执行** — 世界观设定、风格指南、大纲方案和质量审查全部并行运行
- 💾 **断点续写** — 自动检测已完成章节，从中断处继续
- 📝 **丰富的元数据追踪** — 进度、章节摘要、伏笔/悬念追踪器、角色状态，全部以 Markdown 维护
- 🎨 **可自定义参数** — 所有超参数（温度、字数、重试次数等）集中管理在 config 中；用户个人设置（含 API 密钥）单独存放于 `user_config.json`（已 git-ignore）
- 📂 **项目级配置** — 每部小说可拥有独立的 `novel_config.json`，覆盖写作相关参数（字数、质量阈值、引号风格等），互不影响

## 📐 架构

```
┌────────────────────────────────────────────────────────────────┐
│                         main.py                                │
│              (语言选择 → API 设置 → 工作流)                      │
└──────────────────────────┬─────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                       workflow.py                              │
│                      (流水线编排器)                              │
│                                                                │
│   策划 ──▶ 世界观构建 + 风格指南 ──▶ 总大纲                       │
│               (并行)            (多方案对比)                     │
│                              ──▶ 分卷大纲                       │
│                              ──▶ 章节写作                       │
│                                   ├─ 润色循环                   │
│                                   ├─ 并行审查                   │
│                                   └─ 后处理                     │
│                              ──▶ 卷间检查点                     │
│                              ──▶ 完结总结                       │
└──────┬──────────┬──────────┬──────────┬───────────────────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
   agents.py  storage.py  config.py  prompts.py
  (9 个智能体) (文件读写)   (参数)    (语言桥接)
       │
       ▼
  llm_client.py  ──▶  llm_openai.py  (OpenAI 兼容)
```

### 智能体角色

| 智能体 | 职责 |
|--------|------|
| **PlannerAgent** | 通过多轮对话收集小说需求（题材、主题、结构、角色等） |
| **WorldbuildingAgent** | 生成世界观设定、角色档案、地点、时间线、力量/科技体系（并行） |
| **StyleGuideAgent** | 基于小说方案创建写作风格指南 |
| **OutlineAgent** | 生成总大纲（单方案或多风格方案对比）和分卷详细大纲 |
| **WriterAgent** | 按照大纲、风格指南和连续性上下文写作章节正文 |
| **PostWriteAgent** | 分析完成的章节，生成摘要，更新进度/伏笔元数据 |
| **QualityReviewerAgent** | 3 个并行审查员（一致性/文风/伏笔），带置信度评分 |
| **PolishAgent** | 自迭代润色：评估质量 → 改进 → 重新评估，直到达到阈值 |
| **FinalSummaryAgent** | 小说完成后生成完整报告：统计、角色弧线分析、续集线索 |

## 📁 项目结构

```
novel_writer/
├── main.py                  # 入口
├── workflow.py              # 流水线编排器
├── agents.py                # 所有专业智能体
├── config.py                # 集中配置
├── llm_client.py            # 统一 LLM 接口
├── llm_openai.py            # OpenAI 后端
├── prompts.py               # 语言感知的 Prompt 桥接
├── storage.py               # 文件读写管理
├── locale_generator.py      # 自扩展语言生成器
├── user_config.json         # 🔒 用户设置 + API 密钥（已 git-ignore）
├── user_config.example.json # user_config.json 模板
├── novel_config.example.json# 项目级配置模板
├── requirements.txt         # Python 依赖
├── locales/                 # 国际化语言文件
│   ├── __init__.py          # 语言加载器 + 自动发现
│   ├── en.py                # English（基础）
│   ├── zh_cn.py             # 简体中文
│   └── ...                  # 更多语言
├── docs/                    # 多语言 README
└── output/                  # 📂 生成的小说（已 git-ignore）
    └── <小说名>/
        ├── README.md
        ├── plan.json
        ├── meta/            # 元数据（进度、风格、伏笔）
        ├── worldbuilding/   # 世界观设定
        ├── plot/            # 大纲 & 章节摘要
        ├── chapters/        # 章节正文
        └── novel_config.json# 📖 项目级配置覆盖（可选）
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置设置

```bash
cp user_config.example.json user_config.json
```

编辑 `user_config.json`（只需保留想覆盖的字段）：

```json
{
    "OPENAI_API_KEY": "sk-你的密钥",
    "OPENAI_BASE_URL": "https://api.openai.com/v1",
    "OPENAI_MODEL": "gpt-4o",
    "TEMPERATURE": 0.7
}
```

> ⚠️ `user_config.json` 已被 git-ignore，请勿提交你的 API 密钥！
> 所有可用字段参见 `user_config.example.json`。

#### 项目级配置（可选）

每部小说可以拥有独立的 `novel_config.json`，覆盖写作相关参数：

```bash
cp novel_config.example.json output/你的小说名/novel_config.json
```

示例 — 为某部小说单独定制参数：

```json
{
    "CHAPTER_MIN_WORDS": 4000,
    "CHAPTER_MAX_WORDS": 6000,
    "QUOTE_STYLE": "corner",
    "REVIEW_CONFIDENCE_THRESHOLD": 85,
    "LAZY_MODE": true
}
```

> **配置加载顺序**：`config.py` 默认值 → `user_config.json`（全局） → `novel_config.json`（项目级）
>
> 出于安全考虑，`novel_config.json` 中的 API 相关配置（`OPENAI_API_KEY`、`API_MODE` 等）会被 **自动忽略** — 这些请在全局 `user_config.json` 中设置。
> 所有可用的项目级字段参见 `novel_config.example.json`。

### 3. 运行

```bash
python main.py
```

系统将引导你完成：

1. **选择语言** — 选择小说语言（或添加新语言！）
2. **项目设置** — 为小说项目命名
3. **选择操作** — 完整流程、断点续写或单独运行某个阶段

### 4. 操作模式

| 模式 | 说明 |
|------|------|
| **完整流程** | 从策划到最终章节的完整流程 |
| **断点续写** | 从上次中断处继续 |
| **仅策划** | 交互式对话设计小说方案 |
| **仅世界观构建** | 生成世界观设定和风格指南 |
| **仅大纲** | 生成总大纲和分卷大纲 |
| **仅写作** | 写作指定范围的章节 |
| **批量模式** | 依次生成多部小说 |

## 🌐 添加新语言

本系统可以 **自我扩展** 以支持任何新语言：

1. 在语言菜单中选择 `➕ 添加新语言`
2. 输入语言的英文名、原生名和代码
3. LLM 自动翻译所有 UI 字符串、提示词和模板
4. 新语言文件即时生成，立即可用

你也可以手动将 `.py` 语言文件放入 `locales/` 目录 — 下次启动时会自动发现。

## ⚙️ 配置参数

### 核心参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `TEMPERATURE` | 0.7 | LLM 采样温度 |
| `TOP_P` | 0.6 | 核采样阈值 |
| `MAX_OUTPUT_TOKENS` | 32768 | 每次 LLM 回复的最大 token 数 |
| `CHAPTER_MIN_WORDS` | 3000 | 每章最少字数 |
| `CHAPTER_MAX_WORDS` | 4000 | 每章最多字数 |
| `MAX_PARALLEL_WORKERS` | 3 | 并行任务数 |
| `MAX_RETRIES` | 5 | API 调用重试次数 |
| `MAX_PLANNING_ROUNDS` | 20 | 策划对话最大轮次 |

### 高级功能

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `OUTLINE_DRAFT_COUNT` | 3 | 大纲方案数量（设为 1 禁用多方案） |
| `ENABLE_PARALLEL_REVIEW` | True | 每章后运行 3 个并行质量审查 |
| `REVIEW_CONFIDENCE_THRESHOLD` | 80 | 报告问题的最低置信度（0-100） |
| `ENABLE_POLISH_LOOP` | True | 通过评估→改进循环自动精修章节 |
| `MAX_POLISH_ITERATIONS` | 2 | 每章最大润色迭代次数 |
| `POLISH_QUALITY_THRESHOLD` | 8 | 退出润色循环所需的质量分（1-10） |
| `ENABLE_VOLUME_CHECKPOINT` | True | 在卷之间暂停以确认用户意见 |
| `ENABLE_FINAL_SUMMARY` | True | 小说完成后生成完整报告 |

## 📜 许可证

MIT

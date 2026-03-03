<p align="center">
  <h1 align="center">📖 Fluxus Operis Agentis Fabulae (Novel Agent Workflow)</h1>
  <p align="center">
    <strong>Systema scribendi fabulas automaticum AI-actum cum auxilio internationalizationis pleno</strong>
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

## ✨ Proprietates

- 🤖 **Ductus Multi-Agentis** — 9 agentes speciales unamquamque phasin tractant: consilium, aedificatio mundi, adumbratio, scriptio, censura, limatura, et summa
- 🌐 **11+ Linguae Inclusae** — Anglica, Sinensis Simplex/Traditionalis, Iaponica, Coreana, Vietnamica, Thailandica, Sinensis Classica, Iaponica Classica, Latina, Sanscrita
- ➕ **i18n Se-Extendens** — Adde auxilium novae linguae in volatu! Agens utitur suo LLM ad vertendum et generandum nova fascicula loci in tempore executionis
- 🔌 **Backend OpenAI-Compatibile** — Sustinet quodlibet API OpenAI-compatibile (OpenAI, Azure, et procuratores locales sicut LM Studio, Ollama, etc.)
- 📋 **Comparatio Plurium Adumbrationum** — Plures styli (dramaticus/litterarius/commercialis) adumbrationum generantur, eligendae vel miscendae
- 🔍 **Censura Qualitatis Parallela** — 3 censores paralleli (congruentia/stylus/praesagiatio) singula capitula analysant, cum gradu fiduciae
- ✨ **Cyclus Limaturae** — Capitula automatice aestimantur et iterantur donec limen qualitatis configurabile attingatur
- 📍 **Puncta Inspectionis Voluminum** — Inter volumina subsistit, progressum recogitat et directionem ante continuandum accommodat
- 📊 **Summa Finalis** — Post completionem fabulae, automatice report completum generatur: analysis argumenti, arcus personarum, statisticae, et semina sequelae
- ⚡ **Executio Parallela** — Aedificatio mundi, duces stili, schemata adumbrationum, et censurae omnes parallele generantur
- 💾 **Resumptio Puncti-Reprehensionis** — Automatrice detegit capitula completa et resumit unde desiit
- 📝 **Vestigatio Metadata Dives** — Progressus, summaria capitulorum, vestigator praesagiorum/hamorum, status personarum — omnia in Markdown conservata
- 🎨 **Parametri Accommodabiles** — Omnes hyperparametri in config centralizantur; configuratio privata (claves API inclusae) in `user_config.json` separato reponuntur (git-ignorato)

## 📐 Architectura

```
┌────────────────────────────────────────────────────────────────┐
│                         main.py                                │
│              (Selectio Linguae → Configuratio API → Fluxus)     │
└──────────────────────────┬─────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                       workflow.py                              │
│                  (Orchestrator Ductus)                          │
│                                                                │
│   Consilium ──▶ Aedificatio Mundi + Dux Stili ──▶ Adumbratio    │
│                   (parallel)                      Magistra      │
│                                       ──▶ Adumbratio Voluminis  │
│                                       ──▶ Scriptio Capituli     │
│                                            ├─ Cyclus Limaturae  │
│                                            ├─ Censura Parallela │
│                                            └─ Post-Processus    │
│                                       ──▶ Puncta Insp. Vol.    │
│                                       ──▶ Summa Finalis         │
└──────┬──────────┬──────────┬──────────┬───────────────────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
   agents.py  storage.py  config.py  prompts.py
  (9 Agentes) (I/O Fasciculi) (Param) (Pons Loci)
       │
       ▼
  llm_client.py  ──▶  llm_openai.py  (OpenAI-compatibile)
```

### Munera Agentium

| Agens | Responsabilitas |
|-------|-----------------|
| **PlannerAgent** | Dialogus multi-vicis cum usore ad colligenda requisita fabulae (genus, thema, structura, personae, etc.) |
| **WorldbuildingAgent** | Generat occasus mundi, profile personarum, loca, lineam temporis, systemata potestatis/technologiae (parallel) |
| **StyleGuideAgent** | Creat ducem stili scribendi basatum in consilio fabulae |
| **OutlineAgent** | Generat adumbrationem magistram et adumbrationes detaliatas voluminis |
| **WriterAgent** | Scribit textum capituli sequens adumbrationes, ducem stili, et contextum continuitatis |
| **PostWriteAgent** | Analysat capitula completa, generat summaria, et renovat metadata progressus/praesagiorum |
| **QualityReviewerAgent** | 3 censores paralleli (congruentia/stylus/praesagiatio), cum gradu fiduciae |
| **PolishAgent** | Auto-iteratio limaturae: aestimat qualitatem → meliorat → re-aestimat, usque ad limen |
| **FinalSummaryAgent** | Post completionem fabulae, report completum generat: statisticae, arcus personarum, semina sequelae |

## 🚀 Initium Celer

### 1. Instrue Dependentias

```bash
pip install -r requirements.txt
```

### 2. Configura Parametros

```bash
cp user_config.example.json user_config.json
```

Edita `user_config.json` (tantum campos quos mutare vis includi oportet):

> ⚠️ `user_config.json` est git-ignoratum. Numquam committe claves API tuas!
> Vide `user_config.example.json` pro omnibus campis praesto.

#### Configuratio per Fabulam (Optionalis)

Quaeque fabula proprium `novel_config.json` habere potest ad parametros scriptionis superscribendos:

```bash
cp novel_config.example.json output/nomen_fabulae/novel_config.json
```

> **Ordo onerationis**: `config.py` defalta → `user_config.json` (globalis) → `novel_config.json` (per fabulam)
>
> Securitatis causa, claves API in `novel_config.json` **automatice praetermittuntur**. API in `user_config.json` globali configura.
> Vide `novel_config.example.json` pro omnibus campis per fabulam praesto.

### 3. Curre

```bash
python main.py
```

Duceris per:

1. **Selectio Linguae** — Elige linguam fabulae (vel adde novam!)
2. **Configuratio Proiecti** — Nomina proiectum fabulae tuae
3. **Modus Operationis** — Ductus plenus, resume, vel curre phases singulas

### Modi Operationis

| Modus | Descriptio |
|-------|------------|
| **Ductus Plenus** | Curre fluxum completum a consilio ad capitulum finale |
| **Resume** | Continua a puncto reprehensionis ultimo |
| **Consilium Solum** | Dialogus interactivus ad designandum fabulam |
| **Aedificatio Mundi Solum** | Genera occasus mundi et ducem stili |
| **Adumbratio Sola** | Genera adumbrationes magistram et voluminis |
| **Scriptio Sola** | Scribe capitula (specifica ambitum) |
| **Modus Cumulativus** | Plures fabulas ordine genera |

## 🌐 Additio Novae Linguae

Novel Agent Workflow potest **se extendere** ad sustinendum quamlibet linguam novam:

1. Elige `➕ Adde linguam novam` ex menu linguae
2. Intra nomen Anglicum, nomen nativum, et codicem linguae
3. LLM automatice vertit omnes chordas UI, promptus, et formulas
4. Novum fasciculum loci generatur et statim praesto est

Potes etiam manualiter ponere fasciculum `.py` loci in `locales/` — automatice detegitur in proximo initio.

## ⚙️ Configuratio

Omnes hyperparametri in `config.py` centralizantur:

| Parameter | Defalta | Descriptio |
|-----------|---------|------------|
| `TEMPERATURE` | 0.7 | Temperatura exemplaris LLM |
| `TOP_P` | 0.6 | Limen exemplaris nuclei |
| `MAX_OUTPUT_TOKENS` | 32768 | Maxima signa per responsum LLM |
| `CHAPTER_MIN_WORDS` | 3000 | Minima verba per capitulum |
| `CHAPTER_MAX_WORDS` | 4000 | Maxima verba per capitulum |
| `MAX_PARALLEL_WORKERS` | 3 | Operarii muneris paralleli |
| `MAX_RETRIES` | 5 | Conatus iterandi vocationis API |

### Parametri Provecti

| Parameter | Defalta | Descriptio |
|-----------|---------|------------|
| `OUTLINE_DRAFT_COUNT` | 3 | Numerus schematum adumbrationis (1 ad disabilitandum) |
| `ENABLE_PARALLEL_REVIEW` | True | 3 censores paralleli post unumquodque capitulum |
| `ENABLE_POLISH_LOOP` | True | Capitula automatice per cyclum aestimationis→meliorationis limantur |
| `POLISH_QUALITY_THRESHOLD` | 8 | Nota qualitatis ad exitum cycli limaturae (1-10) |
| `ENABLE_VOLUME_CHECKPOINT` | True | Inter volumina subsistit ad confirmationem usoris |
| `ENABLE_FINAL_SUMMARY` | True | Report completum post fabulam completam generat |

## 📜 Licentia

MIT

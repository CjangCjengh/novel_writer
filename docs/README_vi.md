
<p align="center">
  <h1 align="center">📖 Quy Trình Viết Tiểu Thuyết Bằng AI (Novel Agent Workflow)</h1>
  <p align="center">
    <strong>Hệ thống viết tiểu thuyết tự động bằng AI — Hỗ trợ đa ngôn ngữ hoàn chỉnh</strong>
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

## ✨ Tính Năng

- 🤖 **Pipeline Đa Tác Nhân** — 9 tác nhân chuyên biệt đảm nhiệm: lên kế hoạch, xây dựng thế giới, phác thảo, viết chương, đánh giá, chỉnh sửa và tổng kết
- 📋 **So sánh nhiều bản thảo đề cương** — Tạo đề cương với nhiều phong cách (kịch tính/văn học/thương mại) để chọn hoặc hợp nhất
- 🔍 **Đánh giá chất lượng song song** — 3 người đánh giá song song (tính nhất quán/phong cách/phục bút) phân tích mỗi chương, có điểm tin cậy
- ✨ **Vòng chỉnh sửa tự động** — Tự động đánh giá chương và cải thiện lặp lại cho đến khi đạt ngưỡng chất lượng
- 📍 **Điểm kiểm tra giữa các tập** — Tạm dừng giữa các tập để xem xét tiến độ và điều chỉnh hướng đi
- 📊 **Báo cáo tổng kết cuối cùng** — Tự động tạo báo cáo đầy đủ sau khi hoàn thành: phân tích cốt truyện, vòng cung nhân vật, thống kê, manh mối cho phần tiếp theo
- 🌐 **Hơn 11 ngôn ngữ tích hợp** — Tiếng Anh, Trung giản thể/phồn thể, Nhật, Hàn, Việt, Thái, Hán cổ, Nhật cổ, Latinh, Phạn
- ➕ **Tự mở rộng i18n** — Thêm ngôn ngữ mới khi đang chạy!
- 🔌 **Backend Tương Thích OpenAI** — Hỗ trợ bất kỳ API nào tương thích với OpenAI
- ⚡ **Thực thi song song** — Xây dựng thế giới, hướng dẫn phong cách, bản thảo đề cương và đánh giá chất lượng đều chạy song song
- 💾 **Tiếp tục từ điểm kiểm tra** — Tự động phát hiện các chương đã hoàn thành và tiếp tục
- 📝 **Theo dõi siêu dữ liệu phong phú** — Tiến độ, tóm tắt chương, theo dõi phục bút, trạng thái nhân vật
- 🎨 **Tham số tùy chỉnh** — Tất cả siêu tham số tập trung trong config; cài đặt cá nhân (bao gồm khóa API) trong `user_config.json` (git-ignore)

## 📐 Kiến Trúc

```
┌────────────────────────────────────────────────────────────────┐
│                         main.py                                │
│             (Chọn ngôn ngữ → Cài đặt API → Quy trình)         │
└──────────────────────────┬─────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                       workflow.py                              │
│                  (Điều phối Pipeline)                           │
│                                                                │
│   Lên kế hoạch ──▶ Xây dựng thế giới + Hướng dẫn phong cách  │
│                       (song song)                              │
│                                   ──▶ Phác thảo tổng thể      │
│                                       (So sánh đa bản thảo)   │
│                                   ──▶ Phác thảo từng tập      │
│                                   ──▶ Viết chương              │
│                                        ├─ Vòng chỉnh sửa     │
│                                        ├─ Đánh giá song song  │
│                                        └─ Hậu xử lý          │
│                                   ──▶ Điểm kiểm tra giữa tập │
│                                   ──▶ Tổng kết cuối cùng     │
└──────┬──────────┬──────────┬──────────┬───────────────────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
   agents.py  storage.py  config.py  prompts.py
  (9 Tác nhân) (File I/O) (Cấu hình) (Cầu nối ngôn ngữ)
       │
       ▼
  llm_client.py  ──▶  llm_openai.py  (Tương thích OpenAI)
```

### Vai Trò Tác Nhân

| Tác Nhân | Vai Trò |
|----------|---------|
| **PlannerAgent** | Thu thập yêu cầu tiểu thuyết qua đối thoại nhiều lượt (thể loại, chủ đề, cấu trúc, nhân vật, v.v.) |
| **WorldbuildingAgent** | Tạo bối cảnh thế giới, hồ sơ nhân vật, địa điểm, dòng thời gian, hệ thống năng lực/công nghệ (song song) |
| **StyleGuideAgent** | Tạo hướng dẫn phong cách viết dựa trên kế hoạch tiểu thuyết |
| **OutlineAgent** | Tạo phác thảo tổng thể (đơn hoặc so sánh đa bản thảo) và phác thảo chi tiết từng tập |
| **WriterAgent** | Viết nội dung chương theo phác thảo, hướng dẫn phong cách và ngữ cảnh liên tục |
| **PostWriteAgent** | Phân tích chương đã hoàn thành, tạo tóm tắt, cập nhật siêu dữ liệu tiến độ/phục bút |
| **QualityReviewerAgent** | 3 người đánh giá song song (nhất quán/phong cách/phục bút), có điểm tin cậy |
| **PolishAgent** | Tự lặp chỉnh sửa: đánh giá chất lượng → cải thiện → đánh giá lại, đến khi đạt ngưỡng |
| **FinalSummaryAgent** | Báo cáo đầy đủ sau hoàn thành: thống kê, phân tích vòng cung nhân vật, manh mối tiếp theo |

## 🚀 Bắt Đầu Nhanh

### 1. Cài đặt phụ thuộc

```bash
pip install -r requirements.txt
```

### 2. Cấu hình cài đặt

```bash
cp user_config.example.json user_config.json
```

Chỉnh sửa `user_config.json`, điền thông tin xác thực API và các tùy chọn của bạn (chỉ cần giữ lại các trường muốn ghi đè).

> ⚠️ `user_config.json` đã được git-ignore. Đừng commit khóa API!
> Xem `user_config.example.json` để biết tất cả các trường có sẵn.

#### Cấu hình riêng cho từng tiểu thuyết (Tùy chọn)

Mỗi dự án tiểu thuyết có thể có `novel_config.json` riêng để ghi đè các tham số viết:

```bash
cp novel_config.example.json output/ten_tieu_thuyet/novel_config.json
```

> **Thứ tự tải cấu hình**: `config.py` mặc định → `user_config.json` (toàn cục) → `novel_config.json` (riêng tiểu thuyết)
>
> Vì lý do bảo mật, các khóa API trong `novel_config.json` sẽ bị **tự động bỏ qua**. Hãy cấu hình API trong `user_config.json` toàn cục.
> Xem `novel_config.example.json` để biết tất cả các trường có sẵn cho từng tiểu thuyết.

### 3. Chạy

```bash
python main.py
```

Hệ thống sẽ hướng dẫn bạn:

1. **Chọn ngôn ngữ** — Chọn ngôn ngữ tiểu thuyết (hoặc thêm ngôn ngữ mới!)
2. **Cài đặt dự án** — Đặt tên cho dự án tiểu thuyết
3. **Chọn thao tác** — Pipeline đầy đủ, tiếp tục, hoặc chạy từng giai đoạn

### Chế Độ Thao Tác

| Chế Độ | Mô Tả |
|--------|-------|
| **Pipeline đầy đủ** | Toàn bộ quy trình từ lên kế hoạch đến chương cuối |
| **Tiếp tục** | Tiếp tục từ điểm kiểm tra cuối |
| **Chỉ lên kế hoạch** | Đối thoại tương tác để thiết kế tiểu thuyết |
| **Chỉ xây dựng thế giới** | Tạo bối cảnh thế giới và hướng dẫn phong cách |
| **Chỉ phác thảo** | Tạo phác thảo tổng thể và từng tập |
| **Chỉ viết** | Viết các chương trong phạm vi chỉ định |
| **Chế độ hàng loạt** | Tạo nhiều tiểu thuyết tuần tự |

## 🌐 Thêm Ngôn Ngữ Mới

Chọn `➕ Thêm ngôn ngữ mới` từ menu ngôn ngữ, nhập thông tin ngôn ngữ, LLM sẽ tự động dịch tất cả chuỗi UI, prompt và template, tạo tệp ngôn ngữ mới ngay lập tức.

Bạn cũng có thể đặt tệp `.py` vào thư mục `locales/` — nó sẽ được tự động phát hiện khi khởi động lần sau.

## ⚙️ Tham Số Cấu Hình

### Tham Số Cốt Lõi

| Tham Số | Mặc Định | Mô Tả |
|---------|----------|-------|
| `TEMPERATURE` | 0.7 | Nhiệt độ lấy mẫu LLM |
| `TOP_P` | 0.6 | Ngưỡng lấy mẫu hạt nhân |
| `MAX_OUTPUT_TOKENS` | 32768 | Số token tối đa mỗi phản hồi LLM |
| `CHAPTER_MIN_WORDS` | 3000 | Số từ tối thiểu mỗi chương |
| `CHAPTER_MAX_WORDS` | 4000 | Số từ tối đa mỗi chương |
| `MAX_PARALLEL_WORKERS` | 3 | Số tác vụ song song |
| `MAX_RETRIES` | 5 | Số lần thử lại API |

### Tính Năng Nâng Cao

| Tham Số | Mặc Định | Mô Tả |
|---------|----------|-------|
| `OUTLINE_DRAFT_COUNT` | 3 | Số bản thảo đề cương (đặt 1 để tắt) |
| `ENABLE_PARALLEL_REVIEW` | True | Chạy 3 đánh giá chất lượng song song sau mỗi chương |
| `ENABLE_POLISH_LOOP` | True | Tự động chỉnh sửa chương qua vòng đánh giá→cải thiện |
| `POLISH_QUALITY_THRESHOLD` | 8 | Điểm chất lượng cần đạt để thoát vòng chỉnh sửa (1-10) |
| `ENABLE_VOLUME_CHECKPOINT` | True | Tạm dừng giữa các tập để xác nhận người dùng |
| `ENABLE_FINAL_SUMMARY` | True | Tạo báo cáo đầy đủ sau khi hoàn thành tiểu thuyết |

## 📜 Giấy Phép

MIT

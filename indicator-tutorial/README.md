# Hướng dẫn HVI × ST1 × ST2

Video ngang 1920 × 1080, 24 fps, khoảng 8 phút 15 giây. Phong cách kỹ thuật nền sáng, Buy xanh / Sell đỏ. Có thuyết minh tiếng Việt bằng eSpeak NG ngoại tuyến; giọng có âm sắc máy.

## Nội dung
21 cảnh: thiết lập hai indicator, thông số ST1/ST2, logic nhãn HVI, bộ lọc ST2, hai mẫu cơ bản, toàn bộ ngoại lệ ảnh 3 và 5, cách chờ hồi ảnh 4, entry và bảng kiểm.

Vùng Fibonacci: giá hồi vào 0.618–0.786 rồi bị từ chối, theo xác nhận của tác giả trong chat.

Biểu đồ là sơ đồ dựng lại để diễn giải quy tắc, không phải ảnh TradingView gốc, dữ liệu thị trường, kết quả Pine hoặc kết quả kiểm thử chiến lược. Chưa có tệp ảnh gốc trong workspace để lồng ảnh trực tiếp. Các mốc entry không được gán giá thị trường giả.

## Tệp
- `huong-dan-HVI-ST1-ST2.mp4`: video khi xuất hoàn tất.
- `narration.txt`: kịch bản thuyết minh đầy đủ.
- `chapters.txt`: mốc chương.
- `thuyet-minh.srt`: phụ đề ngoài; thời gian câu phân bổ theo độ dài lời đọc, không phải căn chỉnh từng từ.
- `index.html`, `assets/`: bản dựng HyperFrames có thể chỉnh sửa.
- `scenes.json`, `timing.json`: nội dung và thời lượng.

## Đối chiếu mã
- ST1 mặc định ATR 10, hệ số 6; đường Buy xanh dương / Sell cam; nhãn mặc định ẩn.
- ST2 mặc định ATR 10, hệ số 4; nhãn mặc định bật, qua bộ lọc QQE/HVI và RSI.
- HVI Buy: đỏ → xám; RSI và QQE xanh cả hai nến. HVI Sell: cam → xám; RSI và QQE đỏ cả hai nến.
- Cảnh báo ST2 dùng `{{close}}` làm entry tham chiếu.
- Hai file là indicator; các ngoại lệ theo ST1, Fibonacci và chờ hồi là quy tắc diễn giải của tác giả, chưa được tự động hóa toàn bộ.
- Không biên dịch Pine trong môi trường này; cần TradingView để kiểm tra trực tiếp.

## Xuất lại
Bản MP4 giao kèm ghép các khung hình HyperFrames bằng FFmpeg, giữ hình trong lúc thuyết minh và chuyển cảnh qua nền sáng. Tệp nguồn HTML cũng có các hoạt ảnh mở đầu chi tiết để chỉnh sửa tiếp.

Node 22+, FFmpeg và Chromium; chạy trong thư mục dự án:

```sh
HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm run check
HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npx --yes hyperframes@0.9.0 render --fps 24 --quality standard --workers 4 --output huong-dan-HVI-ST1-ST2.mp4
```

`compose.py` dựng HTML từ nội dung và timing. `build.py` tạo lại audio, cần eSpeak NG và các thư viện đã giải nén trong `/workspace/voice-runtime`; đường dẫn này phụ thuộc môi trường. Có thể thay WAV bằng giọng tự thu hoặc giọng tự nhiên, rồi cập nhật timing.

Để xuất đúng bản MP4 dùng các khung hình đã đóng gói, chạy `python3 export_video.py`. Thư mục `delivery-frames/` chứa khung hình từ HyperFrames ở giây thứ hai mỗi cảnh.

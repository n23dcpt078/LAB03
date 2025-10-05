# LAB03 — Selenium Login Form Testing

## 🔎 Mô tả
Dự án kiểm thử form đăng nhập (`login.html`) bằng **Selenium (Python)**.  
Trên form có các thành phần:  
- 2 ô **Username / Password**  
- Nút **LOGIN**  
- Link **Forgot password?**  
- Link **SIGN UP**  
- Nút login social (Facebook, Twitter, Google)

## 📂 Cấu trúc thư mục
LAB03/
│
├── login.html # Giao diện form đăng nhập
├── test.py # Script Selenium để chạy các test case
├── testlogin.png # Screenshot kết quả chạy test
└── README.md # Hướng dẫn sử dụng và liệt kê test case

## ✅ Các Test Case

Dưới đây là **6 test case tối thiểu** đã được thực hiện:

| TC ID | Mục tiêu kiểm thử                        | Dữ liệu nhập                         | Kết quả mong đợi                                               |
|:-----:|--------------------------------------------|---------------------------------------|-----------------------------------------------------------------|
| TC01  | Đăng nhập thành công                       | Username & Password hợp lệ            | Chuyển sang Dashboard hoặc thông báo “Login success”             |
| TC02  | Sai mật khẩu                               | Username đúng, Password sai           | Hiển thị thông báo lỗi “Invalid credentials”                     |
| TC03  | Bỏ trống Username/Password                 | Không nhập hoặc bỏ trống trường        | Hiển thị cảnh báo yêu cầu nhập (ví dụ: “Please fill all required fields”) |
| TC04  | Link **Forgot password?**                  | -                                     | Link hiện và click được, điều hướng đến trang quên mật khẩu     |
| TC05  | Link **SIGN UP**                           | -                                     | Link hiện đúng, click được                                      |
| TC06  | Các nút **Social login** (Facebook, Twitter, Google) | -                           | Cả ba nút đều hiển thị và có thể click được                     |

## 🛠 Hướng dẫn chạy test

1. Clone repo về máy:
   ```bash
   git clone https://github.com/n23dcpt078/LAB03.git
   cd LAB03
   ```

2. Cài các thư viện cần thiết (ví dụ Selenium, webdriver-manager, nếu bạn dùng ChromeDriver):
```
pip install selenium webdriver-manager
```

3. Chạy Live Server hoặc máy chủ web local để phục vụ login.html (hoặc mở trực tiếp file nếu được hỗ trợ).
4. Chạy script test:
```
python test.py
```
5. Quan sát kết quả chạy test trong terminal. Nếu mọi thứ thành công, bạn sẽ thấy dòng thông báo mỗi test case "Passed" và cuối cùng ảnh chụp màn hình (testlogin.png) minh hoạ kết quả.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Mở trang login chạy qua Live Server
driver.get("http://127.0.0.1:5500/login.html")
driver.maximize_window()

def reset_form():
    driver.get("http://127.0.0.1:5500/login.html")
    time.sleep(1)

# ---- Test case 1: Đăng nhập thành công ----
reset_form()
driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
driver.find_element(By.ID, "password").send_keys("P@ssw0rd")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(1)
assert "dashboard" in driver.current_url or "Login success" in driver.page_source
print("✅ Test 1 Passed: Đăng nhập thành công")

# ---- Test case 2: Sai thông tin đăng nhập ----
reset_form()
driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
driver.find_element(By.ID, "password").send_keys("sai123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(1)
msg = driver.find_element(By.ID, "msg-error").text
assert "Invalid credentials" in msg
print("✅ Test 2 Passed: Sai thông tin đăng nhập")

# ---- Test case 3: Bỏ trống trường ----
reset_form()
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "btnLogin").click()
time.sleep(1)
msg = driver.find_element(By.ID, "msg-error").text
assert "Please fill all required fields" in msg
print("✅ Test 3 Passed: Bỏ trống Username/Password hiển thị cảnh báo")

# ---- Test case 4: Link Forgot password? ----
reset_form()
link_forgot = driver.find_element(By.ID, "linkForgot")
assert link_forgot.is_displayed() and link_forgot.is_enabled()
link_forgot.click()
print("✅ Test 4 Passed: Link 'Forgot password?' tồn tại và có thể click")

# ---- Test case 5: Link SIGN UP ----
reset_form()
link_signup = driver.find_element(By.ID, "linkSignup")
assert link_signup.is_displayed() and link_signup.is_enabled()
link_signup.click()
print("✅ Test 5 Passed: Link SIGN UP hiển thị và có thể click")

# ---- Test case 6: Nút social login ----
reset_form()
btn_facebook = driver.find_element(By.ID, "btnFacebook")
btn_twitter = driver.find_element(By.ID, "btnTwitter")
btn_google = driver.find_element(By.ID, "btnGoogle")
assert all([btn_facebook.is_displayed(), btn_twitter.is_displayed(), btn_google.is_displayed()])
print("✅ Test 6 Passed: Hiển thị đủ 3 nút social (Facebook, Twitter, Google)")

# Kết thúc kiểm thử
driver.quit()
print("\n🎉 Tất cả test case đã chạy xong!")

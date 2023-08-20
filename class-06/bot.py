# cheatsheet
import pyautogui

# หาว่าปันจุบันเมาส์อยู่ตรงไหน
x, y = pyautogui.position()
print(x, y)
# จอขนาดเท่าไหร่
width, height = pyautogui.size()
print(width, height)

# ขยับเมาส์ไปที่ บนซ้ายสุด
# pyautogui.moveTo(1, 1, duration=5)

# หยุดชั่วคราว
# pyautogui.sleep(3)

# ขยับเมส์ไปกลางจอ
# pyautogui.moveTo(int(width / 2), int(height / 2), duration=5)

# ขยับเมาส์จากที่ปัจจุบัน
# pyautogui.moveRel(100, 100, duration=1)

# # คลิกซ้าย
# pyautogui.moveTo(50, 175, duration=1)
# pyautogui.click()

# คลิ๊ก
# pyautogui.click(50, 175, duration=1)

# พิมพ์ข้อความ
# pyautogui.click()
# pyautogui.typewrite("Hello World", interval=0.1)

# ฟังก์ชั่นอื่นๆ
# pyautogui.alert("Hello World")
# pyautogui.confirm("Hello World")
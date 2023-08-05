# นี่คือ comment, จะไม่มีผลกับโปรแกรม
# Math operators
# +
1 + 2
# -
1 - 2
# *
4 * 2
# /
4 / 2
5 / 2
# % หารเอาเศษ
5 % 2
5 % 5
# // หารเอาส่วน
5 // 2
5 // 5
# ** ยกกำลัง
2 ** 4
# คิดเลขหลาย steps
5 + 2 * 3 - ( 1 + 5 )
5 + 2 * 3 - ( 1 + 5 ) ** 2

# Types
# int จำนวนเต็ม
1
2
5
-1
-4
type(1)
# float จำนวนจริง
1.0
2.0
-3.0
-5.5
type(1.0)
type(-1.5)
5/5
type(5/5)  # float หรือ int ?
# str string ข้อความ
"jdhvuiasdvnadfv"
"5"
type("5")
'5'
"567"
# เล่นกับ string
"สวัสดี " * 5
# "สวัสดี " * 5.1
# "สวัสดี ชาวโลก
"สวัสดี " + "ชาวโลก" + " 5"
# "ชาวโลก" - 5
'ชาวโลก'  # ' หรือ " ก็ได้
"""
สวัสดี ชาวโลก
เราเขียน comment ยาวๆ ได้
นี่ก็เป็น comment
"""
# สวัสดี ชาวโลก
# เราเขียน comment ยาวๆ ได้

# Variables ตัวแปร
box = "กล้วย"
box
box = "แอปเปิ้ล"
box
box = 5
box
box = 5.0
box = "ส้ม" * 5
box
###
notepad = 5 * 8 * 13
notepad
notepad2 = 2
notepad * notepad2
###
PI = 3.14
radius = 5

area_of_circle = PI * radius ** 2
area_of_circle
area_of_circle2 = PI * 10 ** 2
area_of_circle2

# การตั้งชื่อตัวแปรมีข้อห้ามอยู่
# 0a = 5  # ตัวแรกขค้นต้นตัวเลขไม่ได้
# ไม่ควรเขียนทับฟังก์ชันที่มีอยู่แล้ว
# print(5)
# print = 5
# print(5)

# input
name = input("What is your name? ")
print('สวัสดี, ' + name)
age = input("How old are you? (ปี) ")
print('คุณอายุ ' + age + ' ปี')
print(type(age))
age_in_months = int(age) * 12
age_in_months
print('คุณอายุ ' + str(age_in_months) + ' เดือน')
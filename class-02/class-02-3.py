# Loops
# While loop
"""
while loop ตรวจสอบ condition ก่อน ถ้าเป็นจริงจะทำงาน ถ้าเป็นเท็จจะหยุดทำงาน
"""

num = 5
while num > 0:
    print("num: ", num)
    num = num - 1

# continue คือ ข้ามไป
num = 5
while num > 0:
    print("num: ", num)
    if num == 3:
        num = num - 1
        print("เจอ 3")
        continue
    num = num - 1
    print("hello")

# break คือ หยุดทำงาน
num = 5
while num > 0:
    if num == 3:
        num = num - 1
        print("เจอ 3")
        break
    num = num - 1
    print("hello")
# for loop
# range(1, 9) แปลว่าสร้างกล่องที่มีตัวเลข 1 ถึง 9 ในนั้น
for i in range(1, 10):
    print(i)

# การใช้งาน continue
for i in range(1, 10):
    if i == 3:
        continue
    print(i)

# การใช้งาน break
for i in range(1, 10):
    if i == 3:
        break
    print(i)

# การใช้งานแบบย้อนกลับ
for i in range(10, 0, -1):
    print(i)

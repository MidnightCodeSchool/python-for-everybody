"""
# Challenge
## ให้เขียนโปรแกรม if elif else โดยให้ทำงานตามโจทย์ต่อไปนี้
- [ ] ถ้าเงินเดือนมากกว่า 50000 ให้พิมพ์ว่า "เงินเดือนมากกว่า 50000"
- [ ] ถ้าเงินเดือนมากกว่า 30000 แต่น้อยกว่า 50000 ให้พิมพ์ว่า เงินเดือนมากกว่า 30000 แต่น้อยกว่า 50000
- [ ] เงินเดือนน้อยกว่า 30000 ให้พิมพ์ว่า เงินเดือนน้อยกว่า 30000
- [ ] รับค่าด้วย input()
- [ ] ไม่มี error
- [ ] ไฟล์ชื่อ my_salary.py
"""

salary = input("Enter your salary: ")
salary = float(salary)

if salary > 50000:
    print("เงินเดือนมากกว่า 50000")
elif salary == 50000:
    print("เงินเดือนเท่ากับ 50000, ว๊าว")
elif salary > 30000:
    print("เงินเดือนมากกว่า 30000 แต่น้อยกว่า 50000")
else:
    print("เงินเดือนน้อยกว่า 30000")
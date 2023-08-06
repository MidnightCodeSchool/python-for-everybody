"""
## FizzBuzz fizzbuzz_forloop.py
- [ ] รับค่าด้วย input() เป็นตัวเลข
- [ ] พิมพ์ตัวเลขที่รับเข้ามา จนถึง 0
- [ ] ถ้าเลขหาร 3 ลงตัว ให้พิมพ์ Fizz แทนที่จะพิมพ์ตัวเลข
- [ ] ถ้าเลขหาร 5 ลงตัว ให้พิมพ์ Buzz แทนที่จะพิมพ์ตัวเลข
- [ ] ให้ใช้ for loop
"""
number = int(input("Enter number: "))

for i in range(number, -1, -1):
    if i == 0:
        print("0")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
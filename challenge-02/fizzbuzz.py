"""
## FizzBuzz fizzbuzz.py
- [ ] รับค่าด้วย input() เป็นตัวเลข
- [ ] พิมพ์ตัวเลขที่รับเข้ามา จนถึง 0
- [ ] ถ้าเลขหาร 3 ลงตัว ให้พิมพ์ Fizz แทนที่จะพิมพ์ตัวเลข
- [ ] ถ้าเลขหาร 5 ลงตัว ให้พิมพ์ Buzz แทนที่จะพิมพ์ตัวเลข
"""
# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
number = int(input("Enter number: "))

while number >= 0:
    if number == 0:
        print("0")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number = number - 1

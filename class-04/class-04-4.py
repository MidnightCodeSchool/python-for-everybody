import random


def get_random_number():
    """func คนอื่นเขียนมาแล้วแก้ไม่ได้ ใช้ได้เท่านั้น
    คืนค่า 0, 1 สุ่มออกมา
    """
    return random.choice([0, 1])


random_number = get_random_number()
print(random_number)
if random_number == 0:
    raise ValueError("Cannot be zero")

# ทำงานอื่นตรงนี้ไปเยอะเลย

result = 10 / random_number

# ทำงานอื่นตรงนี้ไปอีกเยอะ

print(result)

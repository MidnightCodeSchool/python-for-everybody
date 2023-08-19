import random


def call_func():
    """
    random ฟังก์ชั่นพัง
    """
    num = random.choice([1, 'one'])  # 1 -> ok, 'one' -> not ok
    num = int(num)
    return {'status': num}

print('start program')
try:
    respond = call_func()
except ValueError as e:
    respond = {'status': 0}
finally:
    print('finally')
print(respond['status'])
print('end program')
v1 = 'hello'
v2 = 5
v3 = 10.5
my_other_list = [3.14, 5, 6]
my_list = [v1, v2, v3]
# เรียกดูสมาชิกใน list
my_list[0]
my_list[1]
my_list[2]
# มีสมาชิกทั้งหมดกี่ตัว
len(my_list)
## การเพิ่มสมาชิกใน list
my_list.append(100)
my_list
my_list[3]
len(my_list)

# function
# เขียน function บวกเลข a, b
def add(a, b):
    """
    บวกเลข a, b แล้วคืนค่า a + b
    """
    return a + b

def subtract(a, b):
    """
    ลบเลข a, b แล้วคืนค่า a - b
    """
    print('a =', a)
    print('b =', b)
    return a - b

# add(5, 7)
subtract(5, 7)
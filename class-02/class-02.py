# Built in fuctions
## Type casting (แปลงชนิดข้อมูล) str, int, float
my_string = "123"
my_int = int(my_string)
my_float = float(my_string)
print("int: ", my_int, " ", "float:", my_float)
my_new_string = str(my_int)
print("str: ", my_new_string)

# Flow control
## boolean
## Keyword: คคำที่มีความหมายพิเศษ ใช้ในการเขียนโปรแกรม ไม่สามารถใช้เป็นชื่อตัวแปรได้
my_bool = True
my_other_bool = False
print(type(my_bool))
print("my_bool: ", my_bool)
## Comparison operators
## >, <, >=, <=, ==, !=
1 > 0
1 < 0
1 >= 1
1 >= 2
1 >= 0
1 == 1
1 != 2
a = '5'
b = '5'
a != b
a == b
c = 5
b == c
age = 19
is_age_more_than_18 = age > 18
print("age_more_than_18: ", is_age_more_than_18)
## Truth table, and, or
print("True and True: ", True and True)  # True
print("True and False: ", True and False)  # False
print("False and True: ", False and True)  # False
print("False and False: ", False and False)  # False
is_age_more_than_18 = age > 18
is_age_less_than_20 = age < 20
print("Age between 18 and 20? : ", is_age_more_than_18 and is_age_less_than_20)
print("True or True: ", True or True)  # True
print("True or False: ", True or False)  # True
print("False or True: ", False or True)  # True
print("False or False: ", False or False)  # False
# กลับด้าน boolean
print("not True: ", not True)  # False
print("not False: ", not False)  # True
# boolean expression
(1 > 0) and (2 > 1)
(1 > 0) and (2 < 1)
(1 < 0) and (2 > 1) or (1 > 0)
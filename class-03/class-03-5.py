# เขียน function อ่านไฟล์ชื่อ input.txt แล้วแสดงผลออกมาทางหน้าจอ
from rich import print


def read_file():
    with open('input.txt', 'r') as file:
        return file.read()


print(read_file())

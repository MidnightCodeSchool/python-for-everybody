from rich import print


def five_divide_by(num):
    result = 5 / num
    return result


def main():
    print("เดี๋ยวจะเอาเลขที่คุณให้มาหาร 5 นะ ex. 5 / (เลข)")
    num = input('give me number: ')
    try:
        converted_num = int(num)
    except ValueError:
        print('ใส่เลขมาให้ถูกต้องนะครับ')
        exit()

    if converted_num == 0:
        print('ห้ามใส่ 0 นะครับ')
        exit()

    result = five_divide_by(converted_num)
    print(f'ผลลัพธ์คือ {result}')


if __name__ == '__main__':
    main()

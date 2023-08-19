global_val = 1234
global_val2 = 4567

def func():
    global global_val
    global_val = 1
    print(f'inside f1: {global_val=}')


def func2():
    global_val2 = 2
    print(f'inside f2: {global_val2=}')


def func3():
    global_val2
    print(f'inside f3: {global_val2=}')


func()
func2()
func3()
print(f'{global_val=}')
print(f'{global_val2=}')
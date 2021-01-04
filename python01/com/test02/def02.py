def func01(x, y):
    print('전달값으로', x, '와', y, '가 들어왔습니다')
    # ? + ? = ??
    print('{0} + {1} = {2}'.format(x, y, x+y))


def func02(x, y):
    return x+y


def func03(x, y):
    return x+y, x-y


if __name__ == "__main__":
    #func01(5, 6)
    #print(func02(4, 7))
    num1 = int(input('첫번째 정수 입력 : '))
    num2 = int(input('두번째 정수 입력 : '))
    sum, minus = func03(num1, num2)
    print(sum)
    print(minus)
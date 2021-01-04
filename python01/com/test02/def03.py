
'''
1. for문을 사용하여 2~9단까지의 구구단을 출력하는 함수 gugu() 만들어서 호출하자!
2. for문을 사용하여 전달받은 단을 출력하는 함수 gugudan(매개변수) 만들어서 호출!
   2번 함수 호출시에 사용자가 입력한 단을 전달하면서 호출
'''
def gugu():
    for dan in range(2, 10):
        print('***', dan, '단 ***')
        for su in range(1, 10):
            print(dan, 'x', su, '=', dan*su)
        print()


def gugudan(dan):
    print('***', dan, '단 ***')
    for su in range(1, 10):
        print('{0} x {1} = {2}'.format(dan, su, dan*su))


if __name__ == "__main__":
    #gugu()
    #gugudan(5)
    gugudan(int(input('단 입력 : ')))
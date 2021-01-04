# def 함수명(매개변수):
def func01():
    print('매개변수 없고 반환값도 없는 함수')


def func02():
    print('매개변수 없고 반환값은 있는 함수')
    return 'I클래스'


def func03():
    print('매개변수 없고 배열을 반환하는 함수')
    return ['java', 'python']


def func04():
    print('매개변수 없고 dictionary를 반환하는 함수')
    return {'name':'홍길동', 'age':10}


def func05():
    print('매개변수 없고 여러개의 결과값을 반환하는 함수')
    return 1, 2


# 메인 함수
if __name__ == "__main__":
    print('프로그램 시작시 가장 먼저 호출됨(자바에서의 main메소드같은 느낌)')
    #func01()
    #print(func02())

    #arr = func03()
    #print(arr)
    #print(arr[0])
    #print(func03()[0])

    #print(func04()['name'])
    result = func05() # 반환값이 여러개이면서 기록하는 변수는 하나일 경우 tuple
    print(result)
    print(type(result))
    print(result[0])

    a, b = func05() # 반환값이 여러개일때 기록하는 변수또한 여러개일 경우 각각담김
    print(a)
    print(b)
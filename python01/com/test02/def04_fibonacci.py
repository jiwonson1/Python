# 피보나치 수열
# 0 1 1 2 3 5 8 13 21 34 ....
# 앞의 두개의 항의 덧셈연산 결과가 그다음에 배치

# 사용자가 입력한 값보다 작은 정수까지의 피보나치 수열을 출력
'''
num = int(input('양수 : ')) # 10
a, b = 0, 1
while a < num:
    print(a, end=' ')
    #temp = a
    #a = b
    #b = b + temp
    a, b = b, a+b
'''

# 함수로 정의해보자!!
# 전달받은 값보다 작은 정수까지의 피보나치 수열을 출력
'''
def fibonacci1(num):
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a+b

if __name__ == "__main__":
    fibonacci1(100)
'''


# 사용자가 입력한 값보다 작은 정수까지의 피보나치 수열을 리스트에 저장해보자
'''
num = int(input('양수 : '))
a,b=0,1
result = list()
while a < num:
    result.append(a)
    a,b=b,a+b
print(result)
'''

# 함수로 정의해보자!
# 전달받은 값보다 작은 정수까지의 피보나치 수열을 리스트에 담은 후 리턴
def fibonacci2(num):
    a,b=0,1
    result = list()
    while a<num:
        result.append(a)
        a,b=b,a+b
    return result


if __name__ == "__main__":
    print(fibonacci2(50))





# 주의할점 : 자바와는 다르게 영역을 지정할때 {} 블럭을 표기하지 않음!!
#           들여쓰기 굉장히 중시 생각해야됨!!


# 조건문

# 단독 if
a = 1

if a==1:
    print('인정')
    print('a는 1이야')


# if-else
a = 10

if a==1:
    print('a는 1입니다')
else:
    print('a는 1이 아닙니다')

# if-else if
b = 2

if b==1:
    print('b는 1입니다')
elif b==2:
    print('b는 2입니다')
else:
    print('b는 1도 아니고 2도 아닙니다')


# 응용 (사용자에게 입력받은 값을 가지고 작업해보기)
test=input('정수 입력 : ') # '20'
print(test)
print(type(test))

if int(test)<10:
    print('10보다 작은값을 입력하셨습니다')
elif int(test)<20:
    print('10이상 20미만의 값을 입력하셨습니다')
else:
    print('20이상의 값을 입력하셨습니다')





# 반복문 - for
'''
    for(int i=1; i<=10; i++) {
        System.out.println(i);
    }
'''
for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

print('---------')

sum = 0
for i in range(1, 11):
    print(i, end='\t')
    sum += i

print('\n총합계 :', sum)

for i in range(10, 0, -1):
    print(i, end=' ')

print()

# 응용
'''
num = int(input('양수 입력 : '))

if num>0:
    for i in range(num):
        print(i, end=' ')
else:
    print('잘못입력했습니다. 양수가 아닙니다.')
'''

subject = ['java', 'javascript', 'python']
'''
    for(String s : subject){
    
    }
'''
for s in subject:
    print(s)
else:
    print('재밋다ㅎㅎ')


for dan in range(2, 10):
    print('<<', dan, '단 >>')
    for su in range(1, 10):
        print(dan, 'x', su, '=', dan*su)
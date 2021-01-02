i = 1
while i<=10:
    if i>5:
        break
    print(i)
    i+=1
else:
    print('출력끝')
    # 애초에 while문에 기술한 그 조건이 false가 되기 전에 break 만나서 빠져나왔기 때문에 실행 x

# 1~9까지 홀수만을 출력
for i in range(1, 10):
    if i%2==0:
        continue
    print(i)
else:
    print('출력끝')


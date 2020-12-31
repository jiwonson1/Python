
# 산술연산
a=21
b=2
print(a + b)
print(a - b)
print(a * b)
print(a ** b) # 제곱
print(a / b) # 나눗셈결과가 실수형 => 실수형으로 나옴
print(a // b) # 몫
print(a % b)

# 비교연산
a, b = 5, 3
print(a == b)
print(a != b)
print(a is b)
print(a is not b)
print(a > b)
print(a <= b)

# 논리 연산
print(True or False)
print(False and True)

# 논리 부정 연산
print(not False)


# 10 ~ 19
list01 = list(range(10, 20))
print(list01)

# 0 ~ 99
list02 = list(range(100))
print(list02)

# 범위연산
print(list02[2])
print(list02[2:10])
print(list02[2:10:2])
# [start]
# [start:end]       -> start ~ end-1
# [stard:end:step]  -> start ~ end-1까지 step만큼씩

str = 'Hello World!'
print(str)
print(str[0])
print(str[0:5])
print(str[0:4] * 2)

# 멤버연산
list03 = [0, 1, 2, 3, 4]
print(3 in list03)
print(5 not in list03)



# set : 집합
# 자바 컬렉션의 Set과 유사 (중복x, 순서유지x)

# 생성자 사용
a = set()
print(a)

a = set([1, '1', '2', '3', '4', '4'])
print(a)

b = set('hello')
print(b)

# {} 사용
c = {'a', 'b', 'c', 'hello', 1, '1', '2', '3'}
print(c)

c.add('world')
print(c)

c.add('a')
print(c)
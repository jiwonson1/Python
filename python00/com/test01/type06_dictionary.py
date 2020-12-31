# dictionary
# 자바 컬렉션의 Map과 유사 (key-value 세트로 저장, 순서유지x, 키값이 중복x)
# 자바스크립트의 객체와 유사 {속성:속성값, 속성:속성값}

# 생성자 사용
a = dict()
print(a)

# a[키값] = 밸류값
a[1] = 1
a[2] = 2
print(a)

a['test'] = 'a'
print(a)

# {}로 생성
b = {}
b['one'] = 1
b['2'] = 'this is two'
b['one'] = 2
print(b)

print(b['one'])

print(b.values())


# list : []             List
# tuple : ()            고정값의 List
# set : {}              Set
# dict : {키:밸류, ..}   Map
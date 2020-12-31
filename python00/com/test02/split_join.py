# split
str = 'Hello, world!\nHello, python!'
print(str)

list01 = str.split(' ')
print(list01)
print(type(list01))

# join
list02 = ['1', '2', '3', '4']
print(list02)

str2 = '+'.join(list02)
print(str2) # '1+2+3+4'
print(type(str2))
print(eval(str2))


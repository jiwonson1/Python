'''
def mysum(x, y):
    return 2 * x + y

if __name__ == "__main__":
    a = mysum(2, 3)
    print(a)
'''

mysum = lambda x,y : 2*x+y
print(mysum(2, 3))


hap = lambda a,b : a+b
print(hap(10, 20))

mul = lambda a,b,c : a*b*c
print(mul(2, 3, 4))

'''
def min(x, y):
    if x<y:
        return x
    else:
        return y
'''
min = (lambda x,y: x if x<y else y)(11, 22)
print(min)

max = (lambda x,y: x if x>y else y)(11, 22)
print(max)

a = lambda x: (lambda y:x+y)
#b = a(100) # lambda y:100+y
#c = b(90)
#print(c)
print(a(100)(90))




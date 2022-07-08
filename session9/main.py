myLambda = lambda a, b , c : a+b+c

# print(myLambda(2,5,6))

def mult(n):
    return lambda a: a*n

result=mult(5)

# print(result(2))

def mult2(n,a):
    return n*a
print(mult2(5, 10))
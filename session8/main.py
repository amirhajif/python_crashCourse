#functions
# def my_func():
#     print("hello world")

# my_func()

def envCircle(r):
    print(r*2*3.14)

def areaRect(tol,arz):
    print(tol*arz)

def printName(name):
    print("hello "+ name)
# envCircle(2)
# areaRect(2, 5)
# printName("amir")

def classStudent(*names):
    print("hello "+ names[1])

# classStudent("amir","ali","reza")

def test(name1,name2,name3):
    print("hello " + name1 +"  " +name2)

# test(name1="amir",name3="reza",name2="ali")

def doubleStar(**fruit):
    print("banana count:"+fruit["banana"])

# doubleStar(apple = "6" , orange = "8",banana="9")

def defaultTest(name = "amir"):
    print("hello "+name)

#defaultTest("reza")
# defaultTest()

def listTest(names):
    for name in names:
        print(name)

# names=["amir","ali","reza"]
# listTest(names)

def returnTestCircleEnv(r):
    return 2*3.14*r

# env=returnTestCircleEnv(2)
# print(env)

def factoriel(n):
    if n==1:
        return 1
    else:
        return (n*factoriel(n-1))

# print(factoriel(4))

def test2():
    pass


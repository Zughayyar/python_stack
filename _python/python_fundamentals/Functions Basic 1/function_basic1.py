###Python Stack###
###Assignment###
###Functions Basic 1###
###Anas Zughayyar###


#1 
def a():
    return 5
print(a())

#2
def a():
    return 5
print(a() + a())

#3 
def a():
    return 5
    return 10
print (a())

#4
print("#4: ")
def a4():
    print(10)
    return 5
    print(10)
print(a4())

#5
print("#5: ")
def a5():
    print(5)
x = a5()
print(x)

#6 
print("#6: ")
def a6(b,c):
    print(b+c)
print(a6(1,2) , a6(2,3)) ## cannot add two undefined values

#7
print("#7: ")
def a7(b,c):
    return str(b) + str(c)
print(a7(2,5))

#8
print("#8: ")
def a8():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a8())

#9
print("#9: ")
def a9(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a9(2,3))
print(a9(5,3))
print(a9(2,3) + a9(5,3))

#10
print("#10: ")
def a10(b,c):
    return b+c
    return 10
print(a10(3,5))

#11
print("#11: ")
b = 500
print(b)
def a11():
    b = 300 
    print(b)
print(b)
a11()
print(b)

#12
print("#12: ")
b = 500
print(b)
def a12():
    b = 300
    print(b)
    return(b)
print(b)
a12()
print(b)

#13 (500,500,300,300)
print("#13: ")
b = 500 
print(b)
def a12():
    b = 300
    print(b)
    return b
print(b)
b = a12()
print(b)

#14
print("#14: ")
def a14():
    print(1)
    b14()
    print(2)
def b14():
    print(3)
a14()

#15 
print("#15: ")
def a15():
    print(1)
    x = b15()
    print(x)
    return 10
def b15():
    print(3)
    return 5
y = a()
print(y)

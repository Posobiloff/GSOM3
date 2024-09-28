# 1. This code inputs 3 integer variables, sorts them and them outputs the result
a = int(input("Please iput the first number"))
b = int(input("Please iput the first number"))
c = int(input("Please iput the first number"))
if a>b:
    x=a
    a=b
    b=x
if a>c:
    y=a
    a=c
    c=y
if b>c:
    z=b
    b=c
    c=z
print("the sorted order is", a, b, c)
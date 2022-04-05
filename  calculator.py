from unittest import result


def add(a,b,c):
    result=a+b+c
    print(result)

def sub(a,b,c):
    result = a-b-c
    print(result)


def div(a,b):
    result=a/b/c
    print(result)

def mul(a,b,c):
    result=a*b*c
    print(result)

a=int(input("enter the first number: "))   
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
op=input("enter the operator: ")

if op=="+":
    add(a,b,c)
elif op=="-":
    sub(a,b,c)
elif op=="/":
    div(a,b,c)
elif op=="*":
     mul(a,b,c)

else:
    print("invalid operator: ")     


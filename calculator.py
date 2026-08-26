def Addition(a,op,b):
    return a+b
def Subtraction(a,op,b):
    return a-b
def Multiplication(a,op,b):
    return a*b
def floor_division(a,op,b):
    return a//b
def division(a,op,b):
    return a/b
def Modulus(a,op,b):
    return a%b

a=float(input("Enter number 1 : "))
operator=input("Enter the operation : ")
b=float(input("Enter number 2 : "))



if operator=='+':
        print(Addition(a,operator,b))
elif operator=='-':
    print(Subtraction(a,operator,b))
elif operator=='*':
    print(Multiplication(a,operator,b))
elif operator=='//':
    print(floor_division(a,operator,b))
elif operator=='/':
    print(division(a,operator,b))
elif operator=='%':
    print(Modulus(a,operator,b))
     
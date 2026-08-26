def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def floor_division(a,b):
    if b == 0:
        print("undefined")
        return
    return a//b
def division(a,b):
    if b ==0:
        print("Undefined")
        return
    return a/b
def Modulus(a,b):
    if b==0:
        print("Undefined")
        return
    return a%b

a=float(input("Enter number 1 : "))
operator=input("Enter the operation : ")
b=float(input("Enter number 2 : "))



if operator=='+':
        print(a,'+',b," = ",end=" ")
        print(Addition(a,b))
elif operator=='-':
    print(a,'-',b," = ",end=" ")
    print(Subtraction(a,b))
elif operator=='*':
    print(a,'*',b," = ",end=" ")
    print(Multiplication(a,b))
elif operator=='//':
    print(a,'//',b," = ",end=" ")
    print(floor_division(a,b))
elif operator=='/':
    print(a,'/',b," = ",end=" ")
    print(division(a,b))
elif operator=='%':
    print(a,'%',b," = ",end=" ")
    print(Modulus(a,b))
else:
    print("Invalid operation")
    


        

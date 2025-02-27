import f2
print("Enter 1 to add numbers.\n Enter 2 to substract numbers.\n Enter 3 to multiply numbers.\n Enter 4 to divide numbers.\n Enter 5 to get the value of power of a number ")
n=int(input("Enter your choice"))
if(n==1):
    a=int(input("Enter the Value of a"))
    b=int(input("Enter the Value of b"))
    result=f2.add(a,b)
    print(f"Sum of {a} and {b} = {result}")
elif(n==2):
    a=int(input("Enter the Value of a"))
    b=int(input("Enter the Value of b"))
    result=f2.substract(a,b)
    print(f"Difference of {a} and {b} = {result}")
elif(n==3):
    a=int(input("Enter the Value of a"))
    b=int(input("Enter the Value of b"))
    result=f2.multiply(a,b)
    print(f"Product of {a} and {b} = {result}")
elif(n==4):
    a=int(input("Enter the Value of a"))
    b=int(input("Enter the Value of b"))
    result=f2.divide(a,b)
    print(f"Quotient of {a} and {b} = {result}")
elif(n==5):
    a=int(input("Enter the Value of a"))
    b=int(input("Enter the Value of b"))
    result=f2.power(a,b)
    print(f"Value of {a} power {b} = {result}")
else:
    print("Wrong Choice")
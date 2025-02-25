def add(a,b):
  return a+b
def substract(a,b):
  return a-b 
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b
print("Enter 1 to add numbers.\n Enter 2 to substract numbers. \n Enter 3 to multiply numbers.\n Enter 4 to divide numbers. ")
n=int(input("Enter your choice"))
if(n==1):
  a=int(input("Enter the Value of a"))
  b=int(input("Enter the Value of b"))
  result=add(a,b)
  print(f"Sum of {a} and {b} = {result}")
elif(n==2):
  a=int(input("Enter the Value of a"))
  b=int(input("Enter the Value of b"))
  result=substract(a,b)
  print(f"Difference of {a} and {b} = {result}")
elif(n==3):
  a=int(input("Enter the Value of a"))
  b=int(input("Enter the Value of b"))
  result=multiply(a,b)
  print(f"Product of {a} and {b} = {result}")
elif(n==4):
   a=int(input("Enter the Value of a"))
   b=int(input("Enter the Value of b"))
   result-divide(a,b)
   print(f"Quotient of {a} and {b} = {result}")
else:
   print("Wrong Choice")


try:
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    result=a/b
    print(f"Division result:{result}")
except Exception as e:
    print(e)
finally:
    print("The final result is printed")
   

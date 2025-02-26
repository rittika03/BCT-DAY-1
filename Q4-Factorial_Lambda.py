a=int(input("Enter a number"))
s=lambda n:n*s(n-1) if n>1 else 1
result=s(a)
print(f"Factorial of {a} = {result}")
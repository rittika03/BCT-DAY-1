a=(int(input("Enter number a")))
b=(int(input("Enter number b")))
s=lambda a,b:a if a>b else b
r=s(a,b)
print(f"Greater Number = {r}")

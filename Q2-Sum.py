def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
a=int(input("Enter a number"))
result=sum(a)
print(f"Sum of {a} = {result}")
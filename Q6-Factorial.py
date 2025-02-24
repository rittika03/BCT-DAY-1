n=int(input("Enter a Number"))
fact=1
for i in range(n+1):
    if(i>0 & i<=n):
        fact=fact*i
print("Factorial of ",n,"=",fact)
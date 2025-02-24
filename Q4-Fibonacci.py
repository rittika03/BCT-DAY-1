a=0
b=1
sum=0
n=int(input("Enter the number of terms"))
print(a,",",b,",")
for i in range(n+1):
    sum=a+b
    print(sum,",")
    a=b
    b=sum

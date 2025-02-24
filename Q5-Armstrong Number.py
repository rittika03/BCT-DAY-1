n=int(input("Enter a Number"))
num=n
sum=0
while n>0:
    r=(int)(n%10)
    cube=r*r*r
    sum=sum+cube
    n=n/10
if(sum==num):
    print(num," is a Armstrong Number")
else:
    print(num," is not a Armstrong Number")
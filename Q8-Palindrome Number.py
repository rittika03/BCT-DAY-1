n=int(input("Enter a Number"))
num=n
reverse=0
while n>0:
    r=n%10
    reverse=(reverse*10)+r
    n=n//10
if(reverse==num):
    print(num," is a Palindrome Number.")
else:
    print(num," is not a Palindrome Number.")
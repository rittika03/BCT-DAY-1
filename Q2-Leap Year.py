year=int(input("Enter a Year"))
if(year%4 == 0 & year%100 != 0):
    print(year," is a Leap Year.")
elif(year%100 != 0 & year%400 == 0):
    print(year," is a Leap Year.")
else:
    print(year,"is not a Leap Year.")

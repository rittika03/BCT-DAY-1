n=int(input("Enter a Number"))
k=0
for i in range(n+1):
  if(i>0):
    if(n%i==0):
      k=k+1
if(k<=2):
  print(n," is a Prime number.")
else:    
   print(n," is not a Prime number.")
print("Check Prime Number")
from math import sqrt
n = int(input("Enter a Number to check"))
if n>3 :
    for i in range(2,n):
        if n%i == 0 :
            p = 0
            break
        else :
            p = 1
elif n==1 : 
    p = 0
elif n==2 : 
    p = 1
else : 
    p = 1 

if p==1 :
   print("The ",n," is a Prime number")
else :
    print("The ",n," is Not a Prime number")

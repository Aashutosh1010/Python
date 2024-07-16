print("Check Leap Year")
n = int(input("Enter a Year to check"))
if n%4==0 or n%400==0 :
    print("The ",n," is a Leap Year")
else :
    print("The ",n," is not a leap Year")


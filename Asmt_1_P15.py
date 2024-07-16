print("Check Armstrong Number")
a = int(input("Enter a number to check"))
list1 = []
z = a
while z>=1 :
    x = int(z%10)
    list1.append(x)
    z = int(z/10)
sum = 0    
for i in range(len(list1)):
    s = list1[i]**len(list1)
    sum = sum + s
if sum == a :
    print('The ',a,' is a Armstrong Number')
else :
    print('The ',a,' is not a Armstrong Number')
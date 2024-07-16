print("Check Armstrong Number")
m = int(input("Enter the starting number of interval"))
n = int(input("Enter the starting number of interval"))
list2 = []
for i in range(m,n) :
    a = i
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
        list2.append(a)
print(list2)
print("Find Factorial")
a = int(input('Enter a number to find factorial'))
f = 1
for i in range(a,1,-1):
    f = f * i
print("Factorial = ",f)    
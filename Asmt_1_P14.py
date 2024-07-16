print('Fibbonacci Series')
n = int(input('Enter a number until you want Series'))
a = 1 
b = 2
print(a)
print(b)
print(3)
c = a + b
for i in range (3,n):
    c = b + c
    b = c - b
    print(c)
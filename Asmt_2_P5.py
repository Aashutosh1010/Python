print("Find Factorial")
a = int(input('Enter a number to find factorial'))
b = a
f = 1
def fact(a):
    if a == 0:
        f = 1
    else :
        f =a*fact(a-1)
    return f;
print(fact(b))

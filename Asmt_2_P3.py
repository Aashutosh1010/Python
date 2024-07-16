print('Simple Calculator')
a = float(input('Enter a numerical value'))
b = float(input('Enter another numerical value'))
print('Enter 1 for Addition')
print('Enter 2 for Substraction')
print('Enter 3 for Multiplication')
print('Enter 4 for Division')

def add(a,b) :
    r = a+b
    print('The Addition :- ',r)
def sub(a,b) :
    r = a-b
    print('The Substraction :- ',r)
def mul(a,b) :
    r = a*b
    print('The Multiplication :- ',r)
def div(a,b) :
    r = a/b
    print('The Division :- ',r)
    
c = int(input())   
if c==1 :
    add(a,b)
elif c==2 :
    sub(a,b)
elif c==3 :
    mul(a,b)
else :
    div(a,b)
print('Fibonacci Sequence Using Recursion')
n = int(input('Enter a number until you want fibbonaci series'))
def fib(c) :
    if c<=1 :
        return c
    else :
        return (fib(c-1) + fib(c-2))
for i in range(n):
    print(fib(i))
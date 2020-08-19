#Defining Functions
def fib(n):
    a, b = 0, 1
    while a < n:
        print (a, end= ' ')
        a, b = b, a+b
    print()

print (fib(2000))

print (fib)
f=fib
print (f(100))

print ('______________________________________')

fib
f = fib 
print (f(100))

fib(0)
print(fib(0))

print ('______________________________________')

def fib2(n):

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b 
    return result

f100 = fib2(100)
print(f100)

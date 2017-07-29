e = 2
ops = 0

def factorial(iter):
    if iter == 1:
        return 1
    else:
        return iter * factorial(iter - 1)
print factorial(e)

def fib(one):
    if one == 0 or one == 1:
        return 1
    else:
        ops += 2
        return fib(one - 1) + fib(one - 2)        

print fib(e)
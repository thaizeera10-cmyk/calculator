def power(base,expondent):
    return base ** expondent
#square root


def square_root(num):
    if num < 0:
        raise valueError("cannot compute square root for negative number")
    return num ** 0.5


#factorial

def factorial(n):
    if n < 0:
        raise ValueError(" Fatorial cannot be compute for negative number")
        
    if n == 0 or n==1:
        return 1
    
    return n * factorial(n-1)
    
print(power(2,3))
print(square_root(16))
print(factorial(5))
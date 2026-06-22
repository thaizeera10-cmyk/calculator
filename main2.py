def factorial(n):
    print(f"current n value is:{n}")
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(10))
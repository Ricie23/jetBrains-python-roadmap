def factorial(n):
    if n <= 1:
        return 1
    else:
        n *= factorial(n-1)
        # calculate n multiplied by the factorial of n - 1
        return n


print(factorial(12))

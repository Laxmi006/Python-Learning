# factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n ==1):
        return 1
    else:
        return n * fsctorial(n-1)
    print(factorial (3))
'''In a programming language of your choice, write a program that
prints all numbers from the fibonacci number series, that are in odd positions'''

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError ("N must be postive integer ")
    if n < 1:
        raise ValueError("N must be postive integer")

    # Compute Nth Fibonacci
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,15):
    if (n % 2 != 0):
        print(fibonacci(n))




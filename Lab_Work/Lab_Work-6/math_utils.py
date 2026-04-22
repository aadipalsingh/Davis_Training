# ---------------- MATH UTILITY MODULE ----------------

# ----------- PRIME CHECK FUNCTION -----------
def is_prime(n):
    # check for numbers less than 2
    if n < 2:
        return False

    # check divisibility from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# ----------- FIBONACCI GENERATOR FUNCTION -----------
def fibonacci(n):
    # generate first n Fibonacci numbers
    fib_list = []

    a, b = 0, 1   # initial values

    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b   # update values

    return fib_list


# ----------- FACTORIAL FUNCTION -----------
def factorial(n):
    # handle negative input
    if n < 0:
        return "Factorial not defined for negative numbers"

    result = 1

    # calculate factorial using loop
    for i in range(1, n + 1):
        result *= i

    return result
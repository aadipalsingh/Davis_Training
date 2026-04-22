''' Custom Module: Math Utility Package

Create a module with:

Prime check
Fibonacci generator
Factorial
Then import and use in main program'''

# ---------------- IMPORT MODULE ----------------
import math_utils as mu


# ---------------- MAIN PROGRAM ----------------

# ----------- PRIME CHECK -----------
num = int(input("Enter a number to check prime: "))

if mu.is_prime(num):
    print(f"{num} is a Prime number")
else:
    print(f"{num} is NOT a Prime number")


# ----------- FIBONACCI -----------
n = int(input("\nEnter number of Fibonacci terms: "))
print("Fibonacci Series:", mu.fibonacci(n))


# ----------- FACTORIAL -----------
fact_num = int(input("\nEnter number for factorial: "))
print(f"Factorial of {fact_num} =", mu.factorial(fact_num))

#create a numpy array from the even factors of a given numbers

# import numpy as np

# def even_factors_array(n):
#     factors = []
    
#     # Find factors
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)
    
#     # Filter even factors
#     even_factors = [x for x in factors if x % 2 == 0]
    
#     # Convert to NumPy array
#     arr = np.array(even_factors)
    
#     return arr

# # Example
# num = 12
# result = even_factors_array(num)
# print("Even factors array:", result)


# Even factors array: [ 2  4  6 12]

import numpy as np
import math

def even_factors_array(n):
    
    if n == 0:
        print("0 has infinite factors, please enter a non-zero number.")
        return np.array([])
    
    n = abs(n)
    factors = set()   # use set to avoid duplicates
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    
    # Filter even factors and sort
    even_factors = sorted([x for x in factors if x % 2 == 0])
    
    return np.array(even_factors)

# Example
print(even_factors_array(12)) #positive
print(even_factors_array(-36))  # negative
print(even_factors_array(0)) #zero


# [ 2  4  6 12]
# [ 2  4  6 12 18 36]
# 0 has infinite factors, please enter a non-zero number.
# []
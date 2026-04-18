# Function definitions

def addNumbers(m, n):
    return m + n

def difference(m, n):
    return m - n

def calculateProduct(m, n):
    return m * n

def divide(m, n):
    if n == 0:
        return "Error! Division by zero is not allowed."
    return m / n

def modulus(m, n):
    if n == 0:
        return "Error! Modulus by zero is not allowed."
    return m % n


# Main program
m=10
n=5

print("Addition:", addNumbers(m, n))
print("Difference:", difference(m, n))
print("Multiplication:", calculateProduct(m, n))
print("Division:", divide(m, n))
print("Modulus:", modulus(m, n))
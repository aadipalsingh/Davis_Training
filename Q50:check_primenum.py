#Write a function to check prime number.
def is_prime(n):
    if n<=1: #check if the number is less than or equal to 1
        return False #return False if the number is less than or equal to 1
    for i in range(2, int(n**0.5)+1): #iterate through the range of numbers from 2 to the square root of the input number
        if n%i==0: #if the input number is divisible by any number in the range then it is not a prime number
            return False 
    return True #return True if the input number is not divisible by any number in the range and is greater than 1
#take input from the user
num=int(input("Enter a number: "))
#call the function and print the result
if is_prime(num): #call the function with the input number and check if it returns True
    print("Prime") #print "Prime" if the function returns True
else:
    print("Not Prime") #print "Not Prime" if the function returns False
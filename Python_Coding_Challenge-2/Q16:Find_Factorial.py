#Write a program to compute factorial of a number.
#take input from the user
num=int(input("Enter a number: "))
#compute factorial of the number
factorial=1
for i in range(1, num+1):
    factorial*=i
print(factorial)
#Write a program to find the largest among three numbers.
#get three numbers from the user
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))
#compare the numbers and find the largest
if num1>=num2 and num1>=num3:
    print("The largest number is:", num1)
elif num2>=num1 and num2>=num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
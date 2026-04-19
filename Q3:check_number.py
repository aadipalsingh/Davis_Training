#Write a program to check if a number satisfies this condition.
#The number should be divisible by 3 and 5.
#take input from the user
num=int(input("Enter a number: "))
#check if the number is divisible by 3 and 5
if num%3==0 and num%5==0:
    print("Yes")
else:
    print("No")    
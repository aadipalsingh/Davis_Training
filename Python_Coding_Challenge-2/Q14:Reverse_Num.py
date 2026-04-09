#Write a program to reverse a number.
#take input from the user
num=int(input("Enter a number: "))
#reverse the number
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(reverse)
#Write a program to check if a number is palindrome.
#take input from the user
num=int(input("Enter a number: "))
#reverse the number
reverse=0
temp=num
while temp>0:   
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
#check if the number is palindrome
if num==reverse:
    print("Palindrome.")
else:
    print("Not a palindrome.")
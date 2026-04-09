#Write a program to check if string is palindrome.
#take input from the user
string=input("Enter a string: ")
#check if string is palindrome
if string==string[::-1]: #reverse the string and compare with original string
    print("Yes")
else:
    print("No") 
#Write a program to check if a character is a vowel.
#take input from the user
char = input("Enter a character: ")
#checking condition for vowel
if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print("vowel.")
else:
    print("Not a vowel.")
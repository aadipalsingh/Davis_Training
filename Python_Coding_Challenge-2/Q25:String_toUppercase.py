#Write a program to convert string to uppercase without built-in methods.
#take input from the user
string=input("Enter a string: ")
#convert string to uppercase without built-in methods
uppercase_string=""
for char in string: #iterate through each character in the string
    if 'a' <= char <= 'z': #if the character is a lowercase letter, convert it to uppercase
        uppercase_char=chr(ord(char)-32) #using ASCII values to convert to uppercase
        uppercase_string+=uppercase_char
    else:
        uppercase_string+=char #if the character is not a lowercase letter, keep it as it is
print(uppercase_string)
#Write a program to count occurrences of a character.
#take input from the user
string=input("Enter a string: ")
char=input("Enter a character to count: ")
#count occurrences of the character in the string
count=0
for c in string: #iterate through each character in the string
    if c==char: #if the character matches the input character, increment the count
        count+=1
print(count)
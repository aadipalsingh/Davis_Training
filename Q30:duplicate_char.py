#Write a program to find duplicate characters.
#take input from the user
string=input("Enter a string: ")
#find duplicate characters
duplicates=""
for char in string: #iterate through each character in the string
    if string.count(char) > 1 and char not in duplicates: #if the character occurs more than once and is not already in duplicates, add it to duplicates
        duplicates+=char+" " #add the duplicate character to the duplicates string with a space
print(duplicates.strip()) #remove the trailing space and print the duplicates

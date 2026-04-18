#Write a program to verify two strings are anagrams.
#take input from the user
string1=input("Enter first string: ")
string2=input("Enter second string: ")
#verify two strings are anagrams
if sorted(string1)==sorted(string2): #sort both strings and compare
    print("True")
else:
    print("False")

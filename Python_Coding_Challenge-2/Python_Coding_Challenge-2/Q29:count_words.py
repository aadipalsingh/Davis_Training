#Write a program to count words in sentence.
#take input from the user
string=input("Enter a string: ")
#count words in sentence
words=string.split()#split the string into words
count=len(words)#count the number of words in the list
print(count)
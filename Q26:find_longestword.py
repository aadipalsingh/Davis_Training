#Write a program to find longest word.
#take input from the user
string=input("Enter a string: ")
#find longest word
words=string.split()#split the string into words
longest_word=words[0]#start longest_word with the first word of the list
for i in range(1, len(words)):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]
print(longest_word)
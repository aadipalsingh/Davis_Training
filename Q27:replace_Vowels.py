#Write a program to replace vowels with *.
#take input from the user
string=input("Enter a string: ")
#replace vowels with *
vowels="aeiouAEIOU"
for i in vowels: #iterate through each vowel in the vowels string
    string=string.replace(i, "*")#using inbuilt replace method to replace vowel with *
print(string)
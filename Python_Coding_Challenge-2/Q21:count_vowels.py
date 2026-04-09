#Write a program to count vowels in a string.
#take input from the user
string=input("Enter a string: ")
#count vowels in the string
vowels="aeiouAEIOU"
count=0
for char in string: #iterate through each character in the string
    if char in vowels: 
        count+=1
print(count)
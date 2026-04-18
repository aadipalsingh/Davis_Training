#Write a program to count number of digits.
#take input from the user
num=int(input("Enter a number: "))
#count number of digits
count=0
while num>0:
    num=num//10
    count+=1
print(count)
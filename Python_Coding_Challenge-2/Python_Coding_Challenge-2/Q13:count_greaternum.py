#Write a program to count numbers greater than 50 in a list.
#take input from the user
numbers=list(map(int, input("Enter a list of numbers: ").split()))#take input list of numbers
#count numbers greater than 50
count=0
for num in numbers:
    if num>50:
        count+=1
print(count)
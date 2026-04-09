#Write a program to find max without using built-in functions.
#take input from the user
numbers=list(map(int, input("Enter a list of numbers: ").split()))#take input list of numbers
#find max without using built-in functions
max_num=numbers[0]#start max_num with the first element of the list
for i in range(1, len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
print(max_num)
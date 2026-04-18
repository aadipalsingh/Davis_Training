#Write a program to find missing number.
#take input from the user
num=list(map(int, input("Enter a list of numbers separated by space: ").split()))#take input list of numbers and convert it to a list of integers
#find missing number
missing_num=0 #start missing number to 0
for i in range(1, len(num)+1): #iterate through the range of numbers from 1 to the length of the input list
    if i not in num: #if the current number is not in the input list then it is the missing number
        missing_num=i #update the missing number to the current number
        break #break out of the loop once the missing number is found
print(missing_num) #print the missing number
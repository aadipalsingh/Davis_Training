#Write a program to find second largest element.
#take input from the user
list=input("Enter a list of numbers separated by space: ").split()#split the input string into a list of strings
#find second largest element    
largest=None
second_largest=None
for i in list: #iterate through each item in the input list
    num=int(i) #convert the string to an integer
    if largest is None or num > largest: #if largest is None or the current number is greater than largest, update largest and second_largest
        second_largest=largest
        largest=num
    elif second_largest is None or (num > second_largest and num != largest): #if second_largest is None or the current number is greater than second_largest and not equal to largest, update second_largest
        second_largest=num
print(second_largest) #print the second largest element
#Write a program to remove duplicates from list.
#take input from the user
list=input("Enter a list of numbers separated by space: ").split()#split the input string into a list of strings
#remove duplicates from list
unique_list=[]#create an empty list to store unique elements
for i in list: #iterate through each item in the input list
    if i not in unique_list: #if the item is not already in the unique list, add it
        unique_list.append(i) #add the item to the unique list
print(unique_list) #print the unique list
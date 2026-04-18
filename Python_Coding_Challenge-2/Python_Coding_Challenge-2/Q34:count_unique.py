#Write a program to count unique elements.
list=input("Enter a list of numbers separated by space: ").split()#split the input string into a list of strings
unique_elements=[]#create an empty list to store unique elements
for i in list: #iterate through each item in the input list
    if i not in unique_elements: #if the item is not already in the unique elements list add it
        unique_elements.append(i) #add the item to the unique elements list
count=len(unique_elements) #count the number of unique elements in the list
print(count) #print the count of unique elements
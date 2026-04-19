#Write a program to find common elements between lists.
#take input from the user
list1=input("Enter the first list of numbers separated by space: ").split()#split the input string into a list of strings
list2=input("Enter the second list of numbers separated by space: ").split()
#find common elements between lists
common_elements=[]#create an empty list to store common elements
for i in list1: #iterate through each item in the first list
    if i in list2 and i not in common_elements: #if the item is in the second list and is not already in common_elements, add it to common_elements
        common_elements.append(i) #add the item to common_elements
print(common_elements) #print the common elements list
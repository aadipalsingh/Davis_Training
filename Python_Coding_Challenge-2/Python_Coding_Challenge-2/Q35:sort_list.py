#Write a program to sort list without using sort().
#take input from the user
list=input("Enter a list of numbers separated by space: ").split()#split the input string into a list of strings
#sort the list without using sort()
sorted_list=[]#create an empty list to store sorted elements
while list: #while the input list is not empty
    min=list[0] #assume the first element is the minimum
    for i in list: #iterate through each item in the input list
        if i<min: #if the item is less than the current minimum then update the minimum
            min=i
    sorted_list.append(min) #add the minimum to the sorted list
    list.remove(min) #remove the minimum from the input list
print(sorted_list) #print the sorted list
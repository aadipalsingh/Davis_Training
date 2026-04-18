#Write a program to count frequency of elements using dictionary.
'''Example:
Input: [1,2,2,3]
Output: {1:1,2:2,3:1}'''
#take input from the user
list=input("Enter a list of numbers separated by space: ").split()#split the input string into a list of strings
#count frequency of elements using dictionary
frequency_dict={} #create an empty dictionary to store the frequency of each element
for i in list: #iterate through each item in the input list
    if i in frequency_dict: #if the item is already in the frequency dictionary increment its count
        frequency_dict[i]+=1 #increment the count of the item in the frequency dictionary
    else: 
        frequency_dict[i]=1 #add the item to the frequency dictionary with a count of 1
print(frequency_dict) #print the dictionary
#Write a program to merge dictionaries.

#take input from the user
dict1=input("Enter the first dictionary (key:value pairs separated by space): ").split()#take input for the second dictionary
dict2=input("Enter the second dictionary (key:value pairs separated by space): ").split()#take input for the second dictionary
#convert the input strings to dictionaries
dict1_dict={} #create an empty dictionary for the first input
for i in dict1: #split the input string by space and iterate through each item
    k, v = i.split(":")
    dict1_dict[k.strip()] = v.strip() #add the key-value pair to the first dictionary
dict2_dict={} #create an empty dictionary for the second input
for i in dict2: #split the input string by space and iterate through each item
    k, v = i.split(":")
    dict2_dict[k.strip()] = v.strip() #add the key-value pair to the second dictionary
#merge the two dictionaries
merged_dict={**dict1_dict, **dict2_dict} #merge the two dictionaries using the unpacking operator **
print(merged_dict) #print the merged dictionary
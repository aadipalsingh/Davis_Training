#Write a program to sort dictionary by keys.

#take input from the user
dict_input=input("Enter a dictionary (key:value pairs separated by comma): ")#take input
#convert the input string to a dictionary
dict={} #create an empty dictionary
for i in dict_input.split(","): #split the input string by comma and iterate through each
    k, v = i.split(":")
    dict[k.strip()] = v.strip() #add the key-value pair to the dictionary
#sort dictionary by keys
sorted_dict=dict(sorted(dict.items())) #sort the dictionary by keys using the sorted() function and
#convert the sorted items back to a dictionary
print(sorted_dict) #print the sorted dictionary
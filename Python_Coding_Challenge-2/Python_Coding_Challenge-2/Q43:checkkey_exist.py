#Write a program to check if key exists in dictionary.
#take input from the user
dictionary=input("Enter a dictionary (key:value pairs separated by comma): ") #take input
key=input("Enter a key to check: ") #take input key to check
#convert the input string to a dictionary
dict={} #create an empty dictionary
for i in dictionary.split(","): #split the input string by comma and iterate through each item
    k, v = i.split(":")
    dict[k.strip()] = v.strip() #add the key-value pair to the dictionary
#check if the key exists in the dictionary
if key in dict:
    print("Yes")
else: 
    print("No")
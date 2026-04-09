#Write a program to convert list to tuple.
#take input from the user
list=input("Enter a list of numbers separated by space: ").split()#split the input string into a list of strings
#convert list to tuple
tuple=tuple(list) #convert the list to a tuple using the tuple() function
print(tuple) #print the tuple
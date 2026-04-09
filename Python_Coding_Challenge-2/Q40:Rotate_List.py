#Write a program to rotate list by one position.

#take input from the user
list=input("Enter a list of numbers separated by space: ").split()#split the input string into a list of strings
#rotate list by one position
rotated_list=[list[-1]]+list[:-1] #create a new list with the last element of the input list followed by all elements of the input list except the last one
print(rotated_list) #print the rotated list
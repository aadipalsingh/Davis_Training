#Write a function to return all even numbers from list.

def evennum_list(lst):
    even_numbers=[] #create an empty list to store even numbers
    for i in lst: #iterate through each item in the input list
        if i%2==0: #if the item is divisible by 2 then it is an even number
            even_numbers.append(i) #add the even number to the even numbers list
    return even_numbers #return the list of even numbers
#take input from the user
list=input("Enter a list of numbers separated by space: ").split()#split the input string into a list of strings
list=[int(i) for i in list] #convert the list of strings to a list of integers
#call the function and print the result
result=evennum_list(list) #call the function with the input list and store the result
print("Even numbers in the list: ", result) #print the list of even numbers
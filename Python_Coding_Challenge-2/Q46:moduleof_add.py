#Create a module with a function to add two numbers and import it.
#Create a module with a function to add two numbers
def add_num(a, b):
    return a + b #return the sum of the two numbers
#take input from the user
num1=int(input("Enter the first number: ")) #take input for the first number 
num2=int(input("Enter the second number: ")) #take input for the second number
#call the function and print the result
result=add_num(num1, num2) #call the function with the input numbers and store the result
print("The sum of the two numbers is: ", result) #print the sum of the two numbers

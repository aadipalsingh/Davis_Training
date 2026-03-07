#write a program to find out the area and parameter of rectangle and validate the data wherever required
#Get the length and breadth from user
l=float(input("Enter the length of the rectangle: "))
#validating the length
if l <0:
    exit("Length cannot be negative.")
b = float(input("Enter the breadth of the rectangle: "))
#validating the breadth
if b < 0:
    exit("Breadth cannot be negative.")
#printing the results
print("The area of the rectangle is:", l*b)
print("The parameter of the rectangle is:", 2*(l+b))
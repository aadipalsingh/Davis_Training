#write the program to simple interest and validate it (if-else statement)
#Get the principal amount, rate of interest and time from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
#calculate the Simple Interest
simple_interest = (principal * rate * time) / 100

#validate the simple interest
if simple_interest > 0:
    print("The simple interest is: ", simple_interest)
else:
    print("Invalid input. Please enter positive values.")

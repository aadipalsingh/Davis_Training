#write the program to simple interest and validate it (if-else statement)
#Get the principal amount, rate of interest and time from user
principal = float(input("Enter the principal amount: "))
#validating the principal amount
if principal < 0:
    exit("Principal amount cannot be negative.")
rate = float(input("Enter the rate of interest: "))
#validating the rate of interest
if rate < 0:
    exit("Rate of interest cannot be negative.")
time = float(input("Enter the time in years: "))
#validating the time
if time < 0:
    exit("Time cannot be negative.")
#calculating simple interest
simple_interest = (principal * rate * time) / 100
#printing the simple interest
print("The simple interest is:", simple_interest)
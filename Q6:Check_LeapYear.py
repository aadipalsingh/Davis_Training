#Write a program to determine whether a year is a leap year.
#take input from the user
year=int(input("Enter a year: "))
#check if the year is a leap year
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year.")
else:
    print("Not a leap year.")
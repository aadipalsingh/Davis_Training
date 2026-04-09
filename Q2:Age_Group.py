#Write a program to find the age group of a person based on their age. The age groups are as follows:
#take input from the user
age = int(input("Enter the age of the person: "))  
#find the age group of a person based on their age
if age < 18:
    print("Minor.")
elif age < 60:
    print("Adult.")
else:
    print(" Senior.")
        
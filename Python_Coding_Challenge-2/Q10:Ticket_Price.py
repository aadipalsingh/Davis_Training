#Write a program to determine ticket price based on day of the week.
#take input from the user
day = input("Enter the day of the week: ")
#determine ticket price based on the day of the week
if day.lower() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    print("150.")
elif day.lower() in ['Saturday', 'Sunday']:
    print("200.")
else:
    print("Invalid day of the week.")
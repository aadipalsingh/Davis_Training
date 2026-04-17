#Check the age of the person and print if they are eligible to vote or not using exception handling
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
except ValueError:
    print("Invalid input. Please enter a valid age.")
else:
    print("----------------Thank you for checking your voting eligibility.------------------")
finally:
    print("----Program Executed Successfully----")
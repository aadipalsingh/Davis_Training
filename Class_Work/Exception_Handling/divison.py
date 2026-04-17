try:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print("--------------------------------------")
    print("On Dividing ",num1,"by",num2)
    print("Quotient: ",(num1/num2))
    print("--------------------------------------")
except ValueError:
    print("Unexpected Data Type. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("---------------------------------")
finally:
    print("----Program Excuted Successfully----")
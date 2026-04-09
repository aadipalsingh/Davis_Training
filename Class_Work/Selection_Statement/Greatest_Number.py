#write a program to findout greatest number among five numbers
#Get the five numbers from user
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))
n4 = float(input("Enter the fourth number: "))
n5 = float(input("Enter the fifth number: "))
#finding the greatest number among five numbers
if n1 == n2 == n3 == n4 == n5:
    print("All numbers are equal.")
elif n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
    print(n1, "is the greatest number.")
elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
    print(n2, "is the greatest number.")
elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
    print(n3, "is the greatest number.")
elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
    print(n4, "is the greatest number.")
else:
    print(n5, "is the greatest number.")
'''Output:
Enter the first number: 10
Enter the second number: 20
Enter the third number: 30
Enter the fourth number: 40
Enter the fifth number: 50
50.0 is the greatest number.
'''
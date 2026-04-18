#to check a number is even or odd
def oddeven(num):
    if num%2 == 0:
        print(num," is an even number")
    else:
        print(num," is odd number")
num = int(input("enter a number"))
oddeven(num)
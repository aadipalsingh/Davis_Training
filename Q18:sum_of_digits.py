#Write a program to find sum of digits.
#take input from the user
num=int(input("Enter a number: "))
#find sum of digits
sod=0#sum of digits=sod
while num>0:
    digit=num%10
    sod+=digit
    num=num//10
print(sod)
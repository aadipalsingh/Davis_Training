#Write a program to print all even numbers from 1 to N.
#take input from the user
N=int(input("Enter a number: "))
#print all even numbers from 1 to N
for i in range(1, N+1):
    if i%2==0:
        print(i, end=" ")


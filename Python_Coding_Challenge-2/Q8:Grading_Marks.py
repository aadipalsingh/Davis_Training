#Write a program to assign grade based on marks.
#take input from the user
marks=int(input("Enter the marks: "))
#assign grade based on the marks
#90 and above: A
if marks>=90:
    print("Grade: A")
#80 and above: B
elif marks>=80:
    print("Grade: B")
#70 and above: C
elif marks>=70:
    print("Grade: C")
#60 and above: D
elif marks>=60:     
    print("Grade: D")
#Below 60: F
else:
    print("Grade: F")
#Write a program to find the highest marks from a dictionary.
#take input from the user
marks_dict={} #create an empty dictionary to store the marks of students
num_stu=int(input("Enter the number of students: ")) #take input for the number of students
for i in range(num_stu): #iterate through the range of number of students
    name=input("Enter the name of student: ") #take input for the name of the student
    marks=int(input("Enter the marks of student: ")) #take input for the marks of the student
    marks_dict[name]=marks #add the name and marks of the student to the dictionary
#find the highest marks from the dictionary
highest_marks=max(marks_dict.values()) #find the maximum value of marks from the dictionary
highest_scorer=[name for name, marks in marks_dict.items() if marks == highest_marks] #create a list of names of students who scored the highest marks
print(highest_scorer[0]) #print the name of the student who scored the highest marks 
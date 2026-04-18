# Program to extract students with marks > 75
# Algorithm:--- 
# Start
# Open the file in read mode
# Read the lines of the file
# Split the lines to get name and marks
# Check if marks > 75
# If yes, write the name to a new file
#repeat for all lines
# Close both files
# Stop

# Open the file in read mode
with open("marks.txt", "r") as f:
    lines = f.readlines()
# Open a new file to write the names of students with marks > 75
with open("top_students.txt", "w") as out:
    for line in lines:
        name, marks = line.split(",")
        if int(marks) > 75:
            out.write(name + "\n")
print("Names of students with marks > 75 have been written to top_students.txt")

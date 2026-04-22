'''Marks Improvement Tracker

Compare two exam files:

Identify students who improved
Calculate improvement %'''

import csv #Importing the csv library to handle reading and processing of CSV files containing student marks data

# Function to read marks from a CSV file and return a dictionary with student ID as key and their name and marks as values
def read_marks(filename):
    data = {}
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file) #it is used to read the CSV file and convert each row into a dictionary where the keys are the column headers and the values are the corresponding data for each student
            
            for row in reader:
                data[row['id']] = {
                    "name": row['name'],
                    "marks": float(row['marks'])
                }
    except FileNotFoundError:
        print(f"{filename} not found!")
    
    return data

# Function to compare marks from two exams and print students who improved along with the improvement details
def compare_marks(file1, file2):
    exam1 = read_marks(file1)
    exam2 = read_marks(file2)

    print("\n--- Improved Students ---")
# Iterate through students in the first exam and check if they are present in the second exam to compare marks
    for student_id in exam1:
        if student_id in exam2:  #Check if the student ID from the first exam is also present in the second exam to ensure we are comparing marks for the same student      
            name = exam1[student_id]["name"]
            m1 = exam1[student_id]["marks"]
            m2 = exam2[student_id]["marks"]

            if m2 > m1:
                improvement = m2 - m1
                
                # Avoid division by zero
                if m1 == 0:
                    percent = 100
                else:
                    percent = (improvement / m1) * 100

                print(f"{name}: +{improvement} marks ({percent:.2f}%)")


# Run program
compare_marks("exam1.csv", "exam2.csv")
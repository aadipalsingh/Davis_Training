'''Student Grouping System

Given list of students:

Group by grade
Store in dictionary of lists
Example:
A: [students]
B: [students]'''

# ---------------- STUDENT GROUPING SYSTEM ----------------

# sample student data → (name, grade)
students = [
    ("Aman", "A"),
    ("Rahul", "B"),
    ("Neha", "A"),
    ("Simran", "C"),
    ("Karan", "B"),
    ("Riya", "A")
]


# ---------------- GROUPING FUNCTION ----------------
def group_by_grade(student_list):

    grade_dict = {}   # dictionary to store grouped students

    # ----------- LOOP THROUGH STUDENTS -----------
    for name, grade in student_list:

        # if grade not present → create new list
        if grade not in grade_dict:
            grade_dict[grade] = []

        # add student name to that grade list
        grade_dict[grade].append(name)

    return grade_dict


# ---------------- RUN PROGRAM ----------------
grouped_students = group_by_grade(students)


# ----------- DISPLAY RESULT -----------
print("\n--- Students Grouped by Grade ---")

for grade, names in grouped_students.items():
    print(f"{grade}: {names}")
'''Employee Attendance Tracker

File contains:

emp_id,date,status

Tasks:

Count present/absent days
Detect employees with low attendance (<75%)
'''
#import necessary libraries
import csv
#define function to track attendance
def attendance_tracker(filename):
    attendance = {} #Dictionary to store attendance data
 #Read CSV file and process attendance data 
    try:
        with open(filename, 'r') as file:  #Open the CSV file for reading
            reader = csv.DictReader(file) #Create a DictReader object to read the CSV file as dictionaries
             #Iterate through each row in the CSV file
            for row in reader:
                emp_id = row['emp_id']
                status = row['status'].strip().upper()

                if emp_id not in attendance:   #If the employee ID is not already in the attendance dictionary, initialize it with 0 present and 0 absent days
                    attendance[emp_id] = {"P": 0, "A": 0}

                if status == 'P':   #If the status is 'P' (present), increment the present count for that employee
                    attendance[emp_id]["P"] += 1
                elif status == 'A':  #If the status is 'A' (absent), increment the absent count for that employee
                    attendance[emp_id]["A"] += 1

        print("\n--- Attendance Report ---")
        low_attendance = [] #List to store employees with low attendance
         #Calculate attendance percentage and identify employees with low attendance

        for emp, data in attendance.items():
            total_days = data["P"] + data["A"]
            percentage = (data["P"] / total_days) * 100 if total_days > 0 else 0

            print(f"Emp {emp}: Present={data['P']}, Absent={data['A']}, %={percentage:.2f}")

            if percentage < 75:
                low_attendance.append(emp)

        print("\n--- Low Attendance Employees (<75%) ---")
        if low_attendance:
            for emp in low_attendance:
                print(f"Emp {emp}")
        else:
            print("None")

    except FileNotFoundError:
        print("File not found!")

# Run
attendance_tracker("attendance.csv")
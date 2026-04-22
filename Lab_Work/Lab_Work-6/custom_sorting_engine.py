'''Custom Sorting Engine

Sort list of tuples:

(name, marks, age)

Sort by:

marks desc
age asc
Without using built-in sorted() (implement logic manually)'''

students = [
    ("Aman", 85, 20),
    ("Rahul", 90, 22),
    ("Neha", 85, 19),
    ("Simran", 92, 21),
    ("Karan", 90, 20)
]

def custom_sort(data):
    n = len(data) #Get the number of students in the list to determine the number of iterations needed for sorting

    # Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):

            # Compare based on rules
            # 1. Marks descending
            if data[j][1] < data[j+1][1]:
                data[j], data[j+1] = data[j+1], data[j]

            # 2. If marks equal → age ascending
            elif data[j][1] == data[j+1][1]:
                if data[j][2] > data[j+1][2]:
                    data[j], data[j+1] = data[j+1], data[j]

    return data


# Run
sorted_students = custom_sort(students)

print("\n--- Sorted Students ---")
for s in sorted_students:
    print(s)
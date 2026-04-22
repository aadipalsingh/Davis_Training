'''Library Management System (Basic)

Features:

Issue/return books
Track availability
Store records in file'''

import json   # used to store data in file

# File name for storing library data
FILE_NAME = "library.json"

# Initial structure of library
library = {
    "books": {},      # stores available books → {"book_name": quantity}
    "issued": {}      # stores issued books → {"book_name": [user1, user2]}
}


# ---------------- LOAD DATA FROM FILE ----------------
def load_data():
    global library
    try:
        # Open file in read mode
        with open(FILE_NAME, "r") as file:
            library = json.load(file)   # load JSON data into dictionary
    except FileNotFoundError:
        # If file does not exist, start with empty data
        pass


# ---------------- SAVE DATA TO FILE ----------------
def save_data():
    # Open file in write mode
    with open(FILE_NAME, "w") as file:
        json.dump(library, file)   # save dictionary as JSON


# ---------------- ADD BOOK ----------------
def add_book():
    # Take book name and quantity from user
    name = input("Enter book name: ").strip().lower()
    qty = int(input("Enter quantity: "))

    # If book already exists → increase quantity
    if name in library["books"]:
        library["books"][name] += qty
    else:
        # Add new book
        library["books"][name] = qty
        library["issued"][name] = []   # initialize issued list

    print("Book added successfully!")
    save_data()   # save changes


# ---------------- ISSUE BOOK ----------------
def issue_book():
    name = input("Enter book name: ").strip().lower()
    user = input("Enter user name: ").strip()

    # Check if book exists
    if name not in library["books"]:
        print("Book not found!")
        return

    # Check availability
    if library["books"][name] > 0:
        library["books"][name] -= 1   # reduce available count
        library["issued"][name].append(user)   # add user to issued list
        print("Book issued successfully!")
    else:
        print("Book not available!")

    save_data()


# ---------------- RETURN BOOK ----------------
def return_book():
    name = input("Enter book name: ").strip().lower()
    user = input("Enter user name: ").strip()

    # Check if record exists
    if name in library["issued"] and user in library["issued"][name]:
        library["books"][name] += 1   # increase available count
        library["issued"][name].remove(user)   # remove user
        print("Book returned successfully!")
    else:
        print("Invalid return (record not found)")

    save_data()


# ---------------- VIEW BOOK STATUS ----------------
def view_books():
    print("\n--- Library Status ---")

    # Loop through all books
    for book, qty in library["books"].items():
        issued_users = library["issued"].get(book, [])
        
        # Display book info
        print(f"{book} → Available: {qty}, Issued: {len(issued_users)}")


# ---------------- MAIN MENU ----------------
def menu():
    load_data()   # load existing data at start

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Perform action based on user choice
        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            view_books()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


# ---------------- PROGRAM START ----------------
menu()
'''Inventory Management System

Features:

Add/update/delete items
Store in dictionary
Save/load from file'''

#import necessary libraries that will be used in the program
import json #Importing the json library to handle JSON file operations because we will be saving and loading the inventory data in JSON format

# In-memory inventory
# Structure:
# {
#   "item_name": {"price": value, "quantity": value}
# }
inventory = {}


# ---------------- ADD ITEM ----------------
def add_item():
    name = input("Enter item name: ").strip().lower() # Get item name and convert to lowercase
    price = float(input("Enter price: ")) # Get item price and convert to float
    quantity = int(input("Enter quantity: "))# Get item quantity and convert to integer

    if name in inventory:
        print("Item already exists. Use update instead.") #check if item already exists in inventory, if it does, prompt user to use update function instead of adding a duplicate item
    else:
        inventory[name] = {"price": price, "quantity": quantity}
        print("Item added successfully!")


# ---------------- UPDATE ITEM ----------------
def update_item():
    name = input("Enter item name to update: ").strip().lower()

    if name in inventory:
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))

        inventory[name]["price"] = price
        inventory[name]["quantity"] = quantity
        print("Item updated successfully!")
    else:
        print("Item not found!")


# ---------------- DELETE ITEM ----------------
def delete_item():
    name = input("Enter item name to delete: ").strip().lower()

    if name in inventory:
        del inventory[name]
        print("Item deleted successfully!")
    else:
        print("Item not found!")


# ---------------- VIEW INVENTORY ----------------
def view_inventory():
    if not inventory:
        print("Inventory is empty!")
        return

    print("\n--- Inventory ---")
    for name, details in inventory.items():
        print(f"{name} → Price: {details['price']}, Quantity: {details['quantity']}")


# ---------------- SAVE TO FILE ----------------
def save_inventory():   
    try:
        with open("inventory.json", "w") as file:    #Open a file named "inventory.json" in write mode to save the inventory data
            json.dump(inventory, file)  #Dump the inventory dictionary to a JSON file named "inventory.json" for persistent storage
        print("Inventory saved to file!")
    except Exception as e:
        print("Error saving file:", e) #If any error occurs during the file saving process, it will be caught and an error message will be printed along with the exception details


# ---------------- LOAD FROM FILE ----------------
def load_inventory():
    global inventory
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file) 
        print("Inventory loaded from file!")
    except FileNotFoundError:
        print("No saved file found!")
    except Exception as e:
        print("Error loading file:", e)


# ---------------- MENU ----------------
def menu():
    while True:
        print("\n===== INVENTORY SYSTEM =====")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            save_inventory()
        elif choice == "6":
            load_inventory()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


# Run program
menu()
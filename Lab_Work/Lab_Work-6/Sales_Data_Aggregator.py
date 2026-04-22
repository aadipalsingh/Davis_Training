'''Sales Data Aggregator

Given file:

product,category,price,quantity

Tasks:

Total sales per category
Highest selling product
Handle invalid rows'''
import csv
# Define the file path
file_path = 'path/to/sales_data.csv'
# Initialize dictionaries to store total sales and product quantities
category_sales = {}
product_sales = {}
# Open the CSV file and process it
with open(file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            # Extract data from the row
            product = row['product']
            category = row['category']
            price = float(row['price'])
            quantity = int(row['quantity'])
            # Calculate total sales for the category
            category_sales[category] = category_sales.get(category, 0) + (price * quantity)
            # Calculate total sales for the product
            product_sales[product] = product_sales.get(product, 0) + (price * quantity)
        except (ValueError, KeyError) as e:
            print(f"Invalid row skipped: {row} - Error: {e}")
# Print total sales per category
print("Total Sales per Category:")
for category, total in category_sales.items():
    print(f"{category}: ${total:.2f}")
# Find the highest selling product
highest_selling_product = max(product_sales, key=product_sales.get)
print(f"Highest Selling Product: {highest_selling_product} with sales of ${product_sales[highest_selling_product]:.2f}")

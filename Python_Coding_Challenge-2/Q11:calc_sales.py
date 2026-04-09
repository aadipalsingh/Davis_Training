#Write a program to calculate total weekly sales.
#take input from user
sales=list(map(int, input("Enter the weekly sales for each day: ").split()))#take input list of sales
#calculate total weekly sales
total_sales=sum(sales)
print("Total weekly sales: ", total_sales)
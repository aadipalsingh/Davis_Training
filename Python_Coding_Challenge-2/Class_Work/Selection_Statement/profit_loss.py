#calculate the profit or loss
#Get the cost price and selling price from user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
#calculate profit or loss
if selling_price > cost_price:
    print("Profit is:", selling_price - cost_price)
elif selling_price < cost_price:
    print("Loss is:", cost_price - selling_price)
else:
    print("No profit, no loss.")
    
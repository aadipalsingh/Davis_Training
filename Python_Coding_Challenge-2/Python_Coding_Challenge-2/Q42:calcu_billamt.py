#Write a function to calculate total bill amount.

#take input from the user
bill_amounts=list(map(int, input("Enter the bill amounts separated by space: ").split()))#take input list of bill amounts and convert it to a list of integers
#calculate total bill amount
total_bill_amount=sum(bill_amounts) #calculate the total bill amount by summing all the bill amounts in the input list
print("Total bill amount: ", total_bill_amount) #print the total bill amount

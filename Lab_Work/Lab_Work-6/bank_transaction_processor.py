'''Bank Transaction Processor

File contains:

account,type(deposit/withdraw),amount

Tasks:

Compute final balance
Prevent overdraft (raise exception)'''
import csv #to handle reading and writing of CSV files containing bank transactions data


# ----------- CUSTOM EXCEPTION FOR OVERDRAFT -----------
class OverdraftError(Exception):
    pass


# ----------- MAIN FUNCTION -----------
def process_transactions(filename):

    balances = {}   # dictionary to store account balances

    try:
        # ----------- READ FILE -----------
        with open(filename, 'r') as file:
            reader = csv.DictReader(file) #to read the keys as column headers and values as corresponding data for each transaction

            # ----------- PROCESS EACH TRANSACTION -----------
            for row in reader:
                try:
                    acc = row['account']  #to get the account number from the current row of the CSV file for processing the transaction
                    t_type = row['type'].strip().lower()
                    amount = float(row['amount']) #to convert the transaction amount from string to float for accurate calculations and to handle decimal values in transactions

                    # initialize account if not present
                    if acc not in balances:
                        balances[acc] = 0

                    # ----------- DEPOSIT -----------
                    if t_type == "deposit":
                        balances[acc] += amount

                    # ----------- WITHDRAW -----------
                    elif t_type == "withdraw":
                        if balances[acc] < amount:
                            # raise custom exception if insufficient balance
                            raise OverdraftError(f"Overdraft! Account {acc}")

                        balances[acc] -= amount

                    else:
                        print(f"Invalid transaction type: {t_type}")

                except OverdraftError as e:
                    print("Error:", e)

                except ValueError:
                    print(f"Invalid amount → Skipped: {row}")

        # ----------- DISPLAY FINAL BALANCES -----------
        print("\n--- Final Account Balances ---")
        for acc, bal in balances.items():
            print(f"Account {acc}: ₹{bal:.2f}")

    except FileNotFoundError:
        print("File not found!")


# ----------- RUN PROGRAM -----------
process_transactions("transactions.csv")
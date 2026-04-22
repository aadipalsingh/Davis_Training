'''Data Cleaning Tool

Input file contains messy data:

Remove null values
Fix formatting issues
Convert types safely using exception handling'''

import csv   # used for reading and writing CSV files


# ---------------- MAIN FUNCTION ----------------
def clean_data(input_file, output_file):

    cleaned_rows = []   # list to store cleaned data

    try:
        # ----------- OPEN INPUT FILE -----------
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)   # read CSV as dictionary

            # ----------- PROCESS EACH ROW -----------
            for row in reader:
                try:
                    # ---------- CLEAN NAME ----------
                    # remove extra spaces and capitalize properly
                    name = row['name'].strip().title()

                    # ---------- REMOVE NULL VALUES ----------
                    # skip row if important fields are missing
                    if not name or not row['age'] or not row['salary']:
                        continue

                    # ---------- SAFE TYPE CONVERSION (AGE) ----------
                    try:
                        age = int(row['age'])   # convert age to integer
                    except ValueError:
                        print(f"Invalid age → Skipped: {row}")
                        continue   # skip invalid row

                    # ---------- SAFE TYPE CONVERSION (SALARY) ----------
                    try:
                        salary = float(row['salary'])   # convert salary to float
                    except ValueError:
                        print(f"Invalid salary → Skipped: {row}")
                        continue   # skip invalid row

                    # ---------- STORE CLEANED DATA ----------
                    cleaned_rows.append({
                        "id": int(row['id']),   # convert id to integer
                        "name": name,
                        "age": age,
                        "salary": salary
                    })

                except Exception as e:
                    # catch unexpected errors for a row
                    print("Error processing row:", row)

        # ----------- WRITE CLEANED DATA TO NEW FILE -----------
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ["id", "name", "age", "salary"]

            writer = csv.DictWriter(outfile, fieldnames=fieldnames) # create a DictWriter object to write dictionaries to the CSV file with specified fieldnames

            writer.writeheader()        # write column names
            writer.writerows(cleaned_rows)   # write cleaned rows

        print("\nData cleaning completed!")
        print(f"Cleaned file saved as: {output_file}")

    except FileNotFoundError:
        # handle case when input file is missing
        print("Input file not found!")


# ---------------- PROGRAM START ----------------
clean_data("raw_data.csv", "cleaned_data.csv")
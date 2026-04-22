'''Email Extractor & Validator

From a text file:

Extract emails
Validate format
Store unique emails'''

import re #Importing the regular expression library to handle pattern matching for email extraction and validation

def extract_validate_emails(filename): 
    unique_emails = set() #to store unique valid emails extracted from the file

    # Email regex pattern
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' 
    try:
        with open(filename, 'r') as file: #Open the specified file in read mode to extract email addresses
            text = file.read() #Read the entire content of the file into a string variable named 'text' for processing

            # Extract possible emails
            emails = re.findall(pattern, text) #Use the re.findall() function to search the text for all occurrences of the email pattern defined by the regular expression and store them in a list named 'emails'

            # Validate and store unique emails
            for email in emails:
                if re.fullmatch(pattern, email):  #Use re.fullmatch() to validate that each extracted email matches the email pattern exactly, ensuring that only valid email addresses are considered
                    unique_emails.add(email)

        print("\n--- Valid Unique Emails ---")
        for email in unique_emails:
            print(email)

    except FileNotFoundError:
        print("File not found!")

# Run
extract_validate_emails("data.txt")
#write a program to extract the email
#Start
#Open file
#read content
#Use pattern to find emails
#Save emails in new file
#Stop

import re

with open("data.txt", "r") as f:
    text = f.read()
# Use regular expression to find email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)# Save emails to a new file
#
with open("emails.txt", "w") as out:
    for email in emails:
        out.write(email + "\n")
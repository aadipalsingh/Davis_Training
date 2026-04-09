#get the username and password from the user
username= input("Enter the username: ")
password= input("Enter the password: ")
#checking the credentials
if username=="admin" and password=="1234":
    print("Login successful!")
else:
    print("Login Not successful!")    
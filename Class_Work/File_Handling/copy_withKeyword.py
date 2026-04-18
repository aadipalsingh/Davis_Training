# Question: copy the content of one file to another using with statement

# opening the file in read mode
with open("Classwork/article.txt", "r") as f:
    # reading the content of file
    content = f.read()

    # creating new file and writing data into it
with open("Classwork/destination.txt", "w") as f:
    # writing the data into the file
    f.write(content)

print("File copied successfully.")
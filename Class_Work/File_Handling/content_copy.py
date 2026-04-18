
# Program to copy contents of one file to another

#algoritm:---
#Start
#take the name of source file(copied)
#take the name of destination file
#open source file in read mode
#open destination file in write mode
#read form source file
#write in destination file
#close both files 
#stop


# Open source file in read mode
source = open("source.txt", "r")

# Open destination file in write mode
destination = open("destination.txt", "w")

# Read content from source file
content = source.read()

# Write content into destination file
destination.write(content)

# Close both files
source.close()
destination.close()

print("File copied successfully!")
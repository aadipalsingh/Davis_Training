#write a program to find the keyword by search tool
#algorithm:--
#Start
#Take keyword from user
#Open file
#Check each line
#If keyword found → print line
#Stop
#takeing keyword from user
keyword = input("Enter keyword: ")

with open("file.txt", "r") as f:
    for line in f:
        if keyword.lower() in line.lower():
            print(line.strip())
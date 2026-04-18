#write a program to remove duplicate lines from a file
#algorithm:--
#Start
#Open source file in read mode
#Open new file in write mode
#Create empty set
#Read each line
#If line not in set → write & add to set
#Stop
# Open the source file in read mode and the destination file in write mode

seen = set()

with open("input.txt", "r") as source, open("output.txt", "w") as dest:
    for line in source:
        if line not in seen:
            dest.write(line)
            seen.add(line)
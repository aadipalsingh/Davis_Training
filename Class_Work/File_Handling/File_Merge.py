#Start
#Open both files
#Read line by line
#Add line numbers
#Write into new file
#Stop
with open("file1.txt") as f1, open("file2.txt") as f2, open("merged.txt", "w") as out:
    lines = f1.readlines() + f2.readlines()
    #merge  the content of file 1 to file 2
    for i, line in enumerate(lines, 1):
        out.write(f"{i}: {line}")
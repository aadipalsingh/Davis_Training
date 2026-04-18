#write a program to comapre two files
#algoritm:--
# Start
#Read both files
#Store second file lines in set
#Compare with first file
#Stop


#open both files to compare them
with open("file1.txt") as f1, open("file2.txt") as f2:
    lines1 = f1.readlines()
    lines2 = set(f2.readlines())
#read the lines of file 1 and comapre it with file 2
for line in lines1:
    if line not in lines2:
        print(line.strip())
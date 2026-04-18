#write the program to reverse the content of file
#algorithm:--
#Start
#Read all lines
#Reverse order
#Write into new file
#Stop
#open file in read mode
with open("input.txt", "r") as f:
    lines = f.readlines()
#reverse the order of lines
lines.reverse()
#open new file in write mode and write reversed lines
with open("reversed.txt", "w") as f:
    f.writelines(lines)
print("Content has been reversed and written to reversed.txt")
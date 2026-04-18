#program for tail implementation
#algorithm:--
# #Start
#Take N from user
#Open file in read mode
#Read all lines
#Get last N lines
#Display them
#Stop

#taking input from user
N = int(input("Enter number of lines to display from the end: "))
#open file in read mode
with open("file.txt", "r") as f:
    lines = f.readlines()
#get last N lines
last_n_lines = lines[-N:]
#display last N lines
print("Last {} lines of the file:".format(N))
for line in last_n_lines:
    print(line.strip()) 

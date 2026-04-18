#wirte  PROGRam to find the longest line into the file
#algorithm:--
#Start
#Read all lines
#Find line with max length
#Print length and content
#Stop
#open file in read mode
with open("file.txt", "r") as f:
    lines = f.readlines()

longest = max(lines, key=len)

print("Length:", len(longest))
print("Line:", longest)
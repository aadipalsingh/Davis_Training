#write a program to count the frequency of each word in a file
#algorithm:--
#Start
#Open article.txt in read mode
#Read content and convert to lowercase
#Remove punctuation
#split into words
#Count frequency using dictionary
#Display result
#Stop

import string
#open file in read mode
with open("article.txt", "r") as f:
    content = f.read().lower()
#remove punctuation
content = content.translate(str.maketrans("", "", string.punctuation))
#split into words
words = content.split()
#count frequency using dictionary
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
#display result
print("Word Frequency Count:")
for word, count in frequency.items():
    print(f"{word}: {count}")

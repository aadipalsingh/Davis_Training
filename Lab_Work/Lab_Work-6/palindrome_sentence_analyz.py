'''Palindrome Sentence Analyzer

Given sentences:

Detect palindrome words
Count frequency
Ignore spaces and case'''

sentence = "Madam Arora teaches malayalam and level civic stats Madam"
# ---------------- FUNCTION TO CHECK PALINDROME ----------------
# A palindrome is a word that reads the same backward as forward, ignoring case and spaces.
def is_palindrome(word):
    # convert to lowercase to ignore case
    word = word.lower()
    
    # check if word is same when reversed
    return word == word[::-1]


# ---------------- MAIN FUNCTION ----------------
def palindrome_analyzer(sentence):  #to analyze a given sentence for palindrome words and count their frequency

    # convert entire sentence to lowercase
    sentence = sentence.lower()

    # split sentence into words (removes spaces automatically)
    words = sentence.split()

    palindrome_freq = {}   # dictionary to store frequency

    # loop through each word
    for word in words:
        
        # remove punctuation (optional improvement)
        word = word.strip(".,!?")

        # check if palindrome
        if is_palindrome(word):

            # count frequency
            if word in palindrome_freq:
                palindrome_freq[word] += 1
            else:
                palindrome_freq[word] = 1

    # ---------------- OUTPUT ----------------
    print("\n--- Palindrome Words ---")
    
    if palindrome_freq:
        for word, count in palindrome_freq.items():
            print(f"{word} → {count}")
    else:
        print("No palindrome words found")


# ---------------- RUN PROGRAM ----------------
sentence = "Madam Arora teaches malayalam and level civic stats Madam"
palindrome_analyzer(sentence)
import string

# Basic stop words list
stop_words = {
    "the", "is", "in", "and", "to", "a", "of", "for", "on", "with",
    "this", "that", "it", "as", "an", "be", "are"
}

def word_frequency(filename):
    word_count = {}

    try:
        with open(filename, 'r') as file:
            text = file.read()

            # Convert to lowercase
            text = text.lower()

            # Remove punctuation
            text = text.translate(str.maketrans('', '', string.punctuation))

            # Split into words
            words = text.split()

            for word in words:
                if word not in stop_words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        # Sort words by frequency (descending)
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

        print("\n--- Top 10 Words ---")
        for word, count in sorted_words[:10]:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found!")

# Run program
word_frequency("sample.txt")
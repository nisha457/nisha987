def load_wordlist(filename):
    with open(filename, "r") as file:
        words = set(line.strip() for line in file)  # Read and normalize words
    return words

# Load the wordlist
wordlist = load_wordlist("words.txt")

# Print the wordlist
print(wordlist)

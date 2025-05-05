from collections import Counter
import string

def find_most_frequent_word(file_name):
    # Open and read the file
    with open(file_name, 'r') as file:
        content = file.read()

    # Remove punctuation and convert text to lowercase for consistent comparison
    content = content.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split the content into words
    words = content.split()

    # Use Counter to count occurrences of each word
    word_counts = Counter(words)

    # Find the word with the highest frequency
    most_common_word, most_common_count = word_counts.most_common(1)[0]

    print(f"The word with the most occurrences is '{most_common_word}' with {most_common_count} occurrences.")

# Example usage:
file_name = input("Enter the file name (e.g., 'file1.txt'): ")
find_most_frequent_word(file_name)

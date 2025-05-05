# Open the file in read mode
with open('file1.txt') as file:
    # Read the contents of the file
    contents = file.read()

# Prompt the user to input a word to search for
search_word = input("Enter a word you want to search in the file: ")

# Check if the word is present in the file contents
if search_word in contents:
    print('Word found')
else:
    print('Word not found')

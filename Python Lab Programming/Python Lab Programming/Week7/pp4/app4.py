def count_file_details(file_name):
    # Open the file in read mode
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            
        # Initialize counters
        word_count = 0
        vowel_count = 0
        space_count = 0
        lowercase_count = 0
        uppercase_count = 0

        vowels = "aeiouAEIOU"

        # Iterate through each character in the content
        for char in content:
            # Check for vowels
            if char in vowels:
                vowel_count += 1

            # Check for blank spaces
            if char == ' ':
                space_count += 1

            # Check for lowercase letters
            if char.islower():
                lowercase_count += 1

            # Check for uppercase letters
            if char.isupper():
                uppercase_count += 1

        # Split the content into words and count them
        words = content.split()
        word_count = len(words)

        # Print the results
        print(f"Number of words: {word_count}")
        print(f"Number of vowels: {vowel_count}")
        print(f"Number of blank spaces: {space_count}")
        print(f"Number of lowercase letters: {lowercase_count}")
        print(f"Number of uppercase letters: {uppercase_count}")

    except FileNotFoundError:
        print(f"The file '{file_name}' was not found. Please check the file name and try again.")

# Example usage:
file_name = input("Enter the file name (e.g., 'file1.txt'): ")
count_file_details(file_name)

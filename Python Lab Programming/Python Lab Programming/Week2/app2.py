# Take input from the user
char = input("Enter a single character: ")

# Check if the input is a single character
if len(char) != 1:
    print("Please enter only one character!")
else:
    # Check if the character is a digit
    if char.isdigit():
        print(f"'{char}' is a digit.")
    # Check if the character is a lowercase letter
    elif char.islower():
        print(f"'{char}' is a lowercase character.")
    # Check if the character is an uppercase letter
    elif char.isupper():
        print(f"'{char}' is an uppercase character.")
    # If none of the above, it is a special character
    else:
        print(f"'{char}' is a special character.")

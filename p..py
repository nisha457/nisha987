
char = input("Enter a single character: ")
if len(char) != 1:
    print("Please enter only one character!")
else:
    if char.isdigit():
        print(f"'{char}' is a digit.")
    elif char.islower():
        print(f"'{char}' is a lowercase character.")
    elif char.isupper():
        print(f"'{char}' is an uppercase character.")
    else:
        print(f"'{char}' is a special character.")

import re

# Improved regex for validating email addresses
regex = re.compile(r'^[A-Za-z0-9]+([.-_][A-Za-z0-9]+)*@[A-Za-z0-9-]+\.[A-Za-z]{2,}$')

def isValid(email):
    # Match the email with the regex
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

# Test cases
isValid("name.surname@gmail.com")
isValid("anonymous123@yahoo.co.uk")
isValid("anonymous123@...uk")  # Invalid email
isValid("...@domain.us")  # Invalid email

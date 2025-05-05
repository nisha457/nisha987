import re

# Function to validate phone numbers
def validate_phone_number(regex, phone_number):
    match = re.search(regex, phone_number)
    if match:
        return True
    return False

# Define the regex pattern for phone number validation
pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

# Test cases for phone numbers
test_phone_numbers = [
    "+1 (555) 123-4567",  # Valid
    "555-123-4567",       # Valid
    "555 123 4567",       # Valid
    "+44 (0) 20 1234 5678", # Valid
    "02012345678",        # Valid
    "25",                 # Invalid (Too short)
    "invalid phone number" # Invalid (Invalid format)
]

# Check each phone number and print whether it's valid or not
for number in test_phone_numbers:
    print(f"{number}: {validate_phone_number(pattern, number)}")

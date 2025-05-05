def palindrome(s):
    rev = ''.join(reversed(s))  # Reverse the string and join it back
    return s == rev  # Compare the original string with the reversed string

# Example usage:
print(palindrome("racecar"))  # True
print(palindrome("hello"))    # False

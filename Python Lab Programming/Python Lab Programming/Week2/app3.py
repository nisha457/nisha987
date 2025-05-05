# Function to print the Fibonacci sequence
def print_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    count = 0

    # Check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(f"Fibonacci sequence up to {n} term:")
        print(a)
    else:
        print(f"Fibonacci sequence up to {n} terms:")
        while count < n:
            print(a, end=" ")
            # Update values
            a, b = b, a + b
            count += 1

# Input: Number of terms
n = int(input("Enter the number of terms: "))

# Print the Fibonacci sequence
print_fibonacci(n)

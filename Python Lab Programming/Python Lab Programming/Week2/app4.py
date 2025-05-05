# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input: Interval from the user
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print(f"Prime numbers between {start} and {end} are:")

# Loop through the interval and print prime numbers
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")

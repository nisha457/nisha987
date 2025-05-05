# Number of rows
rows = 6

# Outer loop to handle the number of rows
for i in range(rows, 0, -1):
    # Inner loop to print the repeated number in each row
    for j in range(rows - i + 1):
        print(i, end=" ")
    # Move to the next line after each row
    print()

# Define two arrays (lists)
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

# Convert arrays to sets and find intersection
common_values = set(array1).intersection(set(array2))

# Convert the result back to a list (optional)
common_values = list(common_values)

# Print the common values
print("Common values between the two arrays:", common_values)



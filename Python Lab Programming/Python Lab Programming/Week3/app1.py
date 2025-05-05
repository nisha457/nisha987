import array

# Convert a list to an array
my_list = [1, 2, 3, 4, 5]
array_from_list = array.array('i', my_list)  # 'i' denotes integer type

# Convert a tuple to an array
my_tuple = (6, 7, 8, 9, 10)
array_from_tuple = array.array('i', my_tuple)  # 'i' denotes integer type

# Print the arrays
print("Array from list:", array_from_list)
print("Array from tuple:", array_from_tuple)

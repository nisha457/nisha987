def is_sorted(lst):
    # Check if each element is less than or equal to the next one
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Example usage:
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print(is_sorted([5, 4, 3, 2, 1]))  # False
print(is_sorted([1]))              # True (single element is considered sorted)

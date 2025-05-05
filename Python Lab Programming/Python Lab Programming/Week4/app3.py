def remove_duplicates(lst):
    # Use a set to remove duplicates while preserving order
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:  # If the item hasn't been seen before
            unique_list.append(item)  # Add it to the unique list
            seen.add(item)  # Mark it as seen
    return unique_list

# Example usage:
print(remove_duplicates([1, 2, 3, 4, 2, 3, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([1, 1, 1, 1]))           # [1]
print(remove_duplicates([]))                     # [] (empty list)

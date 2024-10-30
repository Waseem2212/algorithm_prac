def reverse_iteration(lst, rotations):
    for _ in range(rotations):
        # Remove the last element and insert it at the front
        last_element = lst.pop()  # Remove the last element
        lst.insert(0, last_element)  # Insert it at the front
        print(lst)  # Print the current state of the list

# Example usage
original_list = [1, 2, 3, 4]
num_rotations = 4

print("Original List:")
print(original_list)

print("\nRotated Lists:")
reverse_iteration(original_list, num_rotations)

def reverse_sublist(lst, m, n):
    # Adjust for 0-based index
    m -= 1
    n -= 1
    
    # Check for valid input
    if m < 0 or n >= len(lst) or m >= n:
        return lst  # Return the original list if indices are invalid

    # Reverse the sublist
    sublist = lst[m:n + 1]  # Extract the sublist
    sublist.reverse()  # Reverse the sublist
    lst[m:n + 1] = sublist  # Put the reversed sublist back into the original list

    return lst  # Return the modified list


# Example usage
original_list = [1, 2, 3, 4, 5]
m = 2
n = 4

print("Original List:")
print(original_list)

# Reverse the sublist from position m to n
modified_list = reverse_sublist(original_list, m, n)

print("Modified List:")
print(modified_list)

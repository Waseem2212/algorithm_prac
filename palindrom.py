def is_palindrome(number):
    # Convert the number to a string
    str_number = str(number)
    
    # Reverse the string and compare with the original
    if str_number == str_number[::-1]:
        return True  # It is a palindrome
    else:
        return False  # It is not a palindrome

# Example usage
input_number = 121
print(f"Input: {input_number}")

if is_palindrome(input_number):
    print(f"Output: {input_number} (Palindrome)")
else:
    print(f"Output: {input_number} (Not a palindrome)")

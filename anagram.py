def group_anagrams(words):
    anagram_dict = {}  # Dictionary to hold grouped anagrams

    # Iterate through each word in the input list
    for word in words:
        # Sort the word to generate a key
        sorted_word = ''.join(sorted(word))
        
        # Add the word to the corresponding key in the dictionary
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    # Extract the grouped anagrams as a list
    grouped_anagrams = list(anagram_dict.values())
    
    return grouped_anagrams

# Example usage
input_words = ['ese', 'tan', 'see', 'tea', 'ate', 'nat', 'eat']
output = group_anagrams(input_words)

print("Input:", input_words)
print("Output:", output)

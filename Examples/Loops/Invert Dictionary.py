# This program swaps the keys and values of a dictionary.
# That means, for each key-value pair in the original dictionary,
# the value becomes the key and the key becomes the value in the new dictionary.

# Example dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Create a new dictionary by inverting keys and values using a dictionary comprehension
inverted_dict = {value: key for key, value in original_dict.items()}

# Print the original and inverted dictionaries to see the result
print("Original dictionary:", original_dict)
print("Inverted dictionary:", inverted_dict)
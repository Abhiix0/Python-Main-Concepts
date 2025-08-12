# From a list of names, get only those starting with vowels.

# Define a list of names
names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Charlie", "Ian"]

# Define a tuple of vowels for comparison
vowels = ('A', 'E', 'I', 'O', 'U')

# Use a list comprehension to filter names starting with a vowel
# The name[0] accesses the first character of each name
# name.startswith(vowels) returns True if the name starts with any vowel
names_starting_with_vowel = [name for name in names if name.startswith(vowels)]

# Print the filtered list
print(names_starting_with_vowel)
# Output: ['Alice', 'Eve', 'Oscar', 'Uma', 'Ian']
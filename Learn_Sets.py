# Learning Python: [sets]

# Example 1: Creating a set
# A set is a collection of unique items (no duplicates allowed).
fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits)

# Example 2: Adding items to a set
# Use the add() method to insert a new item.
fruits.add("orange")
print("After adding orange:", fruits)

# Example 3: Sets automatically remove duplicates
# If you try to add a duplicate, it won't be added.
fruits.add("apple")
print("After trying to add 'apple' again:", fruits)

# Example 4: Removing items from a set
# Use remove() to delete an item. If the item doesn't exist, it raises an error.
fruits.remove("banana")
print("After removing banana:", fruits)

# Example 5: Using discard() to remove items safely
# discard() won't raise an error if the item is missing.
fruits.discard("pineapple")  # No error, even though 'pineapple' isn't in the set
print("After discarding pineapple:", fruits)

# Example 6: Checking if an item is in a set
if "cherry" in fruits:
    print("Cherry is in the set!")

# Example 7: Looping through a set
print("All fruits in the set:")
for fruit in fruits:
    print(fruit)

# Example 8: Set operations - union, intersection, difference
# Let's create two sets of numbers
evens = {2, 4, 6, 8}
odds = {1, 3, 5, 7}
primes = {2, 3, 5, 7}

# Union: all unique items from both sets
print("Evens or primes:", evens.union(primes))

# Intersection: items present in both sets
print("Evens and primes:", evens.intersection(primes))

# Difference: items in evens but not in primes
print("Evens but not primes:", evens.difference(primes))

# Example 9: Real-life use case - removing duplicates from a list
names = ["Alice", "Bob", "Alice", "Eve", "Bob"]
unique_names = set(names)
print("Unique names:", unique_names)
# Learning Python: [Dictionaries]

# Example 1: Creating a simple dictionary
# A dictionary stores data in key-value pairs.
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print("Student dictionary:", student)

# Example 2: Accessing values in a dictionary
# Use the key to get the value.
print("Student's name:", student["name"])
print("Student's age:", student["age"])

# Example 3: Adding a new key-value pair
student["grade"] = "A"
print("Updated student dictionary:", student)

# Example 4: Changing the value of an existing key
student["age"] = 21
print("Student's new age:", student["age"])

# Example 5: Removing a key-value pair
del student["major"]
print("After removing major:", student)

# Example 6: Looping through a dictionary
# Print all keys and values
for key, value in student.items():
    print(key, ":", value)

# Example 7: Using a dictionary for a simple project
# Counting the number of times each fruit appears in a list
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_count = {}
for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1
print("Fruit count:", fruit_count)
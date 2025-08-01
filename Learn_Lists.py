# Learning Python: [lists]

# Example 1: Creating a simple list of fruits
fruits = ["apple", "banana", "orange"]
print("My fruit list:", fruits)  # Output: ['apple', 'banana', 'orange']

# Example 2: Accessing items in a list using their index
print("First fruit:", fruits[0])  # Output: apple
print("Second fruit:", fruits[1])  # Output: banana

# Example 3: Changing an item in a list
fruits[2] = "grape"
print("Updated fruit list:", fruits)  # Output: ['apple', 'banana', 'grape']

# Example 4: Adding a new item to the end of the list
fruits.append("mango")
print("After adding mango:", fruits)  # Output: ['apple', 'banana', 'grape', 'mango']

# Example 5: Removing an item from the list
fruits.remove("banana")
print("After removing banana:", fruits)  # Output: ['apple', 'grape', 'mango']

# Example 6: Looping through a list
print("All fruits in the list:")
for fruit in fruits:
    print(fruit)

# Example 7: Checking if an item is in the list
if "apple" in fruits:
    print("Apple is in the list!")

# Example 8: Finding the length of a list
print("Number of fruits:", len(fruits))  # Output: 3

# Example 9: Creating a list of numbers and calculating the sum
numbers = [10, 20, 30, 40]
total = sum(numbers)
print("Sum of numbers:", total)  # Output: 100

# Example 10: Using lists to store user input (simple project)
user_names = []
for i in range(3):
    name = input("Enter a name: ")
    user_names.append(name)
print("Names entered:", user_names)
# Learning Python: [Tuples]

# Example 1: Creating a simple tuple
fruits = ("apple", "banana", "cherry")
print("Fruits tuple:", fruits)

# Example 2: Accessing elements in a tuple
first_fruit = fruits[0]
print("The first fruit is:", first_fruit)

# Example 3: Tuples can store different data types
person = ("Alice", 25, True)
print("Person tuple:", person)

# Example 4: Tuples are immutable (cannot be changed)
# The following line would cause an error if uncommented:
# fruits[1] = "orange"

# Example 5: Looping through a tuple
print("All fruits in the tuple:")
for fruit in fruits:
    print(fruit)

# Example 6: Tuple unpacking
name, age, is_student = person
print("Name:", name)
print("Age:", age)
print("Is student:", is_student)

# Example 7: Using tuples to return multiple values from a function
def min_and_max(numbers):
    return (min(numbers), max(numbers))

scores = [88, 92, 79, 93]
minimum, maximum = min_and_max(scores)
print("Minimum score:", minimum)
print("Maximum score:", maximum)

# Example 8: Tuples with one item need a comma
single_item_tuple = ("hello",)
print("Single item tuple:", single_item_tuple)
print("Type of single_item_tuple:", type(single_item_tuple))
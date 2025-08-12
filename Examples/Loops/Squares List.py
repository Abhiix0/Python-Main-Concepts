#Given a list of numbers, return a new list containing only the squares of even numbers using list comprehension.

# Original list
numbers = [1, 2, 3, 4, 5, 6]

# List comprehension: square only the even numbers
squares_of_even = [n**2 for n in numbers if n % 2 == 0]

print("Original List:", numbers)
print("Squares of Even Numbers:", squares_of_even)
# Output:
# Original List: [1, 2, 3, 4, 5, 6]
# Squares of Even Numbers: [4, 16, 36]
# Learning Python: [ifElse]

# Example 1: Simple if statement
age = 18
if age >= 18:
    print("You are an adult.")  # This will print because age is 18

# Example 2: if-else statement
temperature = 15
if temperature > 20:
    print("It's warm outside.")
else:
    print("It's cold outside.")  # This will print because temperature is 15

# Example 3: if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This will print because score is 85
else:
    print("Grade: C")

# Example 4: Checking if a number is even or odd
number = 7
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")  # This will print because 7 is odd

# Example 5: Nested if statements
has_ticket = True
age = 16
if has_ticket:
    if age >= 18:
        print("You can watch the movie.")
    else:
        print("You need to be 18 or older to watch this movie.")  # This will print
else:
    print("You need a ticket to watch the movie.")

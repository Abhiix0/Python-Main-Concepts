# Learning Python: [Turtle]
import turtle

# Example 1: Drawing a Square with Turtle

# Create a turtle object named "pen"
pen = turtle.Turtle()

# Set the color and speed of the turtle
pen.color("blue")
pen.speed(2)

# Draw a square using a loop
for _ in range(4):
    pen.forward(100)  # Move forward by 100 units
    pen.left(90)      # Turn left by 90 degrees

# Hide the turtle after drawing
pen.hideturtle()

# Keep the window open until clicked
turtle.done()

# ------------------------------------------------------------

# Example 2: Drawing a Triangle with Turtle

# Create a new turtle object named "artist"
artist = turtle.Turtle()
artist.color("green")
artist.speed(3)

# Draw a triangle
for _ in range(3):
    artist.forward(120)
    artist.left(120)

artist.hideturtle()
turtle.done()

# ------------------------------------------------------------

# Example 3: Drawing a Simple House Shape

# Create a turtle object named "builder"
builder = turtle.Turtle()
builder.color("brown")
builder.speed(2)

# Draw the square base of the house
for _ in range(4):
    builder.forward(100)
    builder.left(90)

# Draw the roof (a triangle)
builder.left(45)
builder.forward(70)
builder.left(90)
builder.forward(70)
builder.left(135)

builder.hideturtle()
turtle.done()
# Create a grade report system using functions to calculate average, extremes, and grade classification from student marks.
# Demonstrates: Function definition, return values, and modular code

# Function to calculate average marks from a list
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to find highest and lowest marks in a list
def find_extremes(marks):
    return max(marks), min(marks)

# Function to classify grade based on average marks
def classify_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

# Master function to print a student's report using the above helper functions
def student_report(name, marks):
    avg = calculate_average(marks)
    high, low = find_extremes(marks)
    grade = classify_grade(avg)

    print(f"\nReport for {name}:")
    print(f"Average Marks: {avg:.2f}")
    print(f"Highest: {high}, Lowest: {low}")
    print(f"Grade: {grade}")

# ------------------------------
# Example run: Collect user input and generate report
student_name = input("Enter student name: ")
marks = []

# Input marks for 5 subjects using a loop
for i in range(1, 6):
    mark = float(input(f"Enter mark {i}: "))
    marks.append(mark)

# Generate and display the report
student_report(student_name, marks)

# Student Report System using File I/O and Exception Handling
# Demonstrates: File writing/reading, exception handling, CLI logic, and basic grade calculation

import datetime

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

# Function to save a student's report to a file
def save_report(name, marks):
    avg = sum(marks) / len(marks)
    grade = classify_grade(avg)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"{name}.txt"
    try:
        # Writing report to a text file
        with open(filename, "w") as file:
            file.write(f"Report for {name}\n")
            file.write(f"Date: {timestamp}\n")
            file.write(f"Marks: {marks}\n")
            file.write(f"Average: {avg:.2f}\n")
            file.write(f"Grade: {grade}\n")
        print(f"Report saved as {filename}")
    except Exception as e:
        print("Error saving report:", e)

# Function to read and display a student's report from a file
def read_report(name):
    filename = f"{name}.txt"
    try:
        # Reading report from a text file
        with open(filename, "r") as file:
            content = file.read()
            print("\n" + content)
    except FileNotFoundError:
        print("No report found for this student!")
    except Exception as e:
        print("Error reading report:", e)

# ------------------------
# Command Line Interface (CLI) Logic
print("Student Report System")
print("1. Save Report")
print("2. View Report")

choice = input("Choose an option: ")

if choice == '1':
    # Collect student name and marks, then save report
    name = input("Enter student name: ")
    marks = []
    for i in range(5):
        m = float(input(f"Enter mark {i+1}: "))
        marks.append(m)
    save_report(name, marks)

elif choice == '2':
    # Read and display report for a given student
    name = input("Enter student name to view report: ")
    read_report(name)

else:
    print("Invalid choice!")

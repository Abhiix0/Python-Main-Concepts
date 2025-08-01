# 👨‍💻 Learning Python: [Tkinter GUI]
import tkinter as tk  # Import the Tkinter library

# Function to handle button click event
def on_button_click():
    # Change the label text when the button is clicked
    message_label.config(text="Button was clicked!")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example")      # Set the window title
root.geometry("300x150")           # Set the window size (width x height)

# Create a label widget and add it to the window
message_label = tk.Label(root, text="Click the button below:")
message_label.pack(pady=10)        # Add some vertical padding

# Create a button widget and add it to the window
# When clicked, it calls the on_button_click function
click_button = tk.Button(root, text="Click Me", command=on_button_click)
click_button.pack()

# Start the Tkinter event loop (keeps the window open)
root.mainloop()
# Simulate an ATM system using loops that allows balance check, deposit, withdrawal, and exit.
# Demonstrates: Infinite loops, conditional logic, and user input handling  

# Initial balance for the ATM user
balance = 1000  

# Infinite loop to simulate ATM menu until user chooses to exit
while True:
    print("\n====== ATM Menu ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Option 1: Show current balance
        print(f"Your current balance is ₹{balance}")

    elif choice == '2':
        # Option 2: Deposit money
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount! Please enter a positive value.")

    elif choice == '3':
        # Option 3: Withdraw money
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        elif amount <= 0:
            print("Invalid amount! Please enter a positive value.")
        else:
            print("Insufficient balance!")

    elif choice == '4':
        # Option 4: Exit the loop and end the program
        print("Exiting... Thank you for using the ATM!")
        break  # End the while loop

    else:
        # Invalid input case
        print("Invalid choice. Please select from 1 to 4.")
        continue  # Skip rest and show menu again

def check_balance(balance):
    # Show the current balance.
    print("Your balance is:", balance)


def deposit(balance):
    # Add the deposit and return the new balance.
    amount = float(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Deposit complete.")
    return balance


def withdraw(balance):
    # Subtract the withdrawal if there is enough money.
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal complete.")
    else:
        print("Not enough money in your account.")
    return balance


def main():
    # Step 1: Ask the user to log in with the PIN.
    pin = input("Enter PIN (1234): ")
    if pin != "1234":
        print("Wrong PIN.")
        return

    balance = 1000

    # Step 2: Repeat the menu until the user chooses Exit.
    while True:
        print("\n1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")

        # Step 3: Call the function for the selected operation.
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


main()

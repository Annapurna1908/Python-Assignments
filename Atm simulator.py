correct_pin = "1234"
balance = 5000


def login():
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        return True
    else:
        return False


def check_balance():
    print("Your balance is ₹", balance)


def deposit():
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully")
        print("New balance: ₹", balance)
    else:
        print("Invalid amount")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif amount > balance:
        print("Insufficient balance")

    else:
        balance = balance - amount
        print("Please collect your cash")
        print("Remaining balance: ₹", balance)


# ATM Program

print("================================")
print("       WELCOME TO ATM")
print("================================")

if login():

    print("\nLogin Successful!")

    while True:

        print("\n------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Incorrect PIN")
    print("Access Denied")
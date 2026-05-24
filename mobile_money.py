

users = {}  

def register():
    print("\n--- REGISTER ---")
    phone = input("Enter phone number: ")

    if phone in users:
        print("User already exists!")
        return

    name = input("Enter your name: ")
    pin = input("Set your PIN: ")

    users[phone] = {
        "name": name,
        "pin": pin,
        "balance": 0
    }

    print("Registration successful!")

# ---------------- LOGIN ----------------
def login():
    print("\n--- LOGIN ---")
    phone = input("Enter phone number: ")
    pin = input("Enter PIN: ")

    if phone in users and users[phone]["pin"] == pin:
        print(f"Welcome {users[phone]['name']}!")
        dashboard(phone)
    else:
        print("Invalid phone or PIN!")

# ---------------- DASHBOARD ----------------
def dashboard(phone):
    while True:
        print("\n--- DASHBOARD ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Send Money")
        print("4. Withdraw")
        print("5. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            print(f"Balance: {users[phone]['balance']}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            users[phone]["balance"] += amount
            print("Deposit successful!")

        elif choice == "3":
            receiver = input("Enter receiver phone: ")
            amount = float(input("Enter amount: "))

            if receiver not in users:
                print("Receiver not found!")
            elif users[phone]["balance"] < amount:
                print("Insufficient balance!")
            else:
                users[phone]["balance"] -= amount
                users[receiver]["balance"] += amount
                print("Transfer successful!")

        elif choice == "4":
            amount = float(input("Enter amount to withdraw: "))

            if users[phone]["balance"] < amount:
                print("Insufficient balance!")
            else:
                users[phone]["balance"] -= amount
                print("Withdraw successful!")

        elif choice == "5":
            print("Logged out.")
            break

        else:
            print("Invalid choice!")

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n=== MOBILE MONEY SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Select option: ")

        if option == "1":
            register()
        elif option == "2":
            login()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

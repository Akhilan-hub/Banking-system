# Simple Banking System

accounts = {}  # Stores account info: {account_number: {"name": name, "balance": amount}}

def create_account():
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Account already exists!")
        return
    name = input("Enter your name: ")
    balance = float(input("Enter initial deposit: "))
    accounts[account_number] = {"name": name, "balance": balance}
    print("Account created successfully!")

def deposit():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter deposit amount: "))
    accounts[account_number]["balance"] += amount
    print("Deposit successful!")

def withdraw():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter withdraw amount: "))
    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance!")
        return
    accounts[account_number]["balance"] -= amount
    print("Withdrawal successful!")

def check_balance():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found!")
        return
    print(f"Account Holder: {accounts[account_number]['name']}")
    print(f"Balance: {accounts[account_number]['balance']}")

def main():
    while True:
        print("\nWelcome to Simple Bank")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

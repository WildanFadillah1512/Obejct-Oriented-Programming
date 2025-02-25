class BankDatabase:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1

    def create_account(self, owner, initial_deposit=0):
        account_number = self.next_account_number
        self.accounts[account_number] = {"owner": owner, "balance": initial_deposit}
        self.next_account_number += 1
        print(f"Account created successfully! Account Number: {account_number}")

    def list_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        else:
            print("\nList of Accounts:")
            for acc_no, details in self.accounts.items():
                print(f"Account No: {acc_no} | Owner: {details['owner']} | Balance: ${details['balance']}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print(f"Deposit successful! Added ${amount}.")
        else:
            print("Account not found!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f"Withdrawal successful! Withdrawn ${amount}.")
            else:
                print("Insufficient funds!")
        else:
            print("Account not found!")

# Main Program with Menu
def main():
    bank = BankDatabase()

    while True:
        print("\n===== BANK MENU =====")
        print("1. List Accounts")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            bank.list_accounts()

        elif choice == "2":
            name = input("Enter account owner's name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, initial_deposit)

        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == "4":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == "5":
            print("Thank you for using our bank system!")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()

class BankAccount:
    accounts = [] 
    logged_in_account = None  

    def __init__(self, account_holder, balance=0.0, pin="1234"):
        self.account_holder = account_holder  
        self._balance = balance  
        self.__pin = pin 
        BankAccount.accounts.append(self) 
    

    def get_balance(self, pin):
        if self.verify_pin(pin):
            return self._balance
        else:
            print("Incorrect PIN!")
            return None

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount, pin):
        if self.verify_pin(pin):
            if amount > 0:
                self._balance += amount
                print(f"Deposit successful! New balance: ${self._balance}")
            else:
                print("Deposit amount must be positive!")
        else:
            print("Incorrect PIN!")


    def withdraw(self, amount, pin):
        if self.verify_pin(pin):
            if 0 < amount <= self._balance:
                self._balance -= amount
                print(f"Withdrawal successful! New balance: ${self._balance}")
            else:
                print("Insufficient funds or invalid amount!")
        else:
            print("Incorrect PIN!")

    @staticmethod
    def list_accounts():
        if not BankAccount.accounts:
            print("No accounts available.")
        else:
            print("\nList of Accounts:")
            for acc in BankAccount.accounts:
                print(f"Account Holder: {acc.account_holder} | Balance: ${acc._balance}")


    @staticmethod
    def login():
        name = input("Enter account holder's name: ")
        pin = input("Enter PIN: ")
        for acc in BankAccount.accounts:
            if acc.account_holder == name and acc.verify_pin(pin):
                BankAccount.logged_in_account = acc
                print("Login successful!")
                return
        print("Invalid credentials!")

    @staticmethod
    def logout():
        BankAccount.logged_in_account = None
        print("Logged out successfully!")

def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative. Please enter a valid number.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


while True:
    print("\n===== BANK SYSTEM MENU =====")
    print("1. Login")
    print("2. Create Account")
    print("3. List Accounts")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        BankAccount.login()
        if BankAccount.logged_in_account:
            while True:
                print("\n===== TRANSACTION MENU =====")
                print("1. View Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")
                
                transaction_choice = input("Choose an option: ")
                
                if transaction_choice == "1":
                    pin = input("Enter PIN: ")
                    balance = BankAccount.logged_in_account.get_balance(pin)
                    if balance is not None:
                        print(f"Current Balance: ${balance}")
                elif transaction_choice == "2":
                    amount = get_valid_number("Enter deposit amount: ")
                    pin = input("Enter PIN: ")
                    BankAccount.logged_in_account.deposit(amount, pin)
                elif transaction_choice == "3":
                    amount = get_valid_number("Enter withdrawal amount: ")
                    pin = input("Enter PIN: ")
                    BankAccount.logged_in_account.withdraw(amount, pin)
                elif transaction_choice == "4":
                    BankAccount.logout()
                    break
                else:
                    print("Invalid option! Please try again.")
    elif choice == "2":
        name = input("Enter account holder's name: ")
        initial_balance = get_valid_number("Enter initial deposit amount: ")
        pin = input("Set a PIN for the account: ")
        BankAccount(name, initial_balance, pin)
        print("Account created successfully!")
    elif choice == "3":
        BankAccount.list_accounts()
    elif choice == "4":
        print("Thank you for using our bank system!")
        break
    else:
        print("Invalid option! Please try again.")

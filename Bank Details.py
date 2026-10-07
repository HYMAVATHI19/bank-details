class BankAccount:

    def __init__(self, account_number, name, password, balance=0):
        self.account_number = account_number
        self.name = name
        self.__password = password
        self.balance = balance

    
    def check_password(self, password):
        return self.__password == password

  
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Current balance: ₹{self.balance}")
        else:
            print("Invalid amount.")

    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} debited successfully.")
            print(f"Current balance: ₹{self.balance}")

    
    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")


    def display_details(self):
        print("\n----- Account Details -----")
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        



account = BankAccount(
    account_number="1234567890",
    name="hyma",
    password="1234",
    balance=10000
)


password = input("Enter your password: ")

if account.check_password(password):

    print("\nLogin successful!")

    while True:
        print("\n===== BANK MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw / Debit")
        print("4. Account Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account.check_balance()

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)

        elif choice == "4":
            account.display_details()

        elif choice == "5":
            print("Thank you for using the bank.")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect password!")
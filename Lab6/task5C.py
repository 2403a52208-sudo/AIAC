class BankAccount:
    def __init__(self, name, balance=0):   #  fixed __init__
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")


# Example usage
name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Thank you for using the Bank Account!")
        break
    else:
        print("Invalid choice. Please try again.")

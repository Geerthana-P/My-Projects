class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ₹{amount}")
        else:
            print("Insufficient funds! Withdrawal denied.")

    def get_balance(self):
        return self.balance

my_account = BankAccount(100)


my_account.deposit(50)


my_account.withdraw(100)


print("Current Balance:", my_account.get_balance())

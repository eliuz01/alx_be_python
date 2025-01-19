class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    
    def deposit(self, amount):
        if amount> 0:
            self.account_balance = self.account_balance + amount
        else:
            print("You cannot deposit zero amount")
    def withdraw(self, amount):
        """Withdraw a certain amount from the account, if sufficient funds are available."""
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")



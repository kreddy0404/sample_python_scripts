class BankAccount:

    def __init__(self, initial_balance):
        self._balance = initial_balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

class SavingsAccount(BankAccount): # Child claas from BankAccount

    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)

def main():

    # Create saving account object.
    savings_account = SavingsAccount(400)

    # Current saving balance.
    print 'Savings account balance: $', savings_account.get_balance()
    savings_account.deposit(200)
    print 'Savings account new balance: $', savings_account.get_balance()
    savings_account.withdraw(100)
    print 'Savings account current balance: $', savings_account.get_balance()

main()

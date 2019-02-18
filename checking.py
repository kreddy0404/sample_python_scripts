class BankAccount:

    def __init__(self, initial_balance):
        self._balance = initial_balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print 'You do not have enough funds.'
        else:
            self._balance -= amount

class CheckingAccount(BankAccount):

    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)

def main():

    checking_account = CheckingAccount(200)

    print 'Initial balance: $', checking_account.get_balance()

    checking_account.deposit(300)

    print 'New balance: $', checking_account.get_balance()

    checking_account.withdraw(501)

    print 'New balance after withdraw: $', checking_account.get_balance()

main()

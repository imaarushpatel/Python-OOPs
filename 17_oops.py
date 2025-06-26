# ATM System

# Create a BankAccount class with encapsulated attributes for balance.
# Add subclasses SavingsAccount and CurrentAccount that have different rules for withdrawing money.


class BankAccount:
    def __init__(self, balance):
        self._balance=balance


    def withdraw (self,amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print(f"withdraw: {amount}")

    def get_balance(self):
        print(f"Available balance :{self._balance}")
    


class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self._balance - 1000:
            print("Insuficint funds! Maintain minimum balance of 1000.")

        else:
            super().withdraw(amount)
        

class CurrentAccount(BankAccount):
    pass


savings = SavingAccount(5000)
savings.withdraw(10000)


savings.get_balance()


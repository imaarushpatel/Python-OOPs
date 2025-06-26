# Encapsulation

# Private Attributes and Getters/Setters

# Create a class BankAccount with private attributes _balance.
# Add methods deposit(amount) and withdraw(amount) to update _balance.
# Create a method to view the current balance.


class BankAccount:
    def __init__(self, balance):
        self.__balance=balance  #private attributes

    def deposit(self,amount):
        self.__balance += amount


    def withdraw(self,amount):
        if amount <= self.__balance:
          self.__balance -= amount

        else:
            print("Paisa nhi Hai Bhai")



    def get_balance(self):
       return self.__balance
    


account= BankAccount(5000)
account.deposit(1000)
account.withdraw(66500)

print(account.get_balance())


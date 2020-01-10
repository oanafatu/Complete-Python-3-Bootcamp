class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print('Deposit accepted')

    def withdraw(self, amount):
        if amount >= self.balance:
            print("You don't have enough money to do the withdraw!")
        else:
            self.balance -= amount
            print('Withdraw accepted')

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'


oana = Account('Oana', 100)
print(oana)
oana.deposit(100)
print(oana)
oana.withdraw(50)
print(oana)
oana.withdraw(200)
print(oana)



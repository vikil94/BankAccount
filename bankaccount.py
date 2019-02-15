class Bankaccount:
    """ A class representing a bankaccount """
    def __init__(self, balance=0, interest_rate=0):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return "This is your account, this is your balance is: {:.2f}, and the interest rate is: {:.2f}".format(self.balance, self.interest_rate)
        
# adds money to your account
    def deposit(self, amount):
        self.balance += amount

# takes money out of your account
    def withdraw(self, amount):
        self.balance -= amount

# Increases your interest rate
    def gain_interest(self, interst):
        self.interest_rate += interst




my_account = Bankaccount(50, 3)
print(my_account)
my_account.deposit(300)
print(my_account)
my_account.withdraw(50)
print(my_account)
my_account.gain_interest(5)
print(my_account)

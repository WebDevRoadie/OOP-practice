class BankAccount:
    def __init__(self, rate, balance=0):
        self.int_rate = (2 * .01)
        self.balance = balance

    def deposit(self,amount):       
        self.balance += amount

    def withdraw(self, amount):
        amount_after_withdraw = self.balance - amount
        if amount_after_withdraw < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        print(f"Rate: %{self.int_rate}")
        if self.balance > 0:
            interest_yielded = self.balance * self.int_rate
            self.balance += interest_yielded

jane = BankAccount ("2", "0")
joe = BankAccount ("2", "0")

jane.deposit(200).deposit(300).deposit(400).withdraw(300).yield_interest().display_account_info()
joe.deposit(200).deposit(300).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
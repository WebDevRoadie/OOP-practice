class BankAccount:		
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):	
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

class User:		
    def __init__(self, name, email,int_rate=0, balance=0):
        self.name = name
        self.email = email
        self.account=BankAccount(int_rate, balance)

    def deposit(self, amount):	
        self.account.deposit(amount)
        return self
    
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Email:{self.email}")
        self.account.display_account_info()
        return self

user1=User('Drew','Drew@gmail.com')

user1.deposit(100).deposit(300).withdraw(350).display_user_balance()

user2=User('Bob', 'Bob@gmail.com',.2,1000)

user2.withdraw(100).withdraw(200)

user2.display_user_balance()
user2.account.yield_interest()
user2.display_user_balance()

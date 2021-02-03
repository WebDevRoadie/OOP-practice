class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount	
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
        
    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount 
        return self

todd = User("Todd", "todd@todd.com")
jane = User("Jane", "jane@jane.com")
john = User("John", "john@john.com")

todd.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(50).display_user_balance()

jane.make_deposit(50).make_deposit(1000).make_withdrawl(500).make_withdrawl(100).display_user_balance()

john.make_deposit(100).make_withdrawl(25).make_withdrawl(25).make_withdrawl(25).display_user_balance()

todd.transfer_money(jane,250).display_user_balance()

jane.display_user_balance()
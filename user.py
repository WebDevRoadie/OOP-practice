class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount	
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    
    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount 


todd = User("Todd", "todd@todd.com")
jane = User("Jane", "jane@jane.com")
john = User("John", "john@john.com")

todd.make_deposit(100)
todd.make_deposit(100)
todd.make_deposit(100)
todd.make_withdrawal(50)
todd.display_user_balance()

jane.make_deposit(50)
jane.make_deposit(1000)
jane.make_withdrawal(500)
jane.make_withdrawal(100)
jane.display_user_balance()

john.make_deposit(100)
john.make_withdrawal(25)
john.make_withdrawal(25)
john.make_withdrawal(25)
john.display_user_balance()

todd.transfer_money(jane,250)
todd.display_user_balance()
jane.display_user_balance()
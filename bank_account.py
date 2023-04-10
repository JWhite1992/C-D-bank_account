class BankAccount:

    all_instances = []

    def __init__(self, int_rate= 0.01, balance=0):
        self.int_rate= int_rate
        self.balance = balance
        BankAccount.all_instances.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print(f"Insufficient funds")
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
            
    def yield_interest(self, amount):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print(f"Error")
        return self

            
account_one = BankAccount()
account_two = BankAccount()

account_one.display_account_info().deposit(80).deposit(50).deposit(100).withdraw(93).yield_interest(0.01).display_account_info()
account_two.display_account_info().deposit(200).deposit(300).withdraw(50).withdraw(90).yield_interest(0.02).display_account_info()
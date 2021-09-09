class BankAccount:
        def __init__(self, int_rate, balance): 
                self.int_rate = int_rate
                self.balance = balance

        def deposit(self,amount):
                self.balance += amount
                return self

        def withdraw(self, amount):
                self.balance -= amount 
                return self	

        def display_account_info(self):
                print(self.balance)

        def yield_interest(self):
                self.balance = self.balance + self.balance * self.int_rate
                self.display_account_info()

              

account1= BankAccount(0.01,200)
account2= BankAccount(0.04,400)

account1.deposit(20).deposit(40).deposit(20).withdraw(30).yield_interest()
account2.deposit(30).deposit(40).withdraw(10).withdraw(10).withdraw(10).withdraw(20).yield_interest()


class User:
        def __init__(self,name):
                self.name = name
                self.account=BankAccount(int_rate= 0.04, balance= 0)
                
        def display_user_balance(self):
                print(self.account.balance)
                return self
        
        def tranfer_money(self,amount,other):
                self.account.balance = self.account.balance - amount
                other.account.balance = other.account.balance + amount
                print(f'{self.name} transferred {amount} to {other.name}')
                return self

Guido = User("Guido Rossi")
Monty = User("Monty Python")

Guido.account.deposit(100)
Monty.account.deposit(100)
Guido.display_user_balance()
Monty.display_user_balance()
Guido.tranfer_money(20,Monty)
Monty.display_user_balance()
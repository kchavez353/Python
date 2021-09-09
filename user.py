class User:
    def __init__(self,name,balance):
        self.name = name
        self.account_balance = balance

    def make_withdrawal(self,amount):
        self.account_balance -= amount 
        return self	
        
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
   



Guido = User("Guido Rossi", 500)
Monty = User("Monty Python", 450)
Cara = User("Cara Levin",520)

Guido.make_deposit(20).make_deposit(150).make_deposit(50).make_withdrawal(50)
print(Guido.account_balance)

Monty.make_deposit(40).make_deposit(50).make_withdrawal(20).make_withdrawal(20)
print(Monty.account_balance)

Cara.make_deposit(500).make_withdrawal(200).make_withdrawal(20).make_withdrawal(20)
print(Cara.account_balance)





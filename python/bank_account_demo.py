from bank_account import BankAccount

account1 = BankAccount("123", 100)
print(account1)
account1.deposit(50)
print(account1)
account1.withdraw(30)
print(account1)
print("Balance is:", account1.get_balance())
account1.withdraw(150) # should not withdraw based on current balance 120 not > 150
print(account1)
print(account1.get_balance())

account2 = BankAccount("456")
account2.deposit(200)

account1.deposit(account2.get_balance())
print(account1)
account2.withdraw(199)
print(account2)
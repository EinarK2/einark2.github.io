# Einar Karl Pétursson
# 27/9/2019

from timaverkefni1 import Account
from timaverkefni1 import SavingsAccount
from timaverkefni1 import CheckingAccount


account1 = SavingsAccount(100000, 15)

print("Account 1:")
print("Calculating Interest...")
SavingsAccount.calculateInterest(account1)
print("Adding to Credit...")
SavingsAccount.credit(account1, 20000)
print("Subtracting from Debit...")
SavingsAccount.debit(account1, 130000)

print("-"*45)

account2 = CheckingAccount(50000, 20000)

print("Account 2:")
print("Adding to Credit...")
CheckingAccount.credit(account2, 10000)
print("Subtracting from Debit...")
CheckingAccount.debit(account2, 15000)

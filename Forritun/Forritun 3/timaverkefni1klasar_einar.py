# Einar Karl Pétursson
# 27/9/2019

class Account:
    def __init__(self, balance):
        self.balance = balance

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Transaction completed. Current balance:", self.balance)
        # add an amount to the current balance

    def debit(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print("Transaction completed. Current balance:", self.balance)
        else:
            print("Debit amount exceeded account balance.")
        # withdraw money from the Account and ensure that the debit
        # amount does not exceed the Account ’s balance.
        # If it does, the balance should be left unchanged,
        # and the method should print the message "Debit amount exceeded account balance."


class SavingsAccount(Account):
    def __init__(self, balance, interest):
        super().__init__(balance)
        self.interest = interest

    def calculateInterest(self):
        print("Amount of interest earned by account:", (self.interest / 100) * self.balance)
        # interest sinnum balance en interest er %


class CheckingAccount(Account):
    def __init__(self, balance, fee):
        super().__init__(balance)
        self.fee = fee

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Transaction completed. Current balance:", self.balance)
        self.balance = self.balance - self.fee
        print("Fee subtracted. Current balance:", self.balance)
        # subtract fee

    def debit(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print("Transaction completed. Current balance:", self.balance)
        else:
            print("Debit amount exceeded account balance.")
        if self.balance - self.fee >=0:
            self.balance = self.balance - self.fee
            print("Fee subtracted. Current balance:", self.balance)
        else:
            print("Debit amount exceeded account balance.")


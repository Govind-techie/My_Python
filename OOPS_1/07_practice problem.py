account_number = int(input("Enter your account_no. : "))

class Account:

    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    
    def credit_or_debit(self):
        credit_or_debit = input("Do you want to credit or debit : ")
        amount = int(input(f"Enter the amonut you want to {credit_or_debit} : "))

        if credit_or_debit == "credit":
            self.balance += amount
            print(f"Rs.{amount} is credited in your account")
            print(f"Account Number = {self.account_no}, Balance = {self.balance}")
        elif credit_or_debit == "debit":
            self.balance -= amount
            print(f"Rs.{amount} is debited in your account")
            print(f"Account Number = {self.account_no}, Balance = {self.balance}")
            

account_1 = Account(10000,12345)
account_2 = Account(12000,23456)

Accounts = {12345 : account_1 , 23456 : account_2}

if account_number in Accounts:
    Accounts[account_number].credit_or_debit()
else:
    print(f"Account Number {account_number} not found")


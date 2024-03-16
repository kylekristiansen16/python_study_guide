""" 
encapsulation is all about protecting the data of a class from being accessed directly and modified in undesired ways
"""

class AccountException(Exception):
    pass

class Account:
    counter = 0
    
    def __init__(self) -> None:
        Account.counter += 1
        self.__balance = 0
        self.__account = f'ACCT_{Account.counter}'

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise AccountException('Balance cannot be negative')
        else:
            if amount > 100000:
                print('Warning: withdraw or deposit is greater than 100')
            self.__balance = amount
    
    @property
    def account(self):
        return self.__account
    
    @account.setter
    def account(self, number):
        raise AccountException('Account number cannot be changed')
    
    @account.deleter
    def account(self):
        if self.balance > 0:
            raise AccountException('Cannot delete account with positive balance')
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
my_bank_acct = Account()
print(f'Account number: {my_bank_acct.account}')
print(f'Balance: {my_bank_acct.balance}')

my_bank_acct.balance = 1000
print(f'balance set to 1000: {my_bank_acct.balance}')

try:
    my_bank_acct.balance = -200
except AccountException as e:
    print(f'trying to set negative balance: {e}')

try: 
    my_bank_acct.account = 'ACCT_1000'
except AccountException as e:
    print(f'trying to change account number: {e}')

my_bank_acct.balance += 1000000
print(f'balance after depositing 1000000: {my_bank_acct.balance}')

try:
    del my_bank_acct.account
except AccountException as e:
    print(f'trying to delete account with positive balance: {e}')
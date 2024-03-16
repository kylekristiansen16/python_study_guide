
# Static methods are methods that do not require (and do not expect!) a parameter indicating the class object or the class itself in order to execute their code.
#   **They are basically regular functions, but enclosed in the class' scope.**
# useful when
#   1 When you need a utility method that comes in a class because it is semantically related, but does not require an object of that class to execute its code;
#   2 consequently, when the static method does not need to know the state of the objects or classes.

class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban
            
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False
        
account_numbers = ['8' * 20, '7' * 4, '2222']

for element in account_numbers:
    if Bank_Account.validate(element):
        print('We can use', element, ' to create a bank account')
    else:
        print('The account number', element, 'is invalid')
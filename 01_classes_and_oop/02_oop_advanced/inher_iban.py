# iban = International Bank Account Number

# IBAN Validator

for iban in ['GB72 HBZU 7006 7212 1253 00', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108']:
    # iban = input("Enter IBAN, please: ")
    iban = iban.replace(' ','')
    if not iban.isalnum():
        print("You have entered invalid characters.")
    elif len(iban) < 15:
        print("IBAN entered is too short.")
    elif len(iban) > 31:
        print("IBAN entered is too long.")
    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)
        if ibann % 97 == 1:
            print("IBAN entered is valid.")
        else:
            print("IBAN entered is invalid.")

print('--------------------------------------------------------------------------------------------------------------')

import random

class IBANValidationError(Exception):
    pass

class IBANDict(dict): # inherit from dict to build a custom dictionary
    def __setitem__(self, _key, _val):
        if validateIBAN(_key):
            super().__setitem__(_key, _val)

    def update(self, *args, **kwargs): # update method is used to add multiple items to the dictionary... confused by it
        for _key, _val in dict(*args, **kwargs).items():
            self.__setitem__(_key, _val)

def validateIBAN(iban): # function used to validate IBAN in custom dictionary
    iban = iban.replace(' ', '')

    if not iban.isalnum():
        raise IBANValidationError("You have entered invalid characters.")

    elif len(iban) < 15:
        raise IBANValidationError("IBAN entered is too short.")

    elif len(iban) > 31:
        raise IBANValidationError("IBAN entered is too long.")

    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)

        if ibann % 97 != 1:
            raise IBANValidationError("IBAN entered is invalid.")

        return True


my_dict = IBANDict()
keys = ['GB72 HBZU 7006 7212 1253 00', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108']

for key in keys:
    my_dict[key] = random.randint(0, 1000)

print('The my_dict dictionary contains:')
for key, value in my_dict.items():
    print("\t{} -> {}".format(key, value))

try:
    my_dict.update({'dummy_account': 100})
except IBANValidationError:
    print('IBANDict has protected your dictionary against incorrect data insertion')


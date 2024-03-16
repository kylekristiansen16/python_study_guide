
""" 
improving the student's skills in reading the CSV files;
using the reader function or the DictReader class.

When we buy a new phone, it's necessary to import old contacts. Why not import them from a CSV file? Look again at the familiar contacts.csv file, and then design your new phone as follows:

- create a class called PhoneContact representing a single contact. The PhoneContact class should contain 
        the name and phone properties;
- create a class called Phone that will store your contacts. First, implement the method called load_contacts_from_csv,
        responsible for reading data from the CSV file into the class property called contacts. The contacts 
        property should contain a list of PhoneContact objects;
- add to the Phone class a method called search_contacts, which accepts any phrase entered by the user from the 
        keyboard, and then based on it perform a search for all matching contacts (case insensitive). If there are 
        no results, print the message: "No contacts found".
        
Example input:
        Search contacts: mother
Example output:
        mother (222-555-101)
        mother-in-law (222-555-104)

Example input:
        Search contacts: 103
Example output:
        wife (222-555-103)
"""
import csv

class PhoneContact():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Phone():
    def __init__(self):
        self.contacts = []

    def load_contacts_from_csv(self, file_name):
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.contacts.append(PhoneContact(row['Name'], row['Phone']))

    def search_contacts(self, phrase):
        found = False
        for contact in self.contacts:
            if phrase.lower() in contact.name.lower() or phrase.lower() in contact.phone.lower():
                print(f'{contact.name} ({contact.phone})')
                found = True
        
        if not found:
            print('No contacts found')
        
        print()
            
phone = Phone()
phone.load_contacts_from_csv('/Users/kylekristiansen/cherreco/python/05_file_processing/03_csv/contacts_lab.csv')
phone.search_contacts('mother')
phone.search_contacts('103')
phone.search_contacts('555')
phone.search_contacts('555-123')
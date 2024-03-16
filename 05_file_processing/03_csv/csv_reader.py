
import csv

# create file object with open
with open('/Users/kylekristiansen/cherreco/python/05_file_processing/03_csv/contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') # pass file object to reader() function, does not make any assumptions about header row
    for row in reader:  # iterate over the reader object
        # print(row)  # each row is a list of strings
        # OR
        print(','.join(row)) # join the list of strings into a single string, separated by commas


# map each line to an OrderedDict object using the DictReader class

with open('/Users/kylekristiansen/cherreco/python/05_file_processing/03_csv/contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # assumes first row is header row
    # OR if you want to specify the header row
    # reader = csv.DictReader(csvfile, fieldnames=['Name', 'Phone', 'Email']) , without this, will be inferred
    # additional column names will have values = None
    for row in reader:
        print(row['Name'], ':', row['Phone'])
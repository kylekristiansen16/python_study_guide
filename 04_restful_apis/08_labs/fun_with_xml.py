
# read the data from nyse.xml
# parse the data into a list of dictionaries
# print the list of dictionaries in a pretty format, preferably using the tabulate module

import xml.etree.ElementTree

company_width = 38
key_names = ["last", "change", "min", "max"]
key_widths = [10, 10, 10, 10]


def show_head():
    print("company".ljust(company_width), end='| ')
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()
    print('-' * (company_width + sum(key_widths) + 10 - 1))

def show_quote(element):
    print(element.text.ljust(company_width), end='| ')
    for (n, w) in zip(key_names, key_widths):
        print(str(element.attrib[n]).ljust(w), end='| ')
    print()

data_root = xml.etree.ElementTree.parse("/Users/kylekristiansen/cherreco/python/04_restful_apis/08_labs/nyse.xml").getroot()

# breakpoint()

show_head()
for child in data_root:
    # print a well formatted table of the data
    show_quote(child)


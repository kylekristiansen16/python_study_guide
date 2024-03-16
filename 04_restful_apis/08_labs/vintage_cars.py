import requests
import json

# constants
SERVER = 'localhost'
PORT = 3000
FIELDS = ['id', 'brand', 'model', 'production_year', 'convertible']
WIDTHS = [10, 10, 10, 16, 11]

def check_server(cid=None):
# returns True or False;
# when invoked without arguments simply checks if server responds;
# invoked with car ID checks if the ID is present in the database;
    if cid:
        try:
            reply = requests.get(url=f"http://{SERVER}:{str(PORT)}/cars/{str(cid)}")
            if reply.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.ConnectionError:
            return False
    else:
        try:
            # check if the server responds
            reply = requests.head(url=f"http://{SERVER}:{str(PORT)}")
            if reply.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.ConnectionError:
            return False    

def print_menu():
    # prints user menu - nothing else happens here;
    menu = """
    +-------------------------------------+
    |  VINTAGE CARS DATABASE - MAIN MENU  |
    +-------------------------------------+
    M E N U
    =======
    1. List all cars
    2. Add new car
    3. Delete car
    4. Update car
    0. Exit
    """
    print(menu)

def read_user_choice():
# reads user choice and checks if it's valid;
# returns '0', '1', '2', '3' or '4' 
    user_choice = input("Enter your choice (0..4): ")
    return user_choice

def print_header():
# prints elegant cars table header;
    for f, w in zip(FIELDS, WIDTHS):
        print(f.ljust(w), end='| ')
    print()
        
def print_car(car):
# prints one car's data in a way that fits the header;
    for f, w in zip(FIELDS, WIDTHS):
        print(str(car[f]).ljust(w), end='| ')
    print()

def list_cars():
# gets all cars' data from server and prints it;
# if the database is empty prints diagnostic message instead;
    print_header()
    try:
        cars = requests.get(url=f"http://{SERVER}:{str(PORT)}/cars").json()
        if cars:
            for car in cars:
                print_car(car)
        else:
            print("No cars in the database")
    except requests.exceptions.ConnectionError:
        print("Error: connection error")
        return

def name_is_valid(name):
# checks if name (brand or model) is valid;
# valid name is non-empty string containing
# digits, letters and spaces;
# returns True or False;
    if name and name.replace(" ", "").isalnum():
        return True
    return False

def enter_id():
# allows user to enter car's ID and checks if it's valid;
# valid ID consists of digits only;
# returns int or None (if user enters an empty line);
    id = input("Enter car's ID (empty string to exit): ")
    if id.isdigit():
        return int(id)
    elif not id:
        return None
    else:
        print("Error: invalid ID - only digits are allowed")
        enter_id()

def enter_production_year():
# allows user to enter car's production year and checks if it's valid;
# valid production year is an int from range 1900..2000;
# returns int or None  (if user enters an empty line);
    prd_year = input("Enter car's production year (empty string to exit): ")
    if prd_year.isdigit() and int(prd_year) in range(1900, 2001):
        return int(prd_year)
    elif not prd_year:
        return None
    else:
        print("Error: invalid production year - only digits from 1900 to 2000 are allowed")
        enter_production_year()

def enter_name(what):
# allows user to enter car's name (brand or model) and checks if it's valid;
# uses name_is_valid() to check the entered name;
# returns string or None  (if user enters an empty line);
# argument describes which of two names is entered currently ('brand' or 'model');
    name = input(f"Enter car's {what} name (empty string to exit): ")
    if name_is_valid(name):
        return name
    elif not name:
        return None
    else:
        print(f"Error: invalid {what} name - only digits, letters and spaces are allowed")
        enter_name(what)

def enter_convertible():
# allows user to enter Yes/No answer determining if the car is convertible;
# returns True, False or None  (if user enters an empty line);
    convertible = input("Is the car convertible? (y/n): ")
    if convertible.lower() == 'y':
        return True
    elif convertible.lower() == 'n':
        return False
    elif not convertible:
        return None
    else:
        print("Error: invalid answer - only 'y' and 'n' are allowed")
        enter_convertible()

def delete_car():
# asks user for car's ID and tries to delete it from database;
    delete_id = enter_id()
    if delete_id:
        if check_server(delete_id):
            try:
                reply = requests.delete(url=f"http://{SERVER}:{str(PORT)}/cars/{str(delete_id)}")
                if reply.status_code == 200:
                    print(f"Car with ID {delete_id} deleted successfully")
                else:
                    print(f"Error: car with ID {delete_id} not found")
            except requests.exceptions.ConnectionError:
                print("Error: connection error")
                return
        else:
            print(f"Error: car with ID {delete_id} not found")

def input_car_data(with_id):
# lets user enter car data;
# argument determines if the car's ID is entered (True) or not (False);
# returns None if user cancels the operation or a dictionary of the following structure:
# {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool } 
    if with_id:
        id = enter_id()
        brand = enter_name('brand')
        model = enter_name('model')
        production_year = enter_production_year()
        convertible = enter_convertible()
        if id and brand and model and production_year and convertible != None:
            return {'id': id, 'brand': brand, 'model': model, 'production_year': production_year, 'convertible': convertible}
        else:
            print("Error: invalid data")
            return None
    else:
        brand = enter_name('brand')
        model = enter_name('model')
        production_year = enter_production_year()
        convertible = enter_convertible()
        if brand and model and production_year and convertible != None:
            return {'brand': brand, 'model': model, 'production_year': production_year, 'convertible': convertible}
        else:
            print("Error: invalid data")
            return None

def add_car():
# invokes input_car_data(True) to gather car's info and adds it to the database;
    car = input_car_data(True)
    if car:
        if not check_server(car['id']):
            try:
                reply = requests.post(url=f"http://{SERVER}:{str(PORT)}/cars", json=car)
                if reply.status_code in [200,201]:
                    print(f"Car with ID {car['id']} added successfully")
                else:
                    print(f"Error: car with ID {car['id']} not added")
                    print(f"Error: {reply.status_code}")
                    print(f"Text: {reply.text}")
            except requests.exceptions.ConnectionError:
                print("Error: connection error")
                return None
        else:
            print(f"Error: car with ID {car['id']} already exists")
    else:
        print("add operation cancelled")
        return None

def update_car():
# invokes enter_id() to get car's ID if the ID is present in the database;
# invokes input_car_data(False) to gather new car's info and updates the database;
    update_id = enter_id()
    if update_id:
        if check_server(update_id):
            car = input_car_data(False)
            if car:
                try:
                    reply = requests.put(url=f"http://{SERVER}:{str(PORT)}/cars/{str(update_id)}", json=car)
                    if reply.status_code in [200,201]:
                        print(f"Car with ID {update_id} updated successfully")
                    else:
                        print(f"Error: car with ID {update_id} not updated")
                except requests.exceptions.ConnectionError:
                    print("Error: connection error")
                    return None
            else:
                print("update operation cancelled")
                return None


while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()

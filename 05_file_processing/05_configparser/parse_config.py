
""" 
why config parser? 
Each service may require different data for authentication, but one thing is certain – we need to store it somewhere in our application. It's not a good idea to hardcode them directly in the code.
A better solution is to use the configuration file, which will be read by the code

what does a config file look like?
    consists of sections that are identified by names enclosed in square brackets
    the sections contain items consisting of key value pairs

[DEFAULT]  # section header
host = localhost # key value pair that's accessible through interpolation by the rest of config file

[mariadb]  # info necessary to connect to mariadb
name = hello
user = user
password = password

[redis]
port = 6379
db = 0

to parse a config file...
    create a ConfigParser object, which provides many useful methods for parsing data

"""

import configparser
import os
# set current working directory to the directory of this file
os.chdir('/Users/kylekristiansen/cherreco/python/05_file_processing/05_configparser')

config = configparser.ConfigParser()
print(config.read('config.ini'))

print('Sections:', config.sections(),'\n')  # [DEFAULT] not returned by sections() method

print('mariadb section:')
print('Host:', config['mariadb']['host'])  # aka config.get('mariadb', 'host')}
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))

print()

print(f"using get method on mariadb host: {config.get('mariadb', 'host')}")

""" 
configparser can read from multiple sources...

The read_dict method accepts any dictionary whose keys are section names, 
while the values include dictionaries containing keys and values. 
All values read from the dictionary are converted to strings.

configparser module also has read_file and read_string methods that allow you to read the configuration from an open file or string
"""

print("--------------------")

config = configparser.ConfigParser()

dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}

config.read_dict(dict)

print('Sections:', config.sections(),'\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))

print()

print(f"test bad get: {config['redis']['host']}")  # the [DEFAULT] section fills in the missing value
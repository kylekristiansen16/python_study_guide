
""" 
treat the configparser object as a dictionary and use the write method to write the contents of the object to a file
key is section header,
value is dictionary of key value pairs
"""

import configparser
import os
os.chdir('/Users/kylekristiansen/cherreco/python/05_file_processing/05_configparser')

config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {'name': 'hello',
                     'user': 'root',
                     'password': 'password'}
config['redis'] = {'port': 6379,
                   'db': 0}

with open('config_written.ini', 'w') as configfile:
    config.write(configfile)
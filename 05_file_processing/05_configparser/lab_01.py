
""" 
improving the student's skills in parsing configuration files;
improving the student's skills in creating configuration files.

Imagine a situation in which you receive a configuration file containing access data for various services. 
Unfortunately, the file is a terrible mess, because it contains data used in both production and development environments.

Your task will be to create two files named prod_config.ini and dev_config.ini. The prod_config.ini file should only contain 
sections for the production environment, while dev_config.ini should only contain sections for the development environment.

To distinguish between the environments, use the env option added to all sections in the mess.ini file. The env option should 
be removed from the sections before moving them to the files.
"""

import configparser
import os
os.chdir('/Users/kylekristiansen/cherreco/python/05_file_processing/05_configparser')

config = configparser.ConfigParser()
config.read('config_mess.ini')

dev = configparser.ConfigParser()
prd = configparser.ConfigParser()

for section in config.sections():
    print(config[section])
    if config[section]['env'] == 'dev':
        dev[section] = config[section]
        dev.remove_option(section, 'env')
    elif config[section]['env'] == 'prd':
        prd[section] = config[section]
        prd.remove_option(section, 'env')
    else:
        print(f"section {section} has no env option")
        
with open('dev_config.ini', 'w') as f:
    dev.write(f)

with open('prd_config.ini', 'w') as f:
    prd.write(f)
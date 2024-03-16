
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'env': 'dev'}
config['mariadb'] = {'env': 'dev'}
config['redis'] = {}

print(config['mariadb']['env'])
print(config['redis']['env'])
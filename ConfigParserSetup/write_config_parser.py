
# Use this code to create a configparser file.
 
import configparser

config = configparser.ConfigParser()

# Replace these as needed, adding or removing sections using: config['name_of_section'] = {'name_of_var': 'value'}
config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {'name': 'hello',
                     'user': 'root',
                     'password': 'password'}
config['redis'] = {'port': 6379,
                   'db': 0}

# Writes it to a file called config.ini in the same directory
with open('config.ini', 'w') as configfile:
    config.write(configfile)
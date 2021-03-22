
# Read configparser file with this.

import configparser

# config.read() will open and read the file passed to it as a configparser file.
config = configparser.ConfigParser()
print(config.read('config.ini'))

# config.sections() returns a list of the sections of the configparser file.
print('Sections:', config.sections(),'\n')

# Access parts of the file with:
# config['section']['variable']
print('Host:', config['mariadb']['host']) 

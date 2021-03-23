
# Basic tools to implement a logger

import logging

FORMAT = '%(levelname)s - %(message)s'
FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

# Set the logger
logger = logging.getLogger('<name_of_parent_logger>.<name_of_logger>')
# or
logger = logging.getLogger(__name__)  
logger.setLevel(logging.DEBUG)

# Sort out the filehandler
handler = logging.FileHandler('<filename.log>', mode='w')
handler.setLevel(logging.DEBUG)

# Format
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

# add the handler to the logger
logger.addHandler(handler)


# logging triggers:
logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
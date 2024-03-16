
""" 
Level name	Value
CRITICAL	50
ERROR	    40
WARNING	    30
INFO	    20
DEBUG	    10
NOTSET	    0

INFO and DEBUG levels are not displayed by default configuration in the console

loggers created using the name argument have the NOTSET level set by default. 
In this case, their logging level is set based on the parent levels, starting from the closest parent to the root logger.

standard logger format: level:logger_name:message
"""
import logging

logging.basicConfig()

logger = logging.getLogger()  # root logger has the logging level set to WARNING by default, so only WARNING, ERROR and CRITICAL messages will be displayed
logger.setLevel(logging.DEBUG)  # set the logging level to DEBUG to display all messages > DEBUG

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
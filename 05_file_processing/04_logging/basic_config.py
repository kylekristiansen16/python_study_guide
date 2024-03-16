
""" 
Calling the basicConfig method (without specifying any arguments) creates a StreamHandler object that processes the logs and then displays them in the console
    StreamHandler object is created by the default Formatter object responsible for the log format
        default format consists of the level name, logger name, and defined message

important concepts of Handlers and Formatters
    allow you to customize your logs
    
LogRecord object
    created by the Logger object
    contains all the information about the log
    passed to the Handler object
    attributes : https://docs.python.org/3/library/logging.html#logrecord-attributes
        name - name of the logger
        levelname - level name of the log
        pathname - full pathname of the source file where the logging call was made
        filename - filename portion of pathname
        funcName - name of the function or method from which the logging call was made
        module - module (name portion of filename)
        lineno - line number in the source file where the logging call was made
        message - the logged message
        args - arguments passed to the logging call
        exc_info - exception information (a tuple of type, value, traceback) or None
        created - time when the LogRecord was created (time.time() return value)
        asctime - time when the LogRecord was created (human-readable form)       
"""

import logging

# format we define is created by combining the attributes of the LogRecord object separated by a colon
FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logging.basicConfig(  # basicconfig is set at the root logger level
    level=logging.CRITICAL,  # set the logging level to CRITICAL to display only CRITICAL messages
    filename='/Users/kylekristiansen/cherreco/python/05_file_processing/04_logging/prod.log',   # set the filename to store the logs, creates FileHandler object - responsible for writing logs to a file
    filemode='a',  # set the file mode to append
    format=FORMAT  # set the format of the logs
    )

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

# logical - a LogRecord object is passed to the Handler object, which knows what to do with that log
# what to do with the log is informed by the Formatter object, which knows how to format the log
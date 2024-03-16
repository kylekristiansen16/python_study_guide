
""" 
you can store logs in different places. Most often it's in the form of a file, but it can also be an output stream, or even an external service

root logger is the highest point in the hierarchy. Its place in the hierarchy is assigned based on the names passed to the getLogger function
"""

import logging

logger = logging.getLogger()  # root logger
hello_logger = logging.getLogger('hello')  # hello is a child of root
hello_world_logger = logging.getLogger('hello.world')  # hello.world is a child of hello
recommended_logger = logging.getLogger(__name__)  # recommended_logger is a child of root with the name of the current module

# every name passed into the getLogger() function is automatically a child of the root logger 
# and inherits its configuration unless you specify otherwise

""" 
the default formatting of the root logger is: level:logger_name:message
"""

handler = logging.FileHandler('/Users/kylekristiansen/cherreco/python/05_file_processing/04_logging/standard.log', mode='w')

logger.addHandler(handler)

logger.critical('Your CRITICAL message')

""" 
Each logger can save logs in different locations as well as in different formats. To do this, you must define your own handler and formatter.

handlers:
    allow you to define where the logs will be stored
    responsible for processing logs
    types:
        StreamHandler - displays logs in the console
        FileHandler - stores logs in a file
        RotatingFileHandler - stores logs in a file, but when the file reaches a certain size, it is renamed and a new file is created
        TimedRotatingFileHandler - stores logs in a file, but when the file reaches a certain age, it is renamed and a new file is created
        SocketHandler - sends logs to a TCP/IP socket
        DatagramHandler - sends logs to a UDP socket
        SMTPHandler - sends logs to an email address
        SysLogHandler - sends logs to a Unix syslog
        NTEventLogHandler - sends logs to a Windows NT/2000/XP event log
        MemoryHandler - stores logs in memory
        HTTPHandler - sends logs to a Web server, using either GET or POST semantics
        QueueHandler - sends logs to a queue, such as those implemented in the queue or multiprocessing modules
        NullHandler - does nothing with the logs
    you can create your own handlers by inheriting from the Handler class

formatters:
    allow you to define the format of the logs
    responsible for the log format
    types:
        basic - default format
        simple - format consisting of the level name and message
        default - format consisting of the level name, logger name, and message *** 
        custom - format defined by the user
    you can create your own formatters by inheriting from the Formatter class

"""

import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logger = logging.getLogger(__name__)

handler = logging.FileHandler('/Users/kylekristiansen/cherreco/python/05_file_processing/04_logging/prod_handler.log', mode='w')

# level set on handler
handler.setLevel(logging.DEBUG)  # set the logging level to CRITICAL to display only CRITICAL messages (default on named handlers is NOTSET, then inherit from parent logger)

formatter = logging.Formatter(FORMAT)
# formatter set on handler
handler.setFormatter(formatter)

# handler added to logger
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
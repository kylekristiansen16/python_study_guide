
""" 
improving the student's skills in creating logs;
improving the student's skills in creating their own handler and formatter.

It's likely that the temperature of your phone battery can get pretty high. Check if that’s true. 
Write a program that will simulate the recording of battery temperatures with an interval of one minute. 
The simulation should contain 60 logs (the last hour).

To simulate temperatures, use one of the available random functions in Python. Temperatures should be drawn 
in the range of 20–40 degrees Celsius, and then saved in the following format:

LEVEL_NAME – TEMPERATURE_IN_CELSIUS UNIT => DEBUG – 20 C

The drawn temperatures should be assigned to the appropriate level depending on their value:

DEBUG = TEMPERATURE_IN_CELSIUS < 30
WARNING = TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35
CRITICAL = TEMPERATURE_IN_CELSIUS > 35

Put all logs in the battery_temperature.log file. The task will be completed when you implement your own handler and formatter.
"""

import logging
import random

FORMAT = '%(levelname)s - %(message)s'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # set the logging level to DEBUG on logger if you want to see all messages > DEBUG

handler = logging.FileHandler('/Users/kylekristiansen/cherreco/python/05_file_processing/04_logging/battery_temperature.log', mode='w')

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

# create list of 60 random temperatures between 20 and 40
temps = [random.randint(20, 40) for i in range(60)]
for temp in temps:
    if temp < 30:
        logger.debug(f'{temp} C')
    elif temp >= 30 and temp <= 35:
        logger.warning(f'{temp} C')
    elif temp > 35:
        logger.critical(f'{temp} C')
    else:
        print('error')
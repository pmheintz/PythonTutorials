"""
Logging format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.striftime
"""

import logging

# format arg is set for time, level name, and message. date format is set by datefmt
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
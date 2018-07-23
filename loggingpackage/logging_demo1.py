"""
Logging demo 1
Logging levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging

# # By default, logging only prints warning level and above messages to the console
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# Logging to file with level set to debug (all levels)
logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
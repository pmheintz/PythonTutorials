"""
Logger demo
"""

import logging

class LoggerDemoConsole():

    def testLog(self):
        # Create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

        # Add formatter to console handler -> chandler
        chandler.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(chandler)

        # Logging messages
        # Note: Logging is set to info level on line 12
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")

demo = LoggerDemoConsole()
demo.testLog()
"""
Using a custom generic logger utility
"""

import logging
import custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug("Debug message")
        self.log.info("Info message")
        self.log.warning("Warning message")
        self.log.error("Error message")
        self.log.critical("Critical message")

    def method2(self):
        m2Log = cl.customLogger(logging.INFO)
        m2Log.debug("Debug message")
        m2Log.info("Info message")
        m2Log.warning("Warning message")
        m2Log.error("Error message")
        m2Log.critical("Critical message")

    def method3(self):
        m3Log = cl.customLogger(logging.WARNING)
        m3Log.debug("Debug message")
        m3Log.info("Info message")
        m3Log.warning("Warning message")
        m3Log.error("Error message")
        m3Log.critical("Critical message")


demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()

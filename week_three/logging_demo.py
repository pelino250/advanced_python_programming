import logging

# TODO 1: Create a logger object. Use the 'logging' module's 'getLogger' method. Name the logger 'example_logger'.
logger = logging.getLogger('example_logger')

# TODO 2: Set the level of the logger to 'DEBUG'. Use the 'setLevel' method of the logger object.
logger.setLevel(logging.DEBUG)

# TODO 3: Create a console handler using 'StreamHandler' from the 'logging' module.
console_handler = logging.StreamHandler()

# TODO 4: Set the level of the console handler to 'DEBUG'.
console_handler.setLevel(logging.DEBUG)

# TODO 5: Create a formatter with the format string: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# TODO 6: Set the formatter for the console handler using its 'setFormatter' method.
console_handler.setFormatter(formatter)

# TODO 7: Add the console handler to the logger using its 'addHandler' method.
logger.addHandler(console_handler)

# TODO 8: Log some messages at different severity levels (debug, info, warning, error, critical) using the appropriate methods of the logger object.
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# TODO 9: Remove the console handler from the logger using its 'removeHandler' method.
logger.removeHandler(console_handler)

# TODO 10: Create a file handler using 'FileHandler' from the 'logging' module. Set the filename to 'app.log'.
file_handler = logging.FileHandler('app.log')

# TODO 11: Set the level of the file handler to 'DEBUG'.
file_handler.setLevel(logging.DEBUG)

# TODO 12: Set the formatter for the file handler.
file_handler.setFormatter(formatter)

# TODO 13: Add the file handler to the logger.
logger.addHandler(file_handler)

# TODO 14: Log some messages at different severity levels.
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# TODO 15: Remove the file handler from the logger.
logger.removeHandler(file_handler)


# TODO 16: Create a custom handler that inherits from 'logging.Handler'. Override its 'emit' method to print the log
#  record's message to the console.
class CustomHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        print(log_entry)


# TODO 17: Create an instance of your custom handler.
custom_handler = CustomHandler()

# TODO 18: Set the level of the custom handler to 'DEBUG'.
custom_handler.setLevel(logging.DEBUG)

# TODO 19: Set the formatter for the custom handler.
custom_handler.setFormatter(formatter)

# TODO 20: Add the custom handler to the logger.
logger.addHandler(custom_handler)

# TODO 21: Log some messages at different severity levels.
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# TODO 22: Remove the custom handler from the logger.
logger.removeHandler(custom_handler)

#  EXERCISE
# Path: week_three/exercise.py

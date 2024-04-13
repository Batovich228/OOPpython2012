import logging
# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w")
# logging.debug('debug message')
# logging.info('info message')

#з використанням параметру форматування

logging.basicConfig(level=logging.debug, filename="logs.log", filemode="w", format="We have logging message:%(asctime)s:%(levelname)s -- %(message)s")
logging.debug("This is a debug message")
logging.info('This is an info message')

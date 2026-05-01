### Error Logging
import logging

logging.basicConfig(filename="app_log.txt", level=logging.DEBUG, format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# logging.debug('This is the debug message')
# logging.info('This is an info message')
# logging.warning('THis is an error message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

def divide(a, b):
    try:
        return a/b
    except Exception as e:
        logging.error("Error dividing %d by %d: %s", a, b, e)
        raise

logging.info("Starting division function")
divide(10,0)
import logging

logging.basicConfig(filename = "logging_demo.txt", level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s")

def sum(a, b):
    logging.info("The function: sum execution has started.")
    logging.debug(f"Input values received: a = {a}, b = {b}")

    if not isinstance(a, (int,float)) or not isinstance(b, (int,float)):
        logging.critical("Invalid data types provided. Only int or float allowed.")
        raise TypeError("Inputs must be numeric")

    try:
        if a == 0 or b == 0:
            logging.warning("One of the input values is zero.")

        c = a + b
        logging.info(f"the total sum value is {c}")
        return 

    except Exception as e:
        logging.error("Function: Sum has encountered with some error. Please find the details below")
        logging.error(e)

    logging.info("The function: Sum execution has completed.")

sum(5, 0)


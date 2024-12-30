"""
Logging
"""
import logging
import os


def setup_logging(debug: bool = False) -> logging.Logger:
    """
    Set up the logging for the project.
    :return: None.
    """
    stdout_handler = logging.StreamHandler()
    logging_format = logging.Formatter("%(asctime)s | %(threadName)s | %(levelname)s | %(name).8s | %(message)s")
    stdout_handler.setFormatter(logging_format)

    logger = logging.getLogger("examples")
    logger.addHandler(stdout_handler)

    if debug:
        logger.setLevel(level=logging.DEBUG)
    else:
        logger.setLevel(level=logging.INFO)

    path = "./logs"
    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)
        print(f"Logs directory {path} created.")
    file_handler = logging.FileHandler(f"{path}/main.log", mode='w')
    file_handler.setFormatter(logging_format)
    logger.addHandler(file_handler)

    logger.info("Logger %s set", logger)

    return logger

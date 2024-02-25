"""
Logging
"""
import logging
import sys


def setup_logging(debug: bool = False) -> None:
    """
    Set up the logging for the project.
    :return: None.
    """
    logging_format = logging.Formatter("%(asctime)s | %(threadName)s | %(levelname)s | %(name).8s | %(message)s")
    logger = logging.getLogger()
    if debug:
        logger.setLevel(level=logging.DEBUG)
    else:
        logger.setLevel(level=logging.INFO)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging_format)
    logger.addHandler(stdout_handler)

    file_handler = logging.FileHandler("./logs/main.log", mode='w')
    file_handler.setFormatter(logging_format)
    logger.addHandler(file_handler)

    logging.info("Logger %s set", logger)

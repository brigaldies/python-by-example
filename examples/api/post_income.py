"""
Post an income
"""
import logging
import sys

import requests


def post_income() -> None:
    """
    Post a new income
    :return: None
    """
    income = {
        'description': 'side gig', 'amount': 1000
    }

    api_url = "http://127.0.0.1:5000/incomes"

    response = requests.post(api_url, json=income)

    logging.info("Response: %s", response.status_code)


if __name__ == "__main__":
    logging_format = logging.Formatter("%(asctime)s | %(levelname)s | %(name).8s | %(message)s")
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging_format)
    logger.addHandler(stdout_handler)

    post_income()

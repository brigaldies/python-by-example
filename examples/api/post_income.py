"""
Post an income
"""
import logging

import requests
from examples.app_logging import app_logging


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
    app_logging.setup_logging()
    post_income()

"""
Post an income
"""
import logging

import requests
from app_logging import setup_logging


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
    setup_logging()
    post_income()

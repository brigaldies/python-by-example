"""
A REST API.

Reference: https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
"""
from flask import Flask, jsonify, request
from app_logging import setup_logging

setup_logging()

app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000}
]


@app.route('/incomes')
def get_incomes():
    """
    Retrieve the incomes.
    :return: The incomes in a JSON format.
    """
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    """
    Add an income.
    :return: empty string, and status code 204.
    """
    incomes.append(request.get_json())
    return '', 204

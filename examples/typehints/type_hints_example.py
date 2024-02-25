"""
Type hints examples.
"""
import argparse
import logging


def run_examples(args: argparse.Namespace) -> None:
    """
    Run the type hints examples
    :return:
    """
    type_hints_example(debug=args.debug)
    generate_greetings(name="bertrand", debug=args.debug)


def type_hints_example(debug: bool = False) -> None:
    """
    Examples of type hints
    """
    if debug:
        logging.info("number: int = 1")
    number: int = 1
    number += 1


def generate_greetings(name: str, debug: bool = False) -> dict[str, str]:
    """
    Returns a dictionary of greetings.
    :param name: Name of the person to greet
    :param debug: Flag to debug
    :return: Dictionay of greetings
    """
    greetings = {
        "morning": f"Good morning {name}",
        "afternoon": f"Good afternoon {name}",
        "evening": f"Good evening {name}",
    }
    if debug:
        logging.info("Greetings %s", greetings)
    return greetings

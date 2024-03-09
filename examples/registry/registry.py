"""
Examples registry.
"""
import argparse
import logging
from typing import Callable

REGISTRY: dict[str, Callable[[argparse.Namespace], None]] = {}


def register_example(func):
    """Register a function as an example"""
    logging.info("Registering example \"%s\"", func.__name__)
    REGISTRY[func.__name__] = func
    return func


def example_not_found(args) -> None:
    """
    Fallback function when an example is not registered.
    :param args: Command-line args.
    :return: None
    """
    logging.error("Unknown example \"%s\"", args.example)


def list_registered_examples() -> int:
    """
    List the examples.
    :return: Number of examples.
    """
    if len(REGISTRY) == 0:
        logging.error("The examples registry is empty.")
    else:
        logging.info([key for key, _ in REGISTRY.items()])
    return len(REGISTRY)


def get_registered_examples() -> list[str]:
    """
    Return the list of registered example names.
    :return: List of registered example names.
    """
    return [key for key, _ in REGISTRY.items()]


def run_example(args) -> None:
    """
    Runs an example.

    :param args: Parsed command-line args.
    :return: None.
    """
    REGISTRY.get(args.example, example_not_found)(args)


def is_registered(example):
    """
    Determines if an example is registered.
    :param example: Example name.
    :return: True if registered, false otherwise.
    """
    example_func = REGISTRY.get(example)
    return example_func is not None and callable(example_func)

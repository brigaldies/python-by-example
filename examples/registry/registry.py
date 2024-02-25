"""
Examples registry.
"""
import argparse
import logging
from typing import Callable
from examples.typehints import type_hints_example
from examples.async_io import async_io_examples


class Registry:
    """
    The registry of examples.
    """

    def __init__(self):
        self.registry: dict[str, Callable[[argparse.Namespace], None]] = {
            "type-hints": type_hints_example.run_examples,
            "async-io": async_io_examples.run_examples,
        }
        logging.info("%d examples registered.", len(self.registry))

    def is_registered(self, example: str) -> bool:
        """
        Determines whether an example is registered.

        :param example: Example name
        :return: True if registered, False otherwise
        """
        return self.registry.get(example) is not None and callable(self.registry[example])

    def run_example(self, args) -> None:
        """
        Runs an example.

        :param args: Parsed command-line args.
        :param debug: Debug mode.
        :return: None.
        """
        if not self.is_registered(args.example):
            raise ValueError(f"Example {args.example} is not registered")

        self.registry[args.example](args)

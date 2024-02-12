"""
Examples registry.
"""
import logging
from typing import Callable
from examples.typehints import type_hints_example


class Registry:
    """
    The registry of examples.
    """

    def __init__(self):
        self.registry: dict[str, Callable[[bool], None]] = {
            "type-hints": type_hints_example.run_examples,
        }
        logging.info("%d examples registered.", len(self.registry))

    def is_registered(self, example: str) -> bool:
        """
        Determines whether an example is registered.

        :param example: Example name
        :return: True if registered, False otherwise
        """
        return self.registry.get(example) is not None and callable(self.registry[example])

    def run_example(self, example: str, debug: bool = False) -> None:
        """
        Runs an example.

        :param example: Example name.
        :param debug: Debug mode.
        :return: None.
        """
        if not self.is_registered(example):
            raise ValueError(f"Example {example} is not registered")

        self.registry[example](debug)

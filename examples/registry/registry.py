import logging
from typing import Callable
from examples.typehints import type_hints_example


class Registry:
    def __init__(self):
        self.registry: dict[str, Callable[[bool], None]] = {
            "type-hints": type_hints_example.run_examples,
        }
        logging.info(f"{len(self.registry)} examples registered.")

    def is_registered(self, example: str) -> bool:
        return example in self.registry.keys() and callable(self.registry[example])

    def run_example(self, example: str, debug: bool = False):
        if not self.is_registered(example):
            raise Exception(f"Example {example} is not registered")

        self.registry[example](debug)

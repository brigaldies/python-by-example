import logging
from typing import Callable
from examples.typehints import type_hints_example


def register_examples() -> dict[str, Callable[[bool], None]]:
    registry = {
        "type-hints": type_hints_example.run_examples,
    }
    logging.info(f"{len(registry)} examples registered.")
    return registry

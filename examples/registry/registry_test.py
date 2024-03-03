"""
Registry unit tests.
"""
import argparse
import logging

from examples.registry.registry import register_example, list_registered_examples, is_registered


@register_example
def example(args: argparse.Namespace) -> None:
    """
    Test example.
    :param args: Command-line arguments.
    :return: None.
    """
    logging.info("Test example %s", args)


def test_registry() -> None:
    """
    Test the registry.
    :return: None.
    """
    assert list_registered_examples() > 0
    assert is_registered("example")

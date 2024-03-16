"""
Decorator example 5.

Use case: Plugin registration.
"""
import argparse
import logging
import random
from examples.decorators.plugins import PLUGINS
from examples.decorators.decorators import register

LOG = logging.getLogger("examples")


@register
def say_hello(name: str) -> str:
    """
    Greeting one.
    :param name: Name.
    :return: Greeting.
    """
    return f"Hello {name}"


@register
def be_awesome(name: str) -> str:
    """
    Greeting two.
    :param name: Name.
    :return: Greeting.
    """
    return f"Yo {name}, together we're the awesomest!"


def randomly_greet(name: str) -> str:
    """
    Random greeter.
    :param name: Name
    :return: Greeting
    """
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    greeter_formatted = f"{greeter!r}"
    LOG.info("Using %s", greeter_formatted)
    return greeter_func(name)


def example_5(args: argparse.Namespace) -> None:
    """
    Run example 5.
    :param args: Command-line arguments.
    :return: None
    """
    LOG.info("Running decorator example 5 (args=%s)", vars(args))
    LOG.info("Greeting: %s", randomly_greet("Bertrand"))

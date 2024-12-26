"""
Closure examples
"""

import argparse
import logging
from typing import Callable

LOG = logging.getLogger("examples")


def closure_example_1(args: argparse.Namespace) -> None:
    """
    Closure example 1: Inner function
    :param args: Command-line arguments
    :return: None
    """
    LOG.info("Running closure example 1 (inner function) with args %s", args)
    outer_func()

    # Verify that the greeter does not return anything
    greeter = outer_func()  # pylint: disable=assignment-from-no-return
    assert greeter is None


def outer_func() -> None:
    """
    Outer function.
    :return: None
    """
    name = "Outer function scope"

    def inner_func() -> None:
        """
        Inner function
        :return: None
        """
        LOG.info("Inner func: Hello, %s!", name)

    # Call inner function
    inner_func()


def closure_example_2(args: argparse.Namespace) -> None:
    """
    Closure example 2: Closure with inner function.
    :param args: Command-line arguments
    :return: None
    """
    LOG.info("Running closure example 2 (closure with inner function) with args %s", args)
    greeter: Callable[[], str] = get_greeter()
    greeting = greeter()
    assert greeting == "Closure (inner): Hello, Outer function scope!"


def get_greeter() -> Callable[[], str]:
    """
    Outer function.
    :return: Inner function-based greeter
    """
    name = "Outer function scope"

    def inner_func() -> str:
        """
        Inner function
        :return: None
        """
        greeting = f"Closure (inner): Hello, {name}!"
        LOG.info(greeting)
        return greeting

    # Return the greeter
    return inner_func


def closure_example_3(args: argparse.Namespace) -> None:
    """
    Closure example 3: Closure with lambda.
    :param args: Command-line arguments
    :return: None.
    """
    LOG.info("Running closure example 3 (closure with lambda) with args %s", args)
    greeter: Callable[[], None] = get_greeter_with_lambda()
    assert callable(greeter)
    greeter()


def get_greeter_with_lambda() -> Callable[[], None]:
    """
    Outer function.
    :return: Lambda-based greeter.
    """
    name = "Outer function scope"

    # Return the greeter
    return lambda: LOG.info("Closure (lambda): Hello, %s!", name)


def closure_example_4(args: argparse.Namespace) -> None:
    """
    Closure example 4: Closure with immutable variable update.
    :param args: Command-line arguments
    :return: None
    """
    LOG.info("Running closure example 4 (closure with immutable variable update) with args %s", args)
    counter: Callable[[], int] = make_counter()
    count = counter()
    assert count == 1
    count = counter()
    assert count == 2


def make_counter() -> Callable[[], int]:
    """
    Outer function: Makes a closure-based counter.
    :return: Inner function-based counter
    """
    count = 0

    def counter() -> int:
        # 'count' points to an int, which is immutable (the pointer, not the value it points to)
        nonlocal count
        count += 1
        LOG.info("counter: count=%d", count)
        return count

    return counter


def closure_example_5(args: argparse.Namespace) -> None:
    """
    Closure example 5: Closure with mutable variable update.
    :param args: Command-line arguments
    :return: None
    """
    LOG.info("Running closure example 5 (closure with mutable variable update) with args %s", args)
    appender = make_appender()
    items = appender("one")
    assert items == ["one"]
    items = appender("two")
    assert items == ["one", "two"]


def make_appender() -> Callable[[str], list[str]]:
    """
    Outer function: Makes a closure-based appender.
    :return: Appender closure.
    """
    items = []

    def appender(new_item):
        # A list is mutable, hence items can be appended to it.
        items.append(new_item)
        LOG.info("appender: items=%s", items)
        return items

    return appender


def closure_example_6(args: argparse.Namespace) -> None:
    """
    Closure example 5: Closure-based functions factory.
    :param args: Command-line arguments
    :return: None
    """
    LOG.info("Running closure example 6 (closure-based functions factory) with args %s", args)
    square_root = make_root_calculator(2, 4)
    assert square_root(42) == 6.4807

    cubic_root = make_root_calculator(3)
    assert cubic_root(42) == 3.48


def make_root_calculator(root_degree, precision=2):
    """
    Makes a closure-based root calculator.
    :param root_degree: Root degree of the calculator
    :param precision: Precision of the calculator
    :return: Root calculator
    """

    def root_calculator(number):
        return round(pow(number, 1 / root_degree), precision)

    return root_calculator

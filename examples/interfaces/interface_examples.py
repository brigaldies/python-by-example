"""
Interface examples.

Source: https://realpython.com/python-interface/
"""
import argparse
import logging

from examples.registry.registry import register_example
from examples.interfaces.interface_informal import interface_informal
from examples.interfaces.interface_metaclass import interface_with_metaclass
from examples.interfaces.interface_virtual_base_class import interface_with_virtual_base_class

LOG = logging.getLogger("examples")


@register_example
def interface(args: argparse.Namespace) -> None:
    """
    Run the interface examples.
    :param args: Command-line args.
    :return: None.
    """
    LOG.info("Running interface examples (args=%s)", args)
    interface_informal()
    interface_with_metaclass()
    interface_with_virtual_base_class()

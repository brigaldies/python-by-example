"""
Type hints examples.
"""
import argparse

from examples.registry.registry import register_example
from examples.typehints.type_hints_examples import type_hints_example, generate_greetings


@register_example
def type_hints(args: argparse.Namespace) -> None:
    """
    Run the type hints examples
    :return:
    """
    type_hints_example(debug=args.debug)
    generate_greetings(name="bertrand", debug=args.debug)

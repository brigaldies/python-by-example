"""
Plugins registry.
"""
import argparse
from typing import Callable

PLUGINS: dict[str, Callable[[argparse.Namespace], None]] = {}

"""
A reusable Timer class.
"""
import argparse
import logging
from dataclasses import dataclass, field
import time
from typing import Callable, ClassVar, Dict, Optional
from reader import feed

LOG = logging.getLogger("examples")


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


@dataclass
class Timer:
    timers: ClassVar[Dict[str, float]] = {}
    name: Optional[str] = None
    text: str = "Elapsed time: {:0.4f} seconds"
    logger: Optional[Callable[[str], None]] = print
    _start_time: Optional[float] = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        """Add timer to dict of timers after initialization"""
        if self.name is not None:
            self.timers.setdefault(self.name, 0)

    def start(self) -> None:
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        # Calculate elapsed time
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        # Report elapsed time
        if self.logger:
            self.logger(self.text.format(elapsed_time))
        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time


def timers_example1(args: argparse.Namespace) -> None:
    """Print the 10 latest tutorials from Real Python"""
    t = Timer("download", logger=None)
    for tutorial_num in range(10):
        t.start()
        tutorial = feed.get_article(str(tutorial_num))
        t.stop()
        print(tutorial)

    download_time = Timer.timers["download"]
    LOG.info(f"Downloaded 10 tutorials in {download_time:0.2f} seconds")

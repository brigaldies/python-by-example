"""
Decorators.

Illustrates various decoration use cases.
"""
import functools
import logging
import time

from examples.decorators.plugins import PLUGINS

LOG = logging.getLogger("examples")


def boiler_plate_decorator(func):
    """
    Boilerplate decorator.
    :param func: Function to decorate.
    :return: Decorated function.
    """

    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper_decorator


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        LOG.info("Finished %s() in %.4f secs", func.__name__, run_time)
        return value

    return wrapper_timer


def debug(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        LOG.info("Calling %s(%s)", func.__name__, signature)
        value = func(*args, **kwargs)
        LOG.info("%s() returned %s", func.__name__, repr(value))
        return value

    return wrapper_debug


def slow_down(func):
    """Sleep 1 second before calling the function"""

    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

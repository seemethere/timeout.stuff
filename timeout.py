from contextlib import contextmanager
from functools import partial
from datetime import datetime
import signal

from decorator import decorator


class MaximumTimeoutExceeded(Exception):
    pass


def _raise_timeout(msg):
    def __internal_timeout(signum, frame):
        raise MaximumTimeoutExceeded(msg)

    return __internal_timeout


def _signal_do_nothing(signum, frame):
    pass


@contextmanager
def of(seconds):
    """Mark a timeout in seconds to raise an exception if enough time elapsed

    :param seconds: Seconds until we raise an exception
    :raises MaximumTimeoutExceeded: When the amount of seconds elapsed is
    greater than the amount of seconds specified

    Example:
        Use it to decorate a function!

        .. sourcecode:: python

            import timeout

            with timeout.of(10):
                some_complex_function()

            # Raise if some_complex_function() takes more than 10 seconds
    """
    signal.signal(
        signal.SIGALRM, _raise_timeout(
            'Maximum timeout of {}s reached'.format(seconds)))
    signal.alarm(seconds)
    yield datetime.now()
    signal.signal(signal.SIGALRM, _signal_do_nothing)


def after(seconds):

    @decorator
    def _wrapper(func, *args, **kwargs):
        run_func = partial(func, *args, **kwargs)
        with of(seconds=seconds):
            return run_func()

    return _wrapper

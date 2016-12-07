"""Check us out @ https://github.com/seemethere/timeout.stuff"""
from contextlib import contextmanager
from functools import partial
from datetime import datetime
import signal

from decorator import decorator


class MaximumTimeoutExceeded(Exception):
    """Maximum timeout exceeded for function"""
    pass


def _raise_timeout(msg):
    def __internal_timeout(*_):
        raise MaximumTimeoutExceeded(msg)

    return __internal_timeout


def _signal_do_nothing(*_):
    pass


@contextmanager
def of(seconds):
    """Mark a code-block to timeout after enough time elapses

    :param seconds: Seconds until we raise an exception
    :returns: Current datetime
    :raises MaximumTimeoutExceeded: When the amount of seconds elapsed is
    greater than the amount of seconds specified

    Example:
        Use it to make sure your block of code executes within a certain time!

        .. sourcecode:: python

            import timeout

            with timeout.of(10):
                result = some_complex_function()
                some_other_complex_function(result)

            # Raise if the execution of both takes more than 10 seconds
    """
    signal.signal(
        signal.SIGALRM, _raise_timeout(
            'Maximum timeout of {}s reached'.format(seconds)))
    signal.alarm(seconds)
    yield datetime.now()
    signal.signal(signal.SIGALRM, _signal_do_nothing)


def after(seconds):
    """Mark a function to timeout after enough time elapses

    :param seconds: Seconds until we raise an exception
    :raises MaximumTimeoutExceeded: When the amount of seconds elapsed is
    greater than the amount of seconds specified


    Example:
        Use it to decorate a function!

        .. sourcecode:: python

            import timeout

            # Raise if some_complex_function() takes more than 10 seconds
            @timeout.after(10)
            def some_complex_function():
                # Some complicated logic here
                pass

            some_complex_function()
    """

    @decorator
    def _wrapper(func, *args, **kwargs):
        run_func = partial(func, *args, **kwargs)
        with of(seconds=seconds):
            return run_func()

    return _wrapper


# These are added so people can do things like:
# from timeout import timeout_of, timeout_after
# Or if they want to copy paste it into their own module
timeout_of = of
timeout_after = after

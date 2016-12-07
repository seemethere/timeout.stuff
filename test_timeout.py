from time import sleep

import pytest
import timeout


def test_timeout_not_reached():
    try:
        with timeout.of(3):
            sleep(2)
        # We sleep after the timeout has ended to make sure there's no
        # lasting signal calls
        sleep(2)
    except timeout.MaximumTimeoutExceeded:
        pytest.fail(
            'MaximumTimeoutExceeded reached when it was not supposed to')


def test_timeout_reached():
    with pytest.raises(timeout.MaximumTimeoutExceeded):
        with timeout.of(3):
            sleep(4)


def test_func_timeout_not_reached():
    @timeout.after(3)
    def func():
        sleep(2)

    try:
        func()
        sleep(2)
    except timeout.MaximumTimeoutExceeded:
        pytest.fail(
            'MaximumTimeoutExceeded reached when it was not supposed to')


def test_func_timeout_reached():
    @timeout.after(3)
    def func():
        sleep(4)

    with pytest.raises(timeout.MaximumTimeoutExceeded):
        func()

from datetime import datetime
from time import sleep

import pytest
import timeout


def test_timeout_not_reached():
    """Test when a timeout is not reached"""
    timeout_time = 3
    sleep_time = 2
    try:
        with timeout.of(timeout_time) as then:
            sleep(sleep_time)
        assert (datetime.now() - then).seconds == sleep_time
        # We sleep after the timeout has ended to make sure there's no
        # lasting signal calls
        sleep(2)
    except timeout.MaximumTimeoutExceeded:
        pytest.fail(
            'MaximumTimeoutExceeded reached when it was not supposed to')


def test_timeout_reached():
    """Test when a timeout is reached"""
    timeout_time = 3
    sleep_time = 4
    with pytest.raises(timeout.MaximumTimeoutExceeded):
        with timeout.of(timeout_time) as then:
            sleep(sleep_time)
    assert (datetime.now() - then).seconds == timeout_time


def test_func_timeout_not_reached():
    """Test when a decorated function's timeout is not reached"""
    @timeout.after(3)
    def func():
        sleep(2)
    try:
        func()
        # We sleep after the timeout has ended to make sure there's no
        # lasting signal calls
        sleep(2)
    except timeout.MaximumTimeoutExceeded:
        pytest.fail(
            'MaximumTimeoutExceeded reached when it was not supposed to')


def test_func_timeout_reached():
    """Test when a decorated function's timeout is reached"""
    @timeout.after(3)
    def func():
        sleep(4)
    with pytest.raises(timeout.MaximumTimeoutExceeded):
        func()

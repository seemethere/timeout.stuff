[![Travis](https://img.shields.io/travis/seemethere/timeout.stuff.svg?maxAge=2592000)](https://travis-ci.org/seemethere/timeout.stuff)
[![PyPI](https://img.shields.io/pypi/v/timeout.stuff.svg?maxAge=2592000)](https://pypi.python.org/pypi/timeout.stuff)
[![Documentation Status](https://readthedocs.org/projects/timeoutstuff/badge/?version=latest)](http://timeoutstuff.readthedocs.io/en/latest/?badge=latest)

# :hourglass: timeout.stuff, a simple timeout library
Have you ever wanted to make things `timeout` stuff after so much time has
elapsed?

Do you have an SLA that dictates that if a certain function isn't performing up
to snuff it doesn't reach a certain *time* limit

# Installation


## General use:
```shell
pip install timeout.stuff
```

## Development:
1. Fork the repo and clone your fork
2. Run in the base repo:
```shell
python setup.py develop && pip install -r requirements-test.txt
```

# Features
* Context managers can be used to timeout code blocks if they reach a certain
elapsed amount of time specified by the user
* The same type of functionality can be used as a wrapper for functions

# Examples

### Use it on a code block!
Use it to timeout a block of code after a certain amount of elapsed time
```python
import timeout


# Timeout this code block after 10 seconds has elapsed
with timeout.of(10):
    result = some_complex_stuff()
    some_more_complex_stuff(result)
```

### Use it as a wrapper
Wrap functions that take a long time to do stuff and make sure they timeout
correctly
```python
import timeout


# Set some_complex_stuff to timeout after 10 seconds has elapsed
@timeout.after(10)
def some_complex_stuff():
    # Execute some complex behavior

some_complex_stuff()
```

# Contributing
1. Fork the repo
2. Commit changes to your Fork
3. Run `python setup.py test` and make sure those all pass
3. Submit those changes as a Pull Request!

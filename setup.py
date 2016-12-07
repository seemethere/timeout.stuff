from setuptools import setup

__version__ = '1.0.2'
__author__ = 'Eli Uriegas'

timeout_classifiers = [
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
]

description = 'A small and simple library to timeout functions'

setup(
    name='timeout.stuff',
    version=__version__, author=__author__,
    author_email='seemethere101@gmail.com',
    url='https://github.com/seemethere/timeout.of',
    py_modules=['timeout'],
    description=description,
    long_description=description,
    license='MIT',
    classifiers=timeout_classifiers,
    install_requires=open('requirements.txt', 'r').read().splitlines(),
    setup_requires=['pytest-runner'],
    tests_requires=['pytest', 'pytest-flake8']
)

"""Foo module for testing purposes.

Adds a couple of functions and classes for testing purposes.
"""

import logging

import pandas

from mpspkg.baz import baz_a


logger = logging.getLogger(__name__)


def fact(n: int) -> int:
    """Calculate the n-th factorial.

    :param n: The input variable that determines which factorial is calculated.
    :returns: The n-th factorial.
    """
    logger.debug(f"Calculating factorial of {n}.")
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def uncovered_function(x: str) -> str:
    """Form a nice string.

    Function not covered by a unit test.

    :param x: The string you want to modify.
    :returns: Another string.
    """
    x = "You entered: " + x + str(baz_a(6))
    return x


def create_df() -> pandas.DataFrame:
    """Create a testing Pandas data frame.

    :returns: A data frame.
    """
    return pandas.DateFrame(
        {"Id": [1, 2, 3], "Name": ["Jaap", "Pim", "Mies"], "Age": [21, 22, 23]}
    )


class Dummy:
    """Dummy class for verifying linting and other checks."""

    bla: str = "hoi"

    def __init__(self, y: str) -> None:
        """Set the bla parameter.

        :param y: The string to assign to bla.
        """
        self.bla = y

    def m(self) -> str:
        """Return the bla parameter.

        :returns: The bla.
        """
        return self.bla

import logging

import pandas


logger = logging.getLogger(__name__)


def fact(n: int) -> int:
    """Simple algorithm to calculate the n-th factorial."""
    logger.debug(f"Calculating factorial of {n}.")
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def uncovered_function(x: str) -> None:
    """Function not covered by a unit test."""
    x = "You entered: " + x
    return x


def create_df() -> pandas.DataFrame:
    return pandas.DateFrame(
        {"Id": [1, 2, 3], "Name": ["Jaap", "Pim", "Mies"], "Age": [21, 22, 23]}
    )
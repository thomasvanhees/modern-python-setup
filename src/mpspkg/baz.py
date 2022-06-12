"""A separate module so that foo.py has something to import."""

from typing import Optional


def baz_a(x: Optional[int] = None) -> int:
    """Calculate something from an input int.

    :param x: Input integer.
    :returns: Another integer.
    """
    if x:
        return x + 5
    else:
        return 5

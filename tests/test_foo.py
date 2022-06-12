from math import factorial

import pytest

from mpspkg.foo import fact


@pytest.mark.unit_test
def test_fact():
    """Test the factorial function."""
    assert fact(5) == factorial(5)


@pytest.mark.integration_test
def test_fact_slow():
    """Test the factorial function."""
    assert fact(15) == factorial(15)

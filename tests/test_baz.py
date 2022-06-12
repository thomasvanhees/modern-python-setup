from mpspkg.baz import baz_a


def test_baz_a():
    """Test the baz_a function."""
    assert baz_a(10) == 15
    assert baz_a() == 5


from pkg_folder import core


def test_add_ints():
    expected = 6
    actual = core.add(1,2,3)
    assert actual == expected

def test_add_str():
    expected = 9
    actual = core.add('1', '6', '2')
    assert actual == expected

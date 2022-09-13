import pytest

from str import reverse_string


@pytest.mark.parametrize("string, result", [('hello', 'olleh'),
                                            ('kayak', 'This is palindrome!')])
def test_reverse_string_not_palindrome(string, result):
    assert reverse_string(string) == result


def test_reverse_string_with_integer():
    with pytest.raises(AttributeError):
        reverse_string(1)

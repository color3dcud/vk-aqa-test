import pytest

from float import multiply


@pytest.mark.parametrize("a, b, result", [(10.0, 2.0, 20.0),
                                          (-5.0, -6.0, 30.0),
                                          (1.0, 0.0, 0.0)])
def test_multiply_not_negative_result(a, b, result):
    assert multiply(a, b) == result


@pytest.mark.parametrize("a, b, negative_result", [(10.0, -2.0, -20.0),
                                                   (-5.0, 6.0, -30.0)])
def test_multiply_with_negative_result(a, b, negative_result):
    assert multiply(a, b) == negative_result

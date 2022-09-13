import pytest

from float import multiply


@pytest.mark.parametrize("a, b, positive_result", [(10.0, 2.0, 20.0),
                                                   (-5.0, -6.0, 30.0)])
def test_multiply_positive_result(a, b, positive_result):
    assert multiply(a, b) == positive_result


@pytest.mark.parametrize("a, b, negative_result", [(10.0, -2.0, -20.0),
                                                   (-5.0, 6.0, -30.0)])
def test_multiply_with_negative_result(a, b, negative_result):
    assert multiply(a, b) == negative_result

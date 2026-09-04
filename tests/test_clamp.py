import pytest

from validkit import clamp


def test_value_within_range_is_returned_unchanged() -> None:
    assert clamp(5, 1, 10) == 5


def test_value_below_low_returns_low() -> None:
    assert clamp(0, 1, 10) == 1


def test_value_above_high_returns_high() -> None:
    assert clamp(15, 1, 10) == 10


def test_value_equal_to_low_is_returned() -> None:
    assert clamp(1, 1, 10) == 1


def test_value_equal_to_high_is_returned() -> None:
    assert clamp(10, 1, 10) == 10


def test_float_value_within_range() -> None:
    assert clamp(3.14, 0.0, 10.0) == 3.14


def test_float_value_below_low_returns_low() -> None:
    assert clamp(0.5, 1, 10) == 1


def test_negative_range() -> None:
    assert clamp(-5, -10, -1) == -5
    assert clamp(-20, -10, -1) == -10


def test_mixed_int_and_float() -> None:
    assert clamp(5.5, 1, 10) == 5.5


def test_equal_low_and_high_is_allowed() -> None:
    assert clamp(5, 7, 7) == 7
    assert clamp(9, 7, 7) == 7


def test_low_greater_than_high_raises_value_error() -> None:
    with pytest.raises(ValueError):
        clamp(5, 10, 1)


def test_non_numeric_value_raises_type_error() -> None:
    with pytest.raises(TypeError):
        clamp("5", 1, 10)


def test_non_numeric_low_raises_type_error() -> None:
    with pytest.raises(TypeError):
        clamp(5, "1", 10)


def test_non_numeric_high_raises_type_error() -> None:
    with pytest.raises(TypeError):
        clamp(5, 1, "10")


def test_none_raises_type_error() -> None:
    with pytest.raises(TypeError):
        clamp(None, 1, 10)


def test_bool_raises_type_error() -> None:
    with pytest.raises(TypeError):
        clamp(True, 1, 10)

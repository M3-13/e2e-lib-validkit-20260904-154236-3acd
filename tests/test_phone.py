import time

import pytest

from validkit.phone import normalize_phone


def test_normalize_phone_ac06() -> None:
    assert normalize_phone("030 1234567", 49) == "+49301234567"


def test_normalize_phone_strips_all_non_numeric() -> None:
    assert normalize_phone("+49 (0)30 1234-567", 49) == "+49490301234567"


def test_normalize_phone_without_leading_zero() -> None:
    assert normalize_phone("301234567", 49) == "+49301234567"


def test_normalize_phone_removes_only_one_leading_zero() -> None:
    assert normalize_phone("0030 1234567", 49) == "+490301234567"


def test_normalize_phone_other_country_code() -> None:
    assert normalize_phone("01 2345 6789", 1) == "+1123456789"


def test_normalize_phone_single_digit() -> None:
    assert normalize_phone("5", 1) == "+15"


def test_normalize_phone_single_zero() -> None:
    assert normalize_phone("0", 1) == "+1"


def test_normalize_phone_empty_string_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("", 49)


def test_normalize_phone_whitespace_only_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("   ", 49)


def test_normalize_phone_no_digits_raises_value_error() -> None:
    for bad in ("abc-def", "k. o. + xyz", "!!!"):
        with pytest.raises(ValueError):
            normalize_phone(bad, 49)


def test_normalize_phone_non_string_raises_type_error() -> None:
    for bad in (None, 123, 12.5, b"030", ["030"], ("030",)):
        with pytest.raises(TypeError):
            normalize_phone(bad, 49)


def test_normalize_phone_non_int_country_code_raises_type_error() -> None:
    for bad in ("49", 49.0, None, [49], (49,)):
        with pytest.raises(TypeError):
            normalize_phone("030 1234567", bad)


def test_normalize_phone_bool_country_code_raises_type_error() -> None:
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", True)
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", False)


def test_normalize_phone_large_input_under_one_second() -> None:
    text = "9" * 100_000
    start = time.perf_counter()
    result = normalize_phone(text, 49)
    elapsed = time.perf_counter() - start
    assert result == "+49" + "9" * 100_000
    assert elapsed < 1.0

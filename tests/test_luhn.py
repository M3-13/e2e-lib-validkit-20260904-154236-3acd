import time

import pytest

from validkit.luhn import luhn_check


def test_valid_luhn_number() -> None:
    assert luhn_check("79927398713") is True


def test_valid_luhn_number_with_spaces() -> None:
    assert luhn_check("7992 7398 713") is True


def test_valid_luhn_number_with_hyphens() -> None:
    assert luhn_check("7992-7398-713") is True


def test_valid_luhn_number_with_mixed_separators() -> None:
    assert luhn_check("79 927-3987 13") is True


def test_valid_visa_like_number() -> None:
    assert luhn_check("4242424242424242") is True


def test_single_zero_is_valid() -> None:
    assert luhn_check("0") is True


def test_wrong_check_digit_returns_false() -> None:
    assert luhn_check("79927398714") is False


def test_wrong_checksum_returns_false() -> None:
    assert luhn_check("4242424242424243") is False


def test_single_non_zero_digit_returns_false() -> None:
    assert luhn_check("1") is False


def test_two_digits_returns_false() -> None:
    assert luhn_check("12") is False


def test_empty_string_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("")


def test_spaces_only_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("   ")


def test_hyphens_only_raise_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("--")


def test_whitespace_and_hyphens_only_raise_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("  - -  ")


@pytest.mark.parametrize(
    "invalid",
    [
        "abc",
        "7992739871X",
        "12a34",
        "1.5",
        "79 927 3987 13!",
        "١٢٣٤٥٦٧٨٩",
    ],
)
def test_invalid_characters_raise_value_error(invalid) -> None:
    with pytest.raises(ValueError):
        luhn_check(invalid)


@pytest.mark.parametrize("bad_type", [None, 123, 12.5, ["79927398713"], b"79927398713"])
def test_non_string_raises_type_error(bad_type) -> None:
    with pytest.raises(TypeError):
        luhn_check(bad_type)


def test_large_input_completes_under_one_second() -> None:
    digits = "9" * 100_000
    start = time.perf_counter()
    result = luhn_check(digits)
    elapsed = time.perf_counter() - start
    assert result is True
    assert elapsed < 1.0

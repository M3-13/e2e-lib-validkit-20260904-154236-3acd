import pytest

from validkit import is_valid_isbn13


def test_valid_isbn_with_hyphens() -> None:
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn_without_hyphens() -> None:
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn_with_spaces() -> None:
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_wrong_check_digit_returns_false() -> None:
    assert is_valid_isbn13("978-3-16-148410-1") is False


def test_ten_digit_isbn_is_not_accepted() -> None:
    assert is_valid_isbn13("3-16-148410-0") is False


def test_too_short_returns_false() -> None:
    assert is_valid_isbn13("978-3-16-148410") is False


def test_too_long_returns_false() -> None:
    assert is_valid_isbn13("978-3-16-148410-00") is False


def test_empty_string_returns_false() -> None:
    assert is_valid_isbn13("") is False


def test_only_separators_returns_false() -> None:
    assert is_valid_isbn13("---  --") is False


@pytest.mark.parametrize(
    "value",
    [
        "978-3-16-148410-X",
        "978-3-16-148410-0a",
        "abc",
        "978.3.16.148410.0",
    ],
)
def test_invalid_characters_raise_value_error(value: str) -> None:
    with pytest.raises(ValueError):
        is_valid_isbn13(value)


@pytest.mark.parametrize(
    "value",
    [
        9783161484100,
        None,
        3.14,
        ["978-3-16-148410-0"],
        b"978-3-16-148410-0",
    ],
)
def test_non_string_raises_type_error(value: object) -> None:
    with pytest.raises(TypeError):
        is_valid_isbn13(value)

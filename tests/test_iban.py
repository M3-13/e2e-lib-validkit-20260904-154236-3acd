import pytest

from validkit.iban import is_valid_iban


def test_valid_iban_with_spaces() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_iban_without_spaces() -> None:
    assert is_valid_iban("DE89370400440532013000") is True


def test_valid_gb_iban() -> None:
    assert is_valid_iban("GB29 NWBK 6016 1331 9268 19") is True


def test_valid_fr_iban() -> None:
    assert is_valid_iban("FR14 2004 1010 0505 0001 3M02 606") is True


def test_valid_shortest_iban() -> None:
    assert is_valid_iban("NO93 8601 1117 947") is True


def test_swapped_check_digits_returns_false() -> None:
    assert is_valid_iban("DE98 3704 0044 0532 0130 00") is False


def test_wrong_checksum_returns_false() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 01") is False


def test_wrong_length_too_short_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("DE89 3704 0044 0532 0130")


def test_wrong_length_too_long_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("DE89 3704 0044 0532 0130 0000")


def test_unknown_country_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("XX89 3704 0044 0532 0130 00")


def test_invalid_characters_raise_value_error() -> None:
    for invalid in [
        "DE89 3704 0044 0532 0130 0!",
        "DE89-3704-0044-0532-0130-00",
        "de89 3704 0044 0532 0130 00",
        "DE8A 3704 0044 0532 0130 00",
    ]:
        with pytest.raises(ValueError):
            is_valid_iban(invalid)


def test_empty_string_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("")


def test_whitespace_only_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("   ")


@pytest.mark.parametrize("bad_type", [None, 123, 12.5, ["DE89"], b"DE89"])
def test_non_string_raises_type_error(bad_type) -> None:
    with pytest.raises(TypeError):
        is_valid_iban(bad_type)

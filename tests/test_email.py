import time

import pytest

from validkit.email import is_valid_email


def test_valid_simple_email() -> None:
    assert is_valid_email("test@example.com") is True


def test_valid_email_with_subdomain() -> None:
    assert is_valid_email("name@mail.example.org") is True


def test_valid_minimal_email() -> None:
    assert is_valid_email("a@b.co") is True


def test_no_at_sign_returns_false() -> None:
    assert is_valid_email("kein-at") is False


def test_empty_string_returns_false() -> None:
    assert is_valid_email("") is False


def test_multiple_at_signs_returns_false() -> None:
    assert is_valid_email("a@b@c.com") is False


def test_missing_local_part_returns_false() -> None:
    assert is_valid_email("@example.com") is False


def test_missing_domain_returns_false() -> None:
    assert is_valid_email("test@") is False


def test_domain_without_dot_returns_false() -> None:
    assert is_valid_email("test@example") is False


def test_empty_domain_name_returns_false() -> None:
    assert is_valid_email("test@.com") is False


def test_empty_tld_returns_false() -> None:
    assert is_valid_email("test@example.") is False


@pytest.mark.parametrize("bad", [None, 123, 3.14, ["test@example.com"], b"test@example.com"])
def test_non_string_raises_type_error(bad) -> None:
    with pytest.raises(TypeError):
        is_valid_email(bad)


def test_large_input_terminates_quickly() -> None:
    big = "a" * 50000 + "@" + "b" * 50000 + ".com"
    start = time.perf_counter()
    result = is_valid_email(big)
    elapsed = time.perf_counter() - start
    assert result is True
    assert elapsed < 1.0


def test_large_input_without_at_terminates_quickly() -> None:
    big = "a" * 100000
    start = time.perf_counter()
    result = is_valid_email(big)
    elapsed = time.perf_counter() - start
    assert result is False
    assert elapsed < 1.0

import time

import pytest

from validkit.slug import slugify


def test_slugify_hello_world() -> None:
    assert slugify("Héllo, Wörld!") == "hello-world"


def test_slugify_simple_text() -> None:
    assert slugify("Hello World") == "hello-world"


def test_slugify_collapses_multiple_separators() -> None:
    assert slugify("Hello   World") == "hello-world"


def test_slugify_strips_leading_trailing_separators() -> None:
    assert slugify("  Hello World  ") == "hello-world"


def test_slugify_collapses_hyphens() -> None:
    assert slugify("foo---bar") == "foo-bar"


def test_slugify_keeps_digits() -> None:
    assert slugify("Product 123") == "product-123"


def test_slugify_removes_accents() -> None:
    assert slugify("Zürich Café") == "zurich-cafe"


def test_slugify_uppercase_to_lowercase() -> None:
    assert slugify("ABC DEF") == "abc-def"


def test_slugify_mixed_special_characters() -> None:
    assert slugify("Héllo, Wörld!@#$%^&*()") == "hello-world"


def test_slugify_single_letter() -> None:
    assert slugify("a") == "a"


def test_slugify_single_digit() -> None:
    assert slugify("7") == "7"


def test_slugify_only_digits() -> None:
    assert slugify("12345") == "12345"


def test_slugify_already_slug_unchanged() -> None:
    assert slugify("hello-world") == "hello-world"


def test_slugify_empty_string_raises_value_error() -> None:
    with pytest.raises(ValueError):
        slugify("")


def test_slugify_whitespace_only_raises_value_error() -> None:
    with pytest.raises(ValueError):
        slugify("   ")


def test_slugify_only_special_characters_raises_value_error() -> None:
    for special in ("!!!", "---", "@#$", ".,;:", "!@#$%^&*()"):
        with pytest.raises(ValueError):
            slugify(special)


@pytest.mark.parametrize("bad_type", [None, 123, 12.5, ["text"], b"bytes", object()])
def test_slugify_non_string_raises_type_error(bad_type) -> None:
    with pytest.raises(TypeError):
        slugify(bad_type)


def test_slugify_large_input_completes_quickly() -> None:
    long_text = ("Héllo, Wörld! 123 " * 10000)[:100_000]
    start = time.perf_counter()
    result = slugify(long_text)
    elapsed = time.perf_counter() - start

    assert elapsed < 1.0
    assert result
    assert "-" in result

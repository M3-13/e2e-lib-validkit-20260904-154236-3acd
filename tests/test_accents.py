import pytest

from validkit.accents import strip_accents


def test_strip_accents_ac07_example() -> None:
    assert strip_accents("Grüße aus Zürich \u2013 café") == "Gruße aus Zurich \u2013 cafe"


def test_strip_accents_single_accented_letter() -> None:
    assert strip_accents("café") == "cafe"


def test_strip_accents_umlauts() -> None:
    assert strip_accents("äöüÄÖÜ") == "aouAOU"


def test_strip_accents_combining_character_alone() -> None:
    assert strip_accents("\u0301") == ""


def test_strip_accents_no_accents_unchanged() -> None:
    assert strip_accents("hello world 123") == "hello world 123"


def test_strip_accents_empty_string() -> None:
    assert strip_accents("") == ""


def test_strip_accents_non_latin_unchanged() -> None:
    assert strip_accents("你好 Привет مرحبا") == "你好 Привет مرحبا"


def test_strip_accents_sharp_s_preserved() -> None:
    assert strip_accents("straße") == "straße"


def test_strip_accents_dash_preserved() -> None:
    assert strip_accents("a\u2013b") == "a\u2013b"


@pytest.mark.parametrize("bad", [None, 42, 3.14, b"cafe", ["cafe"], {"a": 1}, True])
def test_strip_accents_non_string_raises_type_error(bad) -> None:
    with pytest.raises(TypeError):
        strip_accents(bad)

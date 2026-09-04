import pytest

from validkit.mask import mask_secret


def test_mask_secret_masks_all_but_last_keep() -> None:
    assert mask_secret("geheim123", 4) == "*****m123"


def test_mask_secret_short_text_unchanged() -> None:
    assert mask_secret("kurz", 10) == "kurz"


def test_mask_secret_default_keep_is_four() -> None:
    assert mask_secret("password123") == "*******d123"


def test_mask_secret_keep_equals_length() -> None:
    assert mask_secret("abc", 3) == "abc"


def test_mask_secret_keep_one() -> None:
    assert mask_secret("abc", 1) == "**c"


def test_mask_secret_keep_zero_masks_everything() -> None:
    assert mask_secret("abc", 0) == "***"


def test_mask_secret_empty_text() -> None:
    assert mask_secret("", 0) == ""
    assert mask_secret("", 4) == ""


def test_mask_secret_single_char_keep_zero() -> None:
    assert mask_secret("a", 0) == "*"


def test_mask_secret_reveals_at_most_last_keep_chars() -> None:
    for text in ("geheim123", "a", "", "hunter2", "x" * 100):
        for keep in range(0, len(text) + 3):
            result = mask_secret(text, keep)
            if len(text) <= keep:
                assert result == text
            else:
                visible = text[-keep:] if keep > 0 else ""
                assert len(result) == len(text)
                assert result.endswith(visible)
                assert result[: len(text) - keep] == "*" * (len(text) - keep)


def test_mask_secret_negative_keep_raises_value_error() -> None:
    with pytest.raises(ValueError):
        mask_secret("x", -1)


def test_mask_secret_large_negative_keep_raises_value_error() -> None:
    with pytest.raises(ValueError):
        mask_secret("geheim", -100)


def test_mask_secret_bool_keep_raises_value_error() -> None:
    with pytest.raises(ValueError):
        mask_secret("geheim", True)
    with pytest.raises(ValueError):
        mask_secret("geheim", False)


def test_mask_secret_non_string_text_raises_type_error() -> None:
    for bad in (123, None, 3.14, b"bytes", ["geheim"], ("geheim",)):
        with pytest.raises(TypeError):
            mask_secret(bad, 4)


def test_mask_secret_non_int_keep_raises_type_error() -> None:
    for bad in ("4", 3.5, None, [4], (4,)):
        with pytest.raises(TypeError):
            mask_secret("geheim", bad)

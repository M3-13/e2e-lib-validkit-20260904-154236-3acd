import validkit

EXPECTED_PUBLIC_API = [
    "is_valid_email",
    "luhn_check",
    "is_valid_iban",
    "is_valid_isbn13",
    "normalize_phone",
    "strip_accents",
    "mask_secret",
    "slugify",
    "clamp",
]


def test_import_validkit_works() -> None:
    assert validkit is not None


def test_all_contains_exactly_the_nine_public_names() -> None:
    assert set(validkit.__all__) == set(EXPECTED_PUBLIC_API)
    assert len(validkit.__all__) == 9


def test_every_public_function_is_callable() -> None:
    for name in EXPECTED_PUBLIC_API:
        func = getattr(validkit, name)
        assert callable(func), f"{name} is not callable"

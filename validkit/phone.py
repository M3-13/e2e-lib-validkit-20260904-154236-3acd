def normalize_phone(text: str, country_code: int) -> str:
    """Return ``text`` normalised to the canonical ``+<country_code><national>`` form.

    All non-numeric characters are removed, a single leading zero of the national
    number is dropped, and the country code is prepended with a leading ``+``.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if isinstance(country_code, bool) or not isinstance(country_code, int):
        raise TypeError("country_code must be an int")

    digits = "".join(ch for ch in text if ch.isdigit())
    if not digits:
        raise ValueError("text must contain at least one digit")

    national = digits[1:] if digits[0] == "0" else digits
    return f"+{country_code}{national}"

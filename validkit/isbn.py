_ALLOWED_CHARS = "0123456789- "


def is_valid_isbn13(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("ISBN must be a string")

    if any(ch not in _ALLOWED_CHARS for ch in text):
        raise ValueError("ISBN-13 may only contain digits, hyphens and spaces")

    digits = text.replace("-", "").replace(" ", "")
    if len(digits) != 13:
        return False

    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))
    return total % 10 == 0

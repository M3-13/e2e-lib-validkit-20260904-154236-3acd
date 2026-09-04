def luhn_check(digits: str) -> bool:
    """Return True if ``digits`` is a valid Luhn checksum number.

    Spaces and hyphens are ignored. If no digits remain or any other
    character is present, a ``ValueError`` is raised; a non-string input
    raises a ``TypeError``.
    """
    if not isinstance(digits, str):
        raise TypeError("luhn_check expects a string")

    compact = digits.replace(" ", "").replace("-", "")

    if not compact:
        raise ValueError("luhn_check contains no digits")

    if any(ch not in "0123456789" for ch in compact):
        raise ValueError("luhn_check contains invalid characters")

    total = 0
    for index, char in enumerate(reversed(compact)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0

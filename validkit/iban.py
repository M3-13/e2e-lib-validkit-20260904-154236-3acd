import re

_IBAN_PATTERN = re.compile(r"^[A-Z]{2}[0-9]{2}[A-Z0-9]+$")

_IBAN_LENGTHS = {
    "AD": 24,
    "AE": 23,
    "AL": 28,
    "AT": 20,
    "AZ": 28,
    "BA": 20,
    "BE": 16,
    "BG": 22,
    "BH": 22,
    "BI": 27,
    "BR": 29,
    "BY": 28,
    "CH": 21,
    "CR": 22,
    "CY": 28,
    "CZ": 24,
    "DE": 22,
    "DJ": 27,
    "DK": 18,
    "DO": 28,
    "EE": 20,
    "EG": 29,
    "ES": 24,
    "FI": 18,
    "FK": 18,
    "FO": 18,
    "FR": 27,
    "GB": 22,
    "GE": 22,
    "GI": 23,
    "GL": 18,
    "GR": 27,
    "GT": 28,
    "HR": 21,
    "HU": 28,
    "IE": 22,
    "IL": 23,
    "IQ": 23,
    "IS": 26,
    "IT": 27,
    "JO": 30,
    "KW": 30,
    "KZ": 20,
    "LB": 28,
    "LC": 32,
    "LI": 21,
    "LT": 20,
    "LU": 20,
    "LV": 21,
    "LY": 25,
    "MC": 27,
    "MD": 24,
    "ME": 22,
    "MK": 19,
    "MR": 27,
    "MT": 31,
    "MU": 30,
    "NL": 18,
    "NO": 15,
    "PK": 24,
    "PL": 28,
    "PS": 29,
    "PT": 25,
    "QA": 29,
    "RO": 24,
    "RS": 22,
    "SA": 24,
    "SC": 31,
    "SE": 24,
    "SI": 19,
    "SK": 24,
    "SM": 27,
    "ST": 25,
    "SV": 28,
    "TL": 23,
    "TN": 24,
    "TR": 26,
    "UA": 29,
    "VA": 22,
    "VG": 24,
    "XK": 20,
}


def is_valid_iban(text: str) -> bool:
    """Return True if ``text`` is a structurally valid IBAN with a correct check sum."""
    if not isinstance(text, str):
        raise TypeError("is_valid_iban expects a string")

    compact = text.replace(" ", "")

    if not _IBAN_PATTERN.fullmatch(compact):
        raise ValueError("IBAN contains invalid characters")

    country = compact[:2]
    length = _IBAN_LENGTHS.get(country)
    if length is None:
        raise ValueError(f"unknown IBAN country code '{country}'")
    if len(compact) != length:
        raise ValueError(
            f"IBAN for country '{country}' must be {length} characters, got {len(compact)}"
        )

    rearranged = compact[4:] + compact[:4]
    digits = "".join(str(ord(ch) - ord("A") + 10) if "A" <= ch <= "Z" else ch for ch in rearranged)

    return int(digits) % 97 == 1

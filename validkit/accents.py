import unicodedata


def strip_accents(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(f"text must be a string, got {type(text).__name__}")

    normalized = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in normalized if unicodedata.combining(ch) == 0)

def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if isinstance(keep, bool):
        raise ValueError("keep must be a non-negative integer, not a bool")
    if not isinstance(keep, int):
        raise TypeError("keep must be an int")
    if keep < 0:
        raise ValueError("keep must be a non-negative integer")

    if len(text) <= keep:
        return text

    return "*" * (len(text) - keep) + (text[-keep:] if keep > 0 else "")

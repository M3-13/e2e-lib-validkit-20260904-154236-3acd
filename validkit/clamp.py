def _is_number(arg: object) -> bool:
    return not isinstance(arg, bool) and isinstance(arg, (int, float))


def clamp(value: float, low: float, high: float) -> float:
    """Begrenze ``value`` auf den Bereich [``low``, ``high``].

    Liefert ``low`` wenn ``value < low``, ``high`` wenn ``value > high`` und
    sonst ``value`` unverändert. ``low > high`` löst ``ValueError`` aus,
    nicht-numerische Argumente ``TypeError``.
    """

    if not _is_number(value):
        raise TypeError(f"value muss eine Zahl sein, nicht {type(value).__name__}")
    if not _is_number(low):
        raise TypeError(f"low muss eine Zahl sein, nicht {type(low).__name__}")
    if not _is_number(high):
        raise TypeError(f"high muss eine Zahl sein, nicht {type(high).__name__}")

    if low > high:
        raise ValueError(f"low ({low}) darf nicht größer als high ({high}) sein")

    if value < low:
        return low
    if value > high:
        return high
    return value

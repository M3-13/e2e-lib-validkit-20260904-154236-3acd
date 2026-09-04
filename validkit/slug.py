import re
import unicodedata


def slugify(text: str) -> str:
    """Erzeuge aus ``text`` einen URL-freundlichen Slug.

    Entfernt Akzente (NFKD-Normalisierung und anschließendes Entfernen der
    Kombinationszeichen), konvertiert in Kleinbuchstaben, ersetzt jede Folge
    von Nicht-Buchstaben/-Ziffern durch ``-`` und entfernt mehrfache sowie
    führende/abschließende Bindestriche. Ein leeres Ergebnis löst ``ValueError``
    aus, ein Nicht-String ``TypeError``.
    """

    if not isinstance(text, str):
        raise TypeError(f"slugify erwartet einen String, nicht {type(text).__name__}")

    normalized = unicodedata.normalize("NFKD", text)
    without_accents = "".join(ch for ch in normalized if not unicodedata.combining(ch))

    slug = re.sub(r"[^a-z0-9]+", "-", without_accents.lower()).strip("-")

    if not slug:
        raise ValueError("slugify erzeugte ein leeres Ergebnis")

    return slug

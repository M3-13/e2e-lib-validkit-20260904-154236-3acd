"""Strukturpruefung von E-Mail-Adressen ohne Netzwerk/DNS und ohne Regex."""


def is_valid_email(text: str) -> bool:
    """Prueft die Struktur einer E-Mail-Adresse rein syntaktisch.

    Erwartet werden: ein nicht-leerer lokaler Teil, genau ein ``@`` sowie
    eine Domain mit mindestens einem Punkt und einem nicht-leeren TLD-Teil
    hinter dem letzten Punkt. Leere oder strukturell falsche Eingaben
    ergeben ``False``; ein Nicht-String loest ``TypeError`` aus.

    Die Pruefung laeuft linear ueber die Eingabe (``str.find``/``str.rfind``)
    und ist damit nicht ReDoS-anfaellig.
    """
    if not isinstance(text, str):
        raise TypeError("text muss ein String sein")

    if not text:
        return False

    at_index = text.find("@")
    if at_index == -1 or at_index != text.rfind("@"):
        return False

    if at_index == 0:
        return False

    domain = text[at_index + 1 :]

    last_dot = domain.rfind(".")
    return not (last_dot <= 0 or last_dot == len(domain) - 1)

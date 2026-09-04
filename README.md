# validkit

validkit ist eine kleine, eigenständige Python-Bibliothek ohne externe Abhängigkeiten. Sie bündelt neun unabhängige, reine Prüf- und Normalisierungsfunktionen für E-Mails, Prüfziffern, IBAN, ISBN-13, Telefonnummern, Akzente, Geheimnisse, Slugs und Wertbegrenzung. Die öffentliche API wird zentral über `__init__.py` exportiert; jede Funktion ist typannotiert, meldet ungültige Eingaben mit einem aussagekräftigen Fehler und besitzt eigene pytest-Unit-Tests inklusive Grenz- und Fehlerfällen.

## Tech-Stack

- **Sprache**: Python 3.9+
- **Runtime**: CPython
- **Build**: setuptools via `pyproject.toml`
- **Tests**: pytest
- **Abhängigkeiten**: nur Standardbibliothek (keine Laufzeitabhängigkeiten)

## Installation

```bash
pip install -e .
```

## Tests

```bash
python -m pytest
```

## Verwendung

Alle neun Funktionen werden über `validkit` exportiert:

```python
import validkit
```

### is_valid_email

```python
from validkit import is_valid_email

is_valid_email("test@example.com")  # True
```

### luhn_check

```python
from validkit import luhn_check

luhn_check("79927398713")  # True
```

### is_valid_iban

```python
from validkit import is_valid_iban

is_valid_iban("DE89 3704 0044 0532 0130 00")  # True
```

### is_valid_isbn13

```python
from validkit import is_valid_isbn13

is_valid_isbn13("978-3-16-148410-0")  # True
```

### normalize_phone

```python
from validkit import normalize_phone

normalize_phone("030 1234567", 49)  # '+49301234567'
```

### strip_accents

```python
from validkit import strip_accents

strip_accents("Grüße aus Zürich – café")  # 'Gruße aus Zurich – cafe'
```

### mask_secret

```python
from validkit import mask_secret

mask_secret("geheim123", 4)  # '*****123'
```

### slugify

```python
from validkit import slugify

slugify("Héllo, Wörld!")  # 'hello-world'
```

### clamp

```python
from validkit import clamp

clamp(5, 1, 10)  # 5
```

## Features

- Neun reine, eigenständige Prüf- und Normalisierungsfunktionen.
- Zentral exportierte öffentliche API über `__all__`.
- Durchgängige Typannotationen.
- Klare Fehlerkonvention: `TypeError` bei falschem Eingabetyp, `ValueError` bei inhaltlich ungültigen Werten.

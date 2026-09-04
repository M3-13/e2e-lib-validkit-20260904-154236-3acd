VERDICT: APPROVED

## Security-Review: validkit

### Scanner-Abdeckung
- `bandit`: `[skipped]` – nicht installiert
- `semgrep`: `[skipped]` – nicht installiert
- `pip-audit`/`npm audit`: nicht ausgeführt / keine Meldung

Aus den übersprungenen Scannern wird kein Befund abgeleitet. Das Projekt hat keine Laufzeit-Drittabhängigkeiten, das Supply-Chain-Risiko ist dadurch gering.

### 1. Secrets
Keine hartkodierten Schlüssel, Passwörter, Token oder sensiblen URLs erkennbar. Die `.gitignore` schließt `.env`, Datenbanken und Logs aus.  
**Befund:** keiner.

### 2. Injection & Inputs
- Keine dynamische Codeausführung (`eval`, `exec`, `pickle`, `subprocess` mit Shell), keine unsichere Deserialisierung.
- Die verwendeten regulären Ausdrücke und String-Operationen sind linear bzw. nicht ReDoS-anfällig.
- Eingaben werden durchgängig typgeprüft (`TypeError`) oder mit `ValueError` abgelehnt.

**Härtungshinweise, niedrig:**

- **`validkit/phone.py` – `normalize_phone`**  
  `str.isdigit()` akzeptiert auch Unicode-Ziffern, z. B. arabisch-indische Ziffern. Für eine kanonische Telefonnummer im E.164-Format sollten nur ASCII-Ziffern zugelassen werden.  
  **Fix:**  
  `digits = "".join(ch for ch in text if ch in "0123456789")`

- **`validkit/phone.py` – `normalize_phone`**  
  `country_code` wird nur als `int` geprüft, nicht als positiver, plausibler Ländercode. Negative Werte erzeugen ungültige Ausgaben wie `+-49123...`.  
  **Fix:**  
  `if not 1 <= country_code <= 999: raise ValueError("country_code muss zwischen 1 und 999 liegen")`

- **`validkit/email.py` – `is_valid_email`**  
  Die Prüfung ist bewusst syntaktisch und erlaubt z. B. Leer- oder Steuerzeichen im lokalen Teil. Im Kontext dieser eigenständigen Bibliothek unkritisch. Falls die Funktion später vor einer E-Mail-Header-Verarbeitung eingesetzt wird, sollte sie restriktiver validieren.  
  **Fix:** lokalen Teil und Domain auf erlaubte Zeichen begrenzen.

- **`validkit/clamp.py` – `clamp`**  
  `float("nan")` und `inf` sind erlaubt; `nan` wird bei Vergleichen unverändert zurückgegeben.  
  **Fix optional:** `math.isfinite()` für alle drei Argumente prüfen.

### 3. AuthN/AuthZ
Keine Authentifizierungs- oder Autorisierungsfunktionalität vorhanden.  
**Befund:** keiner.

### 4. Dependencies
Keine Laufzeitabhängigkeiten außerhalb der Python-Standardbibliothek. Optional nur `pytest>=7.0,<9.0`. Kein bekanntes ausgebeutetes CVE erkennbar.  
**Befund:** keiner.

### 5. Konfiguration & Transport
Keine Netzwerk-, Server- oder Transportfunktion. Keine CORS-, Debug- oder unsicheren Standardkonfigurationen sichtbar.  
**Befund:** keiner.

### Hinweis ohne Sicherheitsrelevanz
Das AC-13-Beispiel `mask_secret('geheim123', 4) == '*****123'` passt nicht zur Implementierung: Die letzten vier Zeichen von `"geheim123"` sind `"m123"`, daher liefert die Funktion korrekt `"*****m123"`. Der zugehörige Test bestätigt dieses Verhalten. Die Implementierung erfüllt die eigentliche Sicherheitsanforderung „höchstens die letzten `keep` Zeichen im Klartext sichtbar“.

**Fazit:** Keine ausnutzbaren Schwachstellen erkennbar.
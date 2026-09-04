VERDICT: CHANGES_REQUESTED

# Prüfbericht validkit – Sprint-Endstand

Projekttyp: `python-backend`, reine Python-Bibliothek ohne Endnutzer-UI. Geprüft wurde der vorgelegte Ist-Stand (`pyproject.toml`, `ruff.toml`, Quellcode unter `validkit/`, Tests unter `tests/`). Nicht einsehbare Dateien wie `README.md`, `AGENTS.md`, `CLAUDE.md`, `RUN.json` werden nicht spekulativ bewertet.

## 1. DSGVO

Die Bibliothek selbst ist kein Verantwortlicher, sondern ein Verarbeitungswerkzeug. Es findet keine eigene Erhebung, Speicherung, Protokollierung oder Übermittlung statt. Die Funktionen verarbeiten Eingaben ausschließlich im Arbeitsspeicher des aufrufenden Prozesses. Personenbezogene Daten können dabei als Funktionsparameter auftreten (E-Mail, Telefonnummer, IBAN, Namen, Geheimnisse).

**Befund DSGVO-1 (low): Fehlende Klarstellung zur lokalen Verarbeitung und Verantwortlichkeit.**  
Für Nutzer der Bibliothek ist nicht aus dem vorgelegten Stand ersichtlich, dass validkit keine Daten speichert, protokolliert oder überträgt und der Verwender bei personenbezogenen Eingaben eine Rechtsgrundlage benötigt.  
**Remedium:** In `README.md` einen Abschnitt „Datenschutz / Datenverarbeitung“ aufnehmen:  
> „validkit arbeitet ausschließlich lokal im Arbeitsspeicher. Es speichert, protokolliert oder überträgt keine Eingabedaten. Für personenbezogene Eingaben wie E-Mail-Adressen, Telefonnummern oder IBAN ist der Verwender verantwortlich und muss eine Rechtsgrundlage sicherstellen. Nutzen Sie für Geheimnisse `mask_secret`.“  
Keine Selbstverpflichtung einbauen, die berechtigte Aufrufe blockiert.

**Befund DSGVO-2 (low): `mask_secret` kann kurze Geheimnisse vollständig im Klartext zurückgeben.**  
`mask_secret("kurz", 10)` gibt `"kurz"` zurück; ebenso gibt ein Standardwert `keep=4` bei Passwörtern/PINs ≤ 4 Zeichen den vollen Klartext aus. Das ist im Code so implementiert und in Tests abgesichert, aber als Sicherheitsfunktion missverständlich. Datenschutz durch Technikgestaltung erfordert mindestens klare Dokumentation.  
**Remedium:** In `validkit/mask.py` einen Docstring ergänzen:  
> „Wenn `len(text) <= keep`, wird `text` unverändert zurückgegeben; kurze Geheimnisse können dadurch vollständig sichtbar bleiben. Verwenden Sie `keep=0`, um den gesamten Text zu maskieren.“  
Zusätzlich im README darauf hinweisen. Eine Verhaltensänderung ist wegen AC-08/AC-13 und der Tests nicht ohne Weiteres möglich und wird nicht erzwungen.

## 2. EU Cyber Resilience Act (CRA)

Die CRA-Pflichten gelten vollumfänglich nur, wenn validkit nicht unter die Open-Source-Ausnahme fällt (Art. 2 CRA: unentgeltliche Bereitstellung außerhalb kommerzieller Tätigkeit). Der vorgelegte Stand enthält keine Anzeichen einer kommerziellen Vermarktung; vorsorglich wird die Konformität für den Fall geprüft, dass die Bibliothek in Verkehr gebracht wird.

**Befund CRA-1 (medium): Keine SBOM vorhanden.**  
Art. 13 Abs. 2 CRA verlangt eine Software Bill of Materials, mindestens mit den obersten Abhängigkeiten. Da validkit keine externen Laufzeitabhängigkeiten nutzt, ist die SBOM trivial, fehlt aber im sichtbaren Stand.  
**Remedium:** SBOM im CycloneDX- oder SPDX-Format ergänzen, z. B. `sbom.cdx.json` im Repository. Inhalt: `validkit == 0.1.0`, Runtime-Abhängigkeiten leer, Build-Abhängigkeit `setuptools>=61.0`, Python `>=3.9`. Alternativ `pyproject.toml` um `[tool.cyclonedx]`-Konfiguration ergänzen und Generierung in CI dokumentieren.

**Befund CRA-2 (medium): Keine dokumentierten Sicherheitseigenschaften und kein Schwachstellen-Meldeverfahren.**  
Security by design/default und Meldepflichten setzen dokumentierte Sicherheitsmerkmale und einen klaren Meldeprozess voraus. Sichtbar sind keine `SECURITY.md` und keine Sicherheitsdokumentation.  
**Remedium:** Im Repository `SECURITY.md` anlegen mit:  
- Sicherheitsmerkmalen: keine Netzwerk- oder Datei-I/O, keine dynamische Codeausführung, lineare Algorithmen ohne ReDoS, keine Persistenz, keine Protokollierung, keine externen Laufzeitabhängigkeiten.  
- Abschnitt „Reporting a Vulnerability“ mit Kontakt / Prozess.  
Zusätzlich `README.md` um die Sicherheitseigenschaften ergänzen, damit sie öffentlich sind.

**Befund CRA-3 (low): Update- und Patch-Kanal nicht dokumentiert.**  
Eine Bibliothek wird üblicherweise über PyPI aktualisiert, das ist aber nicht ersichtlich. Für Rückverfolgbarkeit von Updates fehlt zudem eine Paketversion im Code.  
**Remedium:** In `validkit/__init__.py` `__version__ = "0.1.0"` einführen und aus `pyproject.toml` synchron halten. Im `README.md` Veröffentlichung und Upgrade dokumentieren (z. B. `pip install --upgrade validkit`).

## 3. EU AI Act

**Kein Befund.** validkit enthält keine KI-Funktion, kein Modelltraining, keine generative oder klassifizierende KI. Der AI Act ist nicht einschlägig.

## 4. Pflichttexte / Open Source / UI

Keine Endnutzer-UI, daher keine Impressums-, Datenschutzerklärungs-, Cookie- oder Consent-Pflichten. Relevant ist jedoch die Lizenzierung für die Weitergabe.

**Befund OSS-1 (medium): Vollständiger Lizenztext fehlt.**  
`pyproject.toml` enthält nur `license = { text = "MIT" }`. Das ist der Kurzbezeichner, nicht der vollständige MIT-Lizenztext. Eine `LICENSE`-Datei ist in der Branchliste nicht vorhanden. Für die rechtssichere Weitergabe als Open Source ist das unzureichend.  
**Remedium:** Datei `LICENSE` mit dem vollständigen MIT-Lizenztext ergänzen. `pyproject.toml` anpassen, z. B.:  
```toml
license = "MIT"
license-files = ["LICENSE"]
```
(abhängig von der verwendeten setuptools-Version ggf. PEP 639-Format; Mindestanforderung: vollständigen Lizenztext im Repository).

## 5. Barrierefreiheit (WCAG/BITV/EAA)

**Kein Befund.** Keine öffentliche Web-UI, daher nicht anwendbar.

## 6. Produktspezifische Sicherheits- und Robustheitsbefunde

**Befund SEC-1 (low): Widerspruch zwischen AC-13-Beispiel und Implementierung/Test.**  
Die Sprint-Spec nennt `mask_secret('geheim123', 4) == '*****123'`. Die Implementierung und der Test erwarten dagegen korrekt `'*****m123'` (die letzten vier Zeichen). Das wörtliche Spec-Beispiel würde Länge und Maskierung widersprüchlich machen und kann zu Fehlimplementierungen führen.  
**Remedium:** AC-13 im Spec-/README-Kontext auf `mask_secret('geheim123', 4) == '*****m123'` korrigieren. `validkit/mask.py` mit Docstring versehen (siehe DSGVO-2).

**Befund SEC-2 (low): `normalize_phone` akzeptiert negative `country_code`.**  
`normalize_phone("030 1234567", -49)` liefert `"+-49301234567"`. Das ist keine personenbezogene Leckage, aber eine ungültige, irreführende Normalisierung.  
**Remedium:** In `validkit/phone.py` vor der Verarbeitung prüfen:  
```python
if country_code < 0:
    raise ValueError("country_code must be a non-negative integer")
```
Dokumentation/Tests ergänzen.

## Gesamtergebnis

Kein Blocker: Es werden keine personenbezogenen Daten ohne Rechtsgrundlage verarbeitet, gespeichert oder protokolliert; es gibt keine Datenlecks in Logs; keine unzulässige dynamische Codeausführung; keine ReDoS-Muster. Die offenen Punkte sind behebbare Dokumentations- und Konformitätslücken (SBOM, SECURITY.md, Lizenztext, klare Dokumentation der Maskierungsfunktion). Vor einer Veröffentlichung als marktfähiges Produkt mit digitalen Elementen sollten die mittel-schweren Punkte aus CRA-1, CRA-2 und OSS-1 geschlossen werden.
# Erste (Unit)Tests mit Pytest

## Tools
### Pytest: Die Testumgebung
[HowTo für die Installation und erste Schritte](https://docs.pytest.org/en/7.1.x/getting-started.html)

`pip install pytest`

#### Aufruf:
- `pytest`
- oder: `pytest --verbose` bzw. `pytest -v`(mehr Details)
- oder: `pytest <namederTetsdatei>` (führt nur bestimmte Dateien aus)

Wenn Ihr System `pytest` nach der Installation nicht erkennt, versuchen Sie es mit: `python -m ...` also z.B.: `python -m pytest test_meine_Tests.py -v`

### coverage: Tool zur Analyse der Abdeckung
`pip install coverage`

#### Aufruf:
Anweisungsüberdeckung analysieren, indem wir das Ergebnis von pytest an coverage übergeben:
- ``coverage run -m pytest``

Wir können zusätzlich die Zweigüberdeckung analysieren lassen:
- ``coverage run --branch -m pytest``

Abschließend kann man sich das Ergebnis ansehen mit:
-``coverage report`` oder:
- `coverage html` (empfohlen)


## Konventionen
### Dateibenennung
pytest durchsucht alle Dateien mit dem Muster ``test_*.py` nach Testfunktionen.
pytest findet nur Funktionen mit dem Präfix ``test_`` Daraus ergibt sich diese Namenskonvention für Tests:
- ``zieldatei.py``
- ``test_zieldatei.py``
und darin:
    - ``test_nameDerFunktion`` oder besser: 
    - ``test_nameDerFunktion_hinweis_zum_testinhalt``

### Testaufbau
Innerhalb jedes (Unit)Tests sollte das AAA-Muster befolgt werden:
- Arrange (Vorbereitende Maßnamhmen, kann später durch ein pytest.fixture ersetzt werden)
- Act (Tatsächlicher Test)
- Assert (Vergleich der Ergebnisse)
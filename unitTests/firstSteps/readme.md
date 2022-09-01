# Erste (Unit)Tests mit Pytest

## Tools:
### Die Testumgebung
[HowTo für die Installation und erste Schritte](https://docs.pytest.org/en/7.1.x/getting-started.html)

`pip install pytest`

#### Aufruf:
- `pytest`
- oder `pytest --verbose` (mehr Details)

### Tool zur Analyse der Abdeckung
`pip install coverage`

#### Aufruf:
Pytest kann durch coverage aufgerufen werden:
- ``coverage run -m pytest``

Anschließend kann man sich das Ergebnis ansehen mit:
-``coverage report``

Wir können uns auch die Zweigüberdeckung ausgeben lassen:
- ``coverage run --branch -m pytest``
- ``coverage report``


## Konventionen
pytest sucht nach dem Präfix ``test_`` Daraus ergibt sich diese Namenskonvention für Tests:
- ``test_nameDerFunktion``
oder: 
- ``test_nameDerFunktion_hinweisZumTestinhalt``

Innerhalb jedes (UnitTests) sollte das AAA-Muster befolgt werden:
- Arrange (Vorbereitende Maßnamhmen, kann später durch ein pytest.fixture ersetzt werden)
- Act (Tatsächlicher Test)
- Assert (Vergleich der Ergebnisse)
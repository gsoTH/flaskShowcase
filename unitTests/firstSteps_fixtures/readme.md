# Fixtures
Pytest liefert einige Dekoratoren mit, die wir nutzen können, um unsere Tests zu steuern.

Inhalte:
- `@pytest.fixture` gemeinsamer Arrange-Block für alle Tests
- `conftest.py` Fixture in eigene Datei auslagern
- `@pytest.mark.parametrize` Tests mit mehreren Werten durchführen
- `@pytest.mark.skip` Test überspringen
- `@pytest.mark.<eigeneMarkierung>` Tests gruppieren, nur bestimmte Tests ausführen


## @pytest.fixture
Jede Funktion, die so markiert ist, wird vor jedem Testlauf ausgeführt. So können wir einen gemeinsamen Arrange-Block für mehrere Testfälle erschaffen. 
```python
@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):     # input_value ist der Return-Wert von input_value()
   assert input_value % 3 == 0
```

Wenn Fixtures in eine Datei `confest.py` ausgelagert wird, steht sie allen `test_*.py`-Dateien zur Verfügung. Typischerweise wird hier eine Flask-Instanz erstellt und z.B. mit einer Testdatenbank verbunden.

## @pytest.mark.parametrize
Mit dieser Markierung können wir eine Testfunktion mit verschiedenen Parametern aufrufen. In diesem Beispiel erfolgen vier Aufrufe:
```python
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output
```

## @pytest.mark.skip
Verhindert, dass der Test ausgeführt wird. Wird im Testreport als s markiert: `> test_3_weitere_marker.py .FFs` (ein Test erfolgreich, zwei fehlhaft, einer skipped).

Diese Markierung ist sinnvoll, wenn man z.B. Tests schon entworfen ([TDD](https://en.wikipedia.org/wiki/Test-driven_development)), aber Stück für Stück implementieren will.

## Eigene Markierungen
Mit `@pytest.mark.<eigeneMarkierung>` können wir "Tags" bzw. "Kennzeichen" vergeben. So können wir z.B. nur bestimmte Testgruppen ausführen. Aufruf mit `pytest -m <eigeneMarkierung>`. Z.B. führt `pytest -m mussKriterium` nur einen von zwei Tests aus.

```python
@pytest.mark.mussKriterium
def test_greater():
   num = 1
   assert num > 0

@pytest.mark.kannKriterium
def test_greater_equal():
   num = 100
   assert num >= 100
```

## Quellen
[Basiert ~~komplett~~ großteils auf diesem Tutorial](https://www.tutorialspoint.com/pytest/index.htm)
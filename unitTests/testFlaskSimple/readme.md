# Test Flask (Simple)
- Factory-Pattern (aber ohne Import, alle Routen sind in einer Datei)

## Factory-Pattern ohne Import
Das Factory-Pattern ist vor allem nützlich, um Teile der API in eigene Dateien auszulagern ([Beispiel unter examples/simpleFactory](https://github.com/gsoTH/flaskShowcase/tree/master/examples/simpleFactory)). Hier wird es genutzt, um ein Flask-Objekt zu erzeugen, gegen das wir unsere Tests laufen lassen können. Ich habe in solchen Fällen aber ModuleNotFound-Fehler in Pytest, die ich bisher nicht lösen konnte. Lösungsansatz: venv.


TODO: 
    - Testfälle für Tischreservierung aus Anforderungen ableiten
    
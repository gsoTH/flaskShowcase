# Test Flask (Simple)


## Factory-Pattern ohne Import
Hier kommt ein Factory-Pattern zum Einsatz, aber alle Routen sind in einer Datei.

Das Factory-Pattern ist vor allem nützlich, um Teile der API in eigene Dateien auszulagern ([Beispiel unter examples/simpleFactory](https://github.com/gsoTH/flaskShowcase/tree/master/examples/simpleFactory)). Ich habe in solchen Fällen aber ModuleNotFound-Fehler in Pytest, die ich bisher nicht lösen konnte. Lösungsansatz: venv.





TODO: 
    - markers (--> firstSteps?)
    - conftest.py
    - Testfälle für Tischreservierung aus Anforderungen ableiten
    
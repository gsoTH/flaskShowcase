# TestFlask (Simple)
Dieses Beispiel zeigt einen UnitTest, der einen HTTP-GET Request an einer Flask-Instanz testet.


## Factory-Pattern ohne Import
Hier wird ein Factory-Pattern (python Enthusiasten würden es wahrscheinlich als Wrapper bezeichnen) genutzt, um ein Flask-Objekt zu erzeugen, gegen das wir unsere Tests laufen lassen können. Das Factory-Pattern ist in größeren Projektennützlich, um Teile der API in eigene Dateien auszulagern und den Code damit zu strukturieren([Beispiel unter examples/simpleFactory](https://github.com/gsoTH/flaskShowcase/tree/master/examples/simpleFactory)). Z.B. könnten bestimmte Routen in eine eigene Datei ausgelagert werden.

Ich habe in solchen Fällen aber ModuleNotFound-Fehler in Pytest, die ich bisher nicht lösen konnte. Falls Sie eine Idee haben, bitte ich um Nachricht :)

## return vs. yield
Statt `return app.test_client()` könnten wir `yield app.test_client()` einsetzen. Das setzt allerdings Wissen zu [Generator Functions](https://realpython.com/introduction-to-python-generators/) voraus, weshalb ich `return` nutze, um Lernhürden zu minimieren.
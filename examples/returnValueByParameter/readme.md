# return Value By Parameter
In diesem [Beispiel](returnValueByParameter.py) werden Zitate aus einer Datenbank als JSON ausgegeben.
- request nutzen um Parameter aus GET entgegenzunehmen
- Spruch aus einer Datenbank abfragen
- json manuell zusammenbauen

## JSON erzeugen
[JSON](https://de.wikipedia.org/wiki/JavaScript_Object_Notation) ist im Kern nur ein String (Zeichenkette) mit genormter Syntax. Wir können ein JSON manuell zusammenbauen, indem wir einen String zusammensetzen. Z.B.
```python
s = '{ "schlüssel":"wert" }'
```
oder auch so:
```python
key = 'schlüssel'
value = 'wert'
s = '{ "' + key + '":"' + value + '" }'
```
Der Inhalt von s ist in beiden Fällen identisch. Beachten Sie bitte den Einsatz von ' und ". Der String beginnt mit ', weshalb alles zwischen ' als literaler Wert übernommen wird.

Es gibt es zahlreiche Module, die uns die Arbeit mit JSON erleichtern. Im Kern machen diese alle das gleiche: Informationen so umformen, dass sie als JSON gültig sind. Einige Beispiel: 
- [jsonify - in Flask üblich](https://www.educba.com/flask-jsonify/)
- [json - in python integriert](https://www.w3schools.com/python/python_json.asp)



## Schwachstellen
- Pfad der Datenbank ist mehrfach im Code vorhanden --> In Config-Datei auslagern?
- Datenbank ist ziemlich fix in API eingebaut --> weitere Ebenen der Abstraktion einführen?
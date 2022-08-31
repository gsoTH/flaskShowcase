# FLASK Showcase
Flask maps HTTP requests to Python functions.

Quellen:
- [Erste Schritte (API aufsetzen, Verbindung zur DB, Queries via HTTP entgegennehmen)](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#setting-up "programminghistorian.org")
- [Post-Schnittstelle mit JSON](https://pythonise.com/series/learning-flask/working-with-json-in-flask)
- [QuickStart Dokumentation mit einem guten Überblick über die Struktur von Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)


### Why Flask?

Python has a number of web frameworks that can be used to create web apps and APIs. The most well-known is Django, a framework that has a set project structure and which includes many built-in tools. This can save time and effort for experienced programmers, but can be overwhelming. Flask applications tend to be written on a blank canvas, so to speak, and so are more suited to a contained application such as our prototype API.




## Offene Fragen
- Wie funktioniert ein paralleler Mehrnutzerbetrieb? Docker o.ä.?
- API Design Principles
    - Versionierung von APIs um neue Funktionen entwickeln zu können, ohne bisherige API einzustellen.
    - Reifegrad o.ä.? Worauf ist zu achten?
- Wie sollte die API dokumentiert werden?
    - [Positivbeispiel Weltbank](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-api-documentation)
  

## Examples
Der Order /examples enthält Beispiele für verschiedene Funktionen.

| Skript        | Beschreibung                                                          |
|---------------|-----------------------------------------------------------------------|
| helloWorld.py | Ein Minimalbeispiel für einen laufenden Flask-Server. 10 Zeilen Code.|
| random_404.py | Errorhandling. Hier wird ein zufälliger Text für HTTP-404-Fehler zurückgegeben.|
| returnValueByParameter | Request abfragen, JSON manuell zusammenbauen und zurückgeben |
| returnTemplate | Einsatz von Templates, um html-Seiten mit Werten aus einer Datenbank zu füllen |
| simpleFactory | Verteilen von Routen (o.ä.) über mehrere Dateien |

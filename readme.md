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
  
## Begriffe
- A python module is a single file with a .py extension.
- A python package is a folder that contains at least one python module. For python2, a package requires a __init__.py file
- A python package can contain any number of nested sub-packages, i.e. packages that contain other packages down the hierarchy of the project - structure.
- imports are useful when a module needs to use some piece of functionality (e.g. a function or a class) written in another module (of the same or a different package or sub-package)

[Quelle](https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c>)

## Ordner
api: Meine ersten Versuche mit Flask; Gerne ignorieren :)
Examples:  Beispiele für verschiedene Funktionen, Tipps, Tricks
unitsTests: Alles zum Thema automatisiertes Testen mit Flask



# TestFlask (with Payload)

Dieses Beispiel ist eine Erweiterung von [TestFlaskSimple](https://github.com/gsoTH/flaskShowcase/tree/master/unitTests/testFlaskSimple). Es existieren nun Tests mit Argumenten und JSON.

Wesentliche Informationen stammen aus dieser Dokumentation zu [Flask Testing.](https://flask.palletsprojects.com/en/2.2.x/testing/)

## Arrange
Der folgende Block bereit zwei Variablen vor, die in beiden Tests genutzt werden. 

`route` enthält den Pfad zum API-Endpoint.
``payload` enthält ein python-Dictionary, mit Werten die an unsere API übergeben werden sollen.
```python
route = "/person"
payload = {
    "vorname": "Bud",
    "nachname": "Spencer"
}
```

## Act 
In diesen Tests werden Daten an Flak übergeben, indem wir HTTP-POST simulieren. Das geht mit:
```python
test_client.post(path  [,query_string]  [, json])
```
- `path` der API-Endpoint. Wir würden dies auch Route nennen.
- `query_string` [optional] setzt die Inhalte eines Dicts hinter das ? in der URL.
- `json` [optional] wandelt ein Dict vor der Übergabe in ein json um.


### Beispiele
- Ob `query_string` oder `json` genutzt werden soll geben wir an, indem wir den Parameter benennen und ein Dict zuweisen, z.B. payload aus Assert.

```pyton
response = app.post(path = route, query_string = payload)
```

```python
response = app.post(path = route, json=payload)
```


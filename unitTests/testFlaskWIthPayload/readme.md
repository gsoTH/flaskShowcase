# TestFlask (with Payload)

Dieses Beispiel ist eine Erweiterung von [TestFlaskSimple](https://github.com/gsoTH/flaskShowcase/tree/master/unitTests/testFlaskSimple). Es existieren nun Tests mit Argumenten und JSON.

Wesentliche Informationen stammen aus dieser Dokumentation zu [Flask Testing.](https://flask.palletsprojects.com/en/2.2.x/testing/)

## Arrange
Der folgende Block bereit zwei Variablen vor, die in beiden Tests genutzt werden. 

`route` enthält den Pfad zum API-Endpoint.
``payload` enthält ein python-Dictionary, mit Werten die an unsere API übergeben werden sollen.
```python
route = "/persons"
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

## Assert
Die `response` des **ersten** Tests sieht so aus:
```
[
    {
        'nachname': 'Hill', 
        'vorname': 'Terrence'
    }
]
```

- `.get_json()[0]` greift auf den ersten Eintrag zu: `
    ```
    {
        'nachname': 'Hill', 
        'vorname': 'Terrence'
    }
    ```
    Die Formatierung ist bei JSON egal. Daher ist der obige Eintrag identisch zu: 
    ```
    {'nachname': 'Hill', 'vorname': 'Terrence'}
    ```
- mit `.get_json()[0]["vorname"]` würden wir dieses Ergebnis erhalten:
    ```
    Terrence
    ```

**Nach** dem zweiten Test sieht die Response so aus:
```
[
    {
        'nachname': 'Hill', 
        'vorname': 'Terrence'
    }, 
    {
        'nachname': 'Spencer', 
        'vorname': 'Bud'
    }
]
```

Und `.get_json()[1]` greift auf den zweiten Eintrag zu: `
```
{
    'nachname': 'Spencer', 
    'vorname': 'Bud'
}
```

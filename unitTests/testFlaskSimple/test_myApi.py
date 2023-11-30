import pytest
from myAPI import create_app


@pytest.fixture                                         # pytest führt diese Funktion vor jedem Testlauf durch; Entspricht # Arrange
def app():                                              # Häufig in conftest.py ausgelagert
    app = create_app()
    app.config['TESTING'] = True                        # Vereinfacht das Debugging. Ermöglicht z.B. ausführliche Fehlermeldungen.
    
    #yield app.test_client()                            # Könnte statt return genutzt werden
    return app.test_client()                            # Erzeugt einen TestClient, gegen den wir Tests ausführen können,
                                                        # ohne vorher einen Server zu starten.


def test_hello_world(app):
    route = "/"                                         # Arrange

    response = app.get(route)                           # Ergebnis eines HTTP-GET-Requests speichern

    assert response.status_code == 200
    assert b"<h1>Hello, World!</h1>" in response.data   # b wandelt den string in bytecode um, sonst Typfehler
    

def test_hello_world__with_arguments(app):
    route = "/"
    payload = {                                                 # Python-Dictionary
        "vorname": "Bud",
        "nachname": "Spencer"
    }
    
    response = app.get(path = route, query_string = payload)   # query_string setzt die Inhalte eines Dicts hinter das ? in der URL
                                                               # entspricht hier : GET /?vorname=Bud&nachname=Spencer

    assert response.status_code == 200
    assert b"Hello, Bud Spencer" in response.data

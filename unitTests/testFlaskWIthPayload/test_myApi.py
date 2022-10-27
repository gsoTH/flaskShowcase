import pytest
from myAPI import create_app


@pytest.fixture                                         # pytest führt diese Funktion vor jedem Testlauf durch; Entspricht # Arrange
def app():                                              # Häufig in conftest.py ausgelagert
    app = create_app()
    app.config['TESTING'] = True
    
    #yield app.test_client()                            # Unterschied zu return unklar
    return app.test_client()


def test_hello_world(app):
    response = app.get("/")                             # Ergebnis eines HTTP get-Requests speichern
    assert response.status_code == 200
    assert b"<h1>Hello, World!</h1>" in response.data   # b wandelt den string in bytecode um, sonst Typfehler


def test_hello_person_arguments(app):                           # https://flask.palletsprojects.com/en/2.2.x/testing/
    route = "/person"
    payload = {
        "vorname": "Bud",
        "nachname": "Spencer"
    }
    
    response = app.post(path = route, query_string = payload)   # query_string setzt die Inhalte eines Dicts hinter das ? in der URL

    assert response.status_code == 200
    assert b"Hello, Bud Spencer" in response.data


def test_hello_person_json(app):
    route = "/person/json"
    payload = {
        "vorname": "Bud",
        "nachname": "Spencer"
    }
    
    response = app.post(path = route, json=payload)             # json wandelt ein Dict in ein json um

    assert response.status_code == 200
    assert b"Hello, Bud Spencer" in response.data
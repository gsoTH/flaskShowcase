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

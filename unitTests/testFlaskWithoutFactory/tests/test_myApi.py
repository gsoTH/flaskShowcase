import pytest
# from src.myApp import myAPI
from src.myApp.myAPI import create_app

@pytest.fixture
def app():
    """The @pytest.fixture annotation tells pytest that the following function creates (using the yield command) an app for testing. 
    import later: from test.unit.webapp import client
    Sets app config variable ``TESTING`` to ``True``
    :return: App for testing
    """
    app = create_app()
    app.config['TESTING'] = True
    
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Hello, World!</h1>" in response.data

def test_gibtsNicht(client):
    response = client.get("/gibtsNicht")
    assert response.status_code == 404
    assert b"<h1>Hello, World!</h1>" not in response.data
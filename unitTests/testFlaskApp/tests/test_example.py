import pytest
#import example
#import exampleApp
#from exampleApp import example
#import testFlaskApp.exampleApp.example

#from ..exampleApp import example

from exampleApp import create_app
#import create_app

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

def test_hello_world():
    assert 1 == 1

def test_hello_world(client):
    response = client.get("/")
    assert b"<h1>Hello, World!</h1>" in response.data

""" @pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_hello_world(client):
    response = client.get("/")
    assert b"<h1>Hello, World!</h1>" in response.data """
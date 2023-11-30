import pytest
from myAPI import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    
    #yield app.test_client()
    return app.test_client()


def test_persons_get(app):
    route = "/persons"
    
    response = app.get(route)

    assert response.status_code == 200
    assert response.get_json()[0] == {'nachname': 'Hill', 'vorname': 'Terrence'}


def test_persons_post(app):
    route = "/persons"
    payload = {
        "vorname": "Bud",
        "nachname": "Spencer"
    }
    
    response = app.post(path = route, json=payload)             # json wandelt ein Dict in ein json um
                                                                # nicht verwechsleln mit "query_string = payload"
                                                                # siehe readme.md

    assert response.status_code == 200
    assert response.get_json()[1] == payload                    # Verstoß gegen FIRST-Prinzip!
                                                                # response.get_json()[1] nur korrekt, wenn Testreihenfolge fix
                                                                # Tests daher nicht isoliert ausführbar
                                                                # besser: response.get_json()[len(response.get_json())-1]


@pytest.mark.parametrize("payload", [                           # siehe /unitTests/firstSteps_fixtures
    {"vorname": "Bud"},
    {"nachname": "Spencer"},
    {"v": "Bud", "n": "Spencer"},
])
def test_persons_post__fehlerhaftes_json_wirft_Fehler(app, payload): 
    route = "/persons"
    
    response = app.post(path = route, json=payload)
    
    assert response.status_code == 400
    
# Unit Tests

## Vorausetzungen und Orga
```python
$ pip install pytest coverage
```
 Code in functions only runs when the function is called, and code in branches, such as if blocks, only runs when the condition is met. You want to make sure that each function is tested with data that covers each branch.

The test code is located in the tests directory. The tests/conftest.py file contains setup functions called fixtures that each test will use. Tests are in Python modules that start with test_, and each test function in those modules also starts with test_. [Quelle][1]

Pytest fixtures allow writing pieces of code that are reusable across tests.

The test client makes requests to the application without running a live server. Flask’s client extends Werkzeug’s client, see those docs for additional information.
The client has methods that match the common HTTP request methods, such as client.get() and client.post(). They take many arguments for building the request; you can find the full documentation in EnvironBuilder. Typically you’ll use path, query_string, headers, and data or json.

```python
def test_request_example(client):
    response = client.get("/posts")
    assert b"<h2>Hello, World!</h2>" in response.data
```

```python
def test_json_data(client):
    response = client.post("/graphql", json={
        "query": """
            query User($id: String!) {
                user(id: $id) {
                    name
                    theme
                    picture_url
                }
            }
        """,
        variables={"id": 2},
    })
    assert response.json["data"]["user"]["name"] == "Flask"
```
 [Quelle][2]

## Quellen
[1]: https://flask.palletsprojects.com/en/2.2.x/tutorial/tests/
[2]: https://flask.palletsprojects.com/en/2.2.x/testing/


from flask import Flask


def init_app(app):                          # Normalerweise in eigene Datei ausgelagert, aber Pytest wirft bei mir Import-Fehler :(
    @app.route("/")
    def hello_world():
        return "<h1>Hello, World!</h1>"


def create_app():                           # Factory Pattern
    app = Flask(__name__)
    
    init_app(app)                           # Fügt app die Route für hello_world hinzu

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

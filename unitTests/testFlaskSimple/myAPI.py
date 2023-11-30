from flask import Flask, request


def init_app(app):                                  # Normalerweise in eigene Datei ausgelagert, aber Pytest wirft bei mir Import-Fehler :(

    @app.route("/", methods=['GET'])                # GET ist default, muss nicht angegeben werden
    def hello_person():                             # POST muss explizit angegeben werden, sonst 405
        vorname = request.args.get("vorname")
        nachname = request.args.get("nachname")
        
        result = "<h1>Hello, World!</h1>"
        
        if vorname and nachname:
            result = "<h1>Hello, " + vorname + " " + nachname + "</h1>"            
        
        return result, 200


def create_app():                           # Factory Pattern
    app = Flask(__name__)
    
    init_app(app)                           # Fügt app die Route für hello_world hinzu

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

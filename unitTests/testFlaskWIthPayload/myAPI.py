from flask import Flask
from flask import request


def init_app(app):                          # Normalerweise in eigene Datei ausgelagert, aber Pytest wirft bei mir Import-Fehler :(
    @app.route("/")
    def hello_world():
        return "<h1>Hello, World!</h1>"

    @app.route("/person", methods=['GET','POST'])   # GET ist standard, ermöglicht Test via Browser, z.B. http://127.0.0.1:5000/person?vorname=Bud&nachname=Spencer
    def hello_person():                             # POST muss explizit angegeben werden, sonst 405
        vorname = request.args.get("vorname")
        nachname = request.args.get("nachname")
        
        greeting = "<h1>Hello, " + vorname + " " + nachname + "</h1>"
        
        return greeting, 200


    @app.route("/person/json", methods=['POST'])
    def hello_person_json():
        vorname = request.json.get("vorname")
        nachname = request.json.get("nachname")
        
        greeting = "<h1>Hello, " + vorname + " " + nachname + "</h1>"
        
        return greeting, 200


def create_app():                           # Factory Pattern
    app = Flask(__name__)
    app.config["DEBUG"] = True              # Niemals in Produktivumgebungen!
    
    init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

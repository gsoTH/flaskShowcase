from flask import Flask
from flask import request, jsonify, json


def init_app(app):                          # Normalerweise in eigene Datei ausgelagert, aber Pytest wirft bei mir Import-Fehler :(

    people_data = [                         # Python dictionary entspricht JSON-Struktur
            {
                "vorname": "Terrence",
                "nachname": "Hill"
            }
    ]

    @app.route("/persons", methods=['GET'])
    def get_all_persons():
        return jsonify(people_data), 200


    @app.route("/persons", methods=['POST'])
    def create_new_person():
        vorname = request.json.get("vorname")
        nachname = request.json.get("nachname")
        
        if(vorname and nachname):
            people_data.append({"vorname":vorname, "nachname":nachname})
        
        return  get_all_persons()


def create_app():                           # Factory Pattern
    app = Flask(__name__)
    app.config["DEBUG"] = True              # Niemals in Produktivumgebungen!
    
    init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

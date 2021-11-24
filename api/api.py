import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = true

@app.route('/', methods=['GET'])
def home():
        return "<h1>FLASK Showcase</h1><p>Diese Seite ist eine Testumgebung zur Entwicklung eines Web-Backends mit Python und Flask.</p>"

app.run()
def initialisieren(instance): # Der Verweis auf die Flask-Instanz wird übergeben

    @instance.route("/") # Flask-Instanz erhält eine neue Route
    def hello_world():
        return "<h1>Hello, World!</h1>"

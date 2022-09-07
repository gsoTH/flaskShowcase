from flask import Flask


def init_app(app):
    
    @app.route("/")
    def hello_world():
        return "<h1>Hello, World!</h1>"


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    
    init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

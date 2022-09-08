from flask import Flask
import ausgelagerteRoute                        # macht ausgelagerteRoute.py verfügbar


def create_app():                               # Factory-Pattern

    instance = Flask(__name__)                  # Statt instance steht hier üblicherweise app
                                                # beides bezeichnet eine Instanz von Flask, also den gestarteten Server

    ausgelagerteRoute.initialisieren(instance)  # Auslagern nicht zwingend nötig, aber ohne Factory-Pattern unmöglich

    return instance


if __name__ == "__main__":
    app = create_app()
    app.run()
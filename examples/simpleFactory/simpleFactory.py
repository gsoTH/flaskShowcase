from flask import Flask
import ausgelagerteRoute # Hier wird der Inhalt von ausgelagerteRoute.py verfügbar gemacht

instance = Flask(__name__)
# Statt instance steht hier üblicherweise app
# beides bezeichnet eine Instanz von Flask, also den gestarteten Server

ausgelagerteRoute.initialisieren(instance)


if __name__ == "__main__":
    instance.run()
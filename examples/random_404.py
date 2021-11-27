from flask import Flask
import random

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):

    errorMessageList = ["Whoops, this page doesn't exist.",
                        "There's nothing here.",
                        "There's been a glitch",
                        "404 - Feel free to dance your frustration off",
                        "Four hundred and fourth message of error"]

    return "<h1>404</h1><p>The resource could not be found.</p>", 404



if __name__ == "__main__":
    app.run()
from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

@app.route("/")
def index():
    aktuellerSpruch, aktuelleQuelle = getSpruch();
    return render_template('index.html', spruch = aktuellerSpruch, quelle = aktuelleQuelle)

def getSpruch(nummer: int = 1):
    query = "SELECT spruch, quelle FROM zitate WHERE nr = "
    query = query + str(nummer)

    conn = sqlite3.connect('./giganten.sqlite')
    results = conn.execute(query).fetchone()

    return results[0], results[1]



if __name__ == "__main__":
    app.run()



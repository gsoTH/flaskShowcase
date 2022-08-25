from flask import Flask, request, render_template
import sqlite3
import random


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    query_parameters = request.args
    spruchNr = query_parameters.get('nr') #Aufruf mit http://127.0.0.1:5000/?nr=11
    
    if spruchNr: 
        aktuellerSpruch, aktuelleQuelle = getSpruch(spruchNr)
    else:
        aktuellerSpruch, aktuelleQuelle = getRandomSpruch()
    
    return render_template('index.html', spruch = aktuellerSpruch, quelle = aktuelleQuelle)


def getAnzahlSprueche():
    query = "SELECT count(*) FROM zitate"

    conn = sqlite3.connect('./giganten.sqlite')
    result = conn.execute(query).fetchone()

    return int(result[0]) #Ohne [0] --> TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'

def getRandomSpruch():
    anzahlSprueche = getAnzahlSprueche()
    zufallsNummer = random.randrange(1, anzahlSprueche)

    spruch = getSpruch(zufallsNummer)

    return spruch[0], spruch[1]


def getSpruch(nummer: int):
    query = "SELECT spruch, quelle FROM zitate WHERE nr = "
    query = query + str(nummer)

    conn = sqlite3.connect('./giganten.sqlite')
    results = conn.execute(query).fetchone()

    return results[0], results[1]



if __name__ == "__main__":
    app.run()



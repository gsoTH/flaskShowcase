from flask import Flask, request
import sqlite3
import random


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    query_parameters = request.args
    spruchNr = query_parameters.get('nr') #Aufruf mit http://127.0.0.1:5000/?nr=11
    
    if spruchNr: 
        spruch = getSpruch(spruchNr)
    else:
        spruch = getRandomSpruch()
    
    return spruch

def getAnzahlSprueche():
    query = "SELECT count(*) FROM zitate"

    conn = sqlite3.connect('./giganten.sqlite')
    result = conn.execute(query).fetchone()

    return int(result[0]) #Ohne [0] --> TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'

def getRandomSpruch():
    anzahlSprueche = getAnzahlSprueche()
    zufallsNummer = random.randrange(1, anzahlSprueche + 1) #randrange(von, bis) --> bis ist exklusiv

    spruch = getSpruch(zufallsNummer)
    
    return spruch


def getSpruch(nummer: int):
    query = "SELECT nr, spruch, quelle FROM zitate WHERE nr = "
    query = query + str(nummer)

    conn = sqlite3.connect('./giganten.sqlite')
    result = conn.execute(query).fetchone()

    # Wir bauen uns ein json zusammen:
        # result ist ein Tupel mit 3 Feldern (= Anzahl Spalten, die abgefragt wurden)
        # das erste Feld hat den Index 0
    spruch = '{"nr":"' + result[0] + '", "spruch":"' + result[1] + '", "quelle":"' + result[2] + '"}'

    return spruch 



if __name__ == "__main__":
    app.run()



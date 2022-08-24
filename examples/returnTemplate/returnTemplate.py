from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    aktuellerSpruch = getSpruch();
    return render_template('index.html', spruch = aktuellerSpruch, quelle = "")

def getSpruch():
    return "Nun guck‘ ihn dir an, hat auch nicht mehr Hirn als ’n Spatz Fleisch an der Kniescheibe.";

if __name__ == "__main__":
    app.run()



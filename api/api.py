import flask
from flask import jsonify
from flask import request
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True #Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message

@app.route('/', methods=['GET'])
def home():
        return "<h1>FLASK Showcase</h1><p>Diese Seite ist eine Testumgebung zur Entwicklung eines Web-Backends mit Python und Flask.</p>"

# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_id():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."
#
#     # Create an empty list for our results
#     results = []
#
#     # Loop through the data and match results that fit the requested ID.
#     # IDs are unique, but other fields might return many results
#     for book in books:
#         if book['id'] == id:
#             results.append(book)
#
#     # Use the jsonify function from Flask to convert our list of
#     # Python dictionaries to the JSON format.
#     return jsonify(results)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/api/v1/chinook/customers/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('../chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_customers = cur.execute('SELECT * FROM customers;').fetchall()

    return jsonify(all_customers)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/chinook/customers', methods=['GET'])
def api_filter():
    query_parameters = request.args

    CustomerId = query_parameters.get('CustomerId')
    LastName = query_parameters.get('LastName')
    Country = query_parameters.get('Country')

    query = "SELECT * FROM customers WHERE"
    to_filter = []

    if CustomerId:
        query += ' CustomerId=? AND'
        to_filter.append(CustomerId)
    if LastName:
        query += ' LastName=? AND'
        to_filter.append(LastName)
    if Country:
        query += ' Country=? AND'
        to_filter.append(Country)
    if not (CustomerId or LastName or Country):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('../chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()

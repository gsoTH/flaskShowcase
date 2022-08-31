import sqlite3


# def dict_factory(cursor, row):
#     d = {}  # Sets {} are used to store multiple items in a single variable.
#             # Unordered, Unique Entries, Unchangeable
    
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d


# def start2():
#     conn = sqlite3.connect('../chinook.db')
#     conn.row_factory = dict_factory
#     all_customers = conn.execute('SELECT * FROM customers;').fetchall()

#     return jsonify(all_customers)


def createInMemoryDatabase():
    connection = sqlite3.connect(":memory:") #connection repräsentiert die Verbindung zur Datenbank
    
    # Mit """ können mehrzeilige Strings erzeugt werden.
    query = """ CREATE TABLE zitate (
                    nr integer,
                    zitat text,
                    quelle text,
                    PRIMARY KEY (nr)
                )
            """
    
    connection.execute(query)
    connection.commit()

    return connection

#todo: cursor einfügen
def insertExampleData(connection: sqlite3.Connection):
    data = [
        (1, "Monty Python Live at the Hollywood Bowl", "1"),
        (2, "Monty Python's The Meaning of Life", "2"),
        (3, "Monty Python's Life of Brian", "3"),
    ]
    connection.executemany("INSERT INTO zitate VALUES(?, ?, ?)", data)
    connection.commit()  # Remember to commit the transaction after executing INSERT.= 


def start():
    connection = createInMemoryDatabase()
    insertExampleData(connection)


if __name__ == "__main__":
    start()
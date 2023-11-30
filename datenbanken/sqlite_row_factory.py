#
#   Quellen:
#   1 https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory
#   2 https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#connecting-our-api-to-a-database
#
#   Beispiele, wie die Rückaben von SQL-Abfragen in Python-Typen umgewandelt werden.
#   --> By default, sqlite3 represents each row as a tuple.
#   --> If a tuple does not suit your needs, you can use the sqlite3.Row class or a custom row_factory.

import sqlite3

con: sqlite3.Connection = sqlite3.connect(":memory:")
create_sql: str = """
    CREATE TABLE test(
        id          INTEGER
    ,   vorname     TEXT
    ,   nachname    TEXT
    ,   PRIMARY KEY(id)
    );
    
    INSERT INTO test VALUES 
        (1, 'Donald','Duck')
    ,   (2, 'Mickey','Maus')
    ,   (3, 'Balou', 'Bär' )
    ;
"""
con.executescript(create_sql)



sql: str = "SELECT * FROM test"

# Quelle: 1
# By default, sqlite3 represents each row as a tuple.
# row_factory auf default Wert setzen
# Jede Row wird nun als Python-Tuple ausgegeben
cursor: sqlite3.Cursor = con.execute(sql)
cursor.row_factory = None
print(cursor.fetchall())

# Ergebnis:
#   [
#       (1, 'Donald', 'Duck'),
#       (2, 'Mickey', 'Maus'),
#       (3, 'Balou', 'Bär')
#   ]


# Quelle: 1
# If a tuple does not suit your needs, you can use the sqlite3.Row class or a custom row_factory.
def dict_factory(cursor, row) -> dict:
    """returns each row as a dict, with column names mapped to values"""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

cursor: sqlite3.Cursor = con.execute(sql)
cursor.row_factory = dict_factory
print(cursor.fetchall())

# Ergebnis:
#   [
#       {'id': 1, 'vorname': 'Donald', 'nachname': 'Duck'},
#       {'id': 2, 'vorname': 'Mickey', 'nachname': 'Maus'},
#       {'id': 3, 'vorname': 'Balou', 'nachname': 'Bär'}
#   ]


# Quelle: 2
def dict_factory_short(cursor, row) -> dict:
    """returns each row as a dict, with column names mapped to values"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

cursor: sqlite3.Cursor = con.execute(sql)
cursor.row_factory = dict_factory_short
print(cursor.fetchall())

# Ergebnis:
#   [
#       {'id': 1, 'vorname': 'Donald', 'nachname': 'Duck'},
#       {'id': 2, 'vorname': 'Mickey', 'nachname': 'Maus'},
#       {'id': 3, 'vorname': 'Balou', 'nachname': 'Bär'}
#   ]
import sqlite3

def mapped_fields(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# this returns a dictionary with field names as keys, mapped to values
CONN = sqlite3.connect("melons.db")
CONN.row_factory = mapped_fields
cursor = CONN.cursor()
cursor.execute("select * from customers where id = 1")
print cursor.fetchone()


# if row 11 above is replaced by this, returns just the row values as a tuple
CONN.row_factory = sqlite3.Row

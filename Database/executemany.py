import sqlite3 as sql
people_values = (
        ("Ron", "Obvious", 42),
        ("Luigi", "Vercotti", 43),
        ("Arthur", "Belling", 28)
)

with sql.Connection('learn.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
    print(cur.execute('SELECT * FROM People;').fetchall())

import sqlite3 as sql
with sql.Connection('learn.db') as connection:
    cur = connection.cursor()
    res = cur.execute('select * from People;').fetchone()
    print(res)

import sqlite3 as sql

with sql.connect('learn.db') as connection:
    cursor = connection.cursor()

    # Create the Table
    table = '''CREATE TABLE People(
        FirstName varchar(50),
        LastName varchar(20),
        Age int
    )'''
    cursor.execute(table)

    # Add Data into the table
    cursor.execute('''
    INSERT INTO People VALUES (
    'Alex',
    'White',
    29
    )
    ''')

    # See the data
    res = cursor.execute('SELECT * FROM People').fetchone()
    print(res)

    # Commit the changes
    connection.commit()


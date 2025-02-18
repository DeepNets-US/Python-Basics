import sqlite3 as sql

# Initialize the Connection
connection = sql.connect(':memory:')

# Check the Type of the connection
print(f'Type of Connection: {connection}')

# Start the Cursor
cursor = connection.cursor()

# Check the Type
print(f'Type of Cursor: {cursor}')

# Execute Queries
query = "SELECT datetime('now', 'localtime');"
print(f'\nUser Query: {query}')
print(cursor.execute(query))

# Fetch the Query
print('\nQuery Output:')
print(cursor.fetchone())


# Close the Connection
connection.close()

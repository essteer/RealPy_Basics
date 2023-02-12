import sqlite3

# connection = sqlite3.connect(":memory:")  # to create an in-memory database

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    results = cursor.execute(query)
    row = results.fetchone()
    time = row[0]

# time
# returns '2023-01-03 21:09:06'

import sqlite3

#1
with sqlite3.connect(":memory:") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute("""
        CREATE TABLE Roster(
            Name TEXT,
            Species TEXT,
            Age INT
        );""")

    # 2
    values = (
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    )
    cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", values)
    # print("Test print for #2:")
    # cursor.execute("SELECT Name, Species, Age FROM Roster")
    # for row in cursor.fetchall():
    #     print(row)

    #3
    cursor.execute(
        "UPDATE Roster SET Name=? WHERE Name=?;",
        ('Ezri Dax', 'Jadzia Dax')
    )
    # print("Test print for #3:")
    # cursor.execute("SELECT Name, Species, Age FROM Roster")
    # for row in cursor.fetchall():
    #     print(row)

    #4
    cursor.execute(
        "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';"
    )
    for row in cursor.fetchall():
        print(row)

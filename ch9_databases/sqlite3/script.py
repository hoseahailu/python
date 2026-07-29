import sqlite3
# print(sqlite3.sqlite_version)

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE Players(
#     id INTEGER PRIMARY KEY,
#     username TEXT,
#     coins INTEGER
# )
# """)

# cursor.execute("""
# INSERT INTO Players(username, coins)
# VALUES (?, ?)
# """, ("Steve", 500))

# connection.commit()

# players = [
#     ("Steve", 500),
#     ("Alex", 1000),
#     ("Tim", 250)
# ]

# cursor.executemany("""
# INSERT INTO Players(username, coins)
# VALUES (?, ?)
# """, players)

# cursor.execute("""
# INSERT INTO Players(id, username, coins)
# VALUES (?, ?, ?)
# """, (5, "Steve", 500))

# cursor.execute("SELECT * FROM Players")
# rows = cursor.fetchall()
# print(rows)

# you can add id,coins or * to list one,two or all the colloums

# cursor.execute("""
# SELECT * FROM Players 
# WHERE username=?
# """, ("Steve",))

# print(cursor.fetchall())

# cursor.execute("SELECT * FROM Players")

# for row in cursor.fetchall():
#     print(row)

# cursor.execute("SELECT * FROM Players")

# print(cursor.fetchone())


# cursor.execute("SELECT * FROM Players")

# print(cursor.fetchmany(5))

# cursor.execute("""
# UPDATE Players
# SET coins=1000
# WHERE username=?
# """, ("Steve",))

# cursor.execute("""
# UPDATE Players
# SET username=?, coins=?
# WHERE id=?
# """, ("Bob", 900, 1))

# cursor.execute("""
# DELETE FROM Players
# WHERE username=?
# """, ("Steve",))

# cursor.execute("""
# DELETE FROM Players
# WHERE coins < ?
# """, (500,))

# cursor.execute("""
# DELETE FROM Players
# """)

rows = cursor.execute("""
SELECT *
FROM Players
ORDER BY coins DESC
""")

print(rows.fetchall())

connection.commit()
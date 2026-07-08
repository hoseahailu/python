import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE Students(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER
# )
# """)

# connection.commit()

# cursor.execute("""
# INSERT INTO Students(name, age)
# VALUES (?, ?)
# """, ("Hanan", 11))

# connection.commit()

# cursor.execute("""
# CREATE TABLE Students(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER
# )
# """)

# connection.commit()

# cursor.execute("""
# INSERT INTO Students(name, age)
# VALUES (?, ?)
# """, ("Hanan", 11))

# connection.commit()

cursor.execute("SELECT * FROM Students")

rows = cursor.fetchall()

print(rows)
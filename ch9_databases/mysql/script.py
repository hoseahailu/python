import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="crud_db"
)

cursor = connection.cursor(dictionary=True)

# cursor.execute("CREATE DATABASE IF NOT EXISTS crud_db")

# print("Database created!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
)
""")

cursor.close()
connection.close()
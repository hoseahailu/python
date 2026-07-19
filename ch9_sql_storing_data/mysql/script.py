import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234"
)

cursor = connection.cursor(dictionary=True)

# cursor.execute("CREATE DATABASE IF NOT EXISTS crud_db")

# print("Database created!")

cursor.close()
connection.close()
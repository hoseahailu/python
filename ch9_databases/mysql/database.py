import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="crud_db"
)

cursor = db.cursor(dictionary=True)
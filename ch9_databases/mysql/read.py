from database import db, cursor

cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

for user in users:
    print(user)

cursor.close()
db.close()
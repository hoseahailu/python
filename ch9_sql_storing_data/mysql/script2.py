# ==========================================
# Python CRUD Example Using MySQL
# ==========================================

import mysql.connector


# ==========================================
# Connect to MySQL Database
# ==========================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="crud_db"
)

cursor = db.cursor(dictionary=True)


# ==========================================
# CREATE (Insert Data)
# ==========================================

def create_user(name, email):
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)

    cursor.execute(sql, values)
    db.commit()

    print(f"User created successfully!")
    print(f"Inserted ID: {cursor.lastrowid}")


# ==========================================
# READ ALL (Get Every User)
# ==========================================

def get_users():
    sql = "SELECT * FROM users"

    cursor.execute(sql)

    users = cursor.fetchall()

    if users:
        print("\nAll Users:")
        for user in users:
            print(user)
    else:
        print("No users found.")


# ==========================================
# READ ONE (Get One User)
# ==========================================

def get_user(user_id):
    sql = "SELECT * FROM users WHERE id = %s"

    cursor.execute(sql, (user_id,))

    user = cursor.fetchone()

    if user:
        print(user)
    else:
        print("User not found.")

    return user


# ==========================================
# UPDATE (Edit Existing User)
# ==========================================

def update_user(user_id, name, email):
    sql = """
        UPDATE users
        SET
            name = %s,
            email = %s
        WHERE id = %s
    """

    values = (name, email, user_id)

    cursor.execute(sql, values)
    db.commit()

    print("User updated successfully!")


# ==========================================
# DELETE (Remove User)
# ==========================================

def delete_user(user_id):
    sql = "DELETE FROM users WHERE id = %s"

    cursor.execute(sql, (user_id,))
    db.commit()

    print("User deleted successfully!")


# ==========================================
# EXAMPLE USAGE
# ==========================================

print("\n----- CREATE -----")
create_user("John Doe", "john@example.com")

print("\n----- READ ALL -----")
get_users()

print("\n----- READ ONE -----")
get_user(1)

print("\n----- UPDATE -----")
update_user(
    1,
    "John Smith",
    "johnsmith@example.com"
)

print("\n----- READ AFTER UPDATE -----")
get_user(1)

print("\n----- DELETE -----")
delete_user(1)

print("\n----- FINAL DATABASE -----")
get_users()


# ==========================================
# Close Connection
# ==========================================

cursor.close()
db.close()

print("\nDatabase connection closed.")
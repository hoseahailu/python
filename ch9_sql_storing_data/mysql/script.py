# # Python CRUD Tutorial with MySQL

# In this tutorial, you'll learn how to:

# - Install the MySQL Python connector
# - Create a MySQL database
# - Create a table
# - Connect Python to MySQL
# - Create (INSERT)
# - Read (SELECT)
# - Update (UPDATE)
# - Delete (DELETE)

# ---

# # Step 1 - Install MySQL Connector

# Open your terminal or command prompt and run:

# ```bash
# pip install mysql-connector-python
# ```

# This installs the library Python uses to communicate with a MySQL database.

# ---

# # Step 2 - Create a Database

# Open MySQL Workbench or the MySQL Command Line and run:

# ```sql
# CREATE DATABASE crud_db;
# ```

# Now select the database:

# ```sql
# USE crud_db;
# ```

# ---

# # Step 3 - Create a Table

# Run the following SQL:

# ```sql
# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) NOT NULL
# );
# ```

# Your table now looks like this:

# | id | name | email |
# |----|------|-------|
# | 1 | John | john@example.com |

# ---

# # Step 4 - Create a Python File

# Create a file called:

# ```
# app.py
# ```

# ---

# # Step 5 - Import MySQL Connector

# At the top of your file write:

# ```python
# import mysql.connector
# ```

# This imports the MySQL library.

# ---

# # Step 6 - Connect to MySQL

# ```python
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="your_password",
#     database="crud_db"
# )

# cursor = db.cursor(dictionary=True)

# print("Connected Successfully!")
# ```

# Replace:

# ```python
# password="your_password"
# ```

# with your own MySQL password.

# The `dictionary=True` option means each row returned from MySQL will look like this:

# ```python
# {
#     "id": 1,
#     "name": "John",
#     "email": "john@example.com"
# }
# ```

# instead of

# ```python
# (1, "John", "john@example.com")
# ```

# ---

# # Step 7 - CREATE (Insert Data)

# ## What does CREATE do?

# CREATE adds a new row to the table.

# SQL equivalent:

# ```sql
# INSERT INTO users(name,email)
# VALUES('John','john@example.com');
# ```

# Python code:

# ```python
# def create_user(name, email):

#     sql = "INSERT INTO users (name, email) VALUES (%s, %s)"

#     values = (name, email)

#     cursor.execute(sql, values)

#     db.commit()

#     print("User created successfully!")
#     print("Inserted ID:", cursor.lastrowid)
# ```

# Example:

# ```python
# create_user("John Doe", "john@example.com")
# ```

# ---

# # Step 8 - READ ALL (View Every User)

# ## What does READ do?

# READ retrieves information from the database.

# SQL equivalent:

# ```sql
# SELECT * FROM users;
# ```

# Python code:

# ```python
# def get_users():

#     cursor.execute("SELECT * FROM users")

#     users = cursor.fetchall()

#     for user in users:
#         print(user)
# ```

# Example:

# ```python
# get_users()
# ```

# Output:

# ```python
# {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
# {'id': 2, 'name': 'Sarah', 'email': 'sarah@example.com'}
# ```

# ---

# # Step 9 - READ ONE User

# SQL equivalent:

# ```sql
# SELECT * FROM users
# WHERE id = 1;
# ```

# Python code:

# ```python
# def get_user(user_id):

#     sql = "SELECT * FROM users WHERE id = %s"

#     cursor.execute(sql, (user_id,))

#     user = cursor.fetchone()

#     print(user)

#     return user
# ```

# Example:

# ```python
# get_user(1)
# ```

# Output:

# ```python
# {'id':1,'name':'John','email':'john@example.com'}
# ```

# Notice:

# ```python
# (user_id,)
# ```

# The comma is required because Python needs a tuple.

# ---

# # Step 10 - UPDATE (Edit Data)

# ## What does UPDATE do?

# UPDATE changes existing information.

# SQL equivalent:

# ```sql
# UPDATE users
# SET name='John Smith',
# email='johnsmith@example.com'
# WHERE id=1;
# ```

# Python code:

# ```python
# def update_user(user_id, name, email):

#     sql = """
#     UPDATE users
#     SET name = %s,
#         email = %s
#     WHERE id = %s
#     """

#     values = (name, email, user_id)

#     cursor.execute(sql, values)

#     db.commit()

#     print("User updated successfully!")
# ```

# Example:

# ```python
# update_user(
#     1,
#     "John Smith",
#     "johnsmith@example.com"
# )
# ```

# ---

# # Step 11 - DELETE (Remove Data)

# ## What does DELETE do?

# DELETE removes a row from the table.

# SQL equivalent:

# ```sql
# DELETE FROM users
# WHERE id = 1;
# ```

# Python code:

# ```python
# def delete_user(user_id):

#     sql = "DELETE FROM users WHERE id = %s"

#     cursor.execute(sql, (user_id,))

#     db.commit()

#     print("User deleted successfully!")
# ```

# Example:

# ```python
# delete_user(1)
# ```

# ---

# # Step 12 - Complete Program

# ```python
# import mysql.connector

# # -----------------------------
# # CONNECT TO DATABASE
# # -----------------------------

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="your_password",
#     database="crud_db"
# )

# cursor = db.cursor(dictionary=True)

# print("Connected Successfully!")

# # -----------------------------
# # CREATE
# # -----------------------------

# def create_user(name, email):

#     sql = "INSERT INTO users (name, email) VALUES (%s, %s)"

#     values = (name, email)

#     cursor.execute(sql, values)

#     db.commit()

#     print(f"User created with ID: {cursor.lastrowid}")

# # -----------------------------
# # READ ALL
# # -----------------------------

# def get_users():

#     cursor.execute("SELECT * FROM users")

#     users = cursor.fetchall()

#     for user in users:
#         print(user)

# # -----------------------------
# # READ ONE
# # -----------------------------

# def get_user(user_id):

#     sql = "SELECT * FROM users WHERE id = %s"

#     cursor.execute(sql, (user_id,))

#     user = cursor.fetchone()

#     print(user)

#     return user

# # -----------------------------
# # UPDATE
# # -----------------------------

# def update_user(user_id, name, email):

#     sql = """
#     UPDATE users
#     SET name = %s,
#         email = %s
#     WHERE id = %s
#     """

#     values = (name, email, user_id)

#     cursor.execute(sql, values)

#     db.commit()

#     print("User updated")

# # -----------------------------
# # DELETE
# # -----------------------------

# def delete_user(user_id):

#     sql = "DELETE FROM users WHERE id = %s"

#     cursor.execute(sql, (user_id,))

#     db.commit()

#     print("User deleted")

# # -----------------------------
# # EXAMPLES
# # -----------------------------

# create_user("John Doe", "john@example.com")

# print()

# get_users()

# print()

# get_user(1)

# print()

# update_user(
#     1,
#     "John Smith",
#     "johnsmith@example.com"
# )

# print()

# delete_user(1)

# # -----------------------------
# # CLOSE CONNECTION
# # -----------------------------

# cursor.close()
# db.close()
# ```

# ---

# # CRUD Summary

# | CRUD | SQL Command | Python Function |
# |------|-------------|-----------------|
# | Create | INSERT | create_user() |
# | Read | SELECT | get_users() / get_user() |
# | Update | UPDATE | update_user() |
# | Delete | DELETE | delete_user() |

# ---

# # How It Works

# ```
# Python Program
#       │
#       ▼
# mysql.connector
#       │
#       ▼
# MySQL Server
#       │
#       ▼
# crud_db Database
#       │
#       ▼
# users Table
# ```

# The Python program sends SQL commands through `mysql.connector` to the MySQL server. The server performs the requested operation on the `users` table and returns the results back to Python.
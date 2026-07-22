from database import db, cursor

def create_user(name, email, age):

    sql = """
    INSERT INTO users(name,email,age)
    VALUES(%s,%s,%s)
    """

    values = (name, email, age)

    cursor.execute(sql, values)

    db.commit()

    print("User added!")

create_user("John", "john@gmail.com", 25)
create_user("Joessica", "jessica@gmail.com", 46)
create_user("Jo", "jo@gmail.com", 23)
create_user("Doe", "doe@gmail.com", 12)

cursor.close()
db.close()
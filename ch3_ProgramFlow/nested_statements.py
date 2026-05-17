username = "alex"
password = "python123"
is_admin = True

entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

if entered_username == username:
    if entered_password == password:
        print("Login successful!")

        if is_admin:
            print("Welcome, Admin.")
        else:
            print("Welcome, User.")

    else:
        print("Incorrect password.")
else:
    print("Username not found.")

def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            if age > 150:
                print("That doesn't look like a valid age.")
                continue

            return age

        except ValueError:
            print("Please enter a whole number.")


age = get_age()
print(f"You are {age} years old.")
# Defensive Design - Input Validation and Sanitisation

print("=== Simple Login System ===")

# -----------------------------
# INPUT VALIDATION
# -----------------------------

# Presence check
username = input("Enter your username: ")

# strip() removes spaces from the beginning and end
while username.strip() == "":
    print("Error: You must enter a username.")
    username = input("Enter your username: ")


# Range check
age = int(input("Enter your age (1-100): "))

while age < 1 or age > 100:
    print("Error: Age must be between 1 and 100.")
    age = int(input("Enter your age (1-100): "))


# -----------------------------
# INPUT SANITISATION
# -----------------------------

# Remove unwanted spaces
username = username.strip()

# Remove unwanted characters
username = username.replace("<", "")
username = username.replace(">", "")


print("\nYour details are:")
print("Username:", username)
print("Age:", age)

print("\nInput accepted!")

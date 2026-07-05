person = {
    "first_name" : "Hosea",
    "age" : "13",
    "country" : "England",
    "major" : "Computer Science"
}

# print(person["major"])
print(person.get("first_name"))
person["first_name"] = "Doe"
print(person)
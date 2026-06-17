students = open("list_of_students.txt", "r")
print(students.read())

Hello = open("Hello_world.py", "x")
Hello.close()

students = open("list_of_students.txt", "r")

print(students.read())

students.close()
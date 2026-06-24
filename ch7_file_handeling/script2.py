# import os,shutil

# os.mkdir("Hosea's_folder")
# print("folder created")

# os.makedirs("Timmy/Time/one/two/three")
# print("Make Folders")

# file_content = open("friends.txt", "r")
# print("my friends names are", file_content.read())
# file_content.close()

# with open("friends.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("students.txt", "w") as file:
#     file.write("John,85\n")
#     file.write("Alice,90\n")

# with open("students.txt", "r") as file:
#     data = file.read()

# print(data)

# with open("students.txt", "r") as file:
#     data = file.read()

# print(data)

# with open("students.txt", "r") as file:
#     line = file.readline()

# print(line)

# with open("students.txt", "r") as file:
#     lines = file.readlines()

# print(lines)

# with open("students.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# with open("students.txt", "r") as file:
#     lines = file.readlines()

# with open("students.txt", "w") as file:
#     for line in lines:
#         if line.startswith("John"):
#             file.write("John,95\n")
#         else:
#             file.write(line)

# with open("students.txt", "a") as file:
#     file.write("Bob,88\n")

# with open("students.txt", "r") as file:
#     lines = file.readlines()

# with open("students.txt", "w") as file:
#     for line in lines:
#         if not line.startswith("Alice"):
#             file.write(line)

# import os

# os.remove("students.txt")

# import os

# if os.path.exists("students.txt"):
#     os.remove("students.txt")
# else:
#     print("File not found")

# os.remove("Hosea's_folder")
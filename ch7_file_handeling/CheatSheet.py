# ==========================================
# PYTHON FILE HANDLING CHEAT SHEET
# ==========================================

# ------------------
# OPEN A FILE
# ------------------

file = open("example.txt", "r")   # Read
file = open("example.txt", "w")   # Write (overwrites file)
file = open("example.txt", "a")   # Append
file = open("example.txt", "x")   # Create new file
file = open("example.txt", "rb")  # Read binary
file = open("example.txt", "wb")  # Write binary


# ------------------
# READ FILES
# ------------------

file = open("example.txt", "r")

print(file.read())      # Read entire file
print(file.readline())  # Read one line
print(file.readlines()) # Read all lines into a list

file.close()


# ------------------
# READ FILE LINE BY LINE
# ------------------

file = open("example.txt", "r")

for line in file:
    print(line)

file.close()


# ------------------
# WRITE TO FILE
# ------------------

file = open("example.txt", "w")

file.write("Hello World!")

file.close()


# ------------------
# APPEND TO FILE
# ------------------

file = open("example.txt", "a")

file.write("\nNew line added.")

file.close()


# ------------------
# CREATE A FILE
# ------------------

file = open("newfile.txt", "x")

file.close()


# ------------------
# USING WITH
# (Automatically closes file)
# ------------------

with open("example.txt", "r") as file:
    print(file.read())


with open("example.txt", "w") as file:
    file.write("Hello")


# ------------------
# CHECK CURRENT POSITION
# ------------------

file = open("example.txt", "r")

print(file.tell())

file.close()


# ------------------
# MOVE CURSOR
# ------------------

file = open("example.txt", "r")

file.seek(0)  # Move to beginning

file.close()


# ------------------
# FILE EXISTS CHECK
# ------------------

import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")


# ------------------
# DELETE A FILE
# ------------------

import os

os.remove("example.txt")


# ------------------
# DELETE FILE SAFELY
# ------------------

import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("Deleted")
else:
    print("File not found")


# ------------------
# RENAME A FILE
# ------------------

import os

os.rename("old.txt", "new.txt")


# ------------------
# GET FILE SIZE
# ------------------

import os

size = os.path.getsize("example.txt")

print(size)


# ------------------
# LIST FILES IN FOLDER
# ------------------

import os

print(os.listdir())


# ------------------
# LIST FILES IN SPECIFIC FOLDER
# ------------------

import os

print(os.listdir("Documents"))


# ------------------
# CHECK IF PATH IS FILE
# ------------------

import os

print(os.path.isfile("example.txt"))


# ------------------
# CHECK IF PATH IS FOLDER
# ------------------

import os

print(os.path.isdir("Documents"))


# ------------------
# CREATE FOLDER
# ------------------

import os

os.mkdir("NewFolder")


# ------------------
# CREATE NESTED FOLDERS
# ------------------

import os

os.makedirs("Folder1/Folder2/Folder3")


# ------------------
# REMOVE EMPTY FOLDER
# ------------------

import os

os.rmdir("NewFolder")


# ------------------
# GET CURRENT DIRECTORY
# ------------------

import os

print(os.getcwd())


# ------------------
# CHANGE DIRECTORY
# ------------------

import os

os.chdir("Documents")


# ------------------
# COPY FILE
# ------------------

import shutil

shutil.copy("source.txt", "destination.txt")


# ------------------
# MOVE FILE
# ------------------

import shutil

shutil.move("source.txt", "destination.txt")


# ------------------
# COPY ENTIRE FOLDER
# ------------------

import shutil

shutil.copytree("FolderA", "FolderB")


# ------------------
# DELETE ENTIRE FOLDER
# ------------------

import shutil

shutil.rmtree("FolderB")


# ------------------
# FILE MODES
# ------------------

# r   = Read
# w   = Write (overwrite)
# a   = Append
# x   = Create
# rb  = Read binary
# wb  = Write binary
# r+  = Read and write
# w+  = Read and write (overwrite)
# a+  = Read and append


# ------------------
# EXAMPLE PROJECT
# ------------------

with open("students.txt", "w") as file:
    file.write("Alice\n")
    file.write("Bob\n")
    file.write("Charlie\n")

with open("students.txt", "r") as file:
    print(file.read())


# ==========================================
# END OF FILE HANDLING CHEAT SHEET
# ==========================================
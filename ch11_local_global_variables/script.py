#Global variables are variables that can be accessed
#from different parts of your program.
#They're useful when multiple functions need the same data,
#but they should be used carefully because
#changing them from anywhere can make bugs harder to find.

#Global

score = 0

def show_score():
    print(score)

print(score)

#local

def greet():
    name = "Hosea"
    print(name)

greet()

print(name)
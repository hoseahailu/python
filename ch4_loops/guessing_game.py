# secret = 7

# while True:
#     guess = int(input("Guess the number: "))

#     if guess == secret:
#         print("Correct!")
#         break
#     else:
#         print("Wrong")

import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong")

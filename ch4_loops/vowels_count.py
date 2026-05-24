word = input("Enter a word: ")
count = 0

for letter in word:
    if letter in "aeiou":
        count += 1

print(count)

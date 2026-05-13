# # name = input("whats your name?")
# # print("Hello there,",name)
# # salary = int(input("whats your salary?"))
# # sal ary += 50
# # print(salary)
# # first_name = "Hosea"
# # last_name = "Hailu"
# # full_name = first_name + " " + last_name
# # print(full_name)

# name = "Hosea Hailu"
# print(name.upper())  # HOSEA HAILU
# print(name.lower())  # hosea hailu
# print(name.title())  # Hosea Hailu
# print(name.capitalize())  # Hosea hailu
# print(name.swapcase())  # hOSEA hAILU

# print(len(name))  # 11
# print(name.count("a"))  # counts 'a' → 2
# print(name.count("H"))  # 1

# print(name.find("Hailu"))  # index where "Hailu" starts → 6
# print(name.find("z"))  # -1 (not found)
# print(name.index("Hosea"))  # 0

# print(name.isalpha())  # False (space included)
# print(name.isalnum())  # False (space included)
# print("Hosea".isalpha())  # True

# print(name.startswith("Ho"))  # True
# print(name.endswith("lu"))  # True

# print(name.replace("Hosea", "Happy"))
# # Hero Hailu

# print(name.replace("a", "@"))
# # Hose@ H@ilu

# parts = name.split()
# print(parts)
# # ['Hosea','Hailu']

# joined = "-".join(parts)
# print(joined)
# # Hosea-Hailu

# name2 = "   Hosea Hailu   "
# print(name2.strip())  # removes both sides
# print(name2.lstrip())  # left side only
# print(name2.rstrip())  # right side only

name = "Hosea Hailu"

print(name[:])
print(name[6:11])

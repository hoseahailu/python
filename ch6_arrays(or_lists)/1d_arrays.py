# =========================
# CREATE A 1D ARRAY (LIST)
# =========================

numbers = [1, 2, 3, 4, 5]

# =========================
# ACCESS ITEMS
# =========================

print(numbers[0])   # First item
print(numbers[2])   # Third item
print(numbers[-1])  # Last item

# =========================
# CHANGE ITEMS
# =========================

numbers[0] = 10

# =========================
# PRINT WHOLE ARRAY
# =========================

print(numbers)

# =========================
# ADD ITEMS
# =========================

numbers.append(6)
numbers.insert(0, 0)

# =========================
# REMOVE ITEMS
# =========================

numbers.remove(3)  # Remove value
numbers.pop()      # Remove last item
numbers.pop(0)     # Remove by index

# =========================
# LENGTH
# =========================

print(len(numbers))

# =========================
# LOOP THROUGH ARRAY
# =========================

for item in numbers:
    print(item)

# =========================
# LOOP WITH INDEX
# =========================

for i in range(len(numbers)):
    print(numbers[i])

# =========================
# SEARCH FOR VALUE
# =========================

if 4 in numbers:
    print("Found 4")

# =========================
# FIND INDEX
# =========================

print(numbers.index(4))

# =========================
# COUNT OCCURRENCES
# =========================

print(numbers.count(4))

# =========================
# SORT ARRAY
# =========================

numbers.sort()

# =========================
# SORT DESCENDING
# =========================

numbers.sort(reverse=True)

# =========================
# REVERSE ARRAY
# =========================

numbers.reverse()

# =========================
# SUM OF ITEMS
# =========================

print(sum(numbers))

# =========================
# MAX AND MIN
# =========================

print(max(numbers))
print(min(numbers))

# =========================
# COPY ARRAY
# =========================

copy_numbers = numbers.copy()

# =========================
# COMBINE ARRAYS
# =========================

a = [1, 2]
b = [3, 4]

c = a + b
print(c)

# =========================
# EXTEND ARRAY
# =========================

a.extend(b)
print(a)

# =========================
# SLICING
# =========================

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# =========================
# CREATE EMPTY ARRAY
# =========================

empty = []

# =========================
# CREATE ARRAY WITH REPEATED VALUES
# =========================

zeros = [0] * 5
print(zeros)

# =========================
# CLEAR ARRAY
# =========================

numbers.clear()
print(numbers)
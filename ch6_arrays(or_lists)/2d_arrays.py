# =========================
# CREATE A 2D ARRAY
# =========================

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# =========================
# ACCESS ITEMS
# =========================

print(grid[0][0])  # 1
print(grid[1][2])  # 6

# =========================
# CHANGE ITEMS
# =========================

grid[0][0] = 10

# =========================
# PRINT WHOLE ARRAY
# =========================

print(grid)

# =========================
# PRINT EACH ROW
# =========================

for row in grid:
    print(row)

# =========================
# PRINT EACH ITEM
# =========================

for row in grid:
    for item in row:
        print(item)

# =========================
# ADD A ROW
# =========================

grid.append([10, 11, 12])

# =========================
# INSERT A ROW
# =========================

grid.insert(1, [100, 101, 102])

# =========================
# REMOVE A ROW
# =========================

grid.pop(0)

# =========================
# GET NUMBER OF ROWS
# =========================

print(len(grid))

# =========================
# GET NUMBER OF COLUMNS
# =========================

print(len(grid[0]))

# =========================
# LOOP WITH ROW/COLUMN INDEX
# =========================

for r in range(len(grid)):
    for c in range(len(grid[r])):
        print(f"Row {r}, Column {c} = {grid[r][c]}")

# =========================
# SEARCH FOR A VALUE
# =========================

for row in grid:
    if 5 in row:
        print("Found 5")

# =========================
# SUM ALL VALUES
# =========================

total = 0

for row in grid:
    for item in row:
        total += item

print(total)

# =========================
# COPY A 2D ARRAY
# =========================

copy_grid = [row[:] for row in grid]

# =========================
# CREATE AN EMPTY 2D ARRAY
# =========================

empty_grid = []

# =========================
# CREATE A 3x3 GRID OF ZEROS
# =========================

zero_grid = [[0 for c in range(3)] for r in range(3)]

print(zero_grid)

# =========================
# CLEAR ALL ROWS
# =========================

grid.clear()

print(grid)
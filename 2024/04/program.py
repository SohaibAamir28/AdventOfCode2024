def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    # Helper function to check if word exists in a specific direction
    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    # Iterate over each cell and check all 8 directions
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                # Check all 8 possible directions
                directions = [
                    (0, 1), (1, 0), (1, 1), (-1, 1),
                    (0, -1), (-1, 0), (-1, -1), (1, -1)
                ]
                for dr, dc in directions:
                    if check_direction(r, c, dr, dc):
                        count += 1

    return count

def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Helper function to check if X-MAS pattern exists
    def check_x_mas(r, c):
        # Check if the X-MAS pattern exists with 'A' at the center
        # There are two possible valid configurations for forming an X
        if (
            r - 1 >= 0 and r + 1 < rows and c - 1 >= 0 and c + 1 < cols and
            grid[r][c] == 'A' and
            (
                (grid[r - 1][c - 1] == 'M' and grid[r - 1][c + 1] == 'S' and
                 grid[r + 1][c - 1] == 'S' and grid[r + 1][c + 1] == 'M') or
                (grid[r - 1][c - 1] == 'S' and grid[r - 1][c + 1] == 'M' and
                 grid[r + 1][c - 1] == 'M' and grid[r + 1][c + 1] == 'S') or
                (grid[r - 1][c - 1] == 'M' and grid[r + 1][c - 1] == 'S' and
                 grid[r - 1][c + 1] == 'S' and grid[r + 1][c + 1] == 'M') or
                (grid[r - 1][c + 1] == 'M' and grid[r + 1][c + 1] == 'S' and
                 grid[r - 1][c - 1] == 'S' and grid[r + 1][c - 1] == 'M')
            )
        ):
            return True
        return False

    # Iterate over each cell to find X-MAS patterns
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == 'A' and check_x_mas(r, c):
                count += 1

    return count

# Read the input grid from the file
f = open("2024/04/input.txt").read().strip().split("\n")
grid = [list(line) for line in f]

# Calculate and print the results
result_part_1 = count_xmas(grid)
print("Day 4 Part 1: Number of times XMAS appears: " + str(result_part_1))

result_part_2 = count_x_mas(grid)
print("Day 4 Part 2: Number of times X-MAS appears: " + str(result_part_2))

# def count_xmas(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     word = "XMAS"
#     word_len = len(word)
#     count = 0

#     # Helper function to check if word exists in a specific direction
#     def check_direction(r, c, dr, dc):
#         for i in range(word_len):
#             nr, nc = r + i * dr, c + i * dc
#             if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
#                 return False
#         return True

#     # Iterate over each cell and check all 8 directions
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == word[0]:
#                 # Check all 8 possible directions
#                 directions = [
#                     (0, 1), (1, 0), (1, 1), (-1, 1),
#                     (0, -1), (-1, 0), (-1, -1), (1, -1)
#                 ]
#                 for dr, dc in directions:
#                     if check_direction(r, c, dr, dc):
#                         count += 1

#     return count

# def count_x_mas(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     count = 0

#     # Helper function to check if X-MAS pattern exists
#     def check_x_mas(r, c):
#         # Check for two MAS patterns forming an X with 'A' at the center
#         if (
#             r - 1 >= 0 and r + 1 < rows and c - 1 >= 0 and c + 1 < cols and
#             grid[r][c] == 'A' and
#             grid[r - 1][c - 1] == 'M' and grid[r - 1][c + 1] == 'S' and
#             grid[r + 1][c - 1] == 'M' and grid[r + 1][c + 1] == 'S'
#         ):
#             return True
#         return False

#     # Iterate over each cell to find X-MAS patterns
#     for r in range(1, rows - 1):
#         for c in range(1, cols - 1):
#             if grid[r][c] == 'A' and check_x_mas(r, c):
#                 count += 1

#     return count

# # Read the input grid from the file
# f = open("2024/04/input.txt").read().strip().split("\n")
# grid = [list(line) for line in f]

# # Calculate and print the results
# result_part_1 = count_xmas(grid)
# print("Day 4 Part 1: Number of times XMAS appears: " + str(result_part_1))

# result_part_2 = count_x_mas(grid)
# print("Day 4 Part 2: Number of times X-MAS appears: " + str(result_part_2))

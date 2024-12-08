def predict_guard_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    # Find the initial position and direction of the guard
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    direction_index = 0
    start_row, start_col = -1, -1

    # Locate the starting position of the guard
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '^':
                start_row, start_col = r, c
                direction_index = 0  # Guard starts facing up
                break
        if start_row != -1:
            break

    # Simulate guard's movement
    r, c = start_row, start_col
    visited.add((r, c))

    while True:
        dr, dc = directions[direction_index]
        nr, nc = r + dr, c + dc

        # Check if there's an obstacle in front or if the guard is out of bounds
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == '#':
            # Turn right 90 degrees
            direction_index = (direction_index + 1) % 4
        else:
            # Move forward
            r, c = nr, nc
            visited.add((r, c))

        # Stop if the guard moves out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            break

    return len(visited)

# Read the input grid from the file
file_path = "/2024/06/input.txt"
with open(file_path, "r") as f:
    grid = [list(line.strip()) for line in f]

# Calculate and print the result for Day 6
result_guard_path = predict_guard_path(grid)
print("Day 6: Number of distinct positions visited by the guard: " + str(result_guard_path))

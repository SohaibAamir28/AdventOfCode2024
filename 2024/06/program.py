<<<<<<< HEAD
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
=======
def parse_map(file_path):
    """
    Parse the input file into a 2D map and find the guard's initial position and direction.
    """
    with open(file_path) as f:
        map_data = [list(line.strip()) for line in f]

    guard_pos, guard_dir = None, None
    for r, row in enumerate(map_data):
        for c, cell in enumerate(row):
            if cell in "^>v<":
                guard_pos = (r, c)
                guard_dir = cell
                map_data[r][c] = '.'  # Clear guard's initial position
                break

    return map_data, guard_pos, guard_dir


def simulate_guard_with_obstruction(map_data, guard_pos, guard_dir, obstruction_pos):
    """
    Simulate the guard's movement with a potential obstruction and check if it causes a loop.
    """
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    rows, cols = len(map_data), len(map_data[0])
    visited_states = set()
    current_pos = guard_pos
    current_dir = guard_dir

    # Place the obstruction
    if obstruction_pos:
        map_data[obstruction_pos[0]][obstruction_pos[1]] = '#'

    while True:
        # Record the current state (position + direction)
        state = (current_pos, current_dir)
        if state in visited_states:
            # A loop is detected
            if obstruction_pos:
                map_data[obstruction_pos[0]][obstruction_pos[1]] = '.'  # Clean up
            return True
        visited_states.add(state)

        # Calculate the next position
        dr, dc = directions[current_dir]
        next_pos = (current_pos[0] + dr, current_pos[1] + dc)

        # Check if the guard is leaving the map
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        # Check for obstacles
        if map_data[next_pos[0]][next_pos[1]] == '#':
            current_dir = turn_right[current_dir]  # Turn right
        else:
            current_pos = next_pos  # Move forward

    # Clean up the obstruction
    if obstruction_pos:
        map_data[obstruction_pos[0]][obstruction_pos[1]] = '.'
    return False


def find_valid_obstruction_positions(map_data, guard_pos, guard_dir):
    """
    Identify all valid positions where adding an obstruction causes the guard to loop.
    """
    rows, cols = len(map_data), len(map_data[0])
    valid_positions = []

    for r in range(rows):
        for c in range(cols):
            if (r, c) == guard_pos or map_data[r][c] != '.':
                continue
            # Simulate with this obstruction
            if simulate_guard_with_obstruction(map_data, guard_pos, guard_dir, (r, c)):
                valid_positions.append((r, c))

    return valid_positions


def main():
    """
    Main function to execute the solution for Part Two.
    """
    # Update this to your actual input file path
    file_path = "2024/06/input.txt"
    
    # Parse the input and initialize the simulation
    map_data, guard_pos, guard_dir = parse_map(file_path)
    valid_positions = find_valid_obstruction_positions(map_data, guard_pos, guard_dir)

    # Output the result
    print(f"Number of valid positions for obstruction: {len(valid_positions)}")
    print("Valid positions:", valid_positions)


if __name__ == "__main__":
    main()



# def parse_map(file_path):
#     """
#     Parse the input file into a 2D map and find the guard's initial position and direction.
#     """
#     with open(file_path) as f:
#         map_data = [list(line.strip()) for line in f]

#     guard_pos, guard_dir = None, None
#     for r, row in enumerate(map_data):
#         for c, cell in enumerate(row):
#             if cell in "^>v<":
#                 guard_pos = (r, c)
#                 guard_dir = cell
#                 map_data[r][c] = '.'  # Clear guard's initial position
#                 break

#     return map_data, guard_pos, guard_dir


# def simulate_guard_movement(map_data, guard_pos, guard_dir):
#     """
#     Simulate the guard's movement based on the rules and track visited positions.
#     """
#     directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
#     turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

#     rows, cols = len(map_data), len(map_data[0])
#     visited_positions = set()
#     visited_positions.add(guard_pos)

#     while True:
#         # Calculate the next position
#         dr, dc = directions[guard_dir]
#         next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

#         # Check if the guard is leaving the map
#         if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
#             break

#         # Check for obstacles
#         if map_data[next_pos[0]][next_pos[1]] == '#':
#             guard_dir = turn_right[guard_dir]  # Turn right
#         else:
#             guard_pos = next_pos  # Move forward
#             visited_positions.add(guard_pos)

#     return visited_positions


# def main():
#     """
#     Main function to execute the guard simulation and count distinct positions.
#     """
#     # Update this to your actual input file path
#     file_path = "2024/06/input.txt"
    
#     # Parse the input and initialize the simulation
#     map_data, guard_pos, guard_dir = parse_map(file_path)
#     visited_positions = simulate_guard_movement(map_data, guard_pos, guard_dir)

#     # Output the result
#     print(f"Distinct positions visited: {len(visited_positions)}")


# if __name__ == "__main__":
#     main()
# # 5080
>>>>>>> 6c34ec39d598da55003ceef93697f9c5d6c144d9

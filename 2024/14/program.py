from rich import print

def parse_input(data):
    robots = []
    for line in data:
        p, v = line.strip().split(' ')
        px, py = map(int, p[2:].split(','))
        vx, vy = map(int, v[2:].split(','))
        robots.append(((px, py), (vx, vy)))
    return robots

def move_robot(position, velocity, width, height):
    x, y = position
    vx, vy = velocity
    x = (x + vx) % width
    y = (y + vy) % height
    return (x, y)

def simulate_robots(robots, width, height, seconds):
    for _ in range(seconds):
        robots = [(move_robot(p, v, width, height), v) for p, v in robots]
    return robots

def count_robots_in_quadrants(robots, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]
    for (x, y), _ in robots:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1
    return quadrants

def check_christmas_tree_pattern(robots, width, height):
    tree_pattern = [
        "....#....",
        "...###...",
        "..#####..",
        ".#######.",
        "#########",
        "....#....",
        "....#...."
    ]

    grid = [['.' for _ in range(width)] for _ in range(height)]
    for (x, y), _ in robots:
        grid[y][x] = '#'

    pattern_height = len(tree_pattern)
    pattern_width = len(tree_pattern[0])

    for y in range(height - pattern_height + 1):
        for x in range(width - pattern_width + 1):
            match = True
            for py in range(pattern_height):
                for px in range(pattern_width):
                    if tree_pattern[py][px] == '#' and grid[y + py][x + px] != '#':
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

def find_easter_egg(data):
    width, height = 101, 103
    robots = parse_input(data)
    seconds = 0
    while True:
        robots = simulate_robots(robots, width, height, 1)
        seconds += 1
        if check_christmas_tree_pattern(robots, width, height):
            return seconds

def solve(data):
    width, height = 101, 103
    robots = parse_input(data)
    robots = simulate_robots(robots, width, height, 100)
    quadrants = count_robots_in_quadrants(robots, width, height)
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    return safety_factor

def main():
    # Update this to the path of your input file
    file_path = '2024/14/input.txt'

    # Read the input data from the file
    with open(file_path, 'r') as file:
        data = file.readlines()

    print("Safety Factor:", solve(data))
    print("Seconds to Easter Egg:", find_easter_egg(data))

if __name__ == '__main__':
    main()

# part 1

# def parse_input(file_path):
#     robots = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             pos, vel = line.strip().split()
#             px, py = map(int, pos[2:].split(','))
#             vx, vy = map(int, vel[2:].split(','))
#             robots.append(((px, py), (vx, vy)))
#     return robots

# def simulate_robots(robots, width, height, seconds):
#     new_positions = []
#     for (px, py), (vx, vy) in robots:
#         new_x = (px + vx * seconds) % width
#         new_y = (py + vy * seconds) % height
#         new_positions.append((new_x, new_y))
#     return new_positions

# def calculate_safety_factor(positions, width, height):
#     center_x, center_y = width // 2, height // 2
#     quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

#     for x, y in positions:
#         if x == center_x or y == center_y:
#             continue  # Ignore robots on the center lines

#         if x < center_x and y < center_y:
#             quadrants[0] += 1  # Top-left
#         elif x > center_x and y < center_y:
#             quadrants[1] += 1  # Top-right
#         elif x < center_x and y > center_y:
#             quadrants[2] += 1  # Bottom-left
#         elif x > center_x and y > center_y:
#             quadrants[3] += 1  # Bottom-right

#     # Calculate safety factor
#     safety_factor = 1
#     for count in quadrants:
#         safety_factor *= count

#     return safety_factor

# def main():
#     # Constants for the grid
#     width, height = 101, 103
#     seconds = 100

#     # Parse input
#     file_path = "2024/14/input.txt"  # Replace with your actual input file path
#     robots = parse_input(file_path)

#     # Simulate robot motion
#     positions = simulate_robots(robots, width, height, seconds)

#     # Calculate safety factor
#     safety_factor = calculate_safety_factor(positions, width, height)
#     print(f"Safety Factor: {safety_factor}")

# if __name__ == "__main__":
#     main()

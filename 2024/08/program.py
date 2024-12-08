# Final refined implementation for Advent of Code Day 8 Part 2
import math

def parse_map(file_path):
    """Parses the input map from the file."""
    antennas = []
    with open(file_path, 'r') as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char != '.':
                    antennas.append((x, y, char))
    return antennas

def calculate_antinodes_part_two(antennas, map_width, map_height):
    """Calculates the unique antinodes within the bounds of the map."""
    antinode_positions = set()

    # Group antennas by frequency
    frequency_groups = {}
    for x, y, freq in antennas:
        if freq not in frequency_groups:
            frequency_groups[freq] = []
        frequency_groups[freq].append((x, y))

    # Calculate antinodes for each frequency group
    for freq, positions in frequency_groups.items():
        n = len(positions)

        # Include all antenna positions as antinodes
        antinode_positions.update(positions)

        # Check collinearity for each pair of antennas
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Calculate step size (dx, dy)
                dx = x2 - x1
                dy = y2 - y1
                gcd = math.gcd(dx, dy)
                dx //= gcd
                dy //= gcd

                # Extend both directions from (x1, y1) and (x2, y2)
                x, y = x1 - dx, y1 - dy
                while 0 <= x < map_width and 0 <= y < map_height:
                    antinode_positions.add((x, y))
                    x -= dx
                    y -= dy

                x, y = x2 + dx, y2 + dy
                while 0 <= x < map_width and 0 <= y < map_height:
                    antinode_positions.add((x, y))
                    x += dx
                    y += dy

    return antinode_positions

def main():
    # File path for input
    file_path = '2024/08/input.txt'

    # Parse the input map
    antennas = parse_map(file_path)
    
    # Determine map dimensions (assuming rectangular grid)
    with open(file_path, 'r') as file:
        map_width = len(file.readline().strip())
        map_height = sum(1 for _ in file) + 1

    # Calculate antinodes for Part 2
    antinodes = calculate_antinodes_part_two(antennas, map_width, map_height)

    # Output the total number of unique antinodes
    print("Total unique antinodes (Part 2):", len(antinodes))

if __name__ == "__main__":
    main()

#  Part 1

def parse_map(input_map):
    antennas = []
    for y, line in enumerate(input_map.strip().split("\n")):
        for x, char in enumerate(line):
            if char != ".":
                antennas.append((x, y, char))
    return antennas

def calculate_antinodes(antennas):
    antinode_positions = set()

    # Group antennas by frequency
    frequency_groups = {}
    for x, y, freq in antennas:
        if freq not in frequency_groups:
            frequency_groups[freq] = []
        frequency_groups[freq].append((x, y))

    # Calculate antinodes for each frequency group
    for freq, positions in frequency_groups.items():
        n = len(positions)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Check if one antenna is twice as far as the other
                dx = x2 - x1
                dy = y2 - y1
                
                # Antinode 1 (extend dx, dy from x2, y2)
                ax1, ay1 = x2 + dx, y2 + dy
                
                # Antinode 2 (extend dx, dy from x1, y1)
                ax2, ay2 = x1 - dx, y1 - dy

                antinode_positions.add((ax1, ay1))
                antinode_positions.add((ax2, ay2))

    return antinode_positions

def count_antinodes_in_bounds(input_map, antinode_positions):
    map_lines = input_map.strip().split("\n")
    height = len(map_lines)
    width = len(map_lines[0])

    count = 0
    for x, y in antinode_positions:
        if 0 <= x < width and 0 <= y < height:
            count += 1

    return count

# Process the uploaded file's input
file_path = '2024/08/input.txt'
with open(file_path, 'r') as file:
    input_map = file.read()

# Parse input map
antennas = parse_map(input_map)

# Calculate antinodes
antinodes = calculate_antinodes(antennas)

# Count unique antinodes within map bounds
result = count_antinodes_in_bounds(input_map, antinodes)
result

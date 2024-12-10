# Redefining all functions and processing the input again

from collections import deque

def parse_topographic_map(file_path):
    """
    Parse the topographic map from the input file into a 2D grid of integers.
    """
    with open(file_path, 'r') as f:
        grid = [[int(char) for char in line.strip()] for line in f.readlines()]
    return grid

def find_trailheads(grid):
    """
    Identify all positions in the grid with height 0 (trailheads).
    """
    trailheads = []
    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            if height == 0:
                trailheads.append((x, y))
    return trailheads

def dfs_count_paths(grid, x, y, visited):
    """
    Count distinct paths from the current position (x, y) to height 9.
    """
    if grid[y][x] == 9:
        return 1

    count = 0
    visited.add((x, y))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if (nx, ny) not in visited and grid[ny][nx] == grid[y][x] + 1:
                count += dfs_count_paths(grid, nx, ny, visited)

    visited.remove((x, y))
    return count

def calculate_trailhead_ratings(grid, trailheads):
    """
    Calculate the rating for each trailhead, which is the number of distinct hiking trails.
    """
    total_rating = 0
    for x, y in trailheads:
        total_rating += dfs_count_paths(grid, x, y, set())
    return total_rating

# Reload and process the input file
file_path= '2024/10/input.txt'
grid = parse_topographic_map(file_path)
trailheads = find_trailheads(grid)
total_rating = calculate_trailhead_ratings(grid, trailheads)

print(total_rating)


# # Read the disk map from input file
# with open('2024/09/input.txt', 'r') as file:
#     disk_map_str = file.read().strip()

# # Parse the disk map into lengths of files and free spaces
# block_lengths = [int(c) for c in disk_map_str]

# # Build the initial disk blocks representation
# def build_disk_blocks(block_lengths):
#     disk_blocks = []
#     file_id = 0
#     is_file = True

#     for length in block_lengths:
#         if is_file:
#             # Add file blocks with current file ID
#             disk_blocks.extend([file_id] * length)
#             file_id += 1
#         else:
#             # Add free space blocks
#             disk_blocks.extend(['.'] * length)
#         is_file = not is_file  # Toggle between file and free space
#     return disk_blocks

# # Function to calculate checksum
# def calculate_checksum(disk_blocks):
#     checksum = 0
#     for position, block in enumerate(disk_blocks):
#         if block != '.':
#             checksum += position * block  # block is the file ID
#     return checksum

# # Part One: Simulate the compaction process by moving blocks one at a time
# disk_blocks_part1 = build_disk_blocks(block_lengths)

# # Simulate the compaction process for Part One
# disk_blocks = disk_blocks_part1.copy()
# while True:
#     try:
#         # Find the leftmost free space
#         free_index = disk_blocks.index('.')
#     except ValueError:
#         # No free space left, compaction is complete
#         break

#     # Find the rightmost file block
#     last_file_index = None
#     for i in range(len(disk_blocks) - 1, -1, -1):
#         if disk_blocks[i] != '.':
#             last_file_index = i
#             break

#     if last_file_index is None or last_file_index <= free_index:
#         # No more file blocks to move or no free space ahead of files
#         break

#     # Move the file block to the free space
#     disk_blocks[free_index] = disk_blocks[last_file_index]
#     disk_blocks[last_file_index] = '.'

# # Calculate the filesystem checksum for Part One
# checksum_part1 = calculate_checksum(disk_blocks)

# # Part Two: Reset disk_blocks and perform file-based compaction
# disk_blocks_part2 = build_disk_blocks(block_lengths)

# # Get list of files with their starting indices and lengths
# files = []
# current_index = 0
# file_id = 0
# is_file = True

# for length in block_lengths:
#     if is_file:
#         files.append({'id': file_id, 'start': current_index, 'length': length})
#         file_id += 1
#     current_index += length
#     is_file = not is_file

# # Find all free space spans with their starting indices and lengths
# def find_free_spaces(disk_blocks):
#     free_spaces = []
#     in_free_space = False
#     start = 0
#     for i, block in enumerate(disk_blocks):
#         if block == '.' and not in_free_space:
#             in_free_space = True
#             start = i
#         elif block != '.' and in_free_space:
#             in_free_space = False
#             free_spaces.append({'start': start, 'length': i - start})
#     if in_free_space:
#         free_spaces.append({'start': start, 'length': len(disk_blocks) - start})
#     return free_spaces

# # Process files in decreasing order of file ID
# disk_blocks = disk_blocks_part2.copy()
# for file in sorted(files, key=lambda x: -x['id']):
#     # Find free spaces to the left of the file's current position
#     free_spaces = find_free_spaces(disk_blocks)
#     possible_spaces = [fs for fs in free_spaces if fs['length'] >= file['length'] and fs['start'] < file['start']]
#     if possible_spaces:
#         # Move file to the leftmost possible free space
#         target_space = min(possible_spaces, key=lambda x: x['start'])
#         # Move the file blocks
#         for i in range(file['length']):
#             disk_blocks[target_space['start'] + i] = file['id']
#             disk_blocks[file['start'] + i] = '.'
#         # Update the file's start position
#         file['start'] = target_space['start']

# # Calculate the filesystem checksum for Part Two
# checksum_part2 = calculate_checksum(disk_blocks)

# # Print both checksums
# print("Part One - Filesystem checksum:", checksum_part1)
# print("Part Two - Filesystem checksum:", checksum_part2)
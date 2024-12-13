from collections import deque
vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()
    regions = []

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue

            queue = deque([(r, c)])
            area = 0
            perimeter = 0
            perimeter_sides = {}
            cells = set()

            while queue:
                x, y = queue.popleft()
                if (x, y) in seen:
                    continue
                seen.add((x, y))
                cells.add((x, y))
                area += 1

                for dx, dy in vectors:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y]:
                        queue.append((nx, ny))
                    else:
                        perimeter += 1
                        if (dx, dy) not in perimeter_sides:
                            perimeter_sides[(dx, dy)] = set()
                        perimeter_sides[(dx, dy)].add((x, y))

            regions.append((area, perimeter, perimeter_sides, cells))

    return regions

with open("2024/12/input.txt","r") as f:
    grid = [line.strip() for line in f.readlines()]

regions = find_regions(grid)
part1 = 0
for area, perimeter, _, _ in regions:
    part1 += area * perimeter
print(part1)

regions = find_regions(grid)
part2 = 0

for _, _, perimeter_sides, cells in regions:
    sides = 0
    for direction, border_cells in perimeter_sides.items():
        seen_perimeter = set()
        for px, py in border_cells:
            if (px, py) in seen_perimeter:
                continue

            sides += 1
            perimeter_queue = deque([(px, py)])
            while perimeter_queue:
                sx, sy = perimeter_queue.popleft()
                if (sx, sy) in seen_perimeter:
                    continue

                seen_perimeter.add((sx, sy))
                for dx, dy in vectors:
                    nsx, nsy = sx + dx, sy + dy
                    if (nsx, nsy) in border_cells:
                        perimeter_queue.append((nsx, nsy))

    part2 += len(cells) * sides

print(part2)

#part-1

# Load the input file and process the garden map
input_file_path = '/mnt/data/input.txt'

# Read the garden map
with open(input_file_path, 'r') as file:
    garden_map = [line.strip() for line in file.readlines()]

# Define directions for checking neighbors
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to calculate area and perimeter of a region
def calculate_region_properties(garden_map, visited, x, y, plant_type):
    rows, cols = len(garden_map), len(garden_map[0])
    stack = [(x, y)]
    area = 0
    perimeter = 0
    
    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        area += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if garden_map[nx][ny] == plant_type and not visited[nx][ny]:
                    stack.append((nx, ny))
                elif garden_map[nx][ny] != plant_type:
                    perimeter += 1
            else:
                perimeter += 1  # Edge of the map
    
    return area, perimeter

# Calculate total price for fencing all regions
def calculate_total_price(garden_map):
    rows, cols = len(garden_map), len(garden_map[0])
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0
    
    for x in range(rows):
        for y in range(cols):
            if not visited[x][y]:
                plant_type = garden_map[x][y]
                area, perimeter = calculate_region_properties(garden_map, visited, x, y, plant_type)
                total_price += area * perimeter
    
    return total_price

# Compute the result
total_price = calculate_total_price(garden_map)
total_price
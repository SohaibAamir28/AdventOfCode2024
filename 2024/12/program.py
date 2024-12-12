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
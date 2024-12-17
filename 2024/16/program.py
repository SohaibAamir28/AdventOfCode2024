from collections import deque
from typing import List, Set, Tuple


class MazeSolver:
    def __init__(self, maze: List[List[str]]):
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])
        self.start, self.end = self._find_start_end()

    def _find_start_end(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        start = end = None
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 'S':
                    start = (y, x)
                elif self.maze[y][x] == 'E':
                    end = (y, x)
        return start, end

    def find_optimal_tiles(self) -> int:
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # First pass: Find minimum score to end from each position and direction
        best_scores = {}  # (y, x, dir) -> min_score
        queue = deque([(self.start[0], self.start[1], 0, 0)])  # y, x, dir, score
        min_end_score = float('inf')

        while queue:
            y, x, dir, score = queue.popleft()

            if score >= min_end_score:
                continue

            state = (y, x, dir)
            if state in best_scores and best_scores[state] <= score:
                continue
            best_scores[state] = score

            # Found end
            if (y, x) == self.end:
                min_end_score = min(min_end_score, score)
                continue

            # Try moving forward
            ny, nx = y + directions[dir][0], x + directions[dir][1]
            if (0 <= ny < self.height and 0 <= nx < self.width and
                self.maze[ny][nx] != '#'):
                queue.append((ny, nx, dir, score + 1))

            # Try turning
            queue.append((y, x, (dir - 1) % 4, score + 1000))
            queue.append((y, x, (dir + 1) % 4, score + 1000))

        # Second pass: Find tiles that are part of optimal paths
        optimal_tiles = set()
        visited = set()
        queue = deque([(self.start[0], self.start[1], 0, 0, {(self.start[0], self.start[1])})])

        while queue:
            y, x, dir, score, path = queue.popleft()

            if score > min_end_score:
                continue

            state = (y, x, dir)
            if score > best_scores.get(state, float('inf')):
                continue

            if (y, x) == self.end and score == min_end_score:
                optimal_tiles.update(path)
                continue

            # Try moving forward
            ny, nx = y + directions[dir][0], x + directions[dir][1]
            if (0 <= ny < self.height and 0 <= nx < self.width and
                self.maze[ny][nx] != '#'):
                new_path = path | {(ny, nx)}
                queue.append((ny, nx, dir, score + 1, new_path))

            # Try turning
            queue.append((y, x, (dir - 1) % 4, score + 1000, path.copy()))
            queue.append((y, x, (dir + 1) % 4, score + 1000, path.copy()))

        return len(optimal_tiles)


def visualize_path(maze: List[List[str]], optimal_tiles: Set[Tuple[int, int]]) -> None:
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if (y, x) in optimal_tiles:
                if maze[y][x] in ['S', 'E']:
                    print(maze[y][x], end='')
                else:
                    print('O', end='')
            else:
                print(maze[y][x], end='')
        print()


def main():
    # Read input from file
    with open("2024/16/input.txt", "r") as file:
        input_data = file.read().strip()

    maze = [list(line) for line in input_data.splitlines()]
    solver = MazeSolver(maze)
    result = solver.find_optimal_tiles()
    print(f"Number of tiles in optimal paths: {result}")

    # Optional: Visualize the maze with optimal tiles
    optimal_tiles = solver.find_optimal_tiles()
    visualize_path(maze, optimal_tiles)


if __name__ == "__main__":
    main()


# import heapq

# # Directions: Right, Down, Left, Up
# DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# DIRECTION_COST = 1000  # Cost for changing direction
# MOVE_COST = 1          # Cost for moving forward

# def parse_input(file_path):
#     with open(file_path, 'r') as file:
#         grid = [list(line.strip()) for line in file.readlines()]
#     start, end = None, None
#     for r, row in enumerate(grid):
#         for c, cell in enumerate(row):
#             if cell == 'S':
#                 start = (r, c)
#             elif cell == 'E':
#                 end = (r, c)
#     return grid, start, end

# def in_bounds(grid, r, c):
#     return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#'

# def find_lowest_score(grid, start, end):
#     # Priority queue: (cost, x, y, direction)
#     pq = [(0, start[0], start[1], 0)]
#     visited = set()

#     while pq:
#         cost, x, y, direction = heapq.heappop(pq)
#         if (x, y) == end:
#             return cost
#         if (x, y, direction) in visited:
#             continue
#         visited.add((x, y, direction))
#         for new_dir, (dx, dy) in enumerate(DIRECTIONS):
#             nx, ny = x + dx, y + dy
#             if in_bounds(grid, nx, ny):
#                 new_cost = cost + MOVE_COST
#                 if new_dir != direction:
#                     new_cost += DIRECTION_COST
#                 heapq.heappush(pq, (new_cost, nx, ny, new_dir))
#     return -1  # If no path is found

# def main():
#     file_path = '2024/16/input.txt'  # Replace with your input file
#     grid, start, end = parse_input(file_path)
#     lowest_score = find_lowest_score(grid, start, end)
#     print(f"Lowest Score: {lowest_score}")

# if __name__ == '__main__':
#     main()

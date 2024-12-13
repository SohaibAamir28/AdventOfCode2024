#part 2 
from sympy import symbols, Eq, solve
import re

# Define variables for calculations
a, b = symbols('a b', integer=True)

# Function to parse machine data from multi-line input
def parse_multiline_machine(lines):
    if len(lines) == 3:
        button_a = re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])
        button_b = re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])
        prize = re.match(r"Prize: X=(\d+), Y=(\d+)", lines[2])
        if button_a and button_b and prize:
            return tuple(map(int, button_a.groups() + button_b.groups() + prize.groups()))
    return None

# Function to compute solutions for a list of machines
def compute_solutions(machines, offset_x=0, offset_y=0):
    results = []
    for Ax, Ay, Bx, By, Px, Py in machines:
        # Apply offset if provided
        Px += offset_x
        Py += offset_y
        
        # Solve the system of equations
        eq1 = Eq(a * Ax + b * Bx, Px)
        eq2 = Eq(a * Ay + b * By, Py)
        solutions = solve((eq1, eq2), (a, b), dict=True)
        valid_solutions = [
            (sol[a], sol[b]) for sol in solutions if sol[a] >= 0 and sol[b] >= 0
        ]
        
        # Find the minimum token cost
        min_cost = float('inf')
        best_sol = None
        for sol_a, sol_b in valid_solutions:
            cost = 3 * sol_a + sol_b
            if cost < min_cost:
                min_cost = cost
                best_sol = (sol_a, sol_b)
        if best_sol:
            results.append((min_cost, best_sol))

    # Calculate total cost and machines solved
    results.sort()
    total_cost = sum(cost for cost, _ in results)
    machines_solved = len(results)

    return total_cost, machines_solved


inputFile = "2024/13/input.txt"  # Adjust this to the actual file path

# Parse input data
with open(inputFile, 'r') as f:
    raw_lines = [line.strip() for line in f if line.strip()]

# Group every 3 lines into a machine
machines = [parse_multiline_machine(raw_lines[i:i+3]) for i in range(0, len(raw_lines), 3)]
parsed_machines = [machine for machine in machines if machine is not None]

# Part 2: Solve with large offsets
OFFSET = 10_000_000_000_000
part2_total_cost, part2_machines_solved = compute_solutions(parsed_machines, offset_x=OFFSET, offset_y=OFFSET)

print(part2_total_cost)

# Answer -> 73458657399094
# part 1
# from itertools import product

# def find_minimum_tokens(A, B, prize_x, prize_y, max_presses=100):
#     """
#     Finds the minimum tokens required to align the claw machine with the prize.

#     Parameters:
#         A (tuple): Movement and cost for Button A (dx, dy, cost).
#         B (tuple): Movement and cost for Button B (dx, dy, cost).
#         prize_x (int): Target X-coordinate of the prize.
#         prize_y (int): Target Y-coordinate of the prize.
#         max_presses (int): Maximum number of presses for each button.

#     Returns:
#         int: Minimum tokens required to align with the prize, or None if not possible.
#     """
#     dx_a, dy_a, cost_a = A
#     dx_b, dy_b, cost_b = B

#     min_tokens = None

#     for presses_a in range(max_presses + 1):
#         for presses_b in range(max_presses + 1):
#             total_x = dx_a * presses_a + dx_b * presses_b
#             total_y = dy_a * presses_a + dy_b * presses_b

#             if total_x == prize_x and total_y == prize_y:
#                 tokens = presses_a * cost_a + presses_b * cost_b
#                 if min_tokens is None or tokens < min_tokens:
#                     min_tokens = tokens

#     return min_tokens

# def solve_all_machines(input_data):
#     """
#     Solves for the minimum tokens required to win the maximum number of prizes.

#     Parameters:
#         input_data (str): The input data containing machine configurations as a string.

#     Returns:
#         int: Total tokens required to win the maximum number of prizes.
#     """
#     lines = input_data.strip().split("\n\n")

#     total_tokens = 0
#     won_prizes = 0

#     for machine in lines:
#         machine_lines = machine.split("\n")
#         A = tuple(map(int, machine_lines[0].split("X+")[1].split(", Y+") + [3]))
#         B = tuple(map(int, machine_lines[1].split("X+")[1].split(", Y+") + [1]))
#         prize_x, prize_y = map(int, machine_lines[2].split("X=")[1].split(", Y="))

#         tokens = find_minimum_tokens(A, B, prize_x, prize_y)

#         if tokens is not None:
#             total_tokens += tokens
#             won_prizes += 1

#     return total_tokens, won_prizes

# if __name__ == "__main__":
#     with open("input.txt", "r") as file:
#         input_data = file.read()

#     total_tokens, won_prizes = solve_all_machines(input_data)
#     print(f"Total Tokens: {total_tokens}")


    # main("2024/13/input.txt")

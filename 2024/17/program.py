#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re


INPUT_FILENAME = "2024/17/input.txt"
# INPUT_FILENAME = "sample17.txt"

data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

registers = {}

for line in data:
    if match := re.match(r'Register (\w): (\d+)', line):
        registers[match.group(1)] = int(match.group(2))
    elif match := re.match('Program: (.*)', line):
        program = list(map(int, match.group(1).split(',')))

def run(program, registers):
    registers = registers.copy()
    ip = 0

    def get_combo(operand):
        if operand == 7:
            raise ValueError("invalid program")

        if operand < 4:
            return operand
        return registers["ABC"[operand-4]]

    output = []

    while True:
        opcode = program[ip]
        operand = program[ip+1]

        match opcode:
            case 0:
                registers['A'] = registers['A'] // (2 ** get_combo(operand))
            case 1:
                registers['B'] = registers['B'] ^ operand
            case 2:
                registers['B'] = get_combo(operand) % 8
            case 3:
                if registers['A'] != 0:
                    ip = operand - 2
            case 4:
                registers['B'] = registers['B'] ^ registers['C']
            case 5:
                output.append(get_combo(operand) % 8)
            case 6:
                registers['B'] = registers['A'] // (2 ** get_combo(operand))
            case 7:
                registers['C'] = registers['A'] // (2 ** get_combo(operand))
            case _:
                raise ValueError(f"invalid opcode {opcode}")

        ip += 2
        if ip >= len(program):
            break
    return output

print("part1:", ",".join(map(str, run(program, registers))))

def solve(n=None, offset=0):
    if n is None:
        n = len(program) - 1

    solutions = set()

    for i in range(0, 8 ** (n + 1), 8 ** n):
        registers['A'] = offset + i
        result = run(program, registers)

        if len(result) != len(program):
            continue

        solved_n = n
        while result[solved_n] == program[solved_n]:
            solved_n -= 1
            if solved_n < 0:
                solutions.add(offset + i)
                break

        if solved_n >= 0 and n != solved_n:
            # print(f"n={n}, solved_n={solved_n}, offset={offset+i}, result={result}")
            solutions.update(solve(n - 1, offset + i))

    return solutions

print("part2:", min(solve()))

# def run_program(registers, program):
#     # Registers A, B, and C
#     A, B, C = registers
    
#     # Instruction pointer starts at 0
#     ip = 0
    
#     # Output list
#     output = []
    
#     while ip < len(program):
#         opcode = program[ip]
#         operand = program[ip + 1]
        
#         # Opcodes
#         if opcode == 0:  # adv
#             A //= (2 ** operand if operand <= 3 else 2 ** [A, B, C][operand - 4])
#         elif opcode == 1:  # bxl
#             B ^= operand
#         elif opcode == 2:  # bst
#             B = operand % 8 if operand <= 3 else [A, B, C][operand - 4] % 8
#         elif opcode == 3:  # jnz
#             if A != 0:
#                 ip = operand
#                 continue
#         elif opcode == 4:  # bxc
#             B ^= C
#         elif opcode == 5:  # out
#             value = operand % 8 if operand <= 3 else [A, B, C][operand - 4] % 8
#             output.append(value)
#         elif opcode == 6:  # bdv
#             B = A // (2 ** operand if operand <= 3 else 2 ** [A, B, C][operand - 4])
#         elif opcode == 7:  # cdv
#             C = A // (2 ** operand if operand <= 3 else 2 ** [A, B, C][operand - 4])
        
#         # Increment instruction pointer
#         ip += 2
    
#     return ",".join(map(str, output))


# if __name__ == "__main__":
#     # Initial register values
#     registers = [64854237, 0, 0]  # A = 64854237, B = 0, C = 0
    
#     # Program input
#     program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 0, 5, 5, 0, 3, 3, 0]
    
#     # Run the program and get the output
#     result = run_program(registers, program)
    
#     # Print the result
#     print("Final Output:", result)

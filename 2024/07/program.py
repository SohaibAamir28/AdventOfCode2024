from itertools import product

def parse_input(file_path):
    """
    Parse the input file into a list of (test_value, numbers).
    """
    equations = []
    with open(file_path) as f:
        for line in f:
            if line.strip():
                test_value, numbers = line.split(":")
                test_value = int(test_value.strip())
                numbers = list(map(int, numbers.split()))
                equations.append((test_value, numbers))
    return equations


def evaluate_with_concat(test_value, numbers):
    """
    Evaluate the equation with all combinations of +, *, and || operators.
    Return True if any combination results in the test value.
    """
    num_positions = len(numbers) - 1
    operators = ['+', '*', '||']
    for ops in product(operators, repeat=num_positions):
        result = numbers[0]
        try:
            for num, op in zip(numbers[1:], ops):
                if op == '+':
                    result += num
                elif op == '*':
                    result *= num
                elif op == '||':
                    result = int(str(result) + str(num))
            if result == test_value:
                return True
        except OverflowError:
            continue
    return False


def calculate_total_with_concat(equations):
    """
    Calculate the total calibration result including concatenation operator.
    """
    total = 0
    for test_value, numbers in equations:
        if evaluate_with_concat(test_value, numbers):
            total += test_value
    return total


# Parse the input file
file_path = '2024/07/input.txt'
equations = parse_input(file_path)

# Calculate the total calibration result including concatenation operator
total_calibration_result = calculate_total_with_concat(equations)
print(total_calibration_result)



# from itertools import product

# def parse_input(file_path):
#     """
#     Parse the input file into a list of (test_value, numbers).
#     """
#     equations = []
#     with open(file_path) as f:
#         for line in f:
#             if line.strip():
#                 test_value, numbers = line.split(":")
#                 test_value = int(test_value.strip())
#                 numbers = list(map(int, numbers.split()))
#                 equations.append((test_value, numbers))
#     return equations


# def evaluate_equation(test_value, numbers):
#     """
#     Evaluate the equation with all combinations of + and * operators.
#     Return True if any combination results in the test value.
#     """
#     num_positions = len(numbers) - 1
#     for operators in product(['+', '*'], repeat=num_positions):
#         result = numbers[0]
#         for num, op in zip(numbers[1:], operators):
#             if op == '+':
#                 result += num
#             elif op == '*':
#                 result *= num
#         if result == test_value:
#             return True
#     return False


# def calculate_calibration_result(equations):
#     """
#     Calculate the total calibration result by summing test values of valid equations.
#     """
#     total = 0
#     for test_value, numbers in equations:
#         if evaluate_equation(test_value, numbers):
#             total += test_value
#     return total


# def main():
#     """
#     Main function to solve the problem.
#     """
#     # Update this to your input file path
#     file_path = '2024/07/input.txt'
#     equations = parse_input(file_path)
#     calibration_result = calculate_calibration_result(equations)
#     print(f"Total calibration result: {calibration_result}")


# if __name__ == "__main__":
#     main()

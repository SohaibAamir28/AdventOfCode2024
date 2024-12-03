import re

f = open("2024/03/input.txt").read().strip()

# Define the regex pattern to find valid mul(X, Y) instructions
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all valid mul instructions
matches = re.finditer(pattern, f)

# Variables to keep track of whether mul instructions are enabled
enabled = True
result_sum = 0

# Define the regex patterns for do() and don't() instructions
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Iterate through the matches and check for do() and don't() instructions
for match in matches:
    # Check for do() and don't() instructions before each mul instruction
    preceding_text = f[:match.start()]
    last_do = preceding_text.rfind("do()")
    last_dont = preceding_text.rfind("don't()")
    
    if last_dont > last_do:
        enabled = False
    else:
        enabled = True
    
    if enabled:
        x, y = match.groups()
        result_sum += int(x) * int(y)

print("Day 3: Sum of all valid multiplications with conditions: " + str(result_sum))


# import re

# f = open("2024/03/input.txt").read().strip()

# # Define the regex pattern to find valid mul(X, Y) instructions
# pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# # Find all valid mul instructions
# matches = re.findall(pattern, f)

# # Calculate the sum of all results
# result_sum = sum(int(x) * int(y) for x, y in matches)

# print("Day 3: Sum of all valid multiplications: " + str(result_sum))

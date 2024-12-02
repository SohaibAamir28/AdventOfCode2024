
f = open("2024/02/input.txt").read().strip().split("\n")

safe_count = 0

def is_safe(report):
    levels = list(map(int, report.split()))
    increasing = True
    decreasing = True
    
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if diff < -3 or diff > 3 or diff == 0:
            return False
        if diff > 0:
            decreasing = False
        if diff < 0:
            increasing = False
    
    return increasing or decreasing

def is_safe_with_removal(report):
    levels = list(map(int, report.split()))
    if is_safe(report):
        return True
    
    # Try removing each level and check if the report becomes safe
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe(" ".join(map(str, modified_levels))):
            return True
    
    return False

for report in f:
    if is_safe_with_removal(report):
        safe_count += 1

print("Day 2: Number of safe reports: " + str(safe_count))


# f = open("2024/02/input.txt").read().strip().split("\n")

# safe_count = 0

# def is_safe(report):
#     levels = list(map(int, report.split()))
#     increasing = True
#     decreasing = True
    
#     for i in range(1, len(levels)):
#         diff = levels[i] - levels[i - 1]
#         if diff < -3 or diff > 3 or diff == 0:
#             return False
#         if diff > 0:
#             decreasing = False
#         if diff < 0:
#             increasing = False
    
#     return increasing or decreasing

# for report in f:
#     if is_safe(report):
#         safe_count += 1

# print("Day 2: Number of safe reports: " + str(safe_count))

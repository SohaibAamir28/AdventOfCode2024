# from collections import defaultdict

# def is_valid_order(order, rules):
#     # Check if the given order satisfies all the rules
#     for x, y in rules:
#         if x in order and y in order:
#             if order.index(x) > order.index(y):
#                 return False
#     return True

# def count_valid_updates(rules, updates):
#     valid_updates = []
#     for update in updates:
#         if is_valid_order(update, rules):
#             valid_updates.append(update)
#     return valid_updates

# def parse_input(file_path):
#     with open(file_path) as f:
#         lines = f.read().strip().split("\n")
    
#     # Split into rules and updates sections
#     split_index = lines.index("")
#     rules_section = lines[:split_index]
#     updates_section = lines[split_index + 1:]
    
#     # Parse rules
#     rules = []
#     for rule in rules_section:
#         x, y = map(int, rule.split("|"))
#         rules.append((x, y))
    
#     # Parse updates
#     updates = []
#     for update in updates_section:
#         updates.append(list(map(int, update.split(","))))
    
#     return rules, updates

# def find_middle_sum(valid_updates):
#     middle_sum = 0
#     for update in valid_updates:
#         middle_index = len(update) // 2
#         middle_sum += update[middle_index]
#     return middle_sum

# # Read the input from the file
# file_path = "2024/05/input.txt"
# rules, updates = parse_input(file_path)

# # Find valid updates
# valid_updates = count_valid_updates(rules, updates)

# # Calculate the sum of middle page numbers
# result = find_middle_sum(valid_updates)
# print("Day 5: Sum of middle page numbers of valid updates: " + str(result))


from collections import defaultdict

def is_valid_order(order, rules):
    # Check if the given order satisfies all the rules
    for x, y in rules:
        if x in order and y in order:
            if order.index(x) > order.index(y):
                return False
    return True

def count_valid_updates(rules, updates):
    valid_updates = []
    invalid_updates = []
    for update in updates:
        if is_valid_order(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return valid_updates, invalid_updates

def parse_input(file_path):
    with open(file_path) as f:
        lines = f.read().strip().split("\n")
    
    # Split into rules and updates sections
    split_index = lines.index("")
    rules_section = lines[:split_index]
    updates_section = lines[split_index + 1:]
    
    # Parse rules
    rules = []
    for rule in rules_section:
        x, y = map(int, rule.split("|"))
        rules.append((x, y))
    
    # Parse updates
    updates = []
    for update in updates_section:
        updates.append(list(map(int, update.split(","))))
    
    return rules, updates

def find_middle_sum(updates):
    middle_sum = 0
    for update in updates:
        middle_index = len(update) // 2
        middle_sum += update[middle_index]
    return middle_sum

def order_update(update, rules):
    # Create a graph of dependencies
    dependency_count = {page: 0 for page in update}
    dependency_graph = defaultdict(list)
    
    for x, y in rules:
        if x in update and y in update:
            dependency_count[y] += 1
            dependency_graph[x].append(y)
    
    # Topological sort using Kahn's algorithm
    ordered = []
    zero_dependency = [page for page in update if dependency_count[page] == 0]
    
    while zero_dependency:
        current = zero_dependency.pop()
        ordered.append(current)
        for neighbor in dependency_graph[current]:
            dependency_count[neighbor] -= 1
            if dependency_count[neighbor] == 0:
                zero_dependency.append(neighbor)
    
    return ordered

# Read the input from the file
file_path = "2024/05/input.txt"
rules, updates = parse_input(file_path)

# Find valid and invalid updates
valid_updates, invalid_updates = count_valid_updates(rules, updates)

# Calculate the sum of middle page numbers for valid updates
valid_sum = find_middle_sum(valid_updates)
print("Day 5: Sum of middle page numbers of valid updates: " + str(valid_sum))

# Correctly order the invalid updates and calculate their middle sum
corrected_updates = [order_update(update, rules) for update in invalid_updates]
corrected_sum = find_middle_sum(corrected_updates)
print("Day 5: Sum of middle page numbers of corrected invalid updates: " + str(corrected_sum))

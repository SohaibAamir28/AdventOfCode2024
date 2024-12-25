from functools import lru_cache

def count_ways_to_form_design(design, patterns):
    @lru_cache(None)
    def helper(remaining_design):
        # Base case: if the design is empty, there's exactly one way to form it (use no towels)
        if remaining_design == "":
            return 1
        
        ways = 0
        # Try to match each pattern with the start of the remaining design
        for pattern in patterns:
            if remaining_design.startswith(pattern):
                # Recur with the rest of the design after removing the pattern
                ways += helper(remaining_design[len(pattern):])
        
        return ways

    return helper(design)

def total_ways_to_form_designs(patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_form_design(design, tuple(patterns))
    return total_ways

# Parse the input from a file
def parse_input_from_file(file_path):
    with open(file_path, 'r') as file:
        sections = file.read().strip().split("\n\n")
        patterns = sections[0].split(", ")
        designs = sections[1].split("\n")
    return patterns, designs

# Main function
def main():
    # Replace 'input.txt' with your actual input file path
    file_path = '2024/19/input.txt'
    patterns, designs = parse_input_from_file(file_path)
    result = total_ways_to_form_designs(patterns, designs)
    print(f"Total number of ways: {result}")

if __name__ == "__main__":
    main()


#part 1


# def can_form_design(design, patterns, memo):
#     # If the design is already checked, return its feasibility
#     if design in memo:
#         return memo[design]
#     # Base case: empty design can always be formed
#     if design == "":
#         return True

#     # Try to match each pattern
#     for pattern in patterns:
#         if design.startswith(pattern):
#             # Recur on the remaining substring
#             if can_form_design(design[len(pattern):], patterns, memo):
#                 memo[design] = True
#                 return True
    
#     # If no pattern matches, the design is impossible
#     memo[design] = False
#     return False

# def count_possible_designs(patterns, designs):
#     memo = {}
#     count = 0
#     for design in designs:
#         if can_form_design(design, patterns, memo):
#             count += 1
#     return count

# # Parse the input from a file
# def parse_input_from_file(file_path):
#     with open(file_path, 'r') as file:
#         sections = file.read().strip().split("\n\n")
#         patterns = sections[0].split(", ")
#         designs = sections[1].split("\n")
#     return patterns, designs

# # Main function
# def main():
#     # Replace 'input.txt' with your actual input file path
#     file_path = '2024/19/input.txt'
#     patterns, designs = parse_input_from_file(file_path)
#     result = count_possible_designs(patterns, designs)
#     print(f"Number of possible designs: {result}")

# if __name__ == "__main__":
#     main()

f = open("2024/01/input.txt").read().strip().split("\n")

# Split the input into two lists (left and right)
left_list = []
right_list = []
for line in f:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Sort both lists for part one calculations
left_list.sort()
right_list.sort()

# Calculate the total distance for Part 1
total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
print("Day 1 Part 1 Total Distance: " + str(total_distance))

# Part 2: Calculate similarity score
from collections import Counter

# Count occurrences of each number in the right list
right_counter = Counter(right_list)

# Calculate the similarity score
similarity_score = 0
for left in left_list:
    similarity_score += left * right_counter[left]

print("Day 1 Part 2 Similarity Score: " + str(similarity_score))

from collections import defaultdict

def read_input(file_name):
    """Reads input from the specified file."""
    with open(file_name, 'r') as file:
        connections = [line.strip().split('-') for line in file]
    return connections

def bron_kerbosch(graph, r, p, x, cliques):
    """Bron-Kerbosch algorithm to find maximal cliques."""
    if not p and not x:
        cliques.append(r)
        return
    for v in list(p):
        bron_kerbosch(
            graph, 
            r.union({v}), 
            p.intersection(graph[v]), 
            x.intersection(graph[v]), 
            cliques
        )
        p.remove(v)
        x.add(v)

def find_maximal_cliques(graph):
    """Finds all maximal cliques in the graph."""
    cliques = []
    bron_kerbosch(graph, set(), set(graph.keys()), set(), cliques)
    return cliques

def find_largest_clique(cliques):
    """Finds the largest clique among all cliques."""
    return max(cliques, key=len)

def generate_password(clique):
    """Generates the password from the largest clique."""
    return ",".join(sorted(clique))

def main():
    # Input file name
    input_file = "2024/23/input.txt"
    
    # Read input connections
    connections = read_input(input_file)
    
    # Build the adjacency list
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    
    # Find all maximal cliques
    cliques = find_maximal_cliques(graph)
    
    # Find the largest clique
    largest_clique = find_largest_clique(cliques)
    
    # Generate the password
    password = generate_password(largest_clique)
    print(f"Password to the LAN party: {password}")

if __name__ == "__main__":
    main()

# from collections import defaultdict

# # Load the input file
# with open("2024/23/input.txt", 'r') as file:
#     connections = [line.strip().split('-') for line in file.readlines()]

# # Build the graph
# graph = defaultdict(set)
# for a, b in connections:
#     graph[a].add(b)
#     graph[b].add(a)

# # Find all triads (sets of three interconnected nodes)
# def find_triads(graph):
#     triads = set()
#     for node in graph:
#         neighbors = graph[node]
#         for neighbor1 in neighbors:
#             for neighbor2 in neighbors:
#                 if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
#                     triad = tuple(sorted([node, neighbor1, neighbor2]))
#                     triads.add(triad)
#     return triads

# triads = find_triads(graph)

# # Filter triads for those containing a node starting with 't'
# triads_with_t = [triad for triad in triads if any(node.startswith('t') for node in triad)]

# # Output the result
# print(len(triads_with_t))
# # 1119
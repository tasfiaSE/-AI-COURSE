# AO* Graph node representation
graph = {
    'A': [('B', 1), ('C', 1), ('D', 1)],  # OR between B, C, D
    'B': [('E', 1), ('F', 1)],            # AND between E and F
    'C': [('G', 1), ('H', 1), ('I', 1)],  # AND between G, H, I
    'D': [],                              # Terminal node
    'E': [], 'F': [], 'G': [], 'H': [], 'I': []  # Terminal nodes
}

# Heuristic values from the image
heuristics = {
    'A': 7,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 6,
    'F': 4,
    'G': 2,
    'H': 0,
    'I': 0
}

# Solution path will be stored here
solution_graph = {}

# Get successors of a node
def get_successors(node):
    return graph.get(node, [])

# Calculate minimum cost child(ren) and its total cost
def minimum_cost_child_node(node):
    children = get_successors(node)

    if not children:
        return None, heuristics[node]

    if node in ['B', 'C']:  # AND-node
        cost = sum(c for _, c in children) + sum(heuristics[child] for child, _ in children)
        return [child for child, _ in children], cost
    else:  # OR-node
        min_cost = float('inf')
        best_child = None
        for child, edge_cost in children:
            total = edge_cost + heuristics[child]
            if total < min_cost:
                min_cost = total
                best_child = child
        return best_child, min_cost

# AO* main recursive function
def AOStar(node, backtrack=False):
    print(f"Processing Node: {node}")
    
    if node not in graph or not graph[node]:
        return

    while True:
        child_node, cost = minimum_cost_child_node(node)
        if heuristics[node] != cost:
            heuristics[node] = cost
            solution_graph[node] = child_node

            if isinstance(child_node, list):
                for child in child_node:
                    AOStar(child)
            else:
                AOStar(child_node)
        else:
            break

# Print the optimal path
def print_solution(node, indent=""):
    if node not in solution_graph:
        print(indent + node)
        return
    print(indent + str(node))
    child = solution_graph[node]
    if isinstance(child, list):
        for ch in child:
            print_solution(ch, indent + "  ")
    else:
        print_solution(child, indent + "  ")

# Run the AO* algorithm from root node 'A'
if __name__ == "__main__":
    AOStar('A')
    print("\nOptimal Solution Path:")
    print_solution('A')

explored = set()
path = []
found = False
limit_crossed = False  # New flag to detect if depth limit is crossed

def depth_limited_search(network, current, depth, limit, goal):
    global found, limit_crossed
    if found:
        return
    if depth > limit:
        limit_crossed = True
        return
    if current == goal:
        found = True
        path.append(current)
        return
    if current not in explored:
        path.append(current)
        explored.add(current)
        for adjacent in network[current]:
            depth_limited_search(network, adjacent, depth + 1, limit, goal)

network = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

start = 'A'
goal = 'D'
limit = 2

depth_limited_search(network, start, 0, limit, goal)

if found:
    print("->".join(path))
elif limit_crossed:
    print(f"Goal node '{goal}' is unreachable within depth limit {limit}.")
else:
    print(f"Goal node '{goal}' does not exist in the network.")

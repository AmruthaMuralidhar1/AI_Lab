def iterative_deepening_search(graph, start, goal):
    depth_limit = 0

    while True:
        result = depth_limited_search(graph, start, goal, depth_limit)
        if result == goal:
            return result  # Goal found
        elif result == 'cutoff':
            depth_limit += 1  # Increase depth limit
        else:
            return None  # Goal not reachable

def depth_limited_search(graph, node, goal, depth_limit):
    return recursive_dls(graph, node, goal, depth_limit)

def recursive_dls(graph, node, goal, depth_limit):
    if node == goal:
        return node  # Goal found
    elif depth_limit == 0:
        return 'cutoff'  # Depth limit reached
    else:
        cutoff_occurred = False
        for neighbor in graph[node]:
            result = recursive_dls(graph, neighbor, goal, depth_limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result is not None:
                return result  # Goal found in the subtree
        return 'cutoff' if cutoff_occurred else None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': ['J'],
    'G': [],
    'H': ['K'],
    'I': [],
    'J': [],
    'K': []
}

start_node = 'A'
goal_node = 'K'

result = iterative_deepening_search(graph, start_node, goal_node)

if result:
    print(f"Goal {goal_node} found in the graph.")
else:
    print(f"Goal {goal_node} not reachable in the graph.")

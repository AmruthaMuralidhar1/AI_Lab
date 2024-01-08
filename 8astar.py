from queue import PriorityQueue

# Helper function to find the index of a value in the puzzle state
def find_index(puzzle, value):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == value:
                return i, j

# Helper function to calculate the Manhattan distance heuristic
def manhattan_distance(puzzle, goal):
    distance = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != 0:
                goal_i, goal_j = find_index(goal, puzzle[i][j])
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# A* algorithm implementation
def solve_8_puzzle(start, goal):
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    moves_text = ['left', 'right', 'up', 'down']

    visited = set()
    pq = PriorityQueue()
    pq.put((0, start, []))

    while not pq.empty():
        _, current_state, path = pq.get()
        print("\n")
        for row in current_state:
            print(row)
        if current_state == goal:
            return path

        if tuple(map(tuple, current_state)) not in visited:
            visited.add(tuple(map(tuple, current_state)))
            zero_i, zero_j = find_index(current_state, 0)

            for move, move_text in zip(moves, moves_text):
                new_i, new_j = zero_i + move[0], zero_j + move[1]
                if 0 <= new_i < 3 and 0 <= new_j < 3:
                    new_state = [row[:] for row in current_state]
                    new_state[zero_i][zero_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[zero_i][zero_j]
                    priority = len(path) + 1 + manhattan_distance(new_state, goal)
                    pq.put((priority, new_state, path + [move_text]))

    return None

# Example puzzle
start_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

solution = solve_8_puzzle(start_state, goal_state)
if solution:
    print("\nSolution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")

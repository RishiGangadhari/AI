from collections import deque
import copy

initial_state = ['E', 'E', 'E', '_', 'W', 'W', 'W']
goal_state = ['W', 'W', 'W', '_', 'E', 'E', 'E']

def get_neighbors(state):
    neighbors = []
    idx = state.index('_')
    for move in [-1, -2, 1, 2]:
        new_idx = idx + move
        if 0 <= new_idx < len(state):
            # 1 step move
            if abs(move) == 1:
                new_state = state.copy()
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                neighbors.append(new_state)
            # jump over one rabbit
            elif abs(move) == 2 and state[idx + move // 2] != '_' and state[idx + move // 2] != state[new_idx]:
                new_state = state.copy()
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                neighbors.append(new_state)
    return neighbors

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        state = path[-1]
        state_tuple = tuple(state)

        if state == goal:
            return path

        if state_tuple not in visited:
            visited.add(state_tuple)
            for neighbor in get_neighbors(state):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

def dfs(start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        state = path[-1]
        state_tuple = tuple(state)

        if state == goal:
            return path

        if state_tuple not in visited:
            visited.add(state_tuple)
            for neighbor in get_neighbors(state):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None

# Example usage:
print("BFS Solution:")
for step in bfs(initial_state, goal_state):
    print(step)

print("\nDFS Solution:")
for step in dfs(initial_state, goal_state):
    print(step)
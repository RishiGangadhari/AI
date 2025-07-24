from collections import deque

# Person and crossing time
people = {
    'A': 5,   # Amogh
    'B': 10,  # Ameya
    'C': 20,  # Grandmother
    'D': 25   # Grandfather
}

# Initial state: (left side, right side, is_umbrella_left, time_spent)
def bfs_bridge():
    start = (frozenset(people.keys()), frozenset(), True, 0)
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        current_state = path[-1]
        left, right, is_left, time_spent = current_state

        if time_spent > 60:
            continue

        if len(left) == 0 and not is_left:
            return path  # Everyone crossed

        state_key = (left, right, is_left)
        if state_key in visited:
            continue
        visited.add(state_key)

        if is_left:
            # Choose 1 or 2 to cross
            for p1 in left:
                for p2 in left:
                    if p1 <= p2:  # avoid permutations
                        new_left = set(left)
                        new_right = set(right)
                        new_left.remove(p1)
                        if p1 != p2:
                            new_left.remove(p2)
                            new_right.update([p1, p2])
                            time = max(people[p1], people[p2])
                        else:
                            new_right.add(p1)
                            time = people[p1]
                        new_state = (frozenset(new_left), frozenset(new_right), False, time_spent + time)
                        queue.append(path + [new_state])
        else:
            # One person returns with umbrella
            for p in right:
                new_left = set(left)
                new_right = set(right)
                new_right.remove(p)
                new_left.add(p)
                time = people[p]
                new_state = (frozenset(new_left), frozenset(new_right), True, time_spent + time)
                queue.append(path + [new_state])
    return None

# Example
solution = bfs_bridge()
if solution:
    print("Bridge Crossing Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found within 60 minutes.")
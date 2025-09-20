from collections import deque
from math import gcd

def is_solvable(A, B, T):
    """Check if target T is measurable with jugs A and B."""
    return T <= max(A, B) and T % gcd(A, B) == 0

def water_jug_bfs(A, B, T):
    """Solve the water jug problem using BFS and return the sequence of steps."""
    if not is_solvable(A, B, T):
        return [("Not solvable", (0, 0))]

    start = (0, 0)  
    q = deque([(start, ["Start at (0,0)"])])
    visited = {start}

    while q:
        (a, b), path = q.popleft()

        
        if a == T or b == T:
            return path

        
        next_states = [
            ((A, b), "Fill A"),
            ((a, B), "Fill B"),
            ((0, b), "Empty A"),
            ((a, 0), "Empty B"),
        ]

        
        pour = min(a, B - b)
        next_states.append(((a - pour, b + pour), "Pour A→B"))

        
        pour = min(b, A - a)
        next_states.append(((a + pour, b - pour), "Pour B→A"))

        
        for (na, nb), action in next_states:
            if (na, nb) not in visited:
                visited.add((na, nb))
                q.append(((na, nb), path + [f"{action} → ({na},{nb})"]))

    return [("No solution found", (0, 0))]


if __name__ == "__main__":
    A = int(input("Enter capacity of Jug A: "))
    B = int(input("Enter capacity of Jug B: "))
    T = int(input("Enter target amount: "))

    steps = water_jug_bfs(A, B, T)
    print("\n--- Steps to Solve ---")
    for s in steps:
        print(s)

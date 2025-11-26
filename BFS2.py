from collections import deque

def bfs(graph, start):
    q = deque([start])     # queue with starting node
    visited = {start}      # mark start as visited

    while q:
        node = q.popleft()
        print(node)

        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

# Simple graph
graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

bfs(graph, 1)

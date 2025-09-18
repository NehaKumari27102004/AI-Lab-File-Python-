from collections import deque

def bfsDisconnected(adj):
    V, res = len(adj), []
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            q = deque([i])
            visited[i] = True
            while q:
                node = q.popleft()
                res.append(node)
                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
    return res

n, m = map(int, input("Enter number of vertices and edges: ").split())
adj = [[] for _ in range(n)]

print("Enter edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  

print("BFS Traversal:", *bfsDisconnected(adj))

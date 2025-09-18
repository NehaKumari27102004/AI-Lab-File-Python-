def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# 📥 Input
v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Initialize graph
graph = {i: [] for i in range(v)}

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # For undirected graph

# 🚀 DFS Traversal
start = int(input("Enter starting vertex: "))
print("DFS Traversal:")
dfs(graph, start, set())

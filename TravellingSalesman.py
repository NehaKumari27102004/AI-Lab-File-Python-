import sys

def tsp(graph):
    n = len(graph)
    VISITED_ALL = (1 << n) - 1   
    dp = [[None] * n for _ in range(1 << n)]

    def visit(mask, pos):
        
        if mask == VISITED_ALL:
            return graph[pos][0]

       
        if dp[mask][pos] is not None:
            return dp[mask][pos]

        ans = sys.maxsize
        
        for city in range(n):
            if mask & (1 << city) == 0:
                new_cost = graph[pos][city] + visit(mask | (1 << city), city)
                ans = min(ans, new_cost)

        dp[mask][pos] = ans
        return ans

    return visit(1, 0)  


n = int(input("Enter number of cities: "))
graph = []

print("Enter the adjacency matrix (distance between cities):")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

print("\nMinimum cost of travelling all cities:", tsp(graph))

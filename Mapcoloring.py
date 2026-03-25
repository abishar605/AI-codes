# Map Coloring using Backtracking
# Colors given by user
def is_safe(v, graph, color, c, V):
 for i in range(V):
 if graph[v][i] == 1 and color[i] == c:
 return False
 return True
def solve(graph, m, color, v, V):
 # If all vertices are colored
 if v == V:
 return True
 for c in range(1, m + 1):
 if is_safe(v, graph, color, c, V):
 color[v] = c
 if solve(graph, m, color, v + 1, V):
 return True
 # Backtracking
 color[v] = 0
 return False
def map_coloring(graph, m, V):
 color = [0] * V
 if not solve(graph, m, color, 0, V):
 print("No solution exists")
 return
 print("\nSolution exists:")
 for i in range(V):
 print("Region", i, "-> Color", color[i])
V = int(input("Enter number of regions (vertices): "))
# Taking adjacency matrix as input
print("Enter adjacency matrix row by row:")
graph = []
for i in range(V):
 row = list(map(int, input().split()))
 graph.append(row)
m = int(input("Enter number of colors: "))
map_coloring(graph, m, V)

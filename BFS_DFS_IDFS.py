from collections import deque
# ---------------- BFS ----------------
def bfs(graph, start, goal):
 visited = []
 queue = deque([start])
 print("\n--- BFS ---")
 print("How BFS visits nodes:")
 while queue:
 node = queue.popleft()
 if node not in visited:
 visited.append(node)
 print("Visited ->", node)
 if node == goal:
 print("\nTraversal Order:", visited)
 print("BFS: Goal found!")
 return
 for neighbor in graph.get(node, []):
 if neighbor not in visited:
 queue.append(neighbor)
 print("\nTraversal Order:", visited)
 print("BFS: Goal not found.")
# ---------------- DFS ----------------
def dfs(graph, start, goal):
 visited = []
 stack = [start]
 print("\n--- DFS ---")
 print("How DFS visits nodes:")
 while stack:
 node = stack.pop()
 if node not in visited:
 visited.append(node)
 print("Visited ->", node)
 if node == goal:
 print("\nTraversal Order:", visited)
 print("DFS: Goal found!")
 return
 # Reverse to maintain left-to-right order
 for neighbor in reversed(graph.get(node, [])):
 if neighbor not in visited:
 stack.append(neighbor)
 print("\nTraversal Order:", visited)
 print("DFS: Goal not found.")
# ---------------- IDS ----------------
def dls(graph, node, goal, limit, visited, order):
 visited.add(node)
 order.append(node)
 print("Visited ->", node)
 if node == goal:
 return True
 if limit == 0:
 return False
 for neighbor in graph.get(node, []):
 if neighbor not in visited:
 if dls(graph, neighbor, goal, limit - 1, visited, order):
 return True
 return False
def ids(graph, start, goal, max_depth):
 print("\n--- IDS ---")
 for depth in range(max_depth + 1):
 print(f"\nDepth Limit = {depth}")
 visited = set()
 order = []
 if dls(graph, start, goal, depth, visited, order):
 print("\nTraversal Order:", order)
 print("IDS: Goal found!")
 return
 print("IDS: Goal not found.")
# ---------------- Main Program ----------------
graph = {}
n = int(input("Enter number of nodes: "))
print("\nEnter adjacency list for each node")
print("Enter neighbors separated by space (press Enter if none)\n")
for _ in range(n):
 node = input("Enter node: ")
 neighbors = input(f"Enter neighbors of {node}: ").split()
 graph[node] = neighbors
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth for IDS: "))
# Run all searches on the SAME graph
bfs(graph, start, goal)
dfs(graph, start, goal)
ids(graph, start, goal, max_depth)

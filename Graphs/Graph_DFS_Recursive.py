graph = {'A': ['B', 'C'],
			'B': ['A', 'D', 'E'],
			'C': ['A', 'F'],
			'D': ['B'],
			'E': ['B', 'F'],
			'F': ['C', 'E']}

def dfs(graph, start, visited=None):
	if visited is None:
		visited = []
	visited.append(start)
	arr = []
	for node in graph[start]:
		if node not in visited:
			arr.append(node)
	for i in arr:
		dfs(graph, i, visited)
	return visited

print(dfs(graph, 'A'))
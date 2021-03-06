graph = {'A': ['B', 'C'],
			'B': ['A', 'D', 'E'],
			'C': ['A', 'F'],
			'D': ['B'],
			'E': ['B', 'F'],
			'F': ['C', 'E']}
			
def dfs_paths(graph, start, goal):
	paths = []
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		arr = []
		for node in graph[vertex]:
			if node not in path:
				arr.append(node)
		for node in arr:
			if node == goal:
				paths.append(path + [node])
			else:
				stack.append((node, path + [node]))
	return paths
	

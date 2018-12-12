graph = {'A': ['B', 'C'],
			'B': ['A', 'D', 'E'],
			'C': ['A', 'F'],
			'D': ['B'],
			'E': ['B', 'F'],
			'F': ['C', 'E']}
			
def dfs_paths(graph, start, goal, paths):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		arr = []
		for node in graph[vertex]:
			if node not in path:
				arr.append(node)
		for i in arr:
			if i == goal:
				paths.append(path)
			else:
				stack.append((i, path + [i]))
	return paths
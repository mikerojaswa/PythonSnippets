graph = {'A': ['B', 'C'],
			'B': ['A', 'D', 'E'],
			'C': ['A', 'F'],
			'D': ['B'],
			'E': ['B', 'F'],
			'F': ['C', 'E']}
#shortest path guranteed to be first... easy to bail from.
def bfs_paths(graph, start, goal):
	queue = [(start, [start])]
	paths = []
	while queue:
		(vertex, path) = queue.pop(0)
		arr = []
		for node in graph[vertex]:
			if node not in path:
				arr.append(node)
		
		for node in arr:
			if node == goal:
				paths.append(path + [node])
			else:
				queue.append((node, path + [node]))
	return paths



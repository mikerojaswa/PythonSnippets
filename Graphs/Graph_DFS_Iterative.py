graph = {'A': ['B', 'C'],
			'B': ['A', 'D', 'E'],
			'C': ['A', 'F'],
			'D': ['B'],
			'E': ['B', 'F'],
			'F': ['C', 'E']}
			
def dfs(graph, start):
	visited = set()
	stack = [start]
	while stack: 
		s = stack.pop()
		if s not in visited:
			visited.add(s)
			
			for node in graph[s]:
				if node not in visited:
					stack.append(node)
	return visited

dfs(graph, 'A')

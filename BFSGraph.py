#Breadth First Search on a graph w/ cycles



graph = {
	'A': ['B', 'C'],
	'B': ['D', 'E', 'B'],
	'C': ['A', 'D', 'B', 'C', 'D', 'E'],
	'D': ['E', 'D', 'F'],
	'E': ['F'],
	'F': ['A', 'B']
}


def BFS(graph, start, target):
	visited = set(start)
	current = graph[start]
	while current: 
		#need to pop first element
		s = current.pop(0)
		
		for node in graph[s]:
			if node not in visited:
				current.append(node)
				visited.add(node)
			if node == target:
				print('Found: ', node)
	print(visited)
BFS(graph,'A', 'F')
			
			
			
	
		
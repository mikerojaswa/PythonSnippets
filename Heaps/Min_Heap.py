import heapq

# --------------------------------
# 1
# heapify - basic usage
# --------------------------------

arr = [5,4,3,2,1]
heapq.heapify(arr)
print(arr)
print(heapq.heappop(arr)) # pops 1
heapq.heappush(arr, -1)
print(heapq.heappop(arr)) # pops -1

# --------------------------------
# 2
# heapify with a custom data structure 
# using a tuple as priority
# --------------------------------

class Node:
	def __init__(self, val):
		self.val = val
		
node_arr = [Node(5), Node(8), Node(6), Node(-37), Node(44), Node(-4440), Node(9999)]

tuple_node_arr = [(item.val, item) for item in node_arr] 

heapq.heapify(tuple_node_arr)
print(heapq.heappop(tuple_node_arr)) # pops -4440 node
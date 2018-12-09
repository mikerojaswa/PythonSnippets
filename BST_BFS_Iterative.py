# based off of: https://gist.github.com/jakemmarsh/8273963
class Node:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right
class BST:
	def __init__ (self):
		self.root = None
	
	
	
	def add(self, val):
		node = Node(val)
		if not self.root:
			self._set_root(node)
		else:
			self._insert_node(self.root, node)
	
	def _set_root(self, root):
		self.root = root
		print(f'Set root with value {root.value}')
		
	def _insert_node(self, current_node, node_to_add):
		if current_node.value == node_to_add.value:
			print(f'Node with value of {node_to_add.value} already exists in tree!')
		elif current_node.value > node_to_add.value:
			if current_node.left:
				self._insert_node(current_node.left, node_to_add)
			else:
				current_node.left = node_to_add
				print(f'Added {node_to_add.value}')
		else:
			if current_node.right:
				self._insert_node(current_node.right, node_to_add)
			else:
				current_node.right = node_to_add
				print(f'Added {node_to_add.value}')
		
bst = BST()
bst.add(6)
bst.add(3)
bst.add(9)
bst.add(1)
bst.add(4)
bst.add(7)
bst.add(11)

root = bst.root

def BFS(root):
	
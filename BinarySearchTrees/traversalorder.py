from bstgen import BST

bst = BST()
bst.add(6)
bst.add(3)
bst.add(9)
bst.add(1)
bst.add(4)
bst.add(7)
bst.add(11)	

# pre order
def preorder(root):
	if not root: return
	print(f"Node: {root.value}")
	preorder(root.left)
	preorder(root.right)

#in order
def inorder(root):
	if not root: return
	inorder(root.left)
	print(f"Node: {root.value}")
	inorder(root.right)
	
# post order
def postorder(root):
	if not root: return
	postorder(root.left)
	postorder(root.right)	
	print(f"Node: {root.value}")
	
inorder(bst.root)
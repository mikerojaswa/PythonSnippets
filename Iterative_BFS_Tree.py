def traverse(self, root):
    thislevel = [root]
    while thislevel:
    nextlevel = list()
    for n in thislevel:
        # Do stuff here when analyzing levels
        if n.left: nextlevel.append(n.left)
        if n.right: nextlevel.append(n.right)
    thislevel = nextlevel

class binarytree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printtree(root):
    if root == None:
        return
    print(root.data)
    printtree(root.left)
    printtree(root.right)

def takeinput():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = binarytree(rootdata)
    lefttree = takeinput()
    righttree = takeinput()
    root.left = lefttree
    root.right = righttree
    return root
root = takeinput()
printtree(root)
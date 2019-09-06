class binarytree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def takeinput():
    index = 0
    rootdata = [int(i) for i in input().strip().split()]
    if rootdata[0] == -1:
        return None
    root = binarytree(rootdata[index])
    index += 1
    lefttree = takeinput()
    righttree = takeinput()
    root.left = lefttree
    root.right = righttree
    return root
def sumofnode(root):
    
    if root== None:
        return 0
    
    sumleft = sumofnode(root.left)
    sumright = sumofnode(root.right)
    return root.data + sumleft + sumright
    
root = takeinput()

print(sumofnode(root))
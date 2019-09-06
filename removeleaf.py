class binarytree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printdetailtree(root):
    if root == None:
        return 
    print(root.data, end = ":")
    if root.left != None:
        print(root.left.data, end = ' ')
    if root.right != None:
        print(root.right.data)
    print()
    printdetailtree(root.left)
    printdetailtree(root.right)
    
def takeinput():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = binarytree(rootdata)
    root.left = takeinput()
    root.right = takeinput()
    return root
def removeleaf(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = removeleaf(root.left)
    root.right = removeleaf(root.right)
    return root
    
root = takeinput()
printdetailtree(root)
root = removeleaf(root)
printdetailtree(root)
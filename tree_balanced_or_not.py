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
def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))
def isbalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if rh-lh>1 or lh-rh>1:
        return False
    isleftbalanced = isbalanced(root.left)
    isrightbalanced = isbalanced(root.right)
    if isleftbalanced and isrightbalanced:
        return True
    else:
        return False
root = takeinput()
printdetailtree(root)
print(isbalanced(root))
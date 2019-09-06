class binarytree:
    def __init__(self,data):
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
def findheightandcheckbalanced(root):
    if root == None:
        return 0, True
    lh, isleftbalanced = findheightandcheckbalanced(root.left)
    rh, isrightbalanced = findheightandcheckbalanced(root.right)
    h = 1 +max(lh, rh)
    if lh-rh>1 or rh-lh>1:
        return h, False
    if isleftbalanced and isrightbalanced:
        return h, True
root = takeinput()
printdetailtree(root)
print(findheightandcheckbalanced(root))
    
        
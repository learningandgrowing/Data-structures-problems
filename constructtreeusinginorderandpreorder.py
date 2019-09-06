import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def buildTreePreOrder(preorder, inorder):
    if len(preorder) == 0:
        return None
    rootdata = preorder[0]
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    rootindexinorder = -1
    for i in range (0, len(inorder)):
        if inorder[i] == rootdata:
            rootindexinorder = i
            break
    if rootindexinorder == -1:
        return None
    leftinorder = inorder[0:rootindexinorder]
    rightinorder = inorder[rootindexinorder+1:]
    lenleftsubtree = len(leftinorder)
    leftpreorder = preorder[1:lenleftsubtree+1]
    rightpreorder = preorder[lenleftsubtree+1:]
    leftchild = buildTreePreOrder(leftpreorder, leftinorder)
    rightchild = buildTreePreOrder(rightpreorder, rightinorder)
    root.left = leftchild
    root.right = rightchild
    return root
def printLevelATNewLine(root):
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ
n=int(input())
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePreOrder(preorder, inorder)
printLevelATNewLine(root)

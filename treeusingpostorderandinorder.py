import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    if len(postorder) == 0:
        return None
    rootdata = postorder[-1]
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
    leftpostorder = postorder[:lenleftsubtree]
    rightpostorder = postorder[lenleftsubtree:-1]
    leftchild = buildTreePostOrder(leftpostorder, leftinorder)
    rightchild = buildTreePostOrder(rightpostorder, rightinorder)
    root.left = leftchild
    root.right = rightchild
    return root


def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
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

# Main
n=int(input())
postorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postorder, inorder)
printLevelATNewLine(root)
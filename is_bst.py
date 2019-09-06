import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def maxTree(root):
    if root == None:
        return -10000
    leftmax = maxTree(root.left)
    rightmax = maxTree(root.right)
    return max(leftmax, rightmax, root.data)
def minTree(root):
    if root == None:
        return 10000
    leftmin = minTree(root.left)
    rightmin = minTree(root.right)
    return min(leftmin, rightmin, root.data)
def isBST(root):
    if root == None:
        return True
    leftmax = maxTree(root.left)
    rightmin = minTree(root.right)
    
    if root.data > rightmin or root.data <= leftmax:
        return False
    isleftBST = isBST(root.left)
    isrightBST = isBST(root.right)
    return isleftBST and isrightBST
def takeinputlevelwise():
    q = queue.Queue()
    print("enter root")
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    q.put(root)
    while (not(q.empty())):
        curr_node = q.get()
        print("enter left child of" ,curr_node.data)
        leftnode = int(input())
        if leftnode != -1:
            leftchild = BinaryTreeNode(leftnode)
            curr_node.left = leftchild
            q.put(leftchild)
        print("enter right child of" ,curr_node.data)
        rightnode = int(input())
        if rightnode != -1:
            righttchild = BinaryTreeNode(rightnode)
            curr_node.right = righttchild
            q.put(righttchild)
    return root

root = takeinputlevelwise()
isBST(root)
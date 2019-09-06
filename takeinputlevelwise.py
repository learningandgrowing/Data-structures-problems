import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
def printdetailtree(root):
    q = queue.Queue()
    q.put(root)
    while (not(q.empty())):
        curr_node = q.get()
        print(curr_node.data,end = ":")
        
        if curr_node.left != None:
            q.put(curr_node.left)
            print('L:',curr_node.left.data,end = ',')
        else:
            print('L:-1', end = ',')
        if curr_node.right != None:
            q.put(curr_node.right)
            print('R:',curr_node.right.data)
        else:
            print('R:-1')
        print()
root = takeinputlevelwise()
printdetailtree(root)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    l = len(lst)
    s = 0
    e = l-1
    while s <= e:
        
        
        mid = s+e//2
        
        rootdata = lst[mid]
    #print(rootdata)
        
        root = BinaryTreeNode(rootdata)
        leftlst = lst[:mid]
        rightlst = lst[mid+1:]
        leftsubtree = constructBST(leftlst)
        rightsubtree = constructBST(rightlst)
        root.left = leftsubtree
        root.right = rightsubtree
        return root
    

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)
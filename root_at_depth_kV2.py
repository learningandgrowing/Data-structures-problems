class binarytree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printtreedetail(root):
    if root == None:
        return
    print(root.data, end = ':')
    if root.left != None:
        print('l',root.left.data, end = ',')
    if root.right != None:
        print('r',root.right.data)
    
    print()
    printtreedetail(root.left)
    printtreedetail(root.right)
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
def depthrootkv2(root, k, d=0):
    if root == None:
        return
    if k==d:
        print(root.data)
        return
    depthrootkv2(root.left, k, d+1)
    depthrootkv2(root.right, k, d+1)
    
root = takeinput()
printtreedetail(root)
depthrootkv2(root, 2)
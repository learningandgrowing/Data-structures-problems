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
def printnodek(root,value,k):
    if root == None:
        return
    if root.data == value and k == 0:
        
            
        print(root.data)
        return
    printnodek(root.left,value.k-1)
    printnodek(root.right,value,k-1)
    
root = takeinput()
value = int(input())
k = int(input())
printnodek(root,value,k)
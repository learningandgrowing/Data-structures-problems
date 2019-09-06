class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def printll(head):
    while head is not None:
        print(head.data, end = ' ')
        head = head.next
def takeinput():
    
    head = None
    for currinput in list:
        currdata = int(currinput)
        if currdata == -1:
            break
        currnode = Node(currdata)
        if head is None:
            head = currnode
            tail = currnode
        else:
            tail.next = currnode
            tail = currnode
            
    return head
n = (input())
for i in n:
    list = input().split()
head = takeinput()
printll(head)
        
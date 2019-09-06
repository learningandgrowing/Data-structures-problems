class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def len(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count
def reversell(head):
    if head is None or head.next is None:
        return head
    smallhead = reversell(head.next)
    curr = smallhead
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return smallhead
def printll(head):
    while head is not None:
        print(head.data, end = ' ')
        head = head.next
def takeinput():
    list = input().split()
    head = None
    
    for currinput in list:
        currdata = int(currinput)
        if currdata == -1:
            break
        currnode = node(currdata)
        
        if head is None:
            head = currnode
            tail = currnode
        else:
            tail.next = currnode
            tail = currnode
    return head
head = takeinput()
head = reversell(head)
printll(head)


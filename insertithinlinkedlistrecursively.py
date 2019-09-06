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
def insertatir(head, i, data):
    if i == 0:
        newnode = node(data)
        newnode.next = head
        return newnode
    if head is None:
        return head
    
    smallhead = insertatir(head.next, i-1, data)
    head.next = smallhead
    return head
    
    
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
head = insertatir(head, 2, 8)
printll(head)
print()
head = insertatir(head, 0, 9)
printll(head)

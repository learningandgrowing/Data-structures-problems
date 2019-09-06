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
def insertati(head, i, data):
    if i>len(head):
        return head
    count = 0
    prev = None
    curr = head
    
    while count < i:
        prev = curr
        curr = curr.next
        count += 1
    newnode = node(data)
    if prev is not None:
        prev.next = newnode
    else:
        head = newnode
    newnode.next = curr
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
head = insertati(head, 2, 8)
printll(head)
print()
head = insertati(head, 0, 9)
printll(head)


            
        
        
        
        
        
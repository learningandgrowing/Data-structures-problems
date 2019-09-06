from Node import Node
def printll(head):
    while head is not None:
        print(head.data, end = ' ')
        head = head.next
def takeinput():
    list = input().split()
    head = None
    tail = None
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
head = takeinput()
printll(head)
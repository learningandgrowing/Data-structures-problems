
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

def insertiterative(head, i, n):
    
    pre = None
    curr = head
    count = 0
    
    while count<i:
        pre = curr
        curr = curr.next
        count += 1
    newnode = Node(n)
    if pre is not None:
        pre.next = newnode
    else:
        head = newnode
    newnode.next = curr
    return head
        
def inputtaking(lst):
    if len(lst) == 0:
        return None
    head = Node(lst[0])
    tail = head
    for ele in lst[1:]:
        tail.next = Node(ele)
        tail = tail.next
    return head
def printll(head):
    while head is not None:
        print(head.data, end = " ")
        head = head.next
    print()
    
lst = [int(i) for i in input().split()]
i = int(input())
n = int(input())
head = inputtaking(lst)
l = insertiterative(head, i, n)
printll(l)
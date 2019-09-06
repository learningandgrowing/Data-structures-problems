class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def ith(head, i):
    result = 0
    while(head and i != result):
        result += 1
        head = head.next
    if(i == result):
        return head
    else:
        return None
    
            
        
        
def ll(arr):
    if len(arr) == 0:
        return 0
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head
arr = list(int(x) for x in input().strip().split(' '))
head = ll(arr)
i=int(input())
node = ith(head, i)
if node:
    print(node.data)
        
            
    
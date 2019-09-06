class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None 

class LinkedList: 

    def __init__(self): 
        self.head = None

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
 
    def getCountRec(self, node):
        if (not node):
            return 0
        else: 
            return 1 + self.getCountRec(node.next)
        

    def getCount(self): 
        return self.getCountRec(self.head) 

llist = LinkedList() 
n = int(input())

for i in range(n):
    data = int(input())
    llist.push(data) 
print(llist.getCount())
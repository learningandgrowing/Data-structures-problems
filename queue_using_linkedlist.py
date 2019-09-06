class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class queueusingll:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    def enqueue(self,data):
        newnode = Node(data)
        if self.__head == None:
            self.__head = newnode
            self.__tail = self.__head
        else:
            self.__tail.next = newnode
            self.__tail = self.__tail.next
        self.__count += 1
            
        
    def dequeue(self):
        if self.isEmpty():
            return 0
        ele = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return ele
        
            
    def front(self):
        if self.isEmpty():
            return 0
        data = self.__head.data
        return data
    def isEmpty(self):
        return self.getsize() == 0
    def getsize(self):
        return self.__count
q = queueusingll()

li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        q.enqueue(li[i+1])
        i+=1
    elif choice == 2:
        ans = q.dequeue()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = q.front()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(q.getsize())
    elif choice == 5:
        if(q.isEmpty()):
            print('true')
        else:
            print('false')
    i+=1
        
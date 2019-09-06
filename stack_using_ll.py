mclass Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class StackUsingLL:
    ### Implement all these functions here
    
    def __init__(self):
        self.__head = None
        
        
        self.__count = 0

    def push(self,data):
        newnode = Node(data)
        newnode.next = self.__head
        self.__head = newnode
        self.__count += 1
        

        
    def pop(self):
        if self.isEmpty() is True:
            
            
            
            return 0
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data
    
    
    def top(self):
        if self.isEmpty() is True:
            return 0
        data = self.__head.data
        return data
    
    def isEmpty(self):
        return self.getSize() == 0
            
        
    def getSize(self):
        return self.__count
        
    
s = StackUsingLL()
li = [int(i) for i in input().split()]
j = 0
while j < len(li):
    choice = li[j]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[j+1])
        j += 1
    elif choice == 2:
        ans = s.pop()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        if (s.isEmpty()):
            print('true')
        else:
            print('false')
    j += 1
        
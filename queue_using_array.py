class queue:
    def __init__(self):
        self.__data = []
        self.__front = 0
        self.__count = 0
    def enqueue(self,item):
        self.__data.append(item)
        self.__count += 1
        
        
        
    def dequeue(self):
        if self.isEmpty():
            return 
        
        ele = self.__data[self.__front]
        self.__front += 1
        self.__count -= 1
        return ele
        
        
    
    
            
        
    def front(self):
        if self.isEmpty():
            return self.__data
        return self.__data[self.__front]
    
    def isEmpty(self):
        
        return self.size() == 0
        
        
        
    def size(self):
        return self.__count
    
s = queue()
s.enqueue(12)
s.enqueue(22)
s.enqueue(32)
s.enqueue(42)
while s.isEmpty() is False:
    print(s.front())
    s.dequeue()
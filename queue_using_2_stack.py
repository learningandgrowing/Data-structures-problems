class queueusingstack:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []
        self.__count = 0
    def enqueue(self, data):
        self.__s1.append(data)
        self.__count += 1
        
    def dequeue(self):
        if self.isEmpty():
            return -1
        while len(self.__s1) != 1:
            ele = self.__s1.pop()
            self.__s2.append(ele)
        data= self.__s1.pop()
        while len(self.__s2) != 0:
            ele = self.__s2.pop()
            self.__s1.append(ele)
        self.__count -= 1
        return data
    def front(self):
        if self.isEmpty():
            return -1
        return self.__s1[0]
    def isEmpty(self):
        return self.getSize() == 0
    def getSize(self):
        return self.__count
s = queueusingstack()
s.enqueue(12)
s.enqueue(13)
s.enqueue(14)
s.enqueue(15)
while s.isEmpty() is False:
    print(s.front())
    s.dequeue()
            
class stack:
    def __init__(self):
        self.__arr = []
    def push(self,item):
        self.__arr.append(item)
    def pop(self):
        if self.isEmpty() is True:
            return
        return self.__arr.pop()
    def top(self):
        if self.isEmpty() is True:
            return
        return self.__arr[len(self.__arr)-1]
    def size(self):
        return len(self.__arr)
    def isEmpty(self):
        return self.size() == 0
    
s = stack()
s.push(12)
s.push(13)
s.push(14)
s.push(15)
print(s.size())
print(s.isEmpty())
print(s.top())
while s.isEmpty() is False:
    print(s.pop())
print(s.size())
print(s.isEmpty())
print(s.top())
    
        
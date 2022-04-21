import List as lt

class Stack():
    def __init__(self):
        self.__data=lt.List()
    
    def size(self):
        return self.__data.size
    
    def isEmpty(self):
        return self.size()==0
    
    def push(self,e):
        self.__data.addFirst(e)
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__data.removeFirst()
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__data.First().getData
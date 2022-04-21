import List as lt

class Queue():
    def __init__(self):
        self.__data=lt.List()
    
    def size(self):
        return self.__data.size
    
    def isEmpty(self):
        return self.size()==0
    
    def enqueue(self, e):
        self.__data.addLast(e)
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.__data.removeFirst()
    
    def first(self):
        return self.__data.First().getData
    
    
        
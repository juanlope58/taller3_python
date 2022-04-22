import Queue as qu

class QueueCollection():
    def __init__(self):
        self.__data = qu.Queue()
        self.temp=""
    
    def add(self, e):
        self.__data.enqueue(e) #se agrega elemento a la cola
    
    def remove(self):
        return self.__data.dequeue()
        
    # def find(self, e):
    #     if (e in self.__data):
    #         return (e)
    #     else:
    #         return None
    
        
    def printQueue(self):
        return(self.__data.size())
        
        # for i in self.__data.size:
        #     self.temp = self.__data.dequeue()
        #     print(self.temp)


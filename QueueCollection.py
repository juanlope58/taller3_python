import Queue as qu

class QueueCollection():
    def __init__(self):
        self.__data = qu.Queue()
        
    
    def add(self, e):
        if self.__data.isEmpty():
            self.__data.enqueue(e) # si está vacío agrego a la cola
        else:
            self.__data.enqueue(e) # si no está vacío agrego a la cola
            vec=[]
            for i in range(self.__data.size()):
                vec.append(self.__data.dequeue()) # saco la cola a una lista
                # print(vec)
            for j in range(len(vec)-1):           # ordeno de mayor a menor
                for i in range(len(vec)-1):
                    if (vec[i] < vec[i+1]):
                        aux=vec[i]
                        vec[i]=vec[i+1]
                        vec[i+1]=aux
            for i in range(len(vec)):
                self.__data.enqueue(vec[i])            
            
    
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
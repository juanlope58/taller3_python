from pickle import TRUE


class QueueCollection:
    def __init__(self):
        self.__data = []
    
    def QueueCollection():
        pass
    
    def add(self, e):
        self.__data.append(e) #se agrega elemento a la cola
        self.__data.sort(reverse=True) # se orden a de mayor a menor (mayor en el principio de la cola)
    
    # def remove(self, e):
        
    # def find(self, e):
        
    def printQueue(self):
        print(self.__data)


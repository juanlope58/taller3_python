class StackCollection():
    def __init__(self):
        self.__data=[]
    
    def StackCollection():
        pass
    
    def add(self, e):
        self.__data.append(e)   #se agrega elemento a la pila
        self.__data.sort()      #se ordena (En el tope queda el máximo)
        
    def remove(self, e):
        if (e in self.__data):
            self.__data.remove(e)
            return (e)
        else:
            return None
    
    def find(self, e):
        if (e in self.__data):
            return(e)
        else: 
            return None
        
    def printStack(self):
        print(self.__data)
        
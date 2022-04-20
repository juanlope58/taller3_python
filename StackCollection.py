class StackCollection():
    def __init__(self):
        self.__data=[]
    
    def StackCollection():
        pass
    
    def add(self, e):
        self.__data.append(e)
        self.__data.sort()
        
    # def remove(self, e):
    
    # def find(self, e):
        
    def printStack(self):
        print(self.__data)
        
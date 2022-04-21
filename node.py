class node():
    def __init__(self,o=None):
        self.__data=o
        self.__next=None
    
    @property
    def getData(self):
        return self.__data
    
    @property
    def getNext(self):
        return self.__next
    
    @getData.setter 
    def setData(self,o):
        self.__data=o
        
    @getNext.setter 
    def setNext(self,n):
        self.__next=n
import node as nd
class List():
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    
    @property 
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, s):
        self.__size=s
    
    def isEmpty(self):
        return self.size==0
    
    def First(self):
        return self.__head
    
    def Last(self):
        return self.__tail
    
    def addFirst(self,o):
        n=nd.node(o)
        if self.isEmpty():
            self.__head=n
            self.__tail=n
        else:
            n.setNext=self.__head
            self.__head=n
        self.size+=1      
    
    def addLast(self,o):
        n=nd.node(o)
        if self.isEmpty():
            self.__head=n
            self.__tail=n
        else:
            self.__tail.setNext=n
            self.__tail=n
        self.size+=1
    
    def removeFirst(self):
        if ~self.isEmpty():
            temp=self.__head 
            self.__head=temp.getNext
            temp.setNext=None
            self.size-=1
            return temp.getData
        else:
            return None
    
    def removeLast(self):
        if self.size==1:
            self.removeFirst()
        elif self.size>1:
            temp = self.__tail 
            anterior=self.__head 
            while anterior.getNext!=self.__tail:
                anterior=anterior.getNext
            anterior.setNext=None
            self.__tail=anterior
            self.size-=1
            return temp.getData
        else:
            return None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
            
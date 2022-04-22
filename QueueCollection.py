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
        
    def find(self, e):
        cont=0
        vec=[]
        for i in range(self.__data.size()):     # saco los datos de la cola para buscar el dato pedido
            vec.append(self.__data.dequeue())
            if vec[i] == e :
                cont+=1
        for i in range(len(vec)):
            self.add(vec[i])            # meto los datos de nuevo a la cola
        if cont==0:
            return None
        else:
            return (str(e) + " se encuentra un numero de veces de: " + str(cont))   # retorno el dato pedido y el numero de veces que se encontró en la cola
            
        
    def printQueue(self):
        vec=[]
        for i in range(self.__data.size()):
            vec.append(self.__data.dequeue()) #sacando los valores de la cola para imprimirlos
        for i in range(len(vec)):
            self.add(vec[i])        #devolviendo datos a la cola
        print(vec)
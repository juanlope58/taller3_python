import Stack as st
class StackCollection():
    def __init__(self):
        self.__data=st.Stack()
    
    def add(self, e):
        if self.__data.isEmpty():
            self.__data.push(e)     #agragando dato a la pila
        else:
            self.__data.push(e)  # agragando dato a la pila
            vec=[]
            for i in range(self.__data.size()):
                vec.append(self.__data.pop())       # Sacando los valores de la pila a un vector
            for j in range(len(vec)-1):       # Ordenando los valores del vector
                for i in range(len(vec)-1):
                    if (vec[i]<vec[i+1]):
                        aux=vec[i]
                        vec[i]=vec[i+1]
                        vec[i+1]=aux
            for i in range(len(vec)):
                self.__data.push(vec[i]) # devolviendo los valores ordenados a la pila
        
    def remove(self, e):
        vec=[]
        indicador=False
        for i in range(self.__data.size()): # saco los datos de la pila para eliminar el dato pedido
            vec.append(self.__data.pop())
        for i in range(len(vec)):
            if vec[i]==e:               #omito los datos iguales al que se pide eliminar
                indicador=True
            else:
                self.add(vec[i])             # agrego los elementos a la pila sin meter los datos eliminados
        if indicador:
            return(e)
        else:
            return None
    
    def find(self, e):
        cont=0
        vec=[]
        for i in range(self.__data.size()):         # saco los datos de la pila para poder buscar el que me piden
            vec.append(self.__data.pop())
            if vec[i]==e :
                cont+=1
        for i in range(len(vec)):               #busco cuantas veces está
            self.add(vec[i])
        if cont == 0:
            return None
        else:
            return(str("el dato "+str(e)+" se encuentra un numero de veces de: "+str(cont)))
        
    def printStack(self):
        vec=[]
        for i in range(self.__data.size()):  # saco los datos de la pila para poder imprimirlos
            vec.append(self.__data.pop())
        for i in range(len(vec)):       # retorno los datos a la pila para no alterarla
            self.add(vec[i])
        print(vec)                      #imprimo los datos
        
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
        vec=[]
        for i in range(self.__data.size()):  # saco los datos de la pila para poder imprimirlos
            vec.append(self.__data.pop())
        for i in range(len(vec)):       # retorno los datos a la pila para no alterarla
            self.add(vec[i])
        print(vec)                      #imprimo los datos
        
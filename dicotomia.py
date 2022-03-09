class Dicotomia():

    def __init__(self, tabla) -> None:
        self.fin  = len(tabla) - 1
        self.tabla = tabla
        self.tablaordenada =[]
 
    def bubbleSort(self):
        for i in range(0, self.fin):
            for j in range(0, self.fin - i):
                if self.tabla[j] > self.tabla[j + 1]:
                    temp = self.tabla[j]
                    self.tabla[j] = self.tabla[j+1]
                    self.tabla[j+1] = temp

    def insercion (self):
        for i in range (0,self.fin+1):
            self.tablaordenada.append (self.tabla[i])
            for j in range (i,0,-1):    
                if self.tablaordenada[j-1]>self.tablaordenada[j]:
                    aux = self.tablaordenada[j]
                    self.tablaordenada[j]=self.tablaordenada[j-1]
                    self.tablaordenada[j-1]=aux
class Dicotomia():

    def __init__(self, tabla) -> None:
        self.fin  = len(tabla) - 1
        self.tabla = tabla
 
    def __str__ (self):
        return str(self.tabla)

    def bubbleSort(self):
        for i in range(0, self.fin):
            for j in range(0, self.fin - i):
                if self.tabla[j] > self.tabla[j + 1]:
                    temp = self.tabla[j]
                    self.tabla[j] = self.tabla[j+1]
                    self.tabla[j+1] = temp

tabla =[]
t = int(input ("Numero de elementos en tu vector: "))
for i in range (0, t):
    ele = int(input())
    tabla.append(ele)

miclase = Dicotomia(tabla)
print (miclase)
miclase.bubbleSort()
print (miclase)

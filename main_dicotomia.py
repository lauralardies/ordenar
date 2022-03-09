
from  dicotomia import Dicotomia

tabla =[]
t = int(input ("Numero de elementos en tu vector: "))
for i in range (0, t):
    ele = int(input())
    tabla.append(ele)

print ("Tabla Inicial")
print (tabla)

miclase = Dicotomia(tabla)

print ("Ordenación por inserción")
miclase.insercion()
print(miclase.tablaordenada)

print ("Ordenación por BubbleSort")
miclase.bubbleSort()
print (miclase.tabla)
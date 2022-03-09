from segmentos import Segmentos


tabla =[]
t = int(input ("Numero de elementos en tu vector: "))
for i in range (0, t):
    ele = int(input())
    tabla.append(ele)

s = Segmentos (tabla)
print ("Tabla sin ordenar.")
print (s.t)

s.introducirsegmentos()

for i in range (0, s.NSegmentos):
    s.esta_explorado(i)

print("Segmentos ordenados.")
print (s.t)
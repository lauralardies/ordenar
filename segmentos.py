class Segmentos():

    def __init__(self, tabla) -> None:
        self.t = tabla
        self.NSegmentos = 0
        self.Segmentos = []
        self.esvalido =True

    def introducirsegmentos (self):
        self.NSegmentos=int(input ("Numero de segmentos en tu vector: "))
        for i in range (0,self.NSegmentos):
            id1= int (input ("Índice del extremo inferior del segmento: "))
            id2= int (input ("índice del extremo superior del segmento: "))
            if id1 > id2 or id2 > len(self.t) - 1:
                print("Error de entrada de datos.")
                self.esvalido = False
                return
            s = [id1,id2]
            self.Segmentos.append (s)

        # Comprobamos que los segmentos estan ordenados
        for i in range (1,self.NSegmentos):
            anterior = self.Segmentos[i-1]
            actual =self.Segmentos[i]
            if (anterior[1]>actual[0]):
                print ("Error de entrada de datos. Segmentos no consecutivos")
                self.esvalido = False
                return

    def esta_explorado (self,segmento):
        [di,fi] = self.Segmentos[segmento]
        mi = self.t[di]
        self.t.pop(di)
        self.t.insert(fi, mi)


tabla =[5,7,12,6,18,13,9,10,16,21,19,8,20,3]
#t = int(input ("Numero de elementos en tu vector: "))
#for i in range (0, t):
#    ele = int(input())
#    tabla.append(ele)

s = Segmentos (tabla)
print (s.t)
s.introducirsegmentos()
s.esta_explorado(0)
print (s.t)
s.esta_explorado(1)
print (s.t)

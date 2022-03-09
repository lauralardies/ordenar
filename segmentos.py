class Segmentos():

    def __init__(self, tabla) -> None:
        self.t = tabla
        self.NSegmentos = 0
        self.Segmentos = []
        self.esvalido = True

    def introducirsegmentos (self):
        self.NSegmentos = int(input ("Numero de segmentos en tu vector: "))

        # Comprobamos que los índices de los segmentos sean correctos
        for i in range (0,self.NSegmentos):
            id1 = int (input ("Índice del extremo inferior del segmento: "))
            id2 = int (input ("índice del extremo superior del segmento: "))
            if id1 > id2 or id2 > len(self.t) - 1:
                print("Error de entrada de datos. Los segmentos no son válidos.")
                self.esvalido = False
                return
            s = [id1,id2]
            self.Segmentos.append(s)

        # Comprobamos que los segmentos estan ordenados
        for i in range (1,self.NSegmentos):
            anterior = self.Segmentos[i-1]
            actual = self.Segmentos[i]
            if anterior[1] > actual[0]:
                print ("Error de entrada de datos. Segmentos no consecutivos.")
                self.esvalido = False
                return

        # Comprobamos que el primer numero del segmento es el máximo
        for i in range (0,self.NSegmentos):
            actual = self.Segmentos[i]
            max_i = self.t[actual[0]]
            for j in range (actual[0], actual[1]):
                if self.t[j] > max_i:
                    print ("Error de entrada de datos. El primer valor del segmento no es el máximo.")
                    self.esvalido = False
                    return

    def esta_explorado (self,segmento):
        if self.esvalido:
            [di,fi] = self.Segmentos[segmento]
            mi = self.t[di]
            self.t.pop(di)
            self.t.insert(fi, mi)
# En este algoritmo trataremos las tareas que hay que realizar para limpiar tu habitación.

# Algoritmo para unir dos listas (o sublistas) sobre la lista 1, es decir, la lista 1 contendrá el resultado. 
# Recorre todos los elementos Tj de la lista 2. Luego haces otro recorre todos los elementos Ti de la lista 1.
#   Si Ti = Tj entonces pass y busca el siguiente elemento Tj en lista 2.
#   Si Tj es predecesor de Ti entonces insertar Tj en la posición de Ti - 1 en la lista 1.
#   Si he recorrido lista 1 completa y todavía hay elementos sin estudiar en lista 2, añadirlos al final de la lista 1.

# Algoritmo crear sublistas (2 tareas dependientes):
# for Ti en lista de Tareas
#     for Tj en lista de Tareas
#         si (Ti!= Tj & Ti es predecesora de Tj)
#                CreaSublista (Ti,Tj)

# Algoritmo es_predecesor: Las restricciones que indica el orden de las tareas.

class Tareas():

    def __init__(self) -> None:
        
        self.t = []
        self.t.append("Hacer la cama")
        self.t.append("Barrer")
        self.t.append("Fregar")
        self.t.append("Ventilar")
        self.t.append("Ordenar la mesa")
        self.t.append("Limpiar el polvo")
        self.t.append("Ordenar la ropa")
        self.t.append("Ordenar los zapatos")

        self.sublistas=[]
        self.nsublistas =0

    def __str__(self) -> str:
        
        return str(self.t)

    def es_predecesor(self, Ti, Tj):
    # True si Ti es predecesor de Tj, es decir, Ti se ejecuta antes que Tj.

        if Tj == "Hacer la cama":
            return False

        elif Tj == "Barrer":
            if Ti == "Fregar" or Ti == "Ventilar":
                return False
            else:
                return True
        
        elif Tj == "Fregar":
            if Ti == "Ventilar":
                return False
            else:
                return True
        
        elif Tj == "Ventilar":
            return True
        
        elif Tj == "Ordenar la mesa":
            return False

        elif Tj == "Limpiar el polvo":
            if Ti == "Ordenar la mesa":
                return True
            else:
                False
        
        elif Tj == "Ordenar la ropa":
            return False

        elif Tj == "Ordenar los zapatos":
            return False

    def crear_sublistas(self):
        for Ti in self.t:
            for Tj in self.t:
                if Ti != Tj and self.es_predecesor(Ti, Tj) == True:
                    par = [Ti,Tj]
                    self.sublistas.append(par)
                    self.nsublistas = self.nsublistas + 1

    def imprimir_sublistas (self):
        for i in range (0,self.nsublistas):
            print (self.sublistas[i])

    def unir_listas(self, i, j):

        lista1 = self.sublistas[i]
        lista2 = self.sublistas[j]

        for indexj in range(0, len(lista2)):
            Tj = lista2[indexj]
            logica=False

            for indexi in range(0, len(lista1)):
                Ti = lista1[indexi]

                if Ti==Tj:
                    logica = True
                    break 
                elif self.es_predecesor(Tj,Ti) == True:
                    lista1 = lista1.insert(indexi, Tj)
                    logica = True
                    break

            if logica == False:
                lista1.append(Tj)

    def unir_todas_listas(self):
        for i in range (1, self.nsublistas):
            self.unir_listas(0, i)

clase = Tareas()
decision = clase.es_predecesor("Hacer la cama", "Barrer")
print(decision)
clase.crear_sublistas()
clase.imprimir_sublistas()
print ("**********")
clase.unir_todas_listas()
clase.imprimir_sublistas()
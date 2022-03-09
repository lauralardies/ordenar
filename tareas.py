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
import random

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
        random.shuffle(self.t)

        self.t_ordenadas = []

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

    def ordena_tareas (self):
        for T in self.t:
            # Vamos a valorar donde insertar la tarea T
            done = False
            # Recorremos la lista de tareas ordenadas en orden inverso 
            for i in range (len(self.t_ordenadas)-1,-1,-1):
                Ti= self.t_ordenadas[i]
                if self.es_predecesor(Ti, T):
                    self.t_ordenadas.insert(i+1,T)
                    done = True
                    break
            # Si no tiene dependencias, lo insertamos al principio de la lista
            if done == False:
                self.t_ordenadas.insert(0,T)

# En este algoritmo trataremos las tareas que hay que realizar para limpiar tu habitación.

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
from tareas import Tareas


orden_tareas = Tareas()

print("Esta es tu lista de tareas")
print(orden_tareas.t)

print("Estas son tus tareas ordenadas")
orden_tareas.ordena_tareas()
print (orden_tareas.t_ordenadas)
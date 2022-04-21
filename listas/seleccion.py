# Selección (Selection Sort)

def seleccion(l):
  n = len(l)
  for i in range(n):
    # Asumimos que el mínimo está en la posición i
    min = i

    # Recorremos el resto de la lista
    for j in range(i+1, n):
      if (l[j] < l[min]):
        # Si encontramos un nuevo mínimo, actualizamos la posición
        min = j

    # Llevamos el mínimo a la posición i     
    l[i], l[min] = l[min], l[i]
    
  return l


l = [4, 2, 1, 5, 3]

print(seleccion(l))
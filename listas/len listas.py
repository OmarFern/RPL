def ordenar_palabras_por_longitud(lista):
   
     return sorted( lista ,key=len ,reverse=True)


print(ordenar_palabras_por_longitud(["a", "hola", "si", "string largo", "string"]))
#.-----------------------
def ordenar_lista_por_tupla(lista):
    return sorted( lista ,key=lambda x: x[1] ,reverse=True)

print(ordenar_lista_por_tupla([(1,2), (2,3), (6,7), (5,4), (7,1)]))
#--------------------------------------------------------------------

def ordenar_lista_por_suma_tupla(lista):
    return sorted( lista ,key=lambda x: x[0]+x[1] ,reverse=True)
print(ordenar_lista_por_suma_tupla([(1, 5), (7, 3), (5, 4), (4, 3)]))

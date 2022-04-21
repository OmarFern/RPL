
lista=[5,2,6,23,4]
#---------------------1----------------------------------
def ordenar_lista_menor_a_mayor(lista):
 
    return sorted(lista)
print(ordenar_lista_menor_a_mayor(lista))#[2, 4, 5, 6, 23]

#----------------------2---------------------------------
def ordenar_lista_mayor_a_menor(lista):
     lista.sort(reverse=True)
     return lista
print(ordenar_lista_mayor_a_menor(lista))

a = [5, 2, 3, 1, 4]
a.sort(reverse=True)
print(a)
#---------------------3----------------------------------
def ordenar_lista_alfabeticamente(lista):
    lista.sort()
    return lista #['como', 'estas', 'hola', 'si']

print(ordenar_lista_alfabeticamente(["hola", "estas", "como", "si"]))
#-----------------------4--------------------------------
def ordenar_palabras_por_longitud(lista):
  
    return sorted( lista ,key=len ,reverse=True)#['string largo', 'string', 'hola', 'si', 'a']
print(ordenar_palabras_por_longitud(["a", "hola", "si", "string largo", "string"]))
#-----------------------5--------------------------------
def ordenar_lista_por_tupla(lista):
    return sorted( lista ,key=lambda x: x[1] ,reverse=True)

print(ordenar_lista_por_tupla([(1,2), (2,3), (6,7), (5,4), (7,1)]))
#-----------------------6---------------
def ordenar_lista_por_suma_tupla(lista):
    return sorted( lista ,key=lambda x: x[0]+x[1] ,reverse=True)
print(ordenar_lista_por_suma_tupla([(1, 5), (7, 3), (5, 4), (4, 3)]))


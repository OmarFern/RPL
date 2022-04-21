""" 
Para este apartado, se propone la utilización de la funcionalidad de slices de indexación aplicada a listas.

ultimos_tres_elementos: Recibe una lista previamente inicializada, de longitud mayor o igual a 3. Retorna una lista con los últimos tres elementos de la que se recibi.

Ejemplo:

ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]) => [6,4,7]

ultimos_tres_elementos_concatenados: Recibe una lista de listas. Retorna una única lista que tiene concatenados los últimos tres elementos de cada una de las listas individuales en el orden original.

Ejemplo:

ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) => [2,3,4, 6,7,8,10,11,12]

indices_pares: Recibe una lista previamente inicializada. Retorna una lista que tiene únicamente los elementos correspondientes a los índices pares de la lista que recibió como parámetro.

Hint: Recordar que los índices comienzan en 0.

Ejemplo:

indices_pares(["a","b","c","d","e"]) -> ["a","c","e"]

indices_impares: Recibe una lista previamente inicializada. Retorna una lista que tiene únicamente los elementos correspondientes a los índices impares de la lista que recibió como parámetro.

Ejemplo:

indices_pares(["a","b","c","d","e", "f"]) -> ["b","d","f"]

invertir: Recibe una lista previamente inicializada. Retorna dicha lista invertida.

Ejemplo:

invertir([1,2,3,4,5]) => [5,4,3,2,1]"""
def ultimos_tres_elementos(lista):
     lista2=lista[slice(-1,-4,-1)]
     lista2.reverse()

     return lista2
    
def ultimos_tres_elementos_concatenados(lista):
    lista2=[]
    for j in range(len(lista)):
         for i in range(1,len(lista[j])):
              lista2.append(lista[j][i])
    
    return lista2
    
def indices_pares(lista):
    lista2=[]
    for i in range(len(lista)):
        if i%2==0:
            lista2.append(lista[i])
            
    return lista2
    
def indices_impares(lista):
    lista2=[]
    for i in range(len(lista)):
        if i%2!=0:
            lista2.append(lista[i])
            
    return lista2

def invertir(lista):
    lista.reverse()
    return lista
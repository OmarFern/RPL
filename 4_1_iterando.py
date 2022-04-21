""" Completar los cuerpos de las distintas funciones. A continuación se encuentran los requerimientos que deben cumplir cada una de las funciones. Las funciones deben ser resueltas realizando iteraciones sobre las listas, no se pueden usar funciones de ordenamiento.

filtrar_pares: Recibe una lista con variables numéricas enteras. Retorna una nueva lista con todos los números pares que estaban en la lista que se recibió como parámetro. Los elementos de la lista devuelta deben estar en el orden original.

Ejemplo:

    filtrar_pares([5,6,13,7,11,9,10,11]) => [6,10]

filtrar_primos: Recibe una lista con variables numéricas enteras. Retorna una nueva lista con todos los números primos que estaban en la lista que se recibió como parámetro Los elementos de la lista devuelta deben estar en el orden original.

Hint: Utilizar la función programada en otra actividad que determina si un número es primo o no.

Ejemplo:

    filtrar_primos([5,6,13,7,11,9,10,11]) => [5,13,7,11,11]

sumar_elementos: Recibe una lista con variables numéricas. Retorna la suma de todos sus elementos.
No se puede utilizar la función sum(), ya existente en Python.

Ejemplo:

    sumar_elementos([5,6,13,7,11,9,10,11]) => 72

esta_ordenada: Recibe una lista con variables numericas. Retorna True en caso de que la lista este ordenada ascendentemente (es decir, los mas chicos en las primeras posiciones), False en caso contrario.

Ejemplos:

    esta_ordenada([5,6,13,7,11,9,10,11]) => False
    esta_ordenada([5,6,7,11]) => True

producto_escalar: Recibe dos listas de variables numéricas con la misma longitud. Interpretarlas como vectores. Retorna el producto escalar entre ambos vectores.

Ejemplos:

    producto_escalar([2,5,3], [4,6,7]) => 59

letras_en_palabras: Recibe una lista de letras y una cadena. La lista contiene en cada índice de la misma una letra (string de longitud 1). Retorna True en caso de que todas las letras se encuentren en la palabra, False en caso contrario.

Ejemplos:

    letras_en_palabras(["a","h","e"], "hola como estas") => True
    letras_en_palabras(["a","h","e"], "ola como estas") => False 
    
"""



def filtrar_pares(lista):
    pares = list(filter(lambda x: (x%2 == 0), lista))
    return pares

def filtrar_primos(lista):
    lista_1=[]
    for i in range(len(lista)):
       contador=0
       for j in range(1,lista[i]+1):
             if lista[i] % j ==0:
                contador= contador + 1
            
       if contador==2:
          lista_1.append( lista[i])
    return lista_1      

def sumar_elementos(lista):
    suma=0
    for i in range(len(lista)):
        #print(lista[i])
        suma=suma+lista[i]
    return suma #72  


def esta_ordenada(lista):
    resultado=True #lista2
    lista3=sorted(lista) #ordena la lista
    #print(lista3)
    if lista!=lista3:
          resultado=False #lista3
    return resultado

def producto_escalar(vector_1, vector_2):
    producto=list(map(lambda n1 , n2 : n1*n2 , vector_1 ,  vector_2 ))
    suma=0
    for i in range (len(producto)):
         suma=suma + producto[i]
         #print(producto[i])
    return suma  
    

def letras_en_palabra(letras, frase):
      contador=0
      for i in range(len(letras)):
           if letras[i] in frase:
             contador=contador+1  
            
      if contador==len(letras):
          resultado=True
      else:
          resultado=False
      return resultado

     

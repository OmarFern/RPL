
""" 
Completar el cuerpo de la función. La misma recibe un texto y debe retornar cuál es la palabra más larga del mismo. Se puede asumir que todas las palabras están separadas por espacios y no hay caracteres especiales.

No se pueden utilizar funciones de otras estructuras de datos. El ejercicio se debe resolver iterando la cadena, llevando el registro de las variables que se consideren adecuadas.

Ayuda: Tener cuidado con el caso en el que la palabra más larga es la última de todo el texto.

Ejemplos:

    palabra_mas_larga("Hola como estas este es un texto de prueba") => "prueba"
    palabra_mas_larga("Quiero aprobar algoritmos y algebra") => "algoritmos
    """


texto=input("ingrese un texto: ")

def palabra_mas_larga(texto):
    salida2=texto.split()
    cont=len(salida2)
    print(cont)
    mayor=""
    for i in range(len(salida2)):
        if len(salida2[i]) > len(mayor) :
            mayor=salida2[i]
           
    return print (mayor)
palabra_mas_larga(texto)
#---------------------------------


def palabra_larga(texto):
    lista = list(texto.split(' '))
    print(lista)
    palabra = max(lista, key=len)
    return palabra
palabra_larga(texto)

""" 
Completar el cuerpo de la función. La misma recibe una cadena de caracteres y dos caracteres individuales. Debe retornar la suma de la cantidad de veces que aparecen cada uno de los caracteres en la cadena.

Hint: No utilizar la función .count() de las cadenas. Cada vez que la invocamos, Python realiza un recorrido por la cadena buscando la subcadena que la función recibe como parámetro. Resolver el ejercicio realizando una única iteración en toda la cadena.

Ejemplo:

    contar_caracteres("casa", "c", "a") => 3
    contar_caracteres("cosa", "c", "a") => 2
    contar_caracteres("algoritmos", "a", "o") => 3
    contar_caracteres("algoritmos", "w", "x") => 0
"""


def contar_caracteres(cadena, caracter_1, caracter_2):
    count=0
    print(len(cadena))
    for index in range (len (cadena)):
        print(index)
        
        if cadena[index]==caracter_1 or cadena[index]==caracter_2:
            count=count+1
    return print (count)
cadena=str(input("ingrese datos 1 : "))
caracter_1=str(input("ingrese datos 2 : "))
caracter_2=str(input("ingrese datos 3 : "))

contar_caracteres(cadena, caracter_1, caracter_2)

""" 
def contar_caracteres(cadena, caracter_1, caracter_2):
    count=0
    for index in range (len (cadena)):
        if cadena[index]==caracter_1 or cadena[index]==caracter_2:
            count=count+1
    return count
"""
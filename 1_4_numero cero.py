""" Escribir un programa que solicite al usuario el ingreso de un número e imprima por pantalla si el número ingresado es positivo, negativo o cero.

Ejemplo:


"""
def validar_numero(num):
    """     
    >>> validar_numero(5) 
    Es positivo
    >>> validar_numero(-4) 
    Es negativo
    >>> validar_numero(0)
    Es igual a 0
    """
    
    if num ==0:
         print("Es igual a 0");
    elif num >=1:
        print("Es positivo");
    else :        
        print("Es negativo");
#-----------------------------------#
import doctest
print(doctest.testmod())
#TestResults(failed=0, attempted=3)
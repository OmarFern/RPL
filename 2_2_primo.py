"""
numeros  naturales (enteros positivos)a excepcion del 1
que solo son divisibles por si mismos y el 1
(divisible)= el resultado de su division es un numero entero
-------------------------------------------------------------------
Completar el cuerpo de la función. La misma debe devolver 
True en caso de que el número que se recibe como parámetro sea primo, y False en caso contrario.

Ejemplos:


"""
# numero =int(input("ingrese un numero :"))
# no se pone
def es_primo(numero):
    """ 
    >>> es_primo(3)
    True
    >>> es_primo(4) 
    False
    >>> es_primo(11)
    True
    >>> es_primo(15)
    False
    """
    contador=0
    for i in range (1 ,numero+1):
        if numero % i ==0:
            contador= contador + 1
            
    if contador==2:
        resultado= True
    else:
        resultado= False
    return resultado


#----------------------------------#
import doctest
print(doctest.testmod())
     



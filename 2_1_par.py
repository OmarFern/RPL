#Completar el cuerpo de la función. La misma debe devolver True en caso en el que el número recibido como parámetro recibido sea par, y False en caso contrario.





def es_par(numero):
    """ 
    >>> es_par(3) 
    False
    >>> es_par(32) 
    True
    >>> es_par(2) 
    True
    >>> es_par(20) 
    True
    >>> es_par(55) 
    False
    """    
    if numero%2 == 0:
         x= True
    else:
         x= False  
    
    return x
#-----------------#
import doctest
print (doctest.testmod())


 

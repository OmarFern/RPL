""" 
Completar el cuerpo de la función. 
La misma debe devolver True en caso de que el número recibido sea una potencia de dos, 
y False en caso contrario.

"""


#numero=int(input("ingrese un numero: "))
def es_potencia_de_dos(numero):
     """ 
     >>> es_potencia_de_dos(1) 
     True
     >>> es_potencia_de_dos(2) 
     True
     >>> es_potencia_de_dos(3) 
     False
     >>> es_potencia_de_dos(4) 
     True
     >>> es_potencia_de_dos(15) 
     False
     >>> es_potencia_de_dos(16) 
     True
     >>> es_potencia_de_dos(30) 
     False
     >>> es_potencia_de_dos(32) 
     True
     """
     contador=0
     contador=(2**numero)/numero
     if contador%2==0:
         resultado =True
     else:
         resultado =False
     return print( resultado)



#es_potencia_de_dos(numero)
#--------------------------#
import doctest
print(doctest.testmod())

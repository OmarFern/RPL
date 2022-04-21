""" 
Completar el cuerpo de la función. La misma recibe un número como parámetro y debe devolver el valor absoluto del mismo.

Ejemplos:

valor_absoluto(3) => 3
valor_absoluto(-3) => 3
"""
numero=int(input("ingrese un numero:"))

def valor_absoluto(numero):
    resultado=0
    resultado=abs(numero)
    return resultado
print(valor_absoluto(numero))
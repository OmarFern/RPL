""" 
Completar el cuerpo de la función. La misma recibe un número y debe devolver la suma de todos los divisores de este número. No deben considerarse el número en cuestión ni el número uno.

Por ejemplo, para el número 8, sus divisores son 4 y 2, por lo tanto la función debe devolver 6.

Ejemplos:

suma_de_divisores(8) => 6
suma_de_divisores(7) => 0
suma_de_divisores(10) => 7
suma_de_divisores(31) => 0
suma_de_divisores(32) => 30"""


def suma_de_divisores(numero):
    contador=0
    #contador=[]
    for i in range (2 ,numero):
        if (numero  % i ==0):
            contador= contador + i
           # contador.append(i)
    return print(contador)        


numero=int(input("ingrese un numero : "))
suma_de_divisores(numero)
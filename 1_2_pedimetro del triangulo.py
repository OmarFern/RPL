"""
Escribir un programa que solicite a un usuario la base y la altura de un rectángulo e imprima por pantalla cuál es el perímetro del mismo.

Ejemplo:

    >>> Ingrese la base del rectangulo: 5
    >>> Ingrese la altura del rectangulo: 20
    El perimetro del rectangulo es: 50
"""


base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))
perimetro = 2*base + 2*altura 
print("El perimetro del rectangulo es:", perimetro)

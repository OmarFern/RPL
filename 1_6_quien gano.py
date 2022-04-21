
""" 
Escribir un programa que solicite al usuario el ingreso del nombre de un equipo local con la cantidad de goles que metió en un partido, y del nombre de un equipo visitante con la cantidad de goles que metió en el mismo partido.
Luego, imprimir por pantalla el nombre del ganador o un mensaje indicando que hubo un empate.

    >>> Ingrese equipo local: Boca
    >>> Ingrese goles equipo local: 3
    >>> Ingrese equipo local: River
    >>> Ingrese goles equipo visitante: 1
    Boca

    >>> Ingrese equipo local: Boca
    >>> Ingrese goles equipo local: 0
    >>> Ingrese equipo local: River
    >>> Ingrese goles equipo visitante: 2
    River

    >>> Ingrese equipo local: Boca
    >>> Ingrese goles equipo local:2
    >>> Ingrese equipo local: River
    >>> Ingrese goles equipo visitante: 2
    Empate"""



equipo1=str(input("Ingrese equipo local: "))
goles_1=int(input("Ingrese goles equipo local: "))
equipo2=str(input("Ingrese equipo visitante: "))
goles_2=int(input("Ingrese goles equipo visitante: "))


def quien_gano(equipo1,goles_1,equipo2,goles_2):
    if goles_1>goles_2:
        resultado = equipo1
    elif goles_2>goles_1:
        resultado = equipo2
    else:
        resultado = "Empate"
    return resultado  
    
    
print(quien_gano(equipo1,goles_1,equipo2,goles_2))
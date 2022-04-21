""" 
Este ejercicio requiere la construcción de un pequeño programa que sirva para registrar votos correspondientes a una votación y 
determinar cuál fue el partido ganador.
Para esto, deberemos comenzar solicitando al usuario que ingrese votos
para los distintos partidos hasta que decida finalizar la carga. 
En un diccionario, 
se tienen que ir contabilizando los votos que llegan para los distintos partidos.
Es posible que haya votos que lleguen al centro de votación para un partido para el cual se recibieron votos previamente.
Finalmente, 
se tienen que imprimir ordenadamente una lista con todos los partidos con su correspondiente cantidad de votos,
ordenados de mayor a menor. (HINT: Usar alguna función para formatear strings, por ejemplo .format())
En el siguiente ejemplo se detallan los mensajes que deben ser mostrados al usuario.
Recordar que para que el ejercicio pase las pruebas, 
se tiene que mostrar exactamente el mismo.

Ejemplo:

>> Ingrese el partido a sumarle votos: Blanco
>> Ingrese la cantidad de votos a sumarle: 2
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Rosa
>> Ingrese la cantidad de votos a sumarle: 3
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Rosa
>> Ingrese la cantidad de votos a sumarle: 4
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Blanco
>> Ingrese la cantidad de votos a sumarle: 4
>> Desea seguir ingresando?(s/n): n
El partido Rosa obtuvo 7 votos.
El partido Blanco obtuvo 6 votos.

Notar que se puede asumir que se ingresa al menos un par partido-votos.
Pensar bien la modularización del programa.
"""
def solicitar_datos(partidos):
    """Maneja la entrada de datos por parte del usuario agregandolos al diccionario"""
    seguir_cargando = True
 
    while (seguir_cargando):
        partido = input("Ingrese el partido a sumarle votos: ")
        cantidad_votos = int(input("Ingrese la cantidad de votos a sumarle: "))
 
        if partido in partidos:
            partidos[partido] += cantidad_votos
        else:
            partidos[partido] = cantidad_votos
 
        seguir_cargando = input("Desea seguir ingresando?(s/n): ") == "s"
 
def imprimir_resultados(diccionario):
    # Como se estructuraran las tuplas dentro de la lista ordenada
    NOMBRE_DEL_PARTIDO = 0
    CANTIDAD_DE_VOTOS = 1
 
    # Devuelve una lista de tuplas ordenada por cantidad de votos
    items_ordenados = sorted(diccionario.items(), reverse=True, key=lambda lista: lista[CANTIDAD_DE_VOTOS])
 
    # Iteramos la lista ordenada e imprimimos los valores
    for partido_votos in items_ordenados:
        print("El partido {} obtuvo {} votos.".format(partido_votos[NOMBRE_DEL_PARTIDO], partido_votos[CANTIDAD_DE_VOTOS]))
 
def main():
    partidos = {}
 
    solicitar_datos(partidos)
    imprimir_resultados(partidos)
 
main()

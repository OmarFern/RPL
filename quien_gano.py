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
    return print (resultado  )  
    
    
print(quien_gano(equipo1,goles_1,equipo2,goles_2))

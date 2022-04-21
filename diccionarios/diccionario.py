alumnos={"river":1111 ,"boca":2222 ,"bacelona":3333,"velez":4444}
print(alumnos["river"])
contador=0
resultado=dict(filter(lambda x: x[contador] == "river", alumnos.items()))

print(resultado)

def buscar():
    usuario=str(input("ingrese un usuario :"))
    contraseña=int(input("ingrese contraseña:"))
    valido=""  #           #
    
    if alumnos[usuario]==contraseña:
         valido ="si"
    else:
         valido="no"
    return print(valido)    
buscar()


variables = {'A':1, 'B':2, 'C':3}
print(variables.keys())
print(variables.values())
print(variables.items())
print ( dict(filter(lambda x: x[0] == "B", variables.items())))

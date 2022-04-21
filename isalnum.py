cadena="+*ab"
#+-/* no son alfanumericos son operadores si hay un espacio vacio tambien lo considera que no es un digito
    
print(cadena.isalnum())#false
print(not cadena.isalnum())# true
# determina si todos son alfanumericos 
def validar(cadena):
    if cadena.isalnum():# en el if solo pasa si es verdad la sentencia =>
        print("pasa si es verdad")
    else :
        print (" es falso osea tiene caracteres que  como +/*-")
validar(cadena)        


""" 
Completar el cuerpo de la función. La misma recibe una cadena y debe retornar la misma habiendo filtrado todas las vocales que contenía.

Ejemplos:

    filtrador_de_vocales("hola") => "hl"
    filtrador_de_vocales("facultad") => "fcltd"
    filtrador_de_vocales("algoritmos") => "lgrtms"   
"""


"""
cadena=str(input("ingrese una cadena: "))


def filtrador_de_vocales(cadena):
    lista=[]
    lista.append(",".join(cadena))#['a,l,g,o,r,i,t,m,o,s']
    
    #vocales=[a,e,i,o,u]
    #posicion=[0,1,2,3,4]
    
    return print(lista)
filtrador_de_vocales(cadena)"""

cadena="algoritmos"
result = list(filter(lambda x: x in "bcdfghjklmnñpqrstvwxyz", cadena))
print(result)#['l', 'g', 'r', 't', 'm', 's']
print("".join(result)) #lgrtms


"""
def filtrador_de_vocales(cadena):
    result = list(filter(lambda x: x in "bcdfghjklmnñpqrstvwxyz", cadena))
    return ("".join(result))"""
























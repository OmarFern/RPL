

""" 
Completar el cuerpo de la función. La misma debe retornar un valor booleano: True en caso de que las palabra que se recibe sea capicúa, False en caso contrario.

Intentar resolver el ejercicio en una línea.

Ejemplos:

    es_capicua("neuquen") => True
    es_capicua("mendoza") => False
    es_capicua("menem") => True
    es_capicua("alfonsin") => False 
"""
def es_capicua(palabra):
    resultado=""
    print(palabra[0])
    print(palabra[-1])
    if (palabra[0]==palabra[-1]):    
        resultado = True
    else:
        resultado = False
       
       
    return  print (resultado)
palabra=str(input("ingrese una palabra:"))
es_capicua(palabra)
"""
def es_capicua(palabra):
    return palabra == palabra[::-1] 
"""  

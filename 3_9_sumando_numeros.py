""" 

Completar el cuerpo de la función. La misma recibe una cadena como parámetro y debe retornar el resultado de sumar todos los caracteres numéricos que aparezcan en la misma.

Ejemplo:

    sumar_caracteres_numericos("1") => 1
    sumar_caracteres_numericos("a1") => 1
    sumar_caracteres_numericos("12") => 3
    sumar_caracteres_numericos("123") => 6
    sumar_caracteres_numericos("o1la293fr") => 1 + 2 + 9 + 3 = 15
"""




cadena="o1la293fr"

result = list(filter(lambda x: x in "123456789", cadena))
result2="".join(result)
suma=0
for i in range(len(result2)):
      suma = suma + int(result2[i])
    

print(suma)

#-----------------------------------------------------
def sumar_caracteres_numericos(cadena):
    result = list(filter(lambda x: x in "123456789", cadena))
    result2="".join(result)
    suma=0
    for i in range(len(result2)):
         suma = suma + int(result2[i])
    

    return print(suma)
sumar_caracteres_numericos(cadena)

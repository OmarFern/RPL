""" 
Completar el cuerpo de la función. La misma debe retornar la cantidad de veces que el caracter_1 se encuentra inmediatamente antes (es decir, en el índice anterior) al caracter_2 en la cadena que se recibe como primer parámetro.

No resolver el ejercicio usando la función .count(). Iterar la cadena.

Ejemplos:

   precendencia_de_caracteres("hola hola", "h", "o") => 2
   precendencia_de_caracteres("la igualdad de genero es fundamental para
          el desarrollo de una sociedad", "a", "l") => 2
   precendencia_de_caracteres("la mejor verdura del universo es la pizza y el que
          diga lo contrario esta errado", "e", "r") => 3
"""






texto= "la mejor verdura del universo es la pizza y el que diga lo contrario esta errado"
caracter_1="e"
caracter_2="r"


def palabra_larga(texto):
    lista=texto.split(" ")
    contador=0
    print(lista)
#['la', 'igualdad', 'de', 'genero', 'es', 'fundamental', 'para', 'el', 'desarrollo', 'de', 'una', 'sociedad']    
    for i in range(len(lista)):
        
           if lista[i].find(caracter_1+caracter_2)!= -1:
             contador =contador +1
           
              
    return print(contador)
palabra_larga(texto)
"""
cita = "la igualdad de genero es fundamental para el desarrollo de una sociedad"
ocurrencias = cita.count("al")
print(ocurrencias)"""

def palabra_larga(texto):
    lista=texto.split(" ")
    contador=0
    print(lista)
#['la', 'igualdad', 'de', 'genero', 'es', 'fundamental', 'para', 'el', 'desarrollo', 'de', 'una', 'sociedad']    
    for i in range(len(lista)):
        if  caracter_1+caracter_2 in lista[i]:
               contador =contador +1
           
              
    return print(contador )
palabra_larga(texto)



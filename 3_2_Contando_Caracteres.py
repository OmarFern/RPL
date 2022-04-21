#cadena= "papitas"
#for c in comida:
 #  print(c)

cadena= "algoritmos"
caracter_1="w"
caracter_2="x"


def contar_caracteres(cadena, caracter_1, caracter_2):
    #contador1=[]
    #contador2=[]
    contador1=0
    contador2=0
    for i in cadena:
        if (i==caracter_1):
           contador1=contador1 + 1
         
       
        elif((i==caracter_2)):
           contador2 = contador2 + 1
           
            
    return print(contador1 + contador2)


contar_caracteres(cadena, caracter_1, caracter_2)


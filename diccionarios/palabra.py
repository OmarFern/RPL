
def cantidad_de_letras(palabra):
    contar_letras={}
    for letra in palabra:
        if letra  not in contar_letras:
            contar_letras[letra]=1
        else:
            contar_letras[letra]+=1
    for letra in contar_letras:
        print("la letra", letra ,"se encuentra" , contar_letras[letra],"veces")  
                   
palabra="cargar palabra"
cantidad_de_letras(palabra)
"""la letra c se encuentra 1 veces
la letra a se encuentra 5 veces
la letra r se encuentra 3 veces
la letra g se encuentra 1 veces
la letra   se encuentra 1 veces
la letra p se encuentra 1 veces
la letra l se encuentra 1 veces
la letra b se encuentra 1 veces"""
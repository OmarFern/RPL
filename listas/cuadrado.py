lista_de_tuplas=[(7, -5), (4, -5), (1, 2), (1, -2)]
def filtrar_tuplas_por_suma(lista_de_tuplas):
    lista=[] 
    for i in lista_de_tuplas:
        #print(i)
        #print(i[0],i[1])
        if i[0]+i[1]>0:
            lista.append(i)    
    return  lista #[(7, -5), (1, 2)]
print(filtrar_tuplas_por_suma(lista_de_tuplas))
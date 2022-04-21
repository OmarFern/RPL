numero=7
lista=[1,2,3,4,5,6,7]
#---------------1--------------------------------
def numeros_positivos(numero):
    lista=[]
    for i in range(1,numero+1):
        lista.append(i)
    return lista  #[1, 2, 3, 4, 5, 6, 7]
#---------------2--------------------------------         
def numeros_positivos_pares(numero):
    lista=[]
    for i in range(1,numero+1):
        if i%2==0: 
           lista.append(i)
    return lista #[2, 4, 6]
#----------------3------------------------------    
def numeros_positivos_pares_cuadrado(numero):
    lista=[]
    for i in range(1,numero+1):
        if i%2==0: 
           lista.append(i**2)# si es par entonces 
    
    return lista #[4, 16, 36]
#----------------4-----------------------------
def impares_al_cuadrado(lista):
    numero=len(lista)
    lista_final=[]
    for i in range(numero):
        print(lista[i])
        if lista[i]%2==0: 
           lista_final.append(lista[i])# si es par entonces 
        else:
           lista_final.append(lista[i]**2)# si es impar
    return lista_final #[1, 2, 9, 4, 25, 6, 49]

#-----------------5----------------------------
lista_de_tuplas=[(7, -5), (4, -5), (1, 2), (1, -2)]
def filtrar_tuplas_por_suma(lista_de_tuplas):
    lista=[] 
    for i in lista_de_tuplas:
        #print(i)
        #print(i[0],i[1])
        if i[0]+i[1]>0:
            lista.append(i)    
    return  lista #[(7, -5), (1, 2)]
#----------------6------------------------------------    
def filtrar_tupla_elemento_par(lista_de_tuplas):
    lista=[] 
    for i in lista_de_tuplas:
        #print(i)
        #print(i[0],i[1])
        if i[0]%2==0 or i[1]%2==0:
            lista.append(i)
    return lista    

def main():
       print(numeros_positivos(numero))#1
       print(numeros_positivos_pares(numero))#2
       print(numeros_positivos_pares_cuadrado(numero))#3
       print(impares_al_cuadrado(lista))#4
       print(filtrar_tuplas_por_suma(lista_de_tuplas))#5
       print(filtrar_tupla_elemento_par(lista_de_tuplas))#6
main()    


"""def filtrar_tuplas_por_suma(lista):
    return [x for x in lista if x[0]+x[1] >= 0] # por compresion 

print(filtrar_tuplas_por_suma([(7, -5), (4, -5), (1, 2), (1, -2)]))# => [(7, -5),(1, 2)]"""

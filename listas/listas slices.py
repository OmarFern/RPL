#-----------------1-----------------------------
def ultimos_tres_elementos(lista):
     lista2=lista[slice(-1,-4,-1)]
     lista2.reverse()

     return lista2 #[6, 4, 7]

print(ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]))
#-----------------2------------------------------
def ultimos_tres_elementos_concatenados(lista):
    lista2=[]
    for j in range(len(lista)):
         for i in range(1,len(lista[j])):
              lista2.append(lista[j][i])
    
    return lista2 #[2, 3, 4, 6, 7, 8, 10, 11, 12]

print(ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) )
#-----------------3-----------------------------

def indices_pares(lista):
    lista2=[]
    for i in range(len(lista)):
        if i%2==0:
            lista2.append(lista[i])
            
    return lista2 #['a', 'c', 'e']

print(indices_pares(["a","b","c","d","e"]) )
#-----------------4---------------------------------
    
def indices_impares(lista):
    lista2=[]
    for i in range(len(lista)):
        if i%2!=0:
            lista2.append(lista[i])
            
    return lista2 #['b', 'd', 'f']

print(indices_impares(["a","b","c","d","e", "f"]))
#------------------5--------------------------------

def invertir(lista):
    lista.reverse()
    return lista   #[5, 4, 3, 2, 1]

print(invertir([1,2,3,4,5]))
















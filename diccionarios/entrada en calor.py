#-----------------1---------------------------
def numeros_al_cuadrado(numero):
    dic={}
    for i in range(1,numero+1):
         #dic[i]=[i*i]
         dic[i]=i*i
         
    return dic
print(numeros_al_cuadrado(4))# => {1: 1, 2: 4, 3: 9, 4: 16}
#-------------------2-------------------------
dicc_1 = {'clave1': 1, 'clave3': 3}
dicc_2 = {'clave2': 2, 'clave4': 4}

def mezclar_diccionarios(dicc_uno, dicc_dos):
    dicc_3=dicc_uno.copy()
    dicc_3.update(dicc_dos)
    return dicc_3 #{'clave1': 1, 'clave3': 3, 'clave2': 2, 'clave4': 4}
print(mezclar_diccionarios(dicc_1, dicc_2))
#-------------------3-------------------------

def filtrar_por_sumar_diez(diccionario):
    
    return dict(filter(lambda x: x[0]+ x[1] >=10, diccionario.items()))#{8: 11, 9: 2}
print(filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}))

#--------------------4------------------------

dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}
def ordenar_valores_por_longitud(diccionario):
     lista=list(diccionario.values())
     return sorted( lista ,key=len ,reverse=True)#['algoritmos', 'guarna', 'river']
print(ordenar_valores_por_longitud(dicc))










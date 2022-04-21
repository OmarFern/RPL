import operator

stats = {'key1':20, 'key2':35, 'key3': 44}
max_key = max(stats.items(), key=operator.itemgetter(1))[0]
print(max_key)

#------------------------buscar el minimpo-----#
diccionario = {'key1':[20], 'key2':[35], 'key3': [44]}
llave_minimo=min(diccionario.keys(), key=lambda k :diccionario[k])
#------------------------buscar el maximo-------#
llave_maximo=max(diccionario.keys(), key=lambda k :diccionario[k])
print(llave_minimo) #key1
print(diccionario[llave_minimo])#20 me  muestra el minimo
print(llave_maximo)
print(diccionario[llave_maximo])

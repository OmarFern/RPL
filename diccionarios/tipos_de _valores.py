torneo={"racing":18,"ferro":2,"almagro":"ninguno"}
# duccionario[clave]="valores" o numero o lista o tupla 
torneo["boca"]="?" # agrega al diccionario
print(torneo)#{'racing': 18, 'ferro': 2, 'almagro': 'ninguno', 'boca': '?'}
# claves son inmutables => numeros strings booleamos
#  valores => pueden ser mutables o inmutables

# -----borrar ------ del diccionario["clave"]
del  torneo["boca"]
print(torneo)# borra lo que le agregamos
#{'racing': 18, 'ferro': 2, 'almagro': 'ninguno'}
# for  en diccionarios
for clave in torneo:
# for clave in diccionario:
    
    print(clave , "tiene ", torneo[clave] , "torneo")
   #  racing tiene  18 torneo
   #ferro tiene  2 torneo
   #almagro tiene  ninguno torneo
libertadores={"racing":18,"ferro":2,"almagro":"ninguno"}   
if "river" in libertadores:
    print("esta")   
else :
    print("no esta")    
    
 #--------------
copas={"racing":[4,3],"boca":[5,8],"river":[8,5]}   
copas["boca"].remove(5)# borra el valor 
print(copas)
#{'racing': [4, 3], 'boca': [8], 'river': [8, 5]}
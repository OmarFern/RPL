listas=["fernando","iglesias", 20 ];
print(listas);
print(listas[0]);
print(listas[1]);
print(listas[2]);
listas.append(2021);
print(listas);
listas +=[7,5,8];
print(listas);
listas1=[1,2,3,4,5,6]
listas1.insert(3,"valor");
print(listas1)
print(listas1.pop(0))
print(listas1.remove(4))
print(listas1)
print(listas1.clear())
listas2=[1,2,3,4,5,6]
print(6 in listas2)
valores=[0,1,2,3,4,5,6,7,8]
print(valores[:5])
print(valores[:5])

numero=[];
for i in range (1,100):
   numero.append(i)
numero=[x for x in range (1,101)]
print (numero)

numero2=[x**2 for x in range (1,101)]
print (numero2)
num=tuple((x for x in range(1,1)))
print(num)
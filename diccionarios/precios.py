stock={1:[2,300],2:[5000,3],5:[60,400]}
contador=0
for codigo in stock:
    contador += stock[codigo][0]*stock[codigo][1]
print ("el valor es : ",contador) 

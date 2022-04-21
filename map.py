
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)#<map object at 0x00000232FBE80430>

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
# run {16, 1, 4, 9}

"""---------------map 1 lista------------------------------------"""
lista=[1,2,3,4,5,6]

suma= map(lambda x: x+2, lista )
print(suma) #<map object at 0x00000232FC048F10> sin el list

suma= list (map(lambda x: x+2, lista ))
print(suma) # run [3, 4, 5, 6, 7, 8]
"""---------------map 2 listas -----------------------------"""
num1=[4,5,6]
num2=[5,2,6]

suma_listas=map(lambda n1 , n2 : n1+n2 , num1 ,  num2 )
print(list(suma_listas))
suma_listas2=list(map(lambda n1 , n2 : n1*n2 , num1 ,  num2 ))
print(suma_listas2)

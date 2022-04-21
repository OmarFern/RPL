numbers = [1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers 
even_numbers_iterator = list(filter(lambda x: (x%2 == 0), numbers))
print(even_numbers_iterator)
#---------------------------------1----------------------------------------
lista=[5,6,13,7,11,9,10,11]
def filtrar_pares(lista):
    pares = list(filter(lambda x: (x%2 == 0), lista))
    print(pares)
filtrar_pares(lista)#[6,10]

#----------------------------------2---------------------------
def filtrar_primos(lista):
    lista_1=[]
    for i in range(len(lista)):
       contador=0
       for j in range(1,lista[i]+1):
             if lista[i] % j ==0:
                contador= contador + 1
            
       if contador==2:
          lista_1.append( lista[i])
    return lista_1      
            
 
print(filtrar_primos(lista)) #[5,13,7,11,11]
#----------------------------3-------------------------------

#lista=[5,6,13,7,11,9,10,11]
def sumar_elementos(lista):
    suma=0
    for i in range(len(lista)):
        #print(lista[i])
        suma=suma+lista[i]
    return print(suma) #72   
sumar_elementos(lista)
#--------------------------------4 --------------------
#
# lista= [16, 4, 9, 1, 3, 20, 8]
#lista2=[5,6,7,11]
def esta_ordenada(lista):
    resultado=True #lista2
    lista3=sorted(lista) #ordena la lista
    #print(lista3)
    if lista!=lista3:
          resultado=False #lista3
    return resultado
print(esta_ordenada(lista)) 
#--------------------------5---------------------------
vector_1=[2,5,3]
vector_2=[4,6,7]
def producto_escalar(vector_1, vector_2):
    producto=list(map(lambda n1 , n2 : n1*n2 , vector_1 ,  vector_2 ))
    suma=0
    for i in range (len(producto)):
         suma=suma + producto[i]
         #print(producto[i])
    return suma        
   
print(producto_escalar(vector_1, vector_2))#59
#------------------------6------------------------------
letras=["a","h","e"]
frase="ola como estas"
def letras_en_palabra(letras, frase):
      contador=0
      for i in range(len(letras)):
           if letras[i] in frase:
             contador=contador+1  
            
      if contador==len(letras):
          resultado=True
      else:
          resultado=False
      return resultado    


print(letras_en_palabra(letras, frase))
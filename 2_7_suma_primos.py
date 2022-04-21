"""
numeros  naturales (enteros positivos)a excepcion del 1
que solo son divisibles por si mismos y el 1
(divisible)= el resultado de su division es un numero entero
1
2

Completar el cuerpo de la función. La misma recibe como parámetro un número que 
será tomado como límite superior del cálculo que debemos realizar.
La función debe retornar la suma de todos los números positivos primos 
existentes entre el 0 y el número ingresado inclusive.
Recordar que el 1 no se considera primo y el 2 por definición sí lo es.
Se puede asumir que el parámetro de entrada ha sido verificado previamente y siempre es mayor que 0.

Ejemplos:

suma_de_numeros_primos(1) => 0
suma_de_numeros_primos(2) => 2
suma_de_numeros_primos(3) => 5
suma_de_numeros_primos(4) => 5
suma_de_numeros_primos(5) => 10
suma_de_numeros_primos(17) => 2 + 3 + 5 + 7 + 11 + 13 + 17 = 58

Hint: Pueden utilizar la función es_primo(numero) 
definida en la segunda actividad de la categoría, logrando un mayor grado de modularización.

"""
numero =int(input("ingrese un numero : "))

def suma_de_numeros_primos(numero):
    suma=[]
    suma2=0
    for i in range (2,numero+1):
        if es_primo(i)==True:
            suma2= suma2 + i
            suma.append(i)
    print(suma)   
    return (print (suma2)) # no se pone print
        
# no se pone
def es_primo(numero):
    contador=0
    for i in range (1 ,numero+1):
        if numero % i ==0:
            contador= contador + 1
            
    if contador==2:
        resultado= True
    else:
        resultado= False
    return resultado

#es_primo(numero)# no se pone y prin tampoco
suma_de_numeros_primos(numero)
     

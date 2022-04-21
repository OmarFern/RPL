"""------------------------filter listas----------------------------"""
numbers = [1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers 
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)# run [2, 4, 6]
""""******************************************************"""
num1=10
num2=30

def sumar(num1,num2):
    return print (num1 +num2)

sumar(num1,num2)
""""--------------------lambda-------------------------------------"""
sumar_2= lambda num1 , num2 : num1 + num2
print(sumar_2(15,10)) # si o si tiene que estar los parametros 
"""----------------filter diccionario------------------------------"""
nombre=1
variables = {'A':1, 'B':2, 'C':3}
print ( dict(filter(lambda x: x[nombre] > 1, variables.items())))
##------------------------filter listas---------------------#########
stock_min=1
stock_actual=0
variables_2 = {1:[10,15],22:[25,30],3:[33,15],5:[2,2]}
print(variables_2[1][0])
print(variables_2[1][1])
print ( dict(filter(lambda x: x[1][0] > x[1][1] , variables_2.items())))
"""************************* filter **********************************************"""
stock_min=1
stock_actual=0

variables_2 = {1:[10,15],22:[25,12],3:[33,15],5:[2,2]}
print(variables_2[1][0])#run 10
print(variables_2[1][1])#run 15
print ( dict(filter(lambda x: x[stock_min][stock_actual] > x[stock_min][stock_min] , variables_2.items())))

#{22: [25, 12], 3: [33, 15]}


"""**********************************************"""
def es_primo(numero):
    resultado=True
    if numero == 1:
        resultado=False
    else:        
        for n in range(2, numero):
            if numero % n == 0:
                resultado=False
    return resultado
numeros=[3, 7, 11, 13]
menor_numero=8
#https://www.programiz.com/python-programming/methods/built-in/filter
def filtrar_primos(numeros, menor_numero):
            #filter(function, iterable)
    primos =filter( es_primo ,numeros)
    print(primos)
    primos_filtrados = list(filter(lambda x: x> menor_numero, primos))
    return primos_filtrados
print(filtrar_primos(numeros, menor_numero))#[11, 13]

"""*******************************"""""



numbers = [1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers 
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers) #[2, 4, 6]

"""*************************************"""
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, letters)


# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)#('a', 'e', 'i', 'o')







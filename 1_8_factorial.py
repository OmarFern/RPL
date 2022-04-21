""" Escribir un programa que solicite el ingreso de un número y que luego calcule e imprima su factorial.

    Ingrese un numero: 5  es 120
 """

def A_factorial(numero):
        """
        >>> A_factorial(5)
        120
        >>> A_factorial(6)
        720
        >>> A_factorial(7)
        5040
        >>> A_factorial(8)
        40320
        >>> A_factorial(9)
        362880
        
        """
        #numero=int(input("ingrese un numero:"))
        factorial=1
        for i in range(1,numero +1):
            factorial = factorial*i
        return factorial
 #---------------------------------------------#   
import doctest
print(doctest.testmod())
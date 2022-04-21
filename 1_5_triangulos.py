""" Escribir un programa que solicite el ingreso del valor de los 3 lados de un triángulo. Luego, debe imprimir por pantalla si el triángulo es equilátero (3 lados iguales), escaleno (3 lados distintos) o isósceles (2 lados iguales).

Ejemplos:

    >>> Ingrese la longitud del primer lado del triangulo: 10
    >>> Ingrese la longitud del segundo lado del triangulo: 10
    >>> Ingrese la longitud del tercer lado del triangulo: 10
    Es equilatero

    >>> Ingrese la longitud del primer lado del triangulo: 10
    >>> Ingrese la longitud del segundo lado del triangulo: 15
    >>> Ingrese la longitud del tercer lado del triangulo: 20
    Es escaleno

    >>> Ingrese la longitud del primer lado del triangulo: 10
    >>> Ingrese la longitud del segundo lado del triangulo: 5
    >>> Ingrese la longitud del tercer lado del triangulo: 10
    Es isosceles """






num1=int (input("Ingrese la longitud del primer lado del triangulo: "));
num2=int (input("Ingrese la longitud del segundo lado del triangulo: "));
num3=int (input("Ingrese la longitud del tercer lado del triangulo: "));

if num1==num2==num3 :
    print("Es equilatero");
elif num1!=num2 and num1!=num3:
    print("Es escaleno");
else:
    print("Es isosceles");

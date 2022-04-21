"""
>> Ingrese el partido a sumarle votos: Blanco
>> Ingrese la cantidad de votos a sumarle: 2
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Rosa
>> Ingrese la cantidad de votos a sumarle: 3
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Rosa
>> Ingrese la cantidad de votos a sumarle: 4
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Blanco
>> Ingrese la cantidad de votos a sumarle: 4
>> Desea seguir ingresando?(s/n): n
El partido Rosa obtuvo 7 votos.
El partido Blanco obtuvo 6 votos."""


def definiendo_votacion():
    #partido=str(input("Ingrese el partido a sumarle votos :"))
    #voto=int(input("Ingrese la cantidad de votos a sumarle :"))
    seguir="s" #str(input("Desea seguir ingresando?(s/n):"))
    suma1=0
    suma2=0
    while seguir!="n":
            partido=str(input("Ingrese el partido a sumarle votos :"))
            voto=int(input("Ingrese la cantidad de votos a sumarle :"))
            if partido=="Blanco":
                suma1=suma1+ voto
                seguir=str(input("Desea seguir ingresando?(s/n):"))#sale del while si o no
            elif partido=="Rosa":
                suma2=suma2 +voto
                seguir=str(input("Desea seguir ingresando?(s/n):"))#sale del while si o no
            
    print(f"El partido Rosa obtuvo {suma2} votos.")
    print(f"El partido Blanco obtuvo {suma1} votos.")
    return 
print(definiendo_votacion())
    

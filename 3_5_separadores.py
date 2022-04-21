""" 
Completar el cuerpo de la función. La misma debe tomar la cadena que se pasa como parámetro e insertar el separador cada tantos caracteres como indique el parámetro "espaciado".

Ejemplos:

   insertar_separadores("255255255255", ".", 3) => "255.255.255.255"
   insertar_separadores("holacomoestas", "|", 4) => "hola|como|esta|s"  """


""" rpl

cad=input("Número:")
car=input("Caracter:")
cont=0
cad2=""
for c in cad:
     if cont!=0 and cont%3==0:
         cad2=cad2+car
     cad2=cad2+c
     cont=cont+1
print(cad2)"""

cadena=str(input("numero: "))
separador=str(input("separador:"))
espaciado=int(input("espaciado:"))
def insertar_separadores(cadena, separador, espaciado):
    cont=0
    cad2=""
    for c in cadena:
     if cont!=0 and cont%espaciado==0:
         cad2=cad2+separador
     cad2=cad2+c
     cont=cont+1
    print(cad2)
    
insertar_separadores(cadena, separador, espaciado)    
 

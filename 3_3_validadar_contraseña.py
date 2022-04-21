"""
El método  https://www.programiz.com/
##############    isalnum ()  ############

ejenplo ....string.isalnum()
devuelve True si todos los caracteres de la cadena son alfanuméricos (ya sean alfabetos o números).
Si no, devuelve False.
********************************************************
El método string

###########      isupper ()   ##################
devuelve si todos los caracteres de una cadena están en mayúsculas o no.

"""


def validar_contrasenia(contrasenia):
    tiene_numero = False
    tiene_mayuscula = False
    tiene_caracter_especial = False
    
    if len(contrasenia) > 7 and len(contrasenia) < 15:

        if not contrasenia.isalnum():
            tiene_caracter_especial = True

        for caracter in contrasenia:
            if caracter.isupper():
                tiene_mayuscula = True

            if caracter.isnumeric():
                tiene_numero = True

        return tiene_numero and tiene_mayuscula and tiene_caracter_especial

    else:
        return False
contrasenia=str(input("ingrese una contraseña  min 7 y max 15 carecteres: "))
print(validar_contrasenia(contrasenia))    

cadena="01101011110"

print(cadena.isnumeric())# true
    # Determina si todos los caracteres son alfanuméricos.
print("abc123".isalnum())
    #True
    # Determina si todos los caracteres son alfabéticos.
print("abcdef".isalpha())
    #True
print("abc123".isalpha())
    #False
    # Determina si todas las letras son minúsculas.
print("abcdef".islower())
    #True
    # Mayúsculas.
print("ABCDEF".isupper())
   # True
    # Determina si la cadena contiene todos caracteres imprimibles.
print("Hola \t mundo!".isprintable())
    #False
    # Determina si la cadena contiene solo espacios.
print("Hola mundo".isspace())
    #False
print("    ".isspace())
    #True
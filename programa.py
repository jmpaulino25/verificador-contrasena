# Verificador sencillo de contraseñas

contraseña = input("Escribe una contraseña: ")

tiene_mayuscula = False
tiene_numero = False

for caracter in contraseña:
    if caracter.isupper():
        tiene_mayuscula = True
    if caracter.isdigit():
        tiene_numero = True

if len(contraseña) >= 8 and tiene_mayuscula and tiene_numero:
    print("Contraseña segura")
else:
    print("Contraseña débil") 
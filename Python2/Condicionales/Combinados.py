# pylint: disable=C0103:invalid-name
"""
high level support for doing this and that.
"""
# El condicional "switch" no existe en python

edad = int(input("Inserte su edad: "))

if 0<edad<100:  # Se hace para limitar dentro de un rango ORIGINAL: edad>0 and edad<100
    print("Edad correcta ")
    if edad>=18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")

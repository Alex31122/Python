# pylint: disable=C0103:invalid-name
"""
high level support for doing this and that.
"""

nombre = input("Inserte su nombre: ") # Guarda datos de tipo cadena
edad = int(input("inserte su edad: "))

# print("Hola {} tienes {} años".format(nombre, edad))
print(f"Hola {nombre} tienes {edad+1} años")

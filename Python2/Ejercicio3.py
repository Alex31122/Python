# pylint: disable=C0103:invalid-name
"""
high level support for doing this and that.
"""
# Ejercicio 3 - Intercambiar el valor de 3 variables

a = input("a -> ")
b = input("b -> ")

a , b = b , a

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")

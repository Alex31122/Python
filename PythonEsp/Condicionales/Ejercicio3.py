# pylint: disable=C0103:invalid-name
"""
Ejercicio 3:
Hacer un programa que pida un carácter e indique si es vocal o no.
"""

letra2 = " "
letra = input("Inserte un caracter: ").lower()  # upper
letra.lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Es una vocal")
else:
    print("No es una vocal")

# pylint: disable=C0103:invalid-name
"""
Ejercicio 2:
Hacer un programa que pida 3 numeros y determine cuál es el mayor.
"""

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
num3 = int(input("Introduce otro numero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El numero mayor es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El numero mayor es {num2}")
elif num3 >= num1 and num3 >= num2:
    print(f"El numero mayor es {num3}")

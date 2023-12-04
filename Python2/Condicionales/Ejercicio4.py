# pylint: disable=C0103:invalid-name
"""
Ejercicio 4:
Construir un programa que simule el funcionamiento de una calculadora que puede
realizar las cuatro operaciones aritméticas básicas (suma, resta, multiplicación y división).
El usuario debe especificar la operación con el primer carácter del nombre de la operación.

S, s -- Suma
R, r -- Resta
P, p, M, m -- Multiplicación
D, d -- División
"""

from __future__ import division


num1 = float(input("Inserte un numero: "))
num2 = float(input("Inserte otro numero: "))

print("\nS,s -- Suma:\nR, r -- Resta\nP, p, M, m -- Multiplicación\nD, d -- División")
operacion = input("\nInserte el caracter de nombre de operación: ").upper()

if operacion == 'S':
    suma = num1 + num2
    print(f"\nLa suma es: {suma}")

elif operacion == 'R':
    resta = num1 - num2
    print(f"\nLa resta es: {resta}")

elif operacion == 'P' or operacion == 'M':
    multiplicacion = num1 * num2
    print(f"\nLa multiplicacion es: {multiplicacion:.2f}")

elif operacion == 'D':
    division = num1 / num2
    print(f"\nLa division es: {division:.2f}")

else:
    print("\nEl caracter no es correcto")

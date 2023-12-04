# pylint: disable=C0103:invalid-name
"""
Ejercicio 4:
Hacer un programa para ingresar el radio de un circulo y se reporte su área
y la longitud de la circunferencia.
"""
import math

radio = float(input("Valor de radio: "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"Area: {area:.4f}") # Para que salgan cuatro decimales despues del punto
print(f"Longitud de circunferencia: {longitud:.4f}")

# pylint: disable=C0103:invalid-name
"""
Ejercicio 5:
Hacer un programa que simule un cajero automático con un saldo inicial de $1000
y tendrá el siguiente menú de opciones:

1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
"""

saldo = 1000
print("==========MENU==========\n\n")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir\n")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    suma = float(input("Inserte la cantidad a ingresar: "))
    saldo += suma
    print(f"Dinero en cuenta {saldo}")
elif opcion == 2:
    resta = float(input("\nIngrese la cantidad a retirar: "))
    if resta > saldo:
        print("No tiene la suficiente cantidad a retirar")
    else:
        saldo -= resta
        print(f"Dinero en cuenta {saldo}")
elif opcion == 3:
    print(f"\nEl saldo de la cuenta es {saldo}")
else:
    print("Gracias por ultilizar su cajero automatico")

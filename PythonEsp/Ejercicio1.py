# pylint: disable=C0103:invalid-name
"""
high level support for doing this and that.
"""

a = float(input("a -> "))
b = float(input("b -> "))
c = float(input("c -> "))

resultado = (a**3 * (b**2 - 2*a*c)) / (b*2)

print(f"\nEl resultado de la expresion es: {resultado}")

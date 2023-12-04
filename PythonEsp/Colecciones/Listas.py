# pylint: disable=C0103:invalid-name
"""
    Listas
"""

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",40,5.67,[1,2,3],True]

#print(lista)
#print(lista[2])
#print(lista[-2])

# Sublistas
#print(lista[0:3])   # Imprime desde el indice 0 hasta el indice mas 1 al que se quiere llegar
# Tambien se puede quitar el 0 y automaticamente empezara desde 0
# Se puede quitar el tres y python sabra que es hasta el final de la listas
#print(lista[1:4])

"""
    Listas Parte II
"""
lista2 = [1,2,4,5,2,4,5]*2  # Se copian los elementos tantas veces
lista3 = [6,7,8]
lista4 = lista2 + lista3

lista2.insert(2,"Hola") # Agrega en una posicion en especifico un elemento
lista2.extend([lista]) # Agrega al final de la lista otra lista

lista2.append(6)    # Agrega un elemento a la lista
print(lista2)
lista2.append("Alejandro")
print(len(lista2))

print(lista4)

#   Busqueda de un elemento

print(8 in lista4)
print("Alejandro" in lista4)    #   Busca si el elemento esta en la lista
print(lista4.index(5))  #   Indica en que indice esta un eelemento en la liista
print(lista2.count(4))  #   Indica cuantas veces aparece el elemento en la lista
print(lista2.count(10))

lista2.pop() # Elemina el ultimo elemento
lista2.pop(3)    #   Elimina el elemento en el indice 3
lista2.remove(1)    #   Elimina el elemento en la lista con valor "1"

# lista2.clear()  #   Elimina todos los elementos de la lista
lista2.reverse()    # Voltea la lista
print(lista2)

lista6 = [5,4,-7,9,0,1,3]

lista6.sort()   # Ordena Ascendentemente
lista6.sort(reverse=True)    # Ordena descendentemente

print(lista6)

# index operator [] = gives access to a sequence's element (str,lists,tuples)

name = "hector Hernandez"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[0:6].upper()
last_name = name[7:].upper()

print(last_name)

print(first_name)
print(name)
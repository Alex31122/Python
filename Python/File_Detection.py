import os

path = "/home/smile34/Escritorio/Python/Hola"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That location is a directory")
else:
    print("That location doesn't exist!")